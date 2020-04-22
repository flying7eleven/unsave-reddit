if __name__ == '__main__':
    from praw import Reddit
    from prawcore.exceptions import BadRequest
    reddit_api = Reddit('unsave', user_agent='python/unsave-reddit')
    for upvoted_post in reddit_api.user.me().upvoted():
        try:
            submission = reddit_api.submission(id=upvoted_post)
            submission.clear_vote()
            print(f'Unvoted (up) post {upvoted_post}...')
        except BadRequest as e:
            print(f'Failed to unvote (up) post {upvoted_post}. The error was {str(e)}.')
    for downvoted_post in reddit_api.user.me().downvoted():
        try:
            submission = reddit_api.submission(id=downvoted_post)
            submission.clear_vote()
            print(f'Unvoted (down) post {downvoted_post}...')
        except BadRequest as e:
            print(f'Failed to unvote (down) post {downvoted_post}. The error was {str(e)}.')