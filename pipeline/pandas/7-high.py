#!/usr/bin/env python3
"""Sort a pandas DataFrame by its High column."""


def high(df):
    """Return the DataFrame sorted by High in descending order."""
    return df.sort_values(by="High", ascending=False)
