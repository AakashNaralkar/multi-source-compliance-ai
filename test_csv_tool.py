from tools.csv_tool import search_csv

res = search_csv("passport")

for r in res:
    print(r)