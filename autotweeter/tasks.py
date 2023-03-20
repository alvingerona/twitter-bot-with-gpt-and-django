from __future__ import absolute_import, unicode_literals
from celery import shared_task
from .services import postMyTweet


@shared_task
def post_tweet():
    print("sending tweet")
    try:
        postMyTweet()
    except Exception as err:
        print(err)

    return 0
