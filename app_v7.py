from dotenv import load_dotenv
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from flask import Flask, request, render_template, render_template_string
# from langchain.chat_models import ChatOpenAI
import os

load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')

app = Flask(__name__)
# Import specific variables from var file
from var import  HTML

global_sub = ""
global_exp = ""

# Initialize the language model chain once
# template = """You are the marketing guru Dan Kennedy and based on the following text: '{var}' you will rewrite it to make it more compelling, keep the same length. {focus}
exp_pmt = """You are a seasoned {var} coach. You are assisting a client (me) in identifying the exact way my client thinks about this challenge in their words. Please List out TEN hell experiences my client goes through DAILY related to this problem: LIST YOUR PROBLEM HERE. e.g. They need life insurance but don't have it.
Imagine they are talking with a friend at Starbucks about this problem. Exactly what would they say? (Remember they are not a professional)
Please share 10 different ways this hits them on a daily basis.”
Remember that you can also tell chatty to speak to the pain of someone who is a professional, or "doing well" so it doesn't go  for the bottom half of the pool and give me result as 6 paragraphs .
This is problem: {focus}"""  

coach_pmt = """you are a talented {subject} coach. As {subject} coach, with this user's intro:{user_intro}, generate perfect introduction to user and use 'Life Coach' as a name of coach"""


llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=1, api_key=api_key)
prompt_exp = PromptTemplate(template=exp_pmt, input_variables=["var", "focus"])
llm_chain_exp = LLMChain(prompt=prompt_exp, llm=llm)

prompt_coach = PromptTemplate(template=coach_pmt, input_variables=["subject", "problem", "user_intro"])
llm_chain_coach = LLMChain(prompt=prompt_coach, llm=llm)


# Define a function to generate compelling text using the language model chain
def generate_experience_text(var, focus):
    input_dict = {"var": var, "focus": focus}
    result = llm_chain_exp.invoke(input_dict)
    return result["text"]

def regenerate_experience_text(var, focus):
    input_dict = {"var": var, "focus": focus}
    result = llm_chain_exp.invoke(input_dict)
    return result["text"]

def generate_coach_text(subject, user_intro):
    input_dict = {"subject": subject, "user_intro": user_intro}
    result = llm_chain_coach.invoke(input_dict)
    return result["text"]

def gen_exp(subject, problem):
    exp = generate_experience_text(subject, problem)
    print(exp)

    experiences = exp.split("\n\n")
    if len(experiences) != 10:
        print("eee")
        # exp = regenerate_experience_text(subject, problem)
        # experiences = exp.split("\n\n")
        experiences = exp.split("\n")
        return experiences
        # gen_exp(subject, problem)
    else:
        return experiences

@app.route('/', methods=['POST'])
def index():
    return "hello"

@app.route('/result', methods=['POST'])
def subject():
    try :
        subject = request.form['subject']
        problem = request.form['problem']
        intro = request.form['intro']

        experiences = gen_exp(subject, problem)

        print("experience", experiences)
        introduction = generate_coach_text(subject, intro)
        # Insert variable values into the template using string formatting
        rendered_html = HTML.format(pa0=experiences[0],pa1=experiences[1], pa2=experiences[2], pa3=experiences[3], pa4=experiences[4], pa5=experiences[5], pa6=experiences[6], pa7=experiences[7], pa8=experiences[8], pa9=experiences[9],  info=introduction)
    # Save the rendered HTML to a file
        # file_path = 'templates/html_1/output.html'
        # os.chmod(file_path, 0o600)
        # with open("templates/html_1/output.html", "w", encoding="utf-8") as file:
        #     file.write(rendered_html)
        # permissions = os.stat(file_path).st_mode
        return render_template_string(rendered_html)
    except Exception as e:
        return f"error_subject: {e}"
    

# @app.route('/problem', methods=['POST'])
# def problem():
#     global global_exp, global_sub
#     try:
#         problem = request.form['problem']
#         experiences = gen_exp(global_sub, problem)
#         global_exp = experiences
#         return global_exp
#     except Exception as e:
#         return f"error_problem: {e}"

# @app.route('/intro', methods=['POST'])
# def intro():
#     global global_exp, global_sub
#     try:
#         intro = request.form['intro']
#         introduction = generate_coach_text(global_sub, intro)
#         # Insert variable values into the template using string formatting
#         rendered_html = HTML.format(pa0=global_exp[0],pa1=global_exp[1], pa2=global_exp[2], pa3=global_exp[3], pa4=global_exp[4], pa5=global_exp[5], pa6=global_exp[6], pa7=global_exp[7], pa8=global_exp[8], pa9=global_exp[9],  info=introduction)
#     # Save the rendered HTML to a file
#         # file_path = 'templates/html_1/output.html'
#         # os.chmod(file_path, 0o600)
#         # with open("templates/html_1/output.html", "w", encoding="utf-8") as file:
#         #     file.write(rendered_html)
#         # permissions = os.stat(file_path).st_mode
#         return render_template_string(rendered_html)
#     except Exception as e:
#         return f"error_intro: {e}"
#         # Process the data received from the frontend
    
# @app.route('/visit')
# def display_html():
#     return render_template('html_1/output.html')


if __name__ == '__main__':
    app.run()