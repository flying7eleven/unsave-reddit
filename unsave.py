if __name__ == '__main__':
    from praw import Reddit
    from time import sleep
    reddit_api = Reddit('unsave', user_agent='python/unsave-reddit')
    for save in reddit_api.user.me().saved():
        submission = reddit_api.submission(id=save)
        submission.unsave()
        print(f'Unsaved post {save}...')
        sleep(1)