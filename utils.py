import json

#----------------------------------------------------prompts-----------------------------------------------
schema_linking_prompt = '''Table advisor, columns = [*,s_ID,i_ID]
Table classroom, columns = [*,building,room_number,capacity]
Table course, columns = [*,course_id,title,dept_name,credits]
Table department, columns = [*,dept_name,building,budget]
Table instructor, columns = [*,ID,name,dept_name,salary]
Table prereq, columns = [*,course_id,prereq_id]
Table section, columns = [*,course_id,sec_id,semester,year,building,room_number,time_slot_id]
Table student, columns = [*,ID,name,dept_name,tot_cred]
Table takes, columns = [*,ID,course_id,sec_id,semester,year,grade]
Table teaches, columns = [*,ID,course_id,sec_id,semester,year]
Table time_slot, columns = [*,time_slot_id,day,start_hr,start_min,end_hr,end_min]
Foreign_keys = [course.dept_name = department.dept_name,instructor.dept_name = department.dept_name,section.building = classroom.building,section.room_number = classroom.room_number,section.course_id = course.course_id,teaches.ID = instructor.ID,teaches.course_id = section.course_id,teaches.sec_id = section.sec_id,teaches.semester = section.semester,teaches.year = section.year,student.dept_name = department.dept_name,takes.ID = student.ID,takes.course_id = section.course_id,takes.sec_id = section.sec_id,takes.semester = section.semester,takes.year = section.year,advisor.s_ID = student.ID,advisor.i_ID = instructor.ID,prereq.prereq_id = course.course_id,prereq.course_id = course.course_id]
Q: "Find the buildings which have rooms with capacity more than 50."
A: Let’s think step by step. In the question "Find the buildings which have rooms with capacity more than 50.", we are asked:
"the buildings which have rooms" so we need column = [classroom.capacity]
"rooms with capacity" so we need column = [classroom.building]
Based on the columns and tables, we need these Foreign_keys = [].
Based on the tables, columns, and Foreign_keys, The set of possible cell values are = [50]. So the Schema_links are:
Schema_links: [classroom.building,classroom.capacity,50]

Table department, columns = [*,Department_ID,Name,Creation,Ranking,Budget_in_Billions,Num_Employees]
Table head, columns = [*,head_ID,name,born_state,age]
Table management, columns = [*,department_ID,head_ID,temporary_acting]
Foreign_keys = [management.head_ID = head.head_ID,management.department_ID = department.Department_ID]
Q: "How many heads of the departments are older than 56 ?"
A: Let’s think step by step. In the question "How many heads of the departments are older than 56 ?", we are asked:
"How many heads of the departments" so we need column = [head.*]
"older" so we need column = [head.age]
Based on the columns and tables, we need these Foreign_keys = [].
Based on the tables, columns, and Foreign_keys, The set of possible cell values are = [56]. So the Schema_links are:
Schema_links: [head.*,head.age,56]

Table department, columns = [*,Department_ID,Name,Creation,Ranking,Budget_in_Billions,Num_Employees]
Table head, columns = [*,head_ID,name,born_state,age]
Table management, columns = [*,department_ID,head_ID,temporary_acting]
Foreign_keys = [management.head_ID = head.head_ID,management.department_ID = department.Department_ID]
Q: "what are the distinct creation years of the departments managed by a secretary born in state 'Alabama'?"
A: Let’s think step by step. In the question "what are the distinct creation years of the departments managed by a secretary born in state 'Alabama'?", we are asked:
"distinct creation years of the departments" so we need column = [department.Creation]
"departments managed by" so we need column = [management.department_ID]
"born in" so we need column = [head.born_state]
Based on the columns and tables, we need these Foreign_keys = [department.Department_ID = management.department_ID,management.head_ID = head.head_ID].
Based on the tables, columns, and Foreign_keys, The set of possible cell values are = ['Alabama']. So the Schema_links are:
Schema_links: [department.Creation,department.Department_ID = management.department_ID,head.head_ID = management.head_ID,head.born_state,'Alabama']

Table Addresses, columns = [*,address_id,line_1,line_2,city,zip_postcode,state_province_county,country]
Table Candidate_Assessments, columns = [*,candidate_id,qualification,assessment_date,asessment_outcome_code]
Table Candidates, columns = [*,candidate_id,candidate_details]
Table Courses, columns = [*,course_id,course_name,course_description,other_details]
Table People, columns = [*,person_id,first_name,middle_name,last_name,cell_mobile_number,email_address,login_name,password]
Table People_Addresses, columns = [*,person_address_id,person_id,address_id,date_from,date_to]
Table Student_Course_Attendance, columns = [*,student_id,course_id,date_of_attendance]
Table Student_Course_Registrations, columns = [*,student_id,course_id,registration_date]
Table Students, columns = [*,student_id,student_details]
Foreign_keys = [Students.student_id = People.person_id,People_Addresses.address_id = Addresses.address_id,People_Addresses.person_id = People.person_id,Student_Course_Registrations.course_id = Courses.course_id,Student_Course_Registrations.student_id = Students.student_id,Student_Course_Attendance.student_id = Student_Course_Registrations.student_id,Student_Course_Attendance.course_id = Student_Course_Registrations.course_id,Candidates.candidate_id = People.person_id,Candidate_Assessments.candidate_id = Candidates.candidate_id]
Q: "List the id of students who never attends courses?"
A: Let’s think step by step. In the question "List the id of students who never attends courses?", we are asked:
"id of students" so we need column = [Students.student_id]
"never attends courses" so we need column = [Student_Course_Attendance.student_id]
Based on the columns and tables, we need these Foreign_keys = [Students.student_id = Student_Course_Attendance.student_id].
Based on the tables, columns, and Foreign_keys, The set of possible cell values are = []. So the Schema_links are:
Schema_links: [Students.student_id = Student_Course_Attendance.student_id]

Table Country, columns = [*,id,name]
Table League, columns = [*,id,country_id,name]
Table Player, columns = [*,id,player_api_id,player_name,player_fifa_api_id,birthday,height,weight]
Table Player_Attributes, columns = [*,id,player_fifa_api_id,player_api_id,date,overall_rating,potential,preferred_foot,attacking_work_rate,defensive_work_rate,crossing,finishing,heading_accuracy,short_passing,volleys,dribbling,curve,free_kick_accuracy,long_passing,ball_control,acceleration,sprint_speed,agility,reactions,balance,shot_power,jumping,stamina,strength,long_shots,aggression,interceptions,positioning,vision,penalties,marking,standing_tackle,sliding_tackle,gk_diving,gk_handling,gk_kicking,gk_positioning,gk_reflexes]
Table Team, columns = [*,id,team_api_id,team_fifa_api_id,team_long_name,team_short_name]
Table Team_Attributes, columns = [*,id,team_fifa_api_id,team_api_id,date,buildUpPlaySpeed,buildUpPlaySpeedClass,buildUpPlayDribbling,buildUpPlayDribblingClass,buildUpPlayPassing,buildUpPlayPassingClass,buildUpPlayPositioningClass,chanceCreationPassing,chanceCreationPassingClass,chanceCreationCrossing,chanceCreationCrossingClass,chanceCreationShooting,chanceCreationShootingClass,chanceCreationPositioningClass,defencePressure,defencePressureClass,defenceAggression,defenceAggressionClass,defenceTeamWidth,defenceTeamWidthClass,defenceDefenderLineClass]
Table sqlite_sequence, columns = [*,name,seq]
Foreign_keys = [Player_Attributes.player_api_id = Player.player_api_id,Player_Attributes.player_fifa_api_id = Player.player_fifa_api_id,League.country_id = Country.id,Team_Attributes.team_api_id = Team.team_api_id,Team_Attributes.team_fifa_api_id = Team.team_fifa_api_id]
Q: "List the names of all left-footed players who have overall rating between 85 and 90."
A: Let’s think step by step. In the question "List the names of all left-footed players who have overall rating between 85 and 90.", we are asked:
"names of all left-footed players" so we need column = [Player.player_name,Player_Attributes.preferred_foot]
"players who have overall rating" so we need column = [Player_Attributes.overall_rating]
Based on the columns and tables, we need these Foreign_keys = [Player_Attributes.player_api_id = Player.player_api_id].
Based on the tables, columns, and Foreign_keys, The set of possible cell values are = [left,85,90]. So the Schema_links are:
Schema_links: [Player.player_name,Player_Attributes.preferred_foot,Player_Attributes.overall_rating,Player_Attributes.player_api_id = Player.player_api_id,left,85,90]

Table advisor, columns = [*,s_ID,i_ID]
Table classroom, columns = [*,building,room_number,capacity]
Table course, columns = [*,course_id,title,dept_name,credits]
Table department, columns = [*,dept_name,building,budget]
Table instructor, columns = [*,ID,name,dept_name,salary]
Table prereq, columns = [*,course_id,prereq_id]
Table section, columns = [*,course_id,sec_id,semester,year,building,room_number,time_slot_id]
Table student, columns = [*,ID,name,dept_name,tot_cred]
Table takes, columns = [*,ID,course_id,sec_id,semester,year,grade]
Table teaches, columns = [*,ID,course_id,sec_id,semester,year]
Table time_slot, columns = [*,time_slot_id,day,start_hr,start_min,end_hr,end_min]
Foreign_keys = [course.dept_name = department.dept_name,instructor.dept_name = department.dept_name,section.building = classroom.building,section.room_number = classroom.room_number,section.course_id = course.course_id,teaches.ID = instructor.ID,teaches.course_id = section.course_id,teaches.sec_id = section.sec_id,teaches.semester = section.semester,teaches.year = section.year,student.dept_name = department.dept_name,takes.ID = student.ID,takes.course_id = section.course_id,takes.sec_id = section.sec_id,takes.semester = section.semester,takes.year = section.year,advisor.s_ID = student.ID,advisor.i_ID = instructor.ID,prereq.prereq_id = course.course_id,prereq.course_id = course.course_id]
Q: "Give the title of the course offered in Chandler during the Fall of 2010."
A: Let’s think step by step. In the question "Give the title of the course offered in Chandler during the Fall of 2010.", we are asked:
"title of the course" so we need column = [course.title]
"course offered in Chandler" so we need column = [SECTION.building]
"during the Fall" so we need column = [SECTION.semester]
"of 2010" so we need column = [SECTION.year]
Based on the columns and tables, we need these Foreign_keys = [course.course_id = SECTION.course_id].
Based on the tables, columns, and Foreign_keys, The set of possible cell values are = [Chandler,Fall,2010]. So the Schema_links are:
Schema_links: [course.title,course.course_id = SECTION.course_id,SECTION.building,SECTION.year,SECTION.semester,Chandler,Fall,2010]

Table city, columns = [*,City_ID,Official_Name,Status,Area_km_2,Population,Census_Ranking]
Table competition_record, columns = [*,Competition_ID,Farm_ID,Rank]
Table farm, columns = [*,Farm_ID,Year,Total_Horses,Working_Horses,Total_Cattle,Oxen,Bulls,Cows,Pigs,Sheep_and_Goats]
Table farm_competition, columns = [*,Competition_ID,Year,Theme,Host_city_ID,Hosts]
Foreign_keys = [farm_competition.Host_city_ID = city.City_ID,competition_record.Farm_ID = farm.Farm_ID,competition_record.Competition_ID = farm_competition.Competition_ID]
Q: "Show the status of the city that has hosted the greatest number of competitions."
A: Let’s think step by step. In the question "Show the status of the city that has hosted the greatest number of competitions.", we are asked:
"the status of the city" so we need column = [city.Status]
"greatest number of competitions" so we need column = [farm_competition.*]
Based on the columns and tables, we need these Foreign_keys = [farm_competition.Host_city_ID = city.City_ID].
Based on the tables, columns, and Foreign_keys, The set of possible cell values are = []. So the Schema_links are:
Schema_links: [city.Status,farm_competition.Host_city_ID = city.City_ID,farm_competition.*]

Table advisor, columns = [*,s_ID,i_ID]
Table classroom, columns = [*,building,room_number,capacity]
Table course, columns = [*,course_id,title,dept_name,credits]
Table department, columns = [*,dept_name,building,budget]
Table instructor, columns = [*,ID,name,dept_name,salary]
Table prereq, columns = [*,course_id,prereq_id]
Table section, columns = [*,course_id,sec_id,semester,year,building,room_number,time_slot_id]
Table student, columns = [*,ID,name,dept_name,tot_cred]
Table takes, columns = [*,ID,course_id,sec_id,semester,year,grade]
Table teaches, columns = [*,ID,course_id,sec_id,semester,year]
Table time_slot, columns = [*,time_slot_id,day,start_hr,start_min,end_hr,end_min]
Foreign_keys = [course.dept_name = department.dept_name,instructor.dept_name = department.dept_name,section.building = classroom.building,section.room_number = classroom.room_number,section.course_id = course.course_id,teaches.ID = instructor.ID,teaches.course_id = section.course_id,teaches.sec_id = section.sec_id,teaches.semester = section.semester,teaches.year = section.year,student.dept_name = department.dept_name,takes.ID = student.ID,takes.course_id = section.course_id,takes.sec_id = section.sec_id,takes.semester = section.semester,takes.year = section.year,advisor.s_ID = student.ID,advisor.i_ID = instructor.ID,prereq.prereq_id = course.course_id,prereq.course_id = course.course_id]
Q: "Find the id of instructors who taught a class in Fall 2009 but not in Spring 2010."
A: Let’s think step by step. In the question "Find the id of instructors who taught a class in Fall 2009 but not in Spring 2010.", we are asked:
"id of instructors who taught " so we need column = [teaches.id]
"taught a class in" so we need column = [teaches.semester,teaches.year]
Based on the columns and tables, we need these Foreign_keys = [].
Based on the tables, columns, and Foreign_keys, The set of possible cell values are = [Fall,2009,Spring,2010]. So the Schema_links are:
schema_links: [teaches.id,teaches.semester,teaches.year,Fall,2009,Spring,2010]

Table Accounts, columns = [*,account_id,customer_id,date_account_opened,account_name,other_account_details]
Table Customers, columns = [*,customer_id,customer_first_name,customer_middle_initial,customer_last_name,gender,email_address,login_name,login_password,phone_number,town_city,state_county_province,country]
Table Financial_Transactions, columns = [*,transaction_id,account_id,invoice_number,transaction_type,transaction_date,transaction_amount,transaction_comment,other_transaction_details]
Table Invoice_Line_Items, columns = [*,order_item_id,invoice_number,product_id,product_title,product_quantity,product_price,derived_product_cost,derived_vat_payable,derived_total_cost]
Table Invoices, columns = [*,invoice_number,order_id,invoice_date]
Table Order_Items, columns = [*,order_item_id,order_id,product_id,product_quantity,other_order_item_details]
Table Orders, columns = [*,order_id,customer_id,date_order_placed,order_details]
Table Product_Categories, columns = [*,production_type_code,product_type_description,vat_rating]
Table Products, columns = [*,product_id,parent_product_id,production_type_code,unit_price,product_name,product_color,product_size]
Foreign_keys = [Orders.customer_id = Customers.customer_id,Invoices.order_id = Orders.order_id,Accounts.customer_id = Customers.customer_id,Products.production_type_code = Product_Categories.production_type_code,Financial_Transactions.account_id = Accounts.account_id,Financial_Transactions.invoice_number = Invoices.invoice_number,Order_Items.order_id = Orders.order_id,Order_Items.product_id = Products.product_id,Invoice_Line_Items.product_id = Products.product_id,Invoice_Line_Items.invoice_number = Invoices.invoice_number,Invoice_Line_Items.order_item_id = Order_Items.order_item_id]
Q: "Show the id, the date of account opened, the account name, and other account detail for all accounts."
A: Let’s think step by step. In the question "Show the id, the date of account opened, the account name, and other account detail for all accounts.", we are asked:
"the id, the date of account opened, the account name, and other account detail for all accounts." so we need column = [Accounts.account_id,Accounts.account_name,Accounts.other_account_details,Accounts.date_account_opened]
Based on the columns and tables, we need these Foreign_keys = [].
Based on the tables, columns, and Foreign_keys, The set of possible cell values are = []. So the Schema_links are:
Schema_links: [Accounts.account_id,Accounts.account_name,Accounts.other_account_details,Accounts.date_account_opened]

Table city, columns = [*,City_ID,Official_Name,Status,Area_km_2,Population,Census_Ranking]
Table competition_record, columns = [*,Competition_ID,Farm_ID,Rank]
Table farm, columns = [*,Farm_ID,Year,Total_Horses,Working_Horses,Total_Cattle,Oxen,Bulls,Cows,Pigs,Sheep_and_Goats]
Table farm_competition, columns = [*,Competition_ID,Year,Theme,Host_city_ID,Hosts]
Foreign_keys = [farm_competition.Host_city_ID = city.City_ID,competition_record.Farm_ID = farm.Farm_ID,competition_record.Competition_ID = farm_competition.Competition_ID]
Q: "Show the status shared by cities with population bigger than 1500 and smaller than 500."
A: Let’s think step by step. In the question "Show the status shared by cities with population bigger than 1500 and smaller than 500.", we are asked:
"the status shared by cities" so we need column = [city.Status]
"cities with population" so we need column = [city.Population]
Based on the columns and tables, we need these Foreign_keys = [].
Based on the tables, columns, and Foreign_keys, The set of possible cell values are = [1500,500]. So the Schema_links are:
Schema_links: [city.Status,city.Population,1500,500]

'''

