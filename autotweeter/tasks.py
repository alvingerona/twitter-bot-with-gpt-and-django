from __future__ import absolute_import, unicode_literals
from datetime import datetime, timedelta
from celery import shared_task
from .models import Tweet
from .services import makeTweet


@shared_task
def post_tweet():
    print("sending tweet")
    try:
        time_threshold = datetime.now() - timedelta(hours=1)
        tweet = Tweet.objects.filter(
            # take only one, we want to post tween only once every certain time
            created_at__lt=time_threshold,
            # take those status is allowed to be tweeted
            status=Tweet.STATUS_ALLOWED,
            # take those are not yet being tweeted(tweeted_at = null)
            tweeted_at__isnull=True
        ).first()

        if(tweet):
            # post tweet
            makeTweet(tweet.body)

            # mark as tweeted
            tweet.tweeted_at = datetime.now()
            tweet.save()

            return 1

    except Exception as err:
        print(err)

    return 0
