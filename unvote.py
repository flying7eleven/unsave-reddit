def get_age_of_submission(post_time: int):
    from datetime import datetime

    now = datetime.now()
    post_date = datetime.fromtimestamp(post_time)
    return now - post_date


if __name__ == '__main__':
    from praw import Reddit
    from prawcore.exceptions import BadRequest
    from time import sleep

    reddit_api = Reddit('unsave', user_agent='python/unsave-reddit')
    for upvoted_post in reddit_api.user.me().upvoted():
        post_age = ''
        try:
            submission = reddit_api.submission(id=upvoted_post)
            post_age = get_age_of_submission(int(submission.created_utc))
            if post_age.days < 180:
                submission.clear_vote()
                print(f'Unvoted (up) post {upvoted_post} ({post_age} old)...')
                sleep(1)
            else:
                print(f'Cannot unvote post since it is too old. Its age is: {post_age}')
        except BadRequest as e:
            print(f'Failed to unvote (up) post {upvoted_post} ({post_age} old). The error was {str(e)}.')
            sleep(1)
    for downvoted_post in reddit_api.user.me().downvoted():
        post_age = ''
        try:
            submission = reddit_api.submission(id=downvoted_post)
            post_age = get_age_of_submission(int(submission.created_utc))
            if post_age.days < 180:
                submission.clear_vote()
                print(f'Unvoted (down) post {downvoted_post} ({post_age} old)...')
                sleep(1)
            else:
                print(f'Cannot unvote post since it is too old. Its age is: {post_age}')
        except BadRequest as e:
            print(f'Failed to unvote (down) post {downvoted_post} ({post_age} old). The error was {str(e)}.')
            sleep(1)
