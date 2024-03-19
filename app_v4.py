# Import necessary modules
import os
from dotenv import load_dotenv
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

# Load environment variables
load_dotenv()

# Import specific variables from var file
from var import CTA_1, CTA_2, VIDEO_CTA, VAR_3

# Initialize the language model chain once
template = """You are the marketing guru Dan Kennedy and based on the following text: '{var}' you will rewrite it to make it more compelling, keep the same length. {focus}

Better Text: """
prompt = PromptTemplate(template=template, input_variables=["var"])
llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=1)
llm_chain = LLMChain(prompt=prompt, llm=llm)


def generate_compelling_text(var, default_focus=""):
    """
    Generate compelling text based on a given variable and focus.

    :param var: The original text to be rewritten.
    :param default_focus: The default focus value to use if the user does not provide one.
    :return: The generated compelling text.
    """
    # Prompt the user for a focus value
    print(f"\n")
    print(f"Original Text: '{var}'")
    print(f"\n---------------------------------------\n")
    print(f"Example Focus Value for Inspiration: \n{default_focus}")
    focus = input("Please enter a focus value : ")

    # Check if the focus value provided by the user is an empty string
    if focus == "":
        focus = default_focus

    input_dict = {"var": var, "focus": focus}
    result = llm_chain.run(input_dict)
    print(f"Final Text: {result}")
    print(f"\n---------------------------------------\n")
    return result


def ensure_output_directory(directory_name="output"):
    """
    Ensure that the output directory exists. If not, create it.

    :param directory_name: The name of the directory to check or create.
    """
    if not os.path.exists(directory_name):
        os.makedirs(directory_name)


def get_unique_filename(base_filename, directory_name="output"):
    """
    Generate a unique filename by adding a three-digit suffix if the file already exists within the specified directory.

    :param base_filename: The base name for the file without extension.
    :param directory_name: The directory where the file will be saved.
    :return: A unique filename with a three-digit suffix if needed.
    """
    extension = ".txt"
    counter = 0
    unique_filename = f"{base_filename}{extension}"
    full_path = os.path.join(directory_name, unique_filename)

    while os.path.exists(full_path):
        counter += 1
        suffix = f"{counter:03d}"  # Ensures the suffix is three digits
        unique_filename = f"{base_filename}_{suffix}{extension}"
        full_path = os.path.join(directory_name, unique_filename)
        if counter >= 999:
            raise Exception("Reached maximum number of unique filenames.")

    return full_path


def write_results_to_file(results, base_filename="output", directory_name="output"):
    """
    Write the list of results to an output file with a unique name inside the specified directory.

    :param results: A list of tuples containing variable names and their corresponding generated texts.
    :param base_filename: The base name for the output file.
    :param directory_name: The directory where the file will be saved.
    """
    ensure_output_directory(directory_name)
    unique_filename = get_unique_filename(base_filename, directory_name)
    with open(unique_filename, "w") as file:
        for var_name, text in results:
            file.write(f"{text}\n-------------------------------------\n")


# Collect result
results = []

results.append(
    (
        "CTA_1",
        generate_compelling_text(
            CTA_1,
            """Focus: Utilize the top hack employed by business owners and career professionals to reinvent yourself.
Strive to be recognized not only for your achievements or title, but for who you are as a person.
Emphasize and showcase your ideas, character, and unique perspective to stand out.""",
        ),
    )
)

results.append(("CTA_2", generate_compelling_text(CTA_2)))

results.append(
    (
        "VIDEO_CTA",
        generate_compelling_text(
            VIDEO_CTA,
            """STEP 1: Creating freely and bringing ideas to life without fear or restrictions.
STEP 2: Creating genuine, deep connections with people and overcoming the fear of others' opinions.
STEP 3: Making small tweaks in thinking and operating to reconnect with purpose and passion.
STEP 4: Prioritizing the important things in life such as faith, family, impact, fun, and money.
STEP 5: Letting go of others' expectations and achieving at the level envisioned for oneself.
STEP 6: Finding excitement in what one does, maintaining personal values, and embracing achievements without pretending to struggle.""",
        ),
    )
)

results.append(
    (
        "VAR_3",
        generate_compelling_text(
            VAR_3,
            """
Author names is Roberta.
The author is recognized as a leading voice in personal development.
She was selected as one of 100 women for Times Magazine 2024.
She is the CEO of the 74th fastest-growing company in Canada.
She is the creator of the Diamond Effect™ Neuroscience System.
She has trained over 50,000+ business owners and career professionals in leveraging neuroscience.
She helps individuals achieve their potential and net worth and pay off debt.
""",
        ),
    )
)

# Write all results to the output file at once
write_results_to_file(results)
