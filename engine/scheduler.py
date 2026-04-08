from tasks.btc_task import BTCTask
from engine.judge import judge
from verify.btc_verify import get_btc_price, verify_direction


def run_all_tasks():
    task = BTCTask()

    raw_outputs = task.mock_outputs()

    structured = [task.normalize(o, name) for name, o in raw_outputs.items()]

    ranked = judge(structured)

    prev_price = get_btc_price()
    current_price = get_btc_price()

    print("\n=== ABS REPORT ===")

    for o, s, total in ranked:
        correct = verify_direction(o["claim"], prev_price, current_price)

        print({
            "model": o["model"],
            "score": total,
            "correct": correct
        })
