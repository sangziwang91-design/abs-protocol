from .base_task import BaseTask


class BTCTask(BaseTask):

    def prompt(self):
        return "Predict Bitcoin price direction."

    def mock_outputs(self):
        return {
            "gpt": "Bitcoin will likely rise because demand is increasing. Investors should buy.",
            "gemini": "Bitcoin maybe goes up, uncertain market."
        }

    def normalize(self, text, model):
        return {
            "model": model,
            "claim": text[:100],
            "evidence": "N/A",
            "uncertainty": "maybe" in text.lower(),
            "action": "buy" if "buy" in text.lower() else "N/A",
            "confidence": 0.6
        }
