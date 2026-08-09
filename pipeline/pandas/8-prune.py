#!/usr/bin/env python3
"""Remove rows with missing Close values from a pandas DataFrame."""


def prune(df):
    """Return the DataFrame without rows where Close is NaN."""
    return df.dropna(subset=["Close"])
