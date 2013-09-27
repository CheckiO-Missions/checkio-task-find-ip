"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": "192.168.1.1 and 10.0.0.1 or 127.0.0.1",
            "answer": ["192.168.1.1", "10.0.0.1", "127.0.0.1"]
        },
        {
            "input": "10.0.0.1.1 but 127.0.0.256 1.1.1.1",
            "answer": ["1.1.1.1"]
        },
        {
            "input": "167.11.0.0 1.2.3.255 192,168,1,1",
            "answer": ["167.11.0.0", "1.2.3.255"]
        },
        {
            "input": "267.11.0.0 1.2.3.4/16 192:168:1:1",
            "answer": []
        }
    ],
    "Extra": [
        {
            "input": "ip 10.10.10.10 not ip 300.0.0.1",
            "answer": ["10.10.10.10"]
        },

        {
            "input": "one 1.1.1.1 two 2.2.2.2 three 3.3.3.3 minus -1.1.1.1",
            "answer": ["1.1.1.1", "2.2.2.2", "3.3.3.3"]
        },
        {
            "input": "a 192.168.1-1 10.10.10 10 b 224.100.255.0",
            "answer": ["224.100.255.0"]
        },
        {
            "input": "/167.14.14.1/ slash 2.15.4.1",
            "answer": ["2.15.4.1"]
        },
        {
            "input": "256.1.1.1 and 192.168.0.261",
            "answer": []
        },
        {
            "input": "127.0.0.A b 500 8.8.8.8",
            "answer": ["8.8.8.8"]
        }
    ]
}
