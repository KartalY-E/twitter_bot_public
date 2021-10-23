import requests
import json
import random
import time
##

import tweepy

# Authenticate to Twitter fill in your account consumer key,consumer secret,access key,access secret
auth = tweepy.OAuthHandler("", "")
auth.set_access_token("", "")

#api link with questions and answers
response = requests.get("https://opentdb.com/api.php?amount=10&category=18")

print(response.status_code)
full = json.loads(response.text)

question_list = []
correct_answer_list = []
incorrect_answer_list0 = []
incorrect_answer_list1 = []
incorrect_answer_list2 = []
for i in range(0, 10):
    #print(full['results'][i]['question'])
    question_list.append(full['results'][i]['question'])

    #print(full['results'][i]['correct_answer'])
    correct_answer_list.append(full['results'][i]['correct_answer'])

    if str(full['results'][i]['incorrect_answers'][0]) == "True" or str(
            full['results'][i]['incorrect_answers'][0]) == "False":
        #print(full['results'][i]['incorrect_answers'][0])
        incorrect_answer_list0.append(
            full['results'][i]['incorrect_answers'][0])
    else:
        #print(full['results'][i]['incorrect_answers'][1])
        incorrect_answer_list1.append(
            full['results'][i]['incorrect_answers'][1])

        #print(full['results'][i]['incorrect_answers'][2])
        incorrect_answer_list2.append(
            full['results'][i]['incorrect_answers'][2])


def question():
    rnd1 = random.randint(0, 9)
    api = tweepy.API(auth)
    api.update_status(question_list[rnd1])
    print(question_list[rnd1])
    print(correct_answer_list[rnd1])

    time.sleep(35)
    answers(rnd1)


def answers(x):
    api = tweepy.API(auth)
    for tweet in tweepy.Cursor(api.search, q='@TweetMySnek', rpp=500).items(5):
        if correct_answer_list[x] in tweet.text:
            print("correct antwoord")
            print(tweet.text)
            print(tweet.id)
            api.update_status('Het correcte antwoord :' +
                              correct_answer_list[x])
        pass


question()
