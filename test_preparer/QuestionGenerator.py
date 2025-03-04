from dotenv import load_dotenv
from langchain_text_splitters import RecursiveCharacterTextSplitter
from test_preparer.utils import read_file
from test_preparer.logger import logging

from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from test_preparer.config.OpenAIConfig import OpenAIConfig
from langchain_core.output_parsers import JsonOutputParser


class QuestionGenerator:
      def __init__(self):
            self.openai_config = OpenAIConfig()
            self.llm = self.openai_config.llm

      def generate(self,file_paths:list,number=10):
            merged_document_list=[item for sublist in [read_file(file_path) for file_path in file_paths] for item in sublist]
            text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
            docs = text_splitter.split_documents(merged_document_list)
            all_results = []
            prompt = PromptTemplate.from_template(self.openai_config.prompt_template)
            chain = prompt|self.llm|JsonOutputParser()
            
            for doc in docs:
                chunk_result = chain.invoke({
                    "text": doc.page_content,
                    "number": number // len(docs) or 1,
                    "response_json": self.openai_config.response_format
                })
                all_results.append(chunk_result)
            
            return all_results

