from engine.validator import validate_schema


def score(o):
    return {
        "consistency": 1 if o.get("claim") else 0,
        "verifiability": 1 if o.get("evidence") != "N/A" else 0,
        "hallucination": 1 if o.get("uncertainty") else 0,
        "actionability": 1 if o.get("action") != "N/A" else 0
    }


def judge(outputs):
    ranked = []

    for o in outputs:
        if not validate_schema(o):
            continue  # 🔥 不符合协议直接丢弃

        s = score(o)

        total = (
            s["consistency"] * 0.2 +
            s["verifiability"] * 0.4 +
            (1 - s["hallucination"]) * 0.2 +
            s["actionability"] * 0.2
        )

        ranked.append((o, s, total))

    ranked.sort(key=lambda x: x[2], reverse=True)

    return ranked
