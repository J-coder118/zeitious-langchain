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

global_title = ""
global_exp = ""
global_imagine = ""

# Initialize the language model chain once
# template = """You are the marketing guru Dan Kennedy and based on the following text: '{var}' you will rewrite it to make it more compelling, keep the same length. {focus}
exp_pmt = """You are a seasoned {var} coach. You are assisting a client (me) who has this problem {focus}, pls generate the TEN what client will learn from out this coach. Be sure to generate TEN description and title in paragraph."""  

coach_pmt = """give me an author's introduction of from this short information about me: {user_intro}"""

title_pmt = """give me One and only attractive title for website from this subject without quotation.
                subject: {subject}"""

imagine_pmt = """
I used this sentence.
"👉🏾&nbsp;</i></i>Waking
    up in the morning feeling completely
    excited about who you are BEING in the world
    and what are you doing with your time.<br /><span
        class="dark-color-text"><i><i>👉🏾&nbsp;</i></i>Feeling
        that spark of passion, things that
        deeply matters to
        you</span><br /><i><i>👉🏾&nbsp;</i></i>Imagine just
    being myself in every situation,
    not having to put on a show for anyone."
give me points like this for an {subject} coach website
    
    """


llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=1, api_key=api_key)
prompt_exp = PromptTemplate(template=exp_pmt, input_variables=["var", "focus"])
llm_chain_exp = LLMChain(prompt=prompt_exp, llm=llm)

prompt_coach = PromptTemplate(template=coach_pmt, input_variables=["subject", "user_intro"])
llm_chain_coach = LLMChain(prompt=prompt_coach, llm=llm)

prompt_title = PromptTemplate(template=title_pmt, input_variables=["subject"])
llm_chain_title = LLMChain(prompt=prompt_title, llm=llm)

prompt_imagine = PromptTemplate(template=imagine_pmt, input_variables=["subject"])
llm_imagine_title = LLMChain(prompt=prompt_imagine, llm=llm)

# Define a function to generate compelling text using the language model chain
def generate_experience_text(var, focus):
    input_dict = {"var": var, "focus": focus}
    result = llm_chain_exp.invoke(input_dict)
    # print("reslut", result)
    return result["text"]

def generate_title(subject):
    input_dict = {"subject": subject}
    result = llm_chain_title.invoke(input_dict)
    return result["text"]

def generate_coach_text(user_intro):
    input_dict = {"user_intro": user_intro}
    result = llm_chain_coach.invoke(input_dict)
    return result["text"]

def gen_exp(subject, problem):
    exp = generate_experience_text(subject, problem)

    experiences = exp.split("\n\n")
    if len(experiences) != 10:
        print("eee", len(experiences))
        # exp = regenerate_experience_text(subject, problem)
        # experiences = exp.split("\n\n")
        experiences = exp.split("\n")
        return experiences
        # gen_exp(subject, problem)
    else:
        print("---------------------", len(experiences))
        return experiences
    
def generate_imagine(subject):
    input_dict = {"subject": subject}
    result = llm_imagine_title.invoke(input_dict)
    return result["text"]

@app.route('/', methods=['POST'])
def index():
    return "hello"

@app.route('/experience', methods=['POST'])
def experience():
    try :
        global global_exp, global_title, global_imagine
        subject = request.form['subject']
        problem = request.form['problem']
        # intro = request.form['intro']

        experiences = gen_exp(subject, problem)
        title = generate_title(subject)
        imagine = generate_imagine(subject)
        global_exp = experiences
        global_title = title
        global_imagine = imagine
        return f"{len(experiences)}"
    except Exception as e:
        return f"error_subject: {e}"



@app.route('/intro', methods=['POST'])
def intro():
    global global_exp, global_title, global_imagine
    try:
        intro = request.form['intro']
        # print("experience", global_exp)
        introduction = generate_coach_text(intro)
        # Insert variable values into the template using string formatting
        rendered_html = HTML.format(title=global_title, imagine=global_imagine,  pa0=global_exp[0],pa1=global_exp[1], pa2=global_exp[2], pa3=global_exp[3], pa4=global_exp[4], pa5=global_exp[5], pa6=global_exp[6], pa7=global_exp[7], pa8=global_exp[8], pa9=global_exp[9],  info=introduction)

        return render_template_string(rendered_html)
    except Exception as e:
        return f"error_intro: {e}"
        # Process the data received from the frontend
    
@app.route('/visit')
def display_html():
    return render_template('html_1/output.html')


if __name__ == '__main__':
    app.run()