generation_prompt = '''
Q: "Give the name and building of the departments with greater than average budget."
Schema_links: [department.dept_name,department.building,department.budget]
A: Let's think step by step. "Give the name and building of the departments with greater than average budget." can be solved by knowing the answer to the following sub-question "#1 = Scan the table department and retrieve the budget of each department ; #2 = Calculate the average budget of all departments ; #3 = Scan the table department and retrieve the department names, budgets, and building names ; #4 = Join #2 and #3 based on the budgets and retrieve the department names and building names for the departments with budgets greater than the average budget".
So, the answer to the question "Give the name and building of the departments with greater than average budget." is =
Intermediate_representation: select department.dept_name , department.building from department  where  @.@ > avg ( department.budget )
SQL: SELECT dept_name ,  building FROM department WHERE budget  >  (SELECT avg(budget) FROM department)

Q: "Find the id of instructors who taught a class in Fall 2009 but not in Spring 2010."
Schema_links: [teaches.id,teaches.semester,teaches.YEAR,Fall,2009,Spring,2010]
A: Let's think step by step. "Find the id of instructors who taught a class in Fall 2009 but not in Spring 2010." can be solved by knowing the answer to the following sub-question "#1 = Scan the table teaches and retrieve the semester, instructor IDs, and years of all the classes taught in Fall 2009 ; #2 = Group #1 by instructor ID to find the instructors who taught a class in Fall 2009 ; #3 = Scan the table teaches and retrieve the semester, instructor IDs, and years of all the classes taught in Spring 2010 ; #4 = Group #3 by instructor ID to find the instructors who taught a class in Spring 2010 ; #5 = Return the instructor IDs that are in #2 but not in #4 to find the instructors who taught a class in Fall 2009 but not in Spring 2010".
So, the answer to the question "Find the id of instructors who taught a class in Fall 2009 but not in Spring 2010." is = 
Intermediate_representation: select teaches.ID from teaches  where  teaches.semester = \"Fall\"  and  teaches.year = 2009  and  teaches.semester != \"Spring\"  and  teaches.year = 2010 
SQL: SELECT id FROM teaches WHERE semester  =  'Fall' AND YEAR  =  2009 EXCEPT SELECT id FROM teaches WHERE semester  =  'Spring' AND YEAR  =  2010

Q: "Find the name of the courses that do not have any prerequisite?"
Schema_links: [course.title,course.course_id]
A: Let's think step by step. "Find the name of the courses that do not have any prerequisite?" can be solved by knowing the answer to the following sub-question "#1 = Scan the table course and retrieve the course IDs and titles of all courses. ; #2 = Scan the table prereq and retrieve the course IDs of all courses that have prerequisites. ; #3 = Group #2 by course ID to retrieve the course IDs that have prerequisites. ; #4 = Return the titles of the courses from #1 that are not in #3, indicating the courses that do not have any prerequisites.".
So, the answer to the question "Find the name of the courses that do not have any prerequisite?" is =
Intermediate_representation: select course.title from course  where  @.@ not in prereq.course_id 
SQL: SELECT title FROM course WHERE course_id NOT IN (SELECT course_id FROM prereq)

Q: "Find the salaries of all distinct instructors that are less than the largest salary."
Schema_links: [instructor.salary]
A: Let's think step by step. "Find the salaries of all distinct instructors that are less than the largest salary." can be solved by knowing the answer to the following sub-question "#1 = Scan the table instructor and retrieve the salary of all instructors ; #2 = Aggregate #1 and find the maximum salary ; #3 = Scan the table instructor and retrieve the salary of all instructors ; #4 = Join #2 and #3 based on the condition where the salary of an instructor is less than the maximum salary found in step #2, retrieve the distinct salaries of all instructors that satisfy this condition".
So, the answer to the question "Find the salaries of all distinct instructors that are less than the largest salary." is =
Intermediate_representation: select  distinct instructor.salary from instructor  where  @.@ < max ( instructor.salary )
SQL: SELECT DISTINCT salary FROM instructor WHERE salary  <  (SELECT max(salary) FROM instructor)

Q: "Find the names of students who have taken any course in the fall semester of year 2003."
Schema_links: [student.id,student.name,takes.id,takes.semester,fall,2003]
A: Let's think step by step. "Find the names of students who have taken any course in the fall semester of year 2003." can be solved by knowing the answer to the following sub-question "#1 = Scan the table takes and retrieve the semester, IDs, and year of all the courses taken in the fall semester of year 2003 ; #2 = Group #1 by ID and retrieve the unique IDs ; #3 = Scan the table student and retrieve the names and IDs of all the students ; #4 = Join #2 and #3 based on the matching IDs and retrieve the names".
So, the answer to the question "Find the names of students who have taken any course in the fall semester of year 2003." is =
Intermediate_representation: select student.name from student  where  takes.semester = \"Fall\"  and  takes.year = 2003
SQL: SELECT name FROM student WHERE id IN (SELECT id FROM takes WHERE semester  =  'Fall' AND YEAR  =  2003)

Q: "What is the course title of the prerequisite of course Mobile Computing?"
Schema_links: [course.title,course.course_id = prereq.course_id,prereq.prereq_id,course.title,Mobile Computing]
A: Let's think step by step. "What is the course title of the prerequisite of course Mobile Computing?" can be solved by knowing the answer to the following sub-question "#1 = Scan the table course and retrieve the course ID and title of all courses ; #2 = Scan the table course and retrieve the course ID and title of the course with the title 'Mobile Computing' ; #3 = Scan the table prerequisite and retrieve the prerequisite ID and course ID of all prerequisites ; #4 = Join #2 and #3 based on the matching course ID and retrieve the prerequisite IDs ; #5 = Intersect #1 and #4 based on the matching prerequisite IDs and retrieve the titles of the prerequisites".
So, the answer to the question "What is the course title of the prerequisite of course Mobile Computing?" is =
Intermediate_representation: select course.title from course  where  @.@ in prereq.*  and  course.title = \"Mobile Computing\"
SQL: SELECT title FROM course WHERE course_id IN (SELECT T1.prereq_id FROM prereq AS T1 JOIN course AS T2 ON T1.course_id  =  T2.course_id WHERE T2.title  =  'Mobile Computing')

Q: "Give the title and credits for the course that is taught in the classroom with the greatest capacity."
Schema_links: [classroom.capacity,classroom.building = SECTION.building,classroom.room_number = SECTION.room_number,course.title,course.credits,course.course_id = SECTION.course_id]
A: Let's think step by step. "Give the title and credits for the course that is taught in the classroom with the greatest capacity." can be solved by knowing the answer to the following sub-question "What is the capacity of the largest room?".
The SQL query for the sub-question "What is the capacity of the largest room?" is (SELECT max(capacity) FROM classroom)
So, the answer to the question "Give the title and credits for the course that is taught in the classroom with the greatest capacity." is =
Intermediate_representation: select course.title , course.credits from classroom  order by classroom.capacity desc limit 1"
SQL: SELECT T3.title ,  T3.credits FROM classroom AS T1 JOIN SECTION AS T2 ON T1.building  =  T2.building AND T1.room_number  =  T2.room_number JOIN course AS T3 ON T2.course_id  =  T3.course_id WHERE T1.capacity  =  (SELECT max(capacity) FROM classroom)

'''

