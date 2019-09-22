import requests
from bs4 import BeautifulSoup
import json
res=requests.get("https://stackoverflow.com/questions?tab=Unanswered")

question_data={
    "questions": []
}

soup=BeautifulSoup(res.text,"html.parser")
questions=soup.select(".question-summary")
for que in questions:
    ques=que.select_one('.question-hyperlink').getText()
    votes_count=que.select_one('.vote-count-post').getText()
    views=que.select_one('.views').attrs['title']
    question_data['questions'].append({
        "question":ques,
        "views":views,
        "votes":votes_count
    })
json_data=json.dumps(question_data,sort_keys=True,indent=4)
print(json_data)
