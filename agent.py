# * import librairies
from decouple import config
from pandasai.llm import OpenAI
from pandasai import SmartDataframe


class AgentPandas():
    def __init__(self):
        self.llm = OpenAI(api_token=config("OPENAI_API_KEY"))


    def chat(self, query: str, data) -> any:
        df = SmartDataframe(data, config={"llm": self.llm})

        test = df.chat(query)

        return test
