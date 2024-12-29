# Question Decomposition
# Decomposing the original question into subquestions based on the parsing tree using LLMs

import os
import time
import json
import openai
from tqdm import tqdm
from multiprocessing.dummy import Pool as ThreadPool
from utils import decompose_prompt

API_KEY = "" #API Key
os.environ["OPENAI_API_KEY"] = API_KEY
openai.api_key = os.getenv("OPENAI_API_KEY")
MODEL_NAME = "gpt-3.5-turbo"
SPLIT = "dev"
EXPERIMENT = 'question_decomposition'
TRIES = 2


with open("./cache/db_schemas.json") as f:
    db_schemas = json.load(f)

with open(f"""./cache/parsing_tree_{SPLIT}.json""") as f:
    data = json.load(f)


def get_prompt(example):

    return decompose_prompt + f"""Now your turn:

Schema:
{example['schema_str']}

Question:
{example['question']}

QPL Plan:
{example['parsing_tree_str']}

Natural Language Plan:"""


def get_response(history_messages):
    res = openai.ChatCompletion.create(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": history_messages}],
        n = 1,
        stream = False,
        temperature=0.0,
        max_tokens=600,
        top_p = 1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop = ["Q:"]
    )
    
    if "choices" in res:
        choice = res["choices"][0]
        if choice.get("finish_reason") == "stop":
            return str(choice["message"]['content'])


def gpt_predict_subquestion(i):
    example = data[i]
    try:
        with open(f"./cache/{SPLIT}_{example['id']}.json", "r") as f:
            return
    except:
        pass

    db_id, parsing_tree = example['parsing_tree'].split(' | ')
    schema = db_schemas[db_id]
    schema_str = ""

    for table, columns in schema['tables'].items():
        schema_str += f"""Table {table} ({', '.join([c[0] for c in columns])})\n"""

    example['schema_str'] = schema_str
    example['parsing_tree_str'] = '\n'.join(parsing_tree.split(" ; "))


    history_messages = [{"role": "system", "content": "You are a helpful AI Data Engineer"}, {"role": "user", "content": get_prompt(example)}]
    response_message = get_response(history_messages)
    history_messages.append({"role": "assistant", "content": response_message})

    json_res = {
        'messages': history_messages.copy(),
        'id': example['id'],
        'question': example['question'],
        'parsing_tree': example['parsing_tree']
    }

    json_object = json.dumps(json_res, indent=4)

    with open(f"./cache/{SPLIT}_{example['id']}.json", "w") as outfile:
        outfile.write(json_object)


flag = False

while not flag:
    try:
        with ThreadPool(4) as p:
            r = list(tqdm(p.imap(gpt_predict_subquestion, range(len(data))), total=len(data)))
        flag = True
    except:
        time.sleep(5)
        pass

data_with_subquestion = []

for example in data:
    with open(f"./cache/{SPLIT}_{example['id']}.json", "r") as f:
        subquestion_json = json.load(f)
        subquestion = " ; ".join(subquestion_json["messages"][2]["content"].split("\n"))
        example["subquestions"] = subquestion
        data_with_subquestion.append(example)


with open(f"./cache/{SPLIT}.json", "w") as f:
    json.dump(data_with_subquestion, f, indent=4)



