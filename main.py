import praw
import PySimpleGUI as sg

reddit = praw.Reddit(client_id='6-kZLiC2I6gQmyXilJBXsg', 
                     client_secret='l6Oogs9oVP2uupVhxDLUvrtYXmdbbw',
                     user_agent='reddit-api')

subreddit = reddit.subreddit(input("What subreddit do you wnat to see the comments of? "))
comments = subreddit.comments(limit=5)

layout = [[sg.Text('Top Comments of Your Chosen Subreddit')]]
for comment in comments:
    layout.append([sg.Text(comment.body, size=(80, 5))])
layout.append([sg.Button('Close')])

window = sg.Window('Reddit Comments', layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Close':
        break

window.close()