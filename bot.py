import praw
import time
import prawcore

user = '' #Bot Username
user_pass = '' #Bot Password
c_id = '' #Bot Client ID
c_secret = '' #Bot Client Secret

sleep_time = 5 #Amount of time in minutes the bot should sleep before checking again
sub = 'memes' #The subreddit you want the bot to run in

reddit = praw.Reddit(
    username = user,
    password = user_pass,
    client_id = c_id,
    client_secret = c_secret,
    user_agent = 'HotSaveBot by Rubix'
)

def main():

    #Note that if the bot crashes for any reason it will go through and save any duplicate posts again
    #This happens because I used an array inside the code instead of an outside txt file to store the submission id's

    saved_posts = [] #Array that the saved post id's will go into

    for submission in reddit.subreddit(sub).hot(limit=10): #Picks the top 10 posts in the subreddit of your choosing
        if submission.id not in saved_posts: #Checks if the chosen submission id has been saved before
            print('Saving hot posts...')
            submission.save() #Saves the selected posts
            saved_posts.append(submission.id) #Adds the posts id to an array to check if it has already saved that post
        else:
            pass
        
    sleep(sleep_time*60) #Sets the amount of time between checks

if __name__ == '__main__':
    while True:
        try:
            main()
        except BaseException:
            time.sleep(5)
