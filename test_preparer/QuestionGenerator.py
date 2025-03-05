from test_preparer.utils import read_file
from test_preparer.logger import logging

from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from test_preparer.config.OpenAIConfig import OpenAIConfig
from langchain_core.output_parsers import JsonOutputParser
from langchain.chains import LLMChain
from typing import List

class QuestionGenerator:
    def __init__(self):
        self.openai_config = OpenAIConfig()
        self.llm = ChatOpenAI(model="gpt-4o-mini", temperature=0, api_key=self.openai_config.openai_api_key)
    def generate(self, file_paths: list, mcq_count:List[int], subjective_count:List[int]):
        response=[]
        for file_path, mcq_count, subjective_count in zip(file_paths, mcq_count, subjective_count):
            response.append(self.generate_per_document(file_path, mcq_count, subjective_count))
        return response
      

    def generate_per_document(self,file_path:str, no_of_mcqs: int, no_of_subjective: int):
        text=''.join([item.page_content for item in read_file(file_path)])
        prompt = PromptTemplate.from_template(template=self.openai_config.prompt_template, partial_variables={"RESPONSE_JSON": self.openai_config.response_format})
        chain = LLMChain(llm=self.llm, prompt=prompt, output_parser=JsonOutputParser())
        return chain.invoke({"text":text,"mcq_number":no_of_mcqs,"subjective_number":no_of_subjective})