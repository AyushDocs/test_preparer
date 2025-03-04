import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI


class OpenAIConfig:
      def __init__(self):
            load_dotenv()
            self.llm = ChatOpenAI(model="gpt-4o-mini", temperature=0, api_key=self.openai_api_key)
      
      @property
      def openai_api_key(self):
            return os.getenv("OPENAI_API_KEY")
      
      @property
      def response_format(self):
            return """{
            "1": {
                "mcq": "multiple choice question",
                "options": {
                    "a": "choice here",
                    "b": "choice here",
                    "c": "choice here",
                    "d": "choice here",
                },
                "correct": "correct answer",
            },
            "2": {
                "mcq": "multiple choice question",
                "options": {
                    "a": "choice here",
                    "b": "choice here",
                    "c": "choice here",
                    "d": "choice here",
                },
                "correct": "correct answer",
            },
            "3": {
                "mcq": "multiple choice question",
                "options": {
                    "a": "choice here",
                    "b": "choice here",
                    "c": "choice here",
                    "d": "choice here",
                },
                "correct": "correct answer",
            },
      }"""
      
      @property
      def prompt_template(self):
            return """
            Text:{text}
            You are an expert MCQ maker. Given the above text, it is your job to \
            create a quiz  of {number} multiple choice questions for students. 
            Make sure the questions are not repeated and check all the questions to be conforming the text as well.
            Make sure to format your response like  RESPONSE_JSON below  and use it as a guide. \
            Ensure to make {number} MCQs
            ### RESPONSE_JSON
            {response_json}"""





