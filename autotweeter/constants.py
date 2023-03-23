PROMPT_LIST = [
    "New programming languages and frameworks that you're excited about trying out or learning more about.",
    "Best practices for coding, including tips for improving code quality, performance, and security.",
    "Programming memes and jokes that other developers will appreciate.",
    "Industry news and trends, such as emerging technologies or changes in popular frameworks.",
    "Advice for aspiring developers, such as how to get started with programming or tips for improving coding skills.",
    "Your personal experiences with programming, including challenges you've faced and how you overcame them.",
    "Collaboration opportunities with other developers, such as hackathons or open source projects.",
    "Thought pieces on the role of technology in society and the ethical implications of programming and software development.",
    "The challenges of being a fullstack developer: Discuss some of the difficulties you've faced in your role and how you've overcome them.",
    "One of many things needed to successfully complete a project as a fullstack developer."
]

POST_PROMPT = "Tweet must have maximum 280 characters. Add hastag #fullstack #programming"

GPT_RESULT_COUNT = 5

# when set to True the makeCompletion will not do actual request
# to the API instead it will use this dummy result from variable GPT_TEST_RESULTS
GPT_TEST_ONLY = False

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
