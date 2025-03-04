from langchain_community.document_loaders import PyPDFLoader,TextLoader
from langchain_community.document_loaders import Docx2txtLoader,UnstructuredPowerPointLoader

def read_file(file_path):
      if file_path.endswith('.pdf'):
            return PyPDFLoader(file_path).load()
      elif file_path.endswith('.docx'):
            return Docx2txtLoader(file_path).load()
      elif file_path.endswith('.pptx'):
            return UnstructuredPowerPointLoader(file_path).load()
      elif file_path.endswith('.txt'):
            return TextLoader(file_path).load()
      else:
            raise ValueError(f"Unsupported file type: {file_path}")