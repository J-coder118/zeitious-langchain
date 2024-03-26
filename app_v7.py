from dotenv import load_dotenv
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from flask import Flask, request, render_template, render_template_string
# from langchain.chat_models import ChatOpenAI
import os
import time

load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')

app = Flask(__name__)
# Import specific variables from var file
from var import  HTML

global_title = ""
global_exp = ""
global_subject = ""

# Initialize the language model chain once
# template = """You are the marketing guru Dan Kennedy and based on the following text: '{var}' you will rewrite it to make it more compelling, keep the same length. {focus}
exp_pmt = """As a {var} coach, you are assisting a client (me) who has this problem {focus}, pls generate the 6 descriptions that client will learn from out this coach like this type
'
Understanding the Basics of Machine Learning: In this session, you will learn about the fundamental concepts of machine learning, including algorithms, models, and data preprocessing techniques. We will break down complex topics into easily digestible chunks to help you grasp the key principles of ML.@

' """  

coach_pmt = """give me an author's introduction in dynamic way from this short information about me: {user_intro}"""

title_pmt = """give me One and only attractive title for website from this subject without quotation.
                subject: {subject}"""

# imagine_pmt = """
# I used this sentence.
# "👉🏾&nbsp;</i></i>Waking
#     up in the morning feeling completely
#     excited about who you are BEING in the world
#     and what are you doing with your time.<br /><span
#         class="dark-color-text"><i><i>👉🏾&nbsp;</i></i>Feeling
#         that spark of passion, things that
#         deeply matters to
#         you</span><br /><i><i>👉🏾&nbsp;</i></i>Imagine just
#     being myself in every situation,
#     not having to put on a show for anyone."
# give me points like this(with 👉🏾 and put <br /> at end of each sentence) for an {subject} coach website
    
#     """

htitle_pmt = """
"<span class="white-color-text"><span data-cke-bookmark="1"
style="display: none">&nbsp;</span>
2024 brings change.<br />
The world is changing.<br />
As the world evolves, so does your work and industry.
<br />
Unlock your full potential with expert guidance! Join us to turn your dreams into reality.<br /><br />
<span class="primary-color-text"
style="color: #bf973f"><b>Now is the moment to discover how to enhance yourself.</b></span></span><br />"
generate a similar content like this "" for a {subject} coach (put <br /> at end of each sentence)
"""

imagine_pmt = """
"👉🏾 Waking up in the morning feeling completely excited about who you are BEING in the world and what are you doing with your time.
 👉🏾 Feeling that spark of passion, things that deeply matters to you.
 👉🏾 Imagine just being myself in every situation, not having to put on a show for anyone."
give me points like above (with 👉🏾 and put <br /> at end of each sentence) for an {subject} coach website
    """

last_pmt = """
generate a content like this for a {subject} coach (put <br /> at end of each sentence)
"Contrary to popular belief, I did not just work HARDER...
I committed to myself and my family to learn how to LEARN.
To change how I think.
I learned how to re-invent myself."
"""

