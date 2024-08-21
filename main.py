import streamlit as st
import pandas as pd
from pymongo import MongoClient, errors
import plotly.express as px
import matplotlib.pyplot as plt
from PIL import Image
from pymongo.server_api import ServerApi

# client = MongoClient("mongodb://localhost:27017/")
# db = client['llm_database']
# collection = db['contributions']


mango_uri = "mongodb+srv://llmdatabase:llmdatabase@cluster0.whcpxvq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server

client = MongoClient(mango_uri)
db = client['llm_database']
collection = db['contributions']
#st.write("MongoDB connection successful")



import streamlit as st
from PIL import Image

# Initialize session state for form inputs
if 'student_name' not in st.session_state:
    st.session_state.student_name = ''
if 'student_area' not in st.session_state:
    st.session_state.student_area = ''
if 'student_question' not in st.session_state:
    st.session_state.student_question = ''
if 'student_answer' not in st.session_state:
    st.session_state.student_answer = ''
if 'professor_name' not in st.session_state:
    st.session_state.professor_name = ''
if 'professor_area' not in st.session_state:
    st.session_state.professor_area = ''
if 'professor_question' not in st.session_state:
    st.session_state.professor_question = ''
if 'professor_answer' not in st.session_state:
    st.session_state.professor_answer = ''
if 'professional_name' not in st.session_state:
    st.session_state.professional_name = ''
if 'professional_area' not in st.session_state:
    st.session_state.professional_area = ''
if 'professional_question' not in st.session_state:
    st.session_state.professional_question = ''
if 'professional_answer' not in st.session_state:
    st.session_state.professional_answer = ''
if 'submitted' not in st.session_state:
    st.session_state.submitted = True

def clear_form():
    """Clears the form by resetting the session state."""
    # Student
    st.session_state.student_name = ''
    st.session_state.student_area = ''
    st.session_state.student_question = ''
    st.session_state.student_answer = ''
    # Professor
    st.session_state.professor_name = ''
    st.session_state.professor_area = ''
    st.session_state.professor_question = ''
    st.session_state.professor_answer = ''
    # Professional
    st.session_state.professional_name = ''
    st.session_state.professional_area = ''
    st.session_state.professional_question = ''
    st.session_state.professional_answer = ''
    st.session_state.submitted = True

def main_page():
    st.title("Evaluating LLMs in Interviews: Key Benchmarks and Model Capabilities")
    image1 = Image.open("asset/1.png")
    st.image(image=image1)
    st.header("Abstract")
    st.markdown(""" 
        <div style="text-align: justify;">
            The aim of this project is to develop state-of-the-art benchmarks for evaluating large language models (LLMs). 
            These benchmarks are designed to assess LLMs based on a wide range of capabilities, including technical knowledge, common sense, reasoning, and natural language processing.
            A key focus of the project is on creating a tailored Question Answering benchmark specifically for interview scenarios. 
            This benchmark evaluates how well an LLM can handle the diverse types of questions typically encountered in job interviews, which require a mix of technical expertise, problem-solving abilities, soft skills, and situational judgment.      
        </div>
        """, unsafe_allow_html=True)
    
    aggregate_data()

    st.header("Contribution")
    st.write("Note: Do not copy questions from other sources like ChatGPT, Claude, etc. Each QA should be uniquely crafted.")

    expertise = st.selectbox('Expertise', ['Professor', 'Professional', 'Student'])

    if expertise == 'Professor':
        professor()
    elif expertise == "Professional":
        professional()
    elif expertise == 'Student':
        student()

