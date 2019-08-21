test = {
    "name": "root stats",
    "points": 1,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
                    >>> ## Attacker never rolls lower than defender
                    >>> all((roll_df.attacker - roll_df.defender)  >= 0)
                    True
                    """,
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": r"""
                    >>> ## This checks your model statistics to determine if they're close to correct.
                    >>> ## If you fail this test, your model is almost definitely wrongly specified.
                    >>> np.abs(root_deltas.mean() - root_delta_mean_estimate) <= 0.15
                    True
                    >>> root_deltas.median() == root_delta_median
                    True
                    """,
                    "hidden": False,
                    "locked": False
                }
            ],
            "setup": r"""
            >>> root_samples = util.sample_from(root_model, draws=1000, chains=1, progressbar=False)
            >>> root_df = util.samples_to_dataframe(root_samples)
            >>> root_delta_mean_estimate = 1.24
            >>> root_delta_median = 1.0
            >>> root_deltas = (root_df["attacker"] - root_df["defender"])
            """,
            "teardown": r"""
            """,
            "type": "doctest"}]
        }
