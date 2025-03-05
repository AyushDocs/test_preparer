import os
from dotenv import load_dotenv


class OpenAIConfig:
      def __init__(self):
            load_dotenv()
      
      @property
      def openai_api_key(self):
            return os.getenv("OPENAI_API_KEY")
      
      @property
      def response_format(self):
            return """{
      "mcq":{
            "1": {
                  "question": "multiple choice question here",
                  "options": {
                      "a": "choice here",
                      "b": "choice here",
                      "c": "choice here",
                      "d": "choice here",
                  },
                  "correct": "correct answer here like a,b,c,d",
            },
            "2": {
                  "question": "multiple choice question here",
                  "options": {
                      "a": "choice here",
                      "b": "choice here",
                      "c": "choice here",
                      "d": "choice here",
                },
                "correct": "correct answer here like a,b,c,d",
            },
      "subjective":{
            "1": {
                  "question": "subjective question here",
                  "expected_answer": "subjective answer here",
            },
            "2": {
                  "question": "subjective question here",
                  "expected_answer": "subjective answer here",
            },
      }
      }"""
      
      @property
      def prompt_template(self):
            return """
            Text:{text}
            You are an expert MCQ and Subjective question maker. Given the above text, it is your job to
            create a quiz  of {mcq_number} multiple choice questions and {subjective_number} subjective questions for students. 
            Make sure to format your response like  RESPONSE_JSON below  and use it as a guide.
            ### RESPONSE_JSON
            {RESPONSE_JSON}"""





