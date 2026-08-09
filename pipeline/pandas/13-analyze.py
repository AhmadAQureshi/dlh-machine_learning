#!/usr/bin/env python3
"""Calculate descriptive statistics for a pandas DataFrame."""


def analyze(df):
    """Return statistics for all columns except Timestamp."""
    return df.drop(columns=["Timestamp"]).describe()
