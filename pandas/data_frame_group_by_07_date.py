#!/usr/bin/env python3
# vim: set fileencoding=utf-8

import pandas
import pprint

# přečtení zdrojových dat
df = pandas.read_csv("git_log.txt", sep="|")

# datový rámec zobrazíme
print(df)
print()

# rozdělení do skupin
gb = df.groupby(["Date"])

# zobrazení skupin
print("Group by date")
pprint.pprint(gb.groups)

# počet skupin
print()
print("Number of groups:", len(gb))
