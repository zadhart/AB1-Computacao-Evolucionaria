"""
From the moment I understood the weakness of my flesh, it disgusted me.
I craved the strength and certainty of steel.
I aspired to the purity of the Blessed Machine.

Your kind cling to your flesh, as if it will not decay and fail you.
One day the crude biomass that you call a temple will wither, and you will beg my kind to save you.
But I am already saved, for the Machine is immortal...

...even in death I serve the Omnissiah
"""

import pandas as pd

df = pd.read_csv("TableOfTheTruth.csv")
elements = []

for x in range(len(df["RESPOSTA"])):
    if df["RESPOSTA"][x] == "VERDADEIRO":
        elements.append(df.iloc[x])
y = 0
for x in elements:
    if x["A"] == "VERDADEIRO":
        print("A", end="")
    else:
        print("-A", end="")
    print(" & ", end="")
    if x["B"] == "VERDADEIRO":
        print("B", end="")
    else:
        print("-B", end="")
    print(" & ", end="")
    if x["C"] == "VERDADEIRO":
        print("C", end="")
    else:
        print("-C", end="")

    y += 1

    if y < len(elements):
        print("  ||  ", end="")
