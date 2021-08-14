import pandas as pd

a = ""
matrix = []

while a != "Done":
    a = input()
    matrix.append(a.split())

matrix.pop()

for i in matrix:
    print(i)

df = pd.DataFrame(matrix, columns= ["A", "B", "C", "RESPOSTA"])
df.to_csv("TableOfTheTruth.csv", index=False)