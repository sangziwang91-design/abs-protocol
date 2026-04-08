def validate_schema(o):
    required = ["claim", "evidence", "uncertainty", "action", "confidence"]

    for k in required:
        if k not in o:
            return False

    if not isinstance(o["confidence"], (int, float)):
        return False

    return True
