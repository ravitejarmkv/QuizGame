import requests
import json

r = requests.get("https://opentdb.com/api.php?amount=10&type=boolean")

resonse = r.text
# print(resonse)

data_load = json.loads(resonse)
ques = data_load["results"]

question_d = []
question = {}
for i in ques:
    question["question"] = i["question"]
    question["answer"] = i["correct_answer"]
    question_d.append(question)
# print(question_d)