# Compelling Text Generator

## Video Example of Program Running
https://www.berrycast.com/conversations/58ed2259-56b7-52ac-8dc8-917c6683c70f

## Functionality

The Compelling Text Generator is a Streamlit application that uses OpenAI's GPT-3.5-turbo model to rewrite provided text inputs into more compelling content. Users can specify the focus for the rewriting process, and the application will output text that aligns with the given directives.

### Key Functionalities:

- **Environment Variables**: Securely configures app settings.
- **Dynamic Content Generation**: Utilizes variables from an external file for input content.
- **Language Model Chain**: Employs LangChain with a custom prompt template for text processing.
- **Compelling Text Generation**: Offers a function to generate rewritten text based on user input and focus areas.
- **User Interface**: Provides interactive sections for different types of Call to Action and Author Introduction inputs.

## How to Run the Application

1. Install the necessary Python packages:
   ```bash
   pip install streamlit dotenv langchain langchain_openai
   ```

2. Ensure you have a `.env` file with required environment variables in your project directory.

3. Start the application by running the following command in your terminal:
   ```bash
   streamlit run app_v5.py
   ```
// "functions": {
  //   "app_v7.py": {"maxDuration": 100}
  // }