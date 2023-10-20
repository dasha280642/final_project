import json
from datetime import datetime


def main():
    with open("operations.json") as json_file:
        json_data = json.load(json_file)
    executed_operations = [operation for operation in json_data if operation.get("state", "") == "EXECUTED"]
    sorted_operations = sorted(executed_operations, key=lambda x: datetime.strptime(x["date"], "%Y-%m-%dT%H:%M:%S.%f"))
    last_five_operations = sorted_operations[-5:]

    for operation in last_five_operations:
        date = operation["date"].split("T")[0]
        description = operation["description"]
        from_account = mask_account(operation.get("from"))
        to_account = mask_account(operation.get("to"))
        amount = operation["operationAmount"]["amount"]
        currency = operation["operationAmount"]["currency"]["code"]

        print(f"{date} {description} {from_account} -> {to_account}  {amount} {currency}")
        print()


def mask_account(account):
    return "**" + account[-4:] if account else ""


main()