footer_pmt = """
generate a smaple quote like this 
"BECAUSE REINVENTING YOURSELF IS NOT AN OPTION…
IT'S A NECESSITY
" 
for a {subject} coach (put <br /> at end of each sentence)

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

prompt_htitle = PromptTemplate(template=htitle_pmt, input_variables=["subject"])
llm_header_title = LLMChain(prompt=prompt_htitle, llm=llm)

prompt_last = PromptTemplate(template=last_pmt, input_variables=["subject"])
llm_last_title = LLMChain(prompt=prompt_htitle, llm=llm)

prompt_footer = PromptTemplate(template=footer_pmt, input_variables=["subject"])
llm_footer_title = LLMChain(prompt=prompt_footer, llm=llm)

# Define a function to generate compelling text using the language model chain
def generate_experience_text(var, focus):
    input_dict = {"var": var, "focus": focus}
    result = llm_chain_exp.invoke(input_dict)
    # print("reslut", result)
    return result["text"]

def generate_title(subject):
    input_dict = {"subject": subject}
    result = llm_chain_title.invoke(input_dict)
    return result["text"].replace('"', '')

def generate_coach_text(user_intro):
    input_dict = {"user_intro": user_intro}
    result = llm_chain_coach.invoke(input_dict)
    return result["text"]

def gen_exp(subject, problem):
    exp = generate_experience_text(subject, problem)

    experiences = exp.split("@")
    # print(experiences)
    if len(experiences) != 6:
        print("eee", len(experiences))
        # exp = regenerate_experience_text(subject, problem)
        # experiences = exp.split("\n\n")
        experiences = exp.split("\n\n")
        print("---------------------ddddd", len(experiences))
        return experiences
        # gen_exp(subject, problem)
    else:
        print("---------------------@", len(experiences))
    return experiences

def generate_header_title(subject):
    input_dict = {"subject": subject}
    result = llm_header_title.invoke(input_dict)
    return result["text"].replace('"', '')
    
def generate_imagine(subject):
    input_dict = {"subject": subject}
    result = llm_imagine_title.invoke(input_dict)
    return result["text"].replace('"', '')

def generate_last(subject):
    input_dict = {"subject": subject}
    result = llm_last_title.invoke(input_dict)
    return result["text"].replace('"', '')

def generate_footer(subject):
    input_dict = {"subject": subject}
    result = llm_footer_title.invoke(input_dict)
    return result["text"].replace('"', '')


@app.route('/', methods=['POST'])
def index():
    return "hello"

@app.route('/experience', methods=['POST'])
def experience():
    try :
        global global_exp, global_title, global_subject
        subject = request.form['subject']
        problem = request.form['problem']
        # intro = request.form['intro']

        experiences = gen_exp(subject, problem)
        # time.sleep(5)
        title = generate_title(subject)
        
        print("experience", experiences)
        global_exp = experiences
        global_title = title
        global_subject = subject
        print(experiences)
        return f"{len(experiences)}"
    except Exception as e:
        return f"error_subject: {e}"



@app.route('/intro', methods=['POST'])
def intro():
    global global_exp, global_title, global_subject
    try:
        intro = request.form['intro']
        # print("experience", global_exp)
        introduction = generate_coach_text(intro)
        imagine = generate_imagine(global_subject)
        htitle = generate_header_title(global_subject)

        last = generate_last(global_subject)
        footer = generate_footer(global_subject)
        # Insert variable values into the template using string formatting
        print("ss", global_exp[0])
        ttx = global_exp[0].split(":")
        title0 = ttx[0]
        sentence0 = ttx[1]
        print("--------------------", title0, "++++++++++++++++++", sentence0)
        ttx = global_exp[1].split(":")
        title1 = ttx[0]
        sentence1 = ttx[1]

        ttx = global_exp[2].split(":")
        title2 = ttx[0]
        sentence2 = ttx[1]
        ttx = global_exp[3].split(":")
        title3 = ttx[0]
        sentence3 = ttx[1]
        ttx = global_exp[4].split(":")
        title4 = ttx[0]
        sentence4 = ttx[1]

        ttx = global_exp[5].split(":")
        title5 = ttx[0]
        sentence5 = ttx[1]
        rendered_html = HTML.format(title=global_title,  header_title = htitle, imagine=imagine,
                                    title0 = title0, sentence0 = sentence0, title1 = title1, sentence1 = sentence1, title2 = title2, sentence2 = sentence2,
                                    title3 = title3, sentence3 = sentence3, title4 = title4, sentence4 = sentence4, title5 = title5, sentence5 = sentence5, info=introduction, last = last, footer = footer)

        return render_template_string(rendered_html)
    except Exception as e:
        return f"error_intro: {e}"
        # Process the data received from the frontend
    
@app.route('/visit')
def display_html():
    return render_template('html_1/output.html')


if __name__ == '__main__':
    app.run()