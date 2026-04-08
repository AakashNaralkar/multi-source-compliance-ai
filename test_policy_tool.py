# test_policy_tool.py

from tools.policy_tool import check_policy

res = check_policy("Is passport mandatory?")

for r in res:
    print(r)