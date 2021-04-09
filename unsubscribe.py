if __name__ == '__main__':
    from praw import Reddit
    from time import sleep
    reddit_api = Reddit('unsave', user_agent='python/unsave-reddit')
    with open('unsaved_subreddits.txt', 'a') as output_file:
        for current_subreddit in reddit_api.user.subreddits():
            current_subreddit.unsubscribe()
            output_file.write(f'{current_subreddit}\n')
            print(f'Unsaved subreddit {current_subreddit}, sleeping and then going to the next one...')
            sleep(1)
