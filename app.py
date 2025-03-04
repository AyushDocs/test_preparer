#generate a streamlit app to take in a bunch of files as input as well as how many mcqs and then generate a quiz based on the files

import streamlit as st
from test_preparer.QuestionGenerator import QuestionGenerator


if __name__ == "__main__":
      st.title("Quiz Generator")

      uploaded_files = st.file_uploader("Upload your files", type=["pdf", "docx", "pptx", "txt"], accept_multiple_files=True)
      files_path = []
      if uploaded_files:
            for file in uploaded_files:
                  with open(file.name, "wb") as f:
                        f.write(file.getbuffer())
                  files_path.append(file.name)


      number_of_mcqs = st.number_input("Enter the number of MCQs", min_value=1, max_value=100, value=10)

      if st.button("Generate Quiz"):
            if uploaded_files:
                  st.write("Generating quiz...")
                  question_generator = QuestionGenerator()
                  quiz = question_generator.generate(files_path, number_of_mcqs)
                  st.write(quiz)
            else:
                  st.write("Please upload some files first")

