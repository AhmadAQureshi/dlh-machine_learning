#!/usr/bin/env python3
"""Reverse and transpose a pandas DataFrame."""


def flip_switch(df):
    """Reverse row order and transpose the DataFrame."""
    return df.iloc[::-1].transpose()
