# ABS Protocol v1.0 - Legacy Prototype

## Status

This repository is a minimal historical prototype.

It is retained for early implementation history only. The canonical public research surface has moved to:

https://github.com/sangziwang91-design/model-behavior-observatory

## Boundary

This prototype uses limited or mock outputs and does not represent the current ABS, BRC, or GEO-LINE-X public research line.

It does not provide:

- real model API integration
- long-term tracking
- benchmark validation status
- production-grade audit reliability
- current scoring thresholds or private evaluation gates

---

# Original Historical Content

# ABS Protocol v1.0

A standardized evaluation protocol for AI behavior.

## Status

⚠️ This is a minimal prototype.

* Uses mock model outputs
* Demonstrates schema enforcement and scoring
* Includes a basic real-world verification loop (BTC price)

## What ABS Does

* Enforces a structured output schema
* Scores outputs across defined dimensions
* Enables task-based evaluation

## What ABS Does NOT Do (Yet)

* No real model API integration
* No long-term accuracy tracking
* Limited verification logic

## Run Demo

```bash
cd abs-protocol
pip install -r requirements.txt
python examples/demo_btc.py
```

## Philosophy

ABS does not generate answers.

It judges them.
