import ollama
# Turn in the ollama application (works in background) before loading model here

class LLMEngine:
    def __init__(self, model_name="gemma3:1b"):
        self.model_name = model_name

    def ask(self, chart_summary, question, max_tokens=400):
        prompt = f"""
        You are an astrologer. Based on this natal chart:
        {chart_summary}
        User question: {question}
        Provide an astrology-based response in a fun and insightful way. Avoid pleasantries and
        keep the response concise and clear.
        """
        response = ollama.chat(
            model=self.model_name,
            messages=[{"role": "user", "content": prompt}],
            options={"num_predict": max_tokens}
        )
        return response["message"]["content"]
