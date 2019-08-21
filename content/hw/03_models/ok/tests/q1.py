test = {
    "name": "coin toss",
    "points": 1,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
                    >>> coin_toss_model.logp({"coin": 0}) == coin_toss_model.logp({"coin": 1})
                    True
                    """,
                    "hidden": False,
                    "locked": False
                }
            ],
            "setup": "",
            "teardown": "",
            "type": "doctest"}]
        }