def student():
    st.session_state.student_name = st.text_input(
        "Enter your name:",
        st.session_state.student_name
    )
    st.session_state.student_area = st.text_input(
        "Enter your area of interest:",
        st.session_state.student_area
    )
    st.session_state.student_question = st.text_area(
        "Enter your question:",
        st.session_state.student_question
    )
    st.session_state.student_answer = st.text_area(
        "Enter your answers:",
        st.session_state.student_answer
    )

    if st.button("Submit"):
        if not st.session_state.student_name or not st.session_state.student_area or not st.session_state.student_question or not st.session_state.student_answer:
            st.error("All fields are required. Please fill out every field before submitting.")
        else:
            save_to_mongo({
                'name': st.session_state.student_name,
                'expertise': 'Student',
                'area': st.session_state.student_area,
                'question': st.session_state.student_question,
                'answer': st.session_state.student_answer
            })
            st.success("Your question and answer have been saved!")
            clear_form()
            st.rerun()

def professor():
    st.session_state.professor_name = st.text_input(
        "Enter your name:",
        st.session_state.professor_name
    )
    st.session_state.professor_area = st.text_input(
        "Enter your area of interest:",
        st.session_state.professor_area
    )
    st.session_state.professor_question = st.text_area(
        "Enter your question:",
        st.session_state.professor_question
    )
    st.session_state.professor_answer = st.text_area(
        "Enter your answers:",
        st.session_state.professor_answer
    )

    if st.button("Submit"):
        if not st.session_state.professor_name or not st.session_state.professor_area or not st.session_state.professor_question or not st.session_state.professor_answer:
            st.error("All fields are required. Please fill out every field before submitting.")
        else:
            save_to_mongo({
                'name': st.session_state.professor_name,
                'expertise': 'Professor',
                'area': st.session_state.professor_area,
                'question': st.session_state.professor_question,
                'answer': st.session_state.professor_answer
            })
            st.success("Your question and answer have been saved!")
            clear_form()
            st.rerun()

def professional():
    st.session_state.professional_name = st.text_input(
        "Enter your name:",
        st.session_state.professional_name
    )
    st.session_state.professional_area = st.text_input(
        "Enter your area of interest:",
        st.session_state.professional_area
    )
    st.session_state.professional_question = st.text_area(
        "Enter your question:",
        st.session_state.professional_question
    )
    st.session_state.professional_answer = st.text_area(
        "Enter your answers:",
        st.session_state.professional_answer
    )

    if st.button("Submit"):
        if not st.session_state.professional_name or not st.session_state.professional_area or not st.session_state.professional_question or not st.session_state.professional_answer:
            st.error("All fields are required. Please fill out every field before submitting.")
        else:
            save_to_mongo({
                'name': st.session_state.professional_name,
                'expertise': 'Professional',
                'area': st.session_state.professional_area,
                'question': st.session_state.professional_question,
                'answer': st.session_state.professional_answer
            })
            st.success("Your question and answer have been saved!")
            clear_form()
            st.rerun()

def save_to_mongo(data):
    """Insert the data into the MongoDB collection."""
    collection.insert_one(data)

def aggregate_data():
    """Query the MongoDB collection to get all documents and aggregate the data."""
    data = list(collection.find({}))
    df = pd.DataFrame(data)

    if not df.empty:
        aggregated_df = df.groupby('area').agg(
            num_questions=('question', 'count')
        ).reset_index()

        aggregated_df['Field'] = aggregated_df['area'].str.title()

        aggregated_df.rename(columns={'num_questions': 'Dataset Strength'}, inplace=True)

        total_strength = aggregated_df['Dataset Strength'].sum()
        aggregated_df['Progress'] = (aggregated_df['Dataset Strength'] / total_strength) * 100

        st.dataframe(
            aggregated_df[['Field', 'Dataset Strength', 'Progress']],
            column_config={
                "Progress": st.column_config.ProgressColumn(
                    "Progress",
                    format="%.1f%%",
                    min_value=0,
                    max_value=100,
                ),
            },
            use_container_width=True
        )

        return aggregated_df
    else:
        st.write("No data available to display.")
        return pd.DataFrame()

