#!/usr/bin/python3

import pandas as pd

df = pd.DataFrame(pd.read_excel("Ranges.xlsx"))

def get_range(df, BB, POS, PLAY):
	range = df['RANGE'].loc[(df["BB"] == BB)
		& (df["POS"] == POS)
		& (df["PLAY"] == PLAY)]
	return range.values[0]
