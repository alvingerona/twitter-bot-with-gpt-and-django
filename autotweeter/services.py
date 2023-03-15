import os
import tweepy
import openai
import random
from .constants import PROMPT_LIST, GPT_RESULT_COUNT, GPT_TEST_RESULTS, GPT_TEST_ONLY
from .models import Tweet

"""
Returns an instance of the pytwitter.Api class initialized with the client ID, consumer key, consumer secret, access token, and access secret. These values are used to authenticate with the Twitter API and perform API calls.
"""


def tweeterInstanceOfAPI():

    return tweepy.API(tweepy.OAuth1UserHandler(
        os.getenv("TWITTER_CONSUMER_KEY"),
        os.getenv("TWITTER_CONSUMER_SECRET"),
        os.getenv("TWITTER_ACCESS_TOKEN"),
        os.getenv("TWITTER_ACCESS_SECRET"),
    ))


def makeTweet(text: str):
    api = tweeterInstanceOfAPI()

    return api.update_status(text)


def openaiInstanceOfAPI():
    openai.api_key = os.getenv("OPENAI_API_KEY")

    return openai


"""
This saves an array of tweet texts to a database and marks them as pending by creating new Tweet objects with the given texts and bulk creating them in the database.

@param text_list Array of string
"""


def saveTweets(text_list):
    tweets = []

    for text in text_list:
        tweets.append(Tweet(body=text))

    Tweet.objects.bulk_create(tweets)


"""
This generates tweet completions using the OpenAI API. It randomly selects a prompt from a list, requests a tweet completion from the API, saves the generated tweets, and returns 1.
"""


def makeCompletion():
    api = openaiInstanceOfAPI()

    # chooce 1 randomly from the list of prompts
    prompt = "Write a tweet about: " + random.choice(PROMPT_LIST)

    # request for a completion from the OpenAPI
    results = api.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=100,
        temperature=0.91,
        n=GPT_RESULT_COUNT
    ).choices

    if(GPT_TEST_ONLY):
        results = (GPT_TEST_RESULTS)['choices']

    str_tweets = []
    for choice in results:
        str_tweets.append(choice['text'].lstrip("\n"))

    # every time a completion request is made, save it as tweet
    saveTweets(str_tweets)

    return 1