# Run the app
if __name__ == "__main__":
    main_page()







    # col1,col2 = st.columns([1,1])

    # with col1:
    #     st.header("Researcher")
    #     st.markdown(""" 
    #     <div style="text-align: justify;">
    #         <ul style="list-style-position: inside;">
    #             <li>Omkar  R  Kharkar</li>
    #             <li>Dhanesh Kapadia</li>
    #         </ul>
    #     </div>
    #     """, unsafe_allow_html=True)
        

    # with col2:
    #     st.header("Research Advisor")
    #     st.markdown(""" 
    #     <div style="text-align: justify;">
    #                 <ul style="list-style-position: inside;">
    #             <li>Dr. Katerina Bourazeri <br> Lecturer , University of Essex</li>
    #         </ul>
    #     </div>
    #     """, unsafe_allow_html=True)


# <ul style="list-style-position: inside;">
#                 <li>Technical Knowledge: Assessing the model's ability to solve domain-specific problems, such as coding challenges for software engineers or financial analysis tasks for accountants.</li>
#                 <li>Behavioral Questions: Evaluating the model’s capacity to articulate responses based on past experiences and specific situations, such as overcoming challenges or managing team dynamics.</li>
#                 <li>Situational Judgment: Testing the model's decision-making and problem-solving skills through hypothetical scenarios, such as resolving workplace conflicts.</li>
#                 <li>Soft Skills Assessment: Measuring the model’s proficiency in communication, teamwork, leadership, and other interpersonal skills.</li>
#                 <li>General Knowledge and Company Fit: Understanding the model's ability to reflect a candidate’s alignment with company values and overall suitability for the role.</li>
#             </ul>  
#              Additionally, these benchmarks offer a valuable tool for learners using LLMs, enabling them to compare the original, human-generated answers with those produced by the model. 
#             Our primary goal is to assess the similarity between these answers, helping users understand the model's strengths and areas where it may diverge from human reasoning or expertise. 
#             This comparison not only aids in learning but also provides insights into how effectively LLMs can emulate human responses in real-world scenarios. 
# #def guidelines_page():
#     st.header("Guidelines")
#     st.write("We expect you to follow these guidelines when contributing to this project.")
#     st.subheader("1. How you should frame the question:")
#     # Section: Focus on Relevant and Specific Content
#     st.subheader("Focus on Relevant and Specific Content")
#     st.markdown("""
#     - **Rule:** Ensure that questions are relevant to the specific capabilities of LLMs being assessed, such as coding, reasoning, or natural language processing.
#     - **Suggestion:** Avoid generic questions like "What is AI?" Instead, ask something like, "Is reasoning ability not a critical benchmark for evaluating LLMs in technical interviews?"
#     """)

#     # Section: Avoid Controversial or Political Topics
#     st.subheader("Avoid Controversial or Political Topics")
#     st.markdown("""
#     - **Rule:** Refrain from including questions related to recent politics or highly controversial topics.
#     - **Suggestion:** Stick to technical or factual content, such as "Is bias detection not an important capability to assess in LLM evaluations?"
#     """)

#     # Section: Cultural and Context-Specific Questions
#     st.subheader("Cultural and Context-Specific Questions")
#     st.markdown("""
#     - **Rule:** When applicable, include questions that are culturally or contextually relevant to the audience or use case.
#     - **Suggestion:** Instead of asking, "What is machine translation?", ask "Is language-specific accuracy not a key factor in evaluating LLMs for machine translation tasks?"
#     """)

#     # Section: Incorporate Negations
#     st.subheader("Incorporate Negations")
#     st.markdown("""
#     - **Rule:** Frame questions that can lead to answers beginning with "No" or involve a negation in the question.
#     - **Suggestion:** For example, "Is common sense reasoning not considered when benchmarking LLMs?"
#     """)

#     # Section: Use Complete, Native Language Questions
#     st.subheader("Use Complete, Native Language Questions")
#     st.markdown("""
#     - **Rule:** Always frame questions entirely in the native language of the intended audience, without mixing languages.
#     - **Suggestion:** Ensure that the question is clear and culturally appropriate, avoiding any unnecessary complexity.
#     """)

