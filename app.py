import os
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

            mcq_inputs = []
            subjective_inputs = []
            
            st.write("Specify number of questions for each document:")
            for i, file in enumerate(uploaded_files):
                  col1, col2 = st.columns(2)
                  with col1:
                        mcq = st.number_input(
                              f"MCQs for {file.name}",
                              min_value=1,
                              max_value=100,
                              value=10,
                              key=f"mcq_{i}"
                        )
                        mcq_inputs.append(mcq)
                  with col2:
                        subj = st.number_input(
                              f"Subjective for {file.name}",
                              min_value=0,
                              max_value=50,
                              value=5,
                              key=f"subj_{i}"
                        )
                        subjective_inputs.append(subj)

            if st.button("Generate Quiz"):
                  st.write("Generating quiz...")
                  question_generator = QuestionGenerator()
                  quiz = question_generator.generate(files_path, mcq_inputs, subjective_inputs)
                  st.write(quiz)
                  st.success("Quiz generated successfully!")
                  st.balloons()
                  for file in files_path:
                        os.remove(file)
      else:
            st.write("Please upload some files first")