decompose_prompt = '''
QPL parsing tree is a formalism to describe data retrieval operations over an SQL schema in a modular manner.
A QPL plan is a sequence of instructions for querying tabular data to answer a natural language question.
Forget everything you know about SQL, only use the following explanations.

A schema is specified as a list of <table> specification in the format:
<table>: <comma separated list of columns>

A plan contains a sequence of operations.
All operations return a stream of tuples.
All operations take as input either a physical table from the schema (for the Scan operation) or the output of other operations.

This is the formal specification for each operation:

<step> ::= 1...n

Scan ::= #<step> = Scan Table [ <tableName> ] <Predicate>? Output [ <fieldName>+ ]

// Binary operations
Join ::= Join ( #<InputStep1>, #<InputStep2> ) <Predicate> Output [ <qualifiedFieldName>+ ]
Intersect ::= Intersect  ( #<InputStep1>, #<InputStep2> ) <Predicate>? Output [ <qualifiedFieldName>+ ]
Except ::= Except ( #<InputStep1>, #<InputStep2> ) Output [ <qualifiedFieldName>+ ]
Union ::= Union ( #<InputStep1>, #<InputStep2> ) Output [ <qualifiedFieldName>+ ]

// Unary operations
Aggregate ::= Aggregate ( #<InputStep> ) <GroupBy>? Output [ <fieldName>+ | (<Agg> as <aliasName>)]
Filter ::= Filter ( #<InputStep> ) <Predicate> Output [ <fieldName>+ ]
TopSort ::= TopSort  ( #<InputStep> ) Rows [ <numRows> ] OrderBy [ <fieldName> ASC | DESC ] Output [ <fieldName>+ ]
Top ::= Top ( #<InputStep> ) Rows [ <numRows> ] Output [ <fieldName>+ ]
Sort ::= Sort  ( #<InputStep> ) OrderBy [ <fieldName> ASC | DESC ] (Distinct [ true ])? Output [ <fieldName>+ ]

// Predicate, Aggregate, Sort
Predicate ::= Predicate [ (Comparison AND | OR)+ ]
Comparison ::= ( countstar | <Agg> ) <ComparisonOp> ( countstar | <Agg> | Number | NULL )
Agg ::= ( AVG | COUNT | SUM | MIN | MAX ) ( <fieldName> )
ComparisonOp ::= <> | <= | >= | IS NOT | IS | LIKE | < | > | =
GroupBy ::= GroupBy [ <fieldName>+ ]


Let's think step by step to convert QPL plan to natural language plan given scheme, question, and QPL that describe the question.

In the natural language plan:
1. You must have exactly the same number of questions as there are steps in the QPL.
2. The questions you generate must follow exactly the same order as the steps in the QPL.


Example 1:

Schema:
Table Visitor (ID, Name, Age, Level_of_membership)
Table Museum (Museum_ID, Name, Open_Year, Num_of_staff)
Table Visit (Visitor_ID, Museum_ID, Total_Spent, Num_of_Ticket)

Question:
What is the total ticket expense of the visitors whose membership level is 1?

QPL Plan:
#1 = Scan Table [ visitor ] Predicate [ visitor.Level_of_membership = 1 ] Output [ ID ]
#2 = Scan Table [ visit ] Output [ visitor_ID , Total_spent ]
#3 = Join [ #1, #2 ] Predicate [ visitor.ID = visit.visitor_ID ] Output [ visit.Total_spent ]
#4 = Aggregate [ #3 ] Output [ SUM(visit.Total_spent) ]

Natural Language Plan:
#1 = Scan the table Visitor to find who are the visitors with membership level 1
#2 = Scan the table Visit to find what is the total spent by visitors during their visits
#3 = Join #1 and #2 to find what is the total spent by each visitor with membership level 1 during their visits
#4 = Group #3 by Visitor and aggregate the sum of total spent to find what is the total spent by all visitors with membership level 1 during their visit


Example 2:

Schema:
Table city (ID, Name, CountryCode, District, Population)
Table country (Code, Name, Continent, Region, SurfaceArea, IndepYear, Population, LifeExpectancy, GNP, GNPOld, LocalName, GovernmentForm, HeadOfState, Capital, Code2)
Table countrylanguage (CountryCode, Language, IsOfficial, Percentage)

Question:
What is name of the country that speaks the largest number of languages?

QPL Plan:
#1 = Scan Table [ country ] Output [ Code , Name ]
#2 = Scan Table [ countrylanguage ] Output [ CountryCode ]
#3 = Join [ #1, #2 ] Predicate [ #1.Code = #2.CountryCode ] Output [ #1.Name ]
#4 = Aggregate [ #3 ] GroupBy [ Name ] Output [ Name , countstar as count ]
#5 = TopSort [ #4 ] Rows [ 1 ] OrderBy [ count DESC ] Output [ Name , count ]

Natural Language Plan:
#1 = Scan the table country and retrieve the code, names of all countries.
#2 = Scan the table countrylanguage and retrieve all country codes.
#3 = Join #1 and #2 based on the matching code and retrieve the names of the countries.
#4 = Group #3 by name and aggregate the count per name to find the number of languages that speaks in each country.
#5 = Sort the records from #3 based on the count of the languages in descending order, select the first record, and identify the name of the country that speaks the largest number of languages and the its count of languages.


Example 3:

Schema:
Table museum (Museum_ID, Name, Num_of_Staff, Open_Year)
Table visitor (ID, Name, Level_of_membership, Age)
Table visit (Museum_ID, visitor_ID, Num_of_Ticket, Total_spent)

Question:
Find the number of visitors who did not visit any museum opened after 2010.


QPL Plan:
#1 = Scan Table [ visitor ] Output [ ID ]
#2 = Scan Table [ museum ] Predicate [ Open_Year > 2010 ] Output [ Museum_ID ]
#3 = Scan Table [ visit ] Output [ Museum_ID , visitor_ID ]
#4 = Join [ #2, #3 ] Predicate [ #2.Museum_ID = #3.Museum_ID ] Output [ #3.visitor_ID ]
#5 = Except [ #1, #4 ] Predicate [ #1.ID = #4.visitor_ID ] Output [ #1.ID ]
#6 = Aggregate [ #5 ] Output [ countstar as count ]

Natural Language Plan:
#1 = Scan the table Visitor to find who are the visitors
#2 = Scan the table Museum to find all the museums that opened after 2010
#3 = Scan the table Visit and retrieve the museum IDs and visitor IDs of all visits
#4 = Join #2 and #3 based on the matching museum ID and retrieve all the visitor IDs
#5 = return all the visitors IDs that from #1 that not in #4 to find all the visitors who did not visit any museum opened after 2010
#6 = Aggregate the number of all visitors in #5


Example 4:

Schema:
Table Ref_Feature_Types (feature_type_code, feature_type_name)
Table Ref_Property_Types (property_type_code, property_type_description)
Table Other_Available_Features (feature_id, feature_type_code, feature_name, feature_description)
Table Properties (property_id, property_type_code, date_on_market, date_sold, property_name, property_address, room_count, vendor_requested_price, buyer_offered_price, agreed_selling_price, apt_feature_1, apt_feature_2, apt_feature_3, fld_feature_1, fld_feature_2, fld_feature_3, hse_feature_1, hse_feature_2, hse_feature_3, oth_feature_1, oth_feature_2, oth_feature_3, shp_feature_1, shp_feature_2, shp_feature_3, other_property_details)
Table Other_Property_Features (property_id, feature_id, property_feature_description)

Question:
What are the names of properties that are either houses or apartments with more than 1 room?

QPL Plan:
#1 = Scan Table [ Properties ] Predicate [ property_type_code = 'House' ] Output [ property_name ]
#2 = Scan Table [ Properties ] Predicate [ room_count > 1 AND property_type_code = 'Apartment' ] Output [ property_name ]
#3 = Union [ #1, #2 ] Output [ #1.property_name ]
#4 = Sort [ #3 ] OrderBy [ property_name ASC ] Distinct [ true ] Output [ property_name ]

Natural Language Plan:
#1 = Scan the table Properties and retrieve the property name of all the properties with house code
#2 = Scan the table Properties and retrieve the property name of all the properties with more than 1 room and apartment code
#3 = Union #1 and #2 and retrieve all the property names
#4 = Sort the records from #3 based on the property name in ascending order and retrieve the property name without duplicates


Example 5:

Schema:
Table stadium (Stadium_ID, Location, Name, Capacity, Highest, Lowest, Average)
Table singer (Singer_ID, Name, Country, Song_Name, Song_release_year, Age, Is_male)
Table concert (concert_ID, concert_Name, Theme, Stadium_ID, Year)
Table singer_in_concert (concert_ID, Singer_ID)

Question:
What are the names and locations of the stadiums that had concerts that occurred in both 2014 and 2015?

QPL Plan:
#1 = Scan Table [ concert ] Predicate [ Year = 2014 ] Output [ Stadium_ID ]
#2 = Scan Table [ stadium ] Output [ Stadium_ID , Location , Name ]
#3 = Join [ #1, #2 ] Predicate [ #1.Stadium_ID = #2.Stadium_ID ] Output [ #2.Location , #2.Name ]
#4 = Scan Table [ concert ] Predicate [ Year = 2015 ] Output [ Stadium_ID ]
#5 = Scan Table [ stadium ] Output [ Stadium_ID , Location , Name ]
#6 = Join [ #4, #5 ] Predicate [ #4.Stadium_ID = #5.Stadium_ID ] Output [ #5.Location , #5.Name ]
#7 = Intersect [ #3, #6 ] Predicate [ #3.Name IS #6.Name AND #3.Location IS #6.Location ] Output [ #6.Location , #6.Name ]

Natural Language Plan:
#1 = Scan the table concert and retrieve the stadium IDs of all the concerts that occurred in 2014
#2 = Scan the table stadium and retrieve the stadium IDs, locations, names of all stadiums
#3 = Join #1 and #2 based on the matching Stadium IDs and retrieve the locations and names
#4 = Scan the table concert and retrieve the stadium IDs of all the concerts that occurred in 2015
#5 = Scan the table stadium and retrieve the stadium IDs, locations, names of all stadiums
#6 = Join #4 and #5 based on the matching Stadium IDs and retrieve the locations and names
#7 = Intersect #3 and #6 based on the matching names and locations and retrieve the locations and names


Example 6:

Schema:
Table city (ID, Name, CountryCode, District, Population)
Table sqlite_sequence (name, seq)
Table country (Code, Name, Continent, Region, SurfaceArea, IndepYear, Population, LifeExpectancy, GNP, GNPOld, LocalName, GovernmentForm, HeadOfState, Capital, Code2)
Table countrylanguage (CountryCode, Language, IsOfficial, Percentage)

Question:
How many type of governments are in Africa?

QPL Plan:
#1 = Scan Table [ country ] Output [ Continent , GovernmentForm ]
#2 = Filter [ #1 ] Predicate [ Continent = 'Africa' ] Output [ GovernmentForm ]
#3 = Aggregate [ #2 ] Output [ countstar as count ]

Natural Language Plan:
#1 = Scan table country and retrieve the continent and government form of all countries
#2 = Filter from #1 all the country with Africa continent and retrieve the government form
#3 = Aggregate the number of records of #2

'''
#----------------------------------------------------------------------------------------------------------

def get_subquestion(question):
    file_path = './data/subquestions_dev.json'
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    for item in data:
        if item['question'].lower() == question.lower():
            return item['subquestions']
    return False