#     # Section: Ensure Originality
#     st.subheader("Ensure Originality")
#     st.markdown("""
#     - **Rule:** Avoid repeating or copying questions from other sources. Each question should be unique and tailored to the specific topic.
#     - **Suggestion:** Before finalizing a question, think about its uniqueness and relevance to the title's focus.
#     """)

#     # Section: Avoid Personal Bias and Subjectivity
#     st.subheader("Avoid Personal Bias and Subjectivity")
#     st.markdown("""
#     - **Rule:** Do not include questions that reflect personal views, biases, or subjective opinions.
#     - **Suggestion:** Stick to factual or process-oriented questions, such as "Is the ability to explain outputs not important when evaluating an LLM?"
#     """)
#     st.subheader("2. Examples  ")
    # st.header("Goals and Milestones")
    # st.subheader("Goals:")
    # st.markdown(""" 
    #     <div style="text-align: justify;">
    #         <ul style="list-style-position: inside;">
    #             <li>Develop a state-of-the-art LLMs Benchmark for Interview.</li>
    #             <li>Develop a Comprehensive Benchmarking Framework.</li>
    #             <li>Establish Objective Evaluation Criteria.</li>
    #             <li>Optimize Interview Processes.</li>
    #             <li>Enhance LLM Capabilities Through Feedback.</li>
    #         </ul>
    #     </div>
    #     """, unsafe_allow_html=True)

    # st.subheader("Milestones:")
    # st.markdown(""" 
    #     <div style="text-align: justify;">
    #         <ul style="list-style-position: inside;">
    #             <li>Milestone 1: Initial research and dataset collection.</li>
    #             <li>Milestone 2: Model benchmarking and preliminary testing.</li>
    #             <li>Milestone 3: Dataset Release and Feedback.</li>
    #             <li>Milestone 4: Final evaluation and publication.</li>
    #         </ul>
    #     </div>
    #     """, unsafe_allow_html=True)
    # st.header("Motivation")
    # st.markdown("""
    #     <div style="text-align: justify;">
    #         In the rapidly evolving field of artificial intelligence, large language models (LLMs) are becoming increasingly integral to various applications, from coding assistance to natural language processing tasks like translation and summarization.
    #         As these models grow more sophisticated, it is crucial to have a robust framework for evaluating their capabilities, particularly in high-stakes scenarios such as interviews. <br><br>
    #         The title "Evaluating LLMs in Interviews: Key Benchmarks and Model Capabilities" reflects the importance of systematic assessment in ensuring that LLMs meet the specific demands of real-world applications. 
    #         By establishing and utilizing key benchmarks, interviewers can objectively measure the strengths and weaknesses of different models, leading to more informed decisions.  <br><br>
    #         This approach not only helps identify the most suitable models for specific tasks but also drives the continued improvement of LLMs, ensuring that they evolve to meet the ever-growing expectations of users and developers alike.
    #         In essence, this title underscores the critical role of benchmarks in the interview process, guiding the selection of LLMs that are not only proficient but also well-matched to the nuanced requirements of diverse applications.
    #     </div>
    #     """, unsafe_allow_html=True)
    
    # st.header("Guidelines")
    # st.subheader("How you should frame the question:")
    # st.markdown(""" 
    #     <div style="text-align: justify;">
    #         <ul style="list-style-position: inside;">
    #             <li>Focus on Relevant and Specific Content.</li>
    #             <li>Avoid Controversial or Political Topics.</li>
    #             <li>Cultural and Context-Specific Questions.</li>
    #             <li>Incorporate Negations.</li>
    #             <li>Use Complete, Native Language Questions.</li>
    #             <li>Ensure Originality.</li>
    #             <li>Avoid Personal Bias and Subjectivity</li>
    #         </ul>
    #     </div>
    #     """, unsafe_allow_html=True)

       
    # st.subheader("Example:")
    # image = Image.open("asset/eg.png")  
    # st.image(image=image)  
            