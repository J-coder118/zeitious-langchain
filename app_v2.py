import os
import csv
from dotenv import load_dotenv
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

# Load environment variables
load_dotenv()

# Initialize the language model chain once
template = """You are the marketing guru Dan Kennedy and based on the following text: '{example}' you will rewrite it to make it more compelling, keep the same length. {focus}

Better Text: """
prompt = PromptTemplate(template=template, input_variables=["example", "focus"])
llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=1)
llm_chain = LLMChain(prompt=prompt, llm=llm)


def generate_compelling_text(example, focus=""):
    """
    Generate compelling text based on a given example and optional focus.

    :param example: The original text to be rewritten.
    :param focus: Additional context or instructions for rewriting.
    :return: The generated compelling text.
    """
    input_dict = {"example": example, "focus": focus}
    result = llm_chain.run(input_dict)
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
            file.write(f"{var_name}: {text}\n-------------------------------------\n")


def read_input_csv(file_path):
    """
    Read the input CSV file and return a list of dictionaries with 'name', 'example', and 'focus' keys.

    :param file_path: Path to the input CSV file.
    :return: List of dictionaries with 'name', 'example', and 'focus'.
    """
    data = []
    with open(file_path, mode="r") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    return data


# Collect result
results = []

# Read the input CSV file
input_data = read_input_csv("input.csv")

# Process each row in the CSV file
for row in input_data:
    name = row["name"]
    example = row["example"]
    focus = row["focus"]
    generated_text = generate_compelling_text(example, focus)
    results.append((name, generated_text))

# Write all results to the output file at once
write_results_to_file(results)
