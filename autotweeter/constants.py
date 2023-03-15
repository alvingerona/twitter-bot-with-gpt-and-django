PROMPT_LIST = [
    "New programming languages and frameworks that you're excited about trying out or learning more about.",
    "Best practices for coding, including tips for improving code quality, performance, and security.",
    "Programming memes and jokes that other developers will appreciate.",
    "Industry news and trends, such as emerging technologies or changes in popular frameworks.",
    "Advice for aspiring developers, such as how to get started with programming or tips for improving coding skills.",
    "Your personal experiences with programming, including challenges you've faced and how you overcame them.",
    "Collaboration opportunities with other developers, such as hackathons or open source projects.",
    "Thought pieces on the role of technology in society and the ethical implications of programming and software development."
]

GPT_RESULT_COUNT = 5

# when set to True the makeCompletion will not do actual request
# to the API instead it will use this dummy result from variable GPT_TEST_RESULTS
GPT_TEST_ONLY = True

# sample result from completion API
GPT_TEST_RESULTS = {
    "choices": [
        {
            "finish_reason": "stop",
            "index": 0,
            "logprobs": None,
            "text": "\n\nWe must consider how #technology shapes our society and the ethical implications of its development. Check out these thought pieces on the role of #programming and #software development. #ethicaltech #techethics #society"
        }
    ],
    "created": 1678798979,
    "id": "cmpl-6tyapWQ2NkVo9aq6NPlzByUsV7vEK",
    "model": "text-davinci-003",
    "object": "text_completion",
    "usage": {
        "completion_tokens": 46,
        "prompt_tokens": 24,
        "total_tokens": 70
    }
}