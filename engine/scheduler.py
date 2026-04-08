from tasks.btc_task import BTCTask
from engine.judge import judge
from verify.btc_verify import get_btc_price
from datetime import datetime


def run_all_tasks():
    task = BTCTask()

    raw_outputs = task.mock_outputs()

    structured = [task.normalize(o, name) for name, o in raw_outputs.items()]

    ranked = judge(structured)

    price = get_btc_price()

    print("\n=== ABS REPORT ===")
    print("Time:", datetime.utcnow())
    print("BTC Price:", price)

    for r in ranked:
        print(r)
