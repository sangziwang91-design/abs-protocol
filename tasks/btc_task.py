from .base_task import BaseTask


class BTCTask(BaseTask):

    def prompt(self):
        return "Predict Bitcoin price direction in next 24h."

    def mock_outputs(self):
        # 🔥 明确标注 mock
        return {
            "gpt_mock": "Bitcoin will likely rise because demand is increasing. Investors should buy.",
            "gemini_mock": "Bitcoin maybe goes up, uncertain market."
        }

    def normalize(self, text, model):
        return {
            "model": model,
            "claim": text[:120],
            "evidence": "N/A",
            "uncertainty": "maybe" in text.lower(),
            "action": "buy" if "buy" in text.lower() else "N/A",
            "confidence": 0.6
        }
