import streamlit as st
from dotenv import load_dotenv
from langchain import LLMChain
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
# from langchain.chat_models import ChatOpenAI
import os

load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')

# Import specific variables from var file
from var import CTA_1, CTA_2, VIDEO_CTA, VAR_3, HTML


# Initialize the language model chain once
# template = """You are the marketing guru Dan Kennedy and based on the following text: '{var}' you will rewrite it to make it more compelling, keep the same length. {focus}
exp_pmt = """You are a seasoned {var} coach. You are assisting a client (me) in identifying the exact way my client thinks about this challenge in their words. Please List out TEN hell experiences my client goes through DAILY related to this problem: LIST YOUR PROBLEM HERE. e.g. They need life insurance but don't have it.
Imagine they are talking with a friend at Starbucks about this problem. Exactly what would they say? (Remember they are not a professional)
Please share 10 different ways this hits them on a daily basis.”
Remember that you can also tell chatty to speak to the pain of someone who is a professional, or "doing well" so it doesn't go  for the bottom half of the pool and give me result as 6 paragraphs .
This is problem: {focus}"""  

coach_pmt = """you are a talented {subject} coach. As {subject} coach, generate perfect introduction and use 'Life Coach' as a name of coach"""


llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=1, api_key=api_key)
prompt_exp = PromptTemplate(template=exp_pmt, input_variables=["var", "focus"])
llm_chain_exp = LLMChain(prompt=prompt_exp, llm=llm)

prompt_coach = PromptTemplate(template=coach_pmt, input_variables=["subject", "problem"])
llm_chain_coach = LLMChain(prompt=prompt_coach, llm=llm)


# Define a function to generate compelling text using the language model chain
def generate_experience_text(var, focus):
    input_dict = {"var": var, "focus": focus}
    result = llm_chain_exp.run(input_dict)
    return result

def generate_coach_text(subject, problem):
    input_dict = {"subject": subject, "problem": problem}
    result = llm_chain_coach.run(input_dict)
    return result


def save_uploaded_file(uploaded_file, save_path):
    with open(os.path.join(save_path, uploaded_file.name), "wb") as f:
        f.write(uploaded_file.getbuffer())


# Streamlit app layout
st.title("Client Challenge: Define Problem")


# Section for CTA_2
st.header("Subject")
subject = st.text_area(
    "What is your subject to know?",
    value="",
    key="subject1",
)

# Update the session state variable
st.session_state.subject = subject


# Section for CTA_1
st.header("Problem")
problem = st.text_area(
    "What is your problem?",
    value="",
    key="cta1_focus",
)
if st.button("Generate experience:", key="experience_btn"):
    experience = generate_experience_text(subject, problem)
    coach = generate_coach_text(subject, problem)
    st.session_state.experience = experience
    st.session_state.intro_info = coach
    st.write(experience)
    st.write(coach)


# st.title("File Uploader")

# uploaded_file = st.file_uploader("Choose a file", type=['png', 'jpg', 'jpeg'])

# if uploaded_file is not None:
#     st.image(uploaded_file, caption='Uploaded Image', use_column_width=True)
    
#     save_path = st.text_input("Enter the path to save the file:", "./saved_images")
    
#     if st.button("Save File"):
#         if not os.path.exists(save_path):
#             os.makedirs(save_path)
#         save_uploaded_file(uploaded_file, save_path)
#         st.success("File saved successfully!")

# Section for VAR_3
# st.header("Author Introduction")
# intro_info = st.text_area(
#     "What should Author section focus on?",
#     value="""Author names is Roberta.
# The author is recognized as a leading voice in personal development.
# She was selected as one of 100 women for Times Magazine 2024.
# She is the CEO of the 74th fastest-growing company in Canada.
# She is the creator of the Diamond Effect™ Neuroscience System.
# She has trained over 50,000+ business owners and career professionals in leveraging neuroscience.
# She helps individuals achieve their potential and net worth and pay off debt.
# """,
#     key="var3_focus",
# )
# if st.button("Generate Coach:", key="coach_btn"):
#     experience = generate_coach_text(subject, problem)
    
#     st.session_state.experience = experience
#     st.write(experience)


if st.button("Generate HTML", key="html_button"):
    pa = st.session_state.experience.split("\n\n")
    print("result",pa, len(pa), st.session_state.subject, st.session_state.intro_info, 
    pa[0],pa[1],pa[2],pa[3],pa[4],pa[5],pa[6],pa[7],pa[8],pa[9]
    )
    

    # Insert variable values into the template using string formatting
    rendered_html = HTML.format(subject=st.session_state.subject, pa0=pa[0],pa1=pa[1], pa2=pa[2], pa3=pa[3], pa4=pa[4], pa5=pa[5], pa6=pa[6], pa7=pa[7], pa8=pa[8], pa9=pa[9],  info=st.session_state.intro_info)

    # Save the rendered HTML to a file
    with open("html_1/output.html", "w", encoding="utf-8") as file:
        file.write(rendered_html)




