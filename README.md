Chat GPT Link Scrapper

This script extracts code snippets from a chat GPT Link based on specified start and end terms.
I've created this for my own requirements. Feel free to branch out.

Prerequisites

    Python 3.x
    Required Python extensions:
        beautifulsoup4
        requests

Usage

    Clone or download the code snippet extractor repository.
    Install the required Python extensions by running the following command:

pip install -r requirements.txt

Open a terminal or command prompt and navigate to the code snippet extractor directory.
Run the script using the following command:

    python code_snippet_extractor.py

    Follow the prompts:
        Enter the chat GPT link: [Enter the URL of the chat GPT HTML file]
        Enter the start term: [Enter the start term for extracting code snippets]
        Enter the end term: [Enter the end term for extracting code snippets]
        Enter the directory path for code snippet files (default: output): [Enter the directory path where the code snippet files should be saved]
        Enter the file name with extension for code snippets (default: code_snippet.txt): [Enter the file name for the code snippet file]

Output

The script will download the chat GPT HTML file, extract the code snippets between the specified start and end terms, and save them in the specified directory as a separate file.

The path to the generated code snippet file will be displayed in the terminal upon successful extraction.
Cleanup

The script will automatically remove any temporary files generated during the extraction process.

Tips on preparing the Chat GPT Link.
Make sure you entered specific random terms in between chat to identify code snippets separately. i.e "##srat1##", "##end1##" and so.
Example char link: https://chat.openai.com/share/92890f7f-d440-4ada-8e9b-e744927b1937
