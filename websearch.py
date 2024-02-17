# source of this code: https://www.educative.io/answers/how-to-enable-web-search-with-gpt-api
#git clone https://github.com/bdambrosio/llmsearch.git
#pip3 install -r requirements.txt

import openai
import search_service
import os
# Initialize OpenAI API
openai.api_key = os.environ['SECRET_KEY']

def main():
    # Get user input
    user_prompt = input("Enter your query about a topic or website: ")

    # Use OpenAI GPT to generate a query for llmsearch
    extraction_prompt = f"I have a plugin that can extract information from the web. Based on the user's query '{user_prompt}', what should I search for on the web?"
    extraction_query = openai.Completion.create(engine="davinci", prompt=extraction_prompt, max_tokens=100).choices[0].text.strip()

    # Search the web using llmsearch's from_gpt function
    search_results = search_service.from_gpt(extraction_query, search_level="full")  # You can choose between "quick" and "full" for search_level

    # Extract the most relevant result (for simplicity, we're taking the first result)
    relevant_content = search_results[0]['response']

    # Use GPT to generate an answer based on the extracted content and user's initial prompt
    answer_prompt = f"The user asked: '{user_prompt}'. The extracted content from the web is: '{relevant_content}'. How should I respond?"
    answer = openai.Completion.create(engine="davinci", prompt=answer_prompt, max_tokens=200).choices[0].text.strip()

    # Print the answer
    print(f"Answer: {answer}")

if __name__ == "__main__":
    main()