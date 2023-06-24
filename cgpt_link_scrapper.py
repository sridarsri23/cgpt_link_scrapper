import requests
from bs4 import BeautifulSoup
import re
import os

"""
Code Snippet Extractor
Author: Sridar Sri
License : GNPL v3
"""
# Default values
default_dir = "output"
default_subdir = "code_snippets"
default_file = "code_snippet.txt"

# Get the chat GPT link from user input
chat_gpt_link = input("Enter the chat GPT link: ")

# Download the chat GPT HTML file
response = requests.get(chat_gpt_link)
html_content = response.text

# Write the HTML content to a file
with open('chat_gpt.html', 'w') as f:
    f.write(html_content)

# Write the formatted HTML to a file
formatted_html_file = 'formatted_chat_gpt.html'
with open('chat_gpt.html', 'r') as f:
    soup = BeautifulSoup(f, 'html.parser')
    formatted_html = soup.prettify()

with open(formatted_html_file, 'w') as f:
    f.write(formatted_html)

# Output the path to the formatted HTML file
print("Formatted HTML file path:", os.path.abspath(formatted_html_file))

# Prompt the user to enter the start term
start_term = input("Enter the start term: ")

# Prompt the user to enter the end term
end_term = input("Enter the end term: ")

# Extract the lines between the start and end terms
with open(formatted_html_file, 'r') as f:
    lines = f.readlines()

start_line = next((i for i, line in enumerate(lines, start=1) if re.search(start_term, line, re.IGNORECASE)), None)
end_line = next((i for i, line in enumerate(lines, start=1) if re.search(end_term, line, re.IGNORECASE)), None)

if start_line is None or end_line is None:
    extracted_lines = ""
else:
    extracted_lines = "".join(lines[start_line-1:end_line])

# Write the extracted lines to a temp file
temp_file = 'extracted_lines.txt'
with open(temp_file, 'w') as f:
    f.write(extracted_lines)

# Output the path to the temp file
print("Extracted lines file path:", os.path.abspath(temp_file))

# Use BeautifulSoup to extract code snippets from the extracted lines
soup = BeautifulSoup(extracted_lines, 'html.parser')
code_snippets = soup.find_all('code', class_=re.compile('!whitespace-pre.*'))

# Prompt the user to enter the directory path for code snippet files
output_dir = input(f"Enter the directory path for code snippet files (default: {default_dir}): ") or default_dir

# Create the output directory if not exists
os.makedirs(output_dir, exist_ok=True)

# Prompt the user to enter the file name for the code snippets
output_file_name = input(f"Enter the file name with extension for code snippets (default: {default_file}): ") or default_file

# Determine the file path
output_file_path = os.path.join(os.getcwd(), output_dir, output_file_name)

# Write each code snippet to the file
with open(output_file_path, 'w') as f:
    for snippet in code_snippets:
        snippet_text = snippet.get_text()
        f.write(f"{snippet_text}\n\n")

print(f"Code snippets have been written to: {os.path.abspath(output_file_path)}")

# Remove the temporary files
os.remove('chat_gpt.html')
os.remove('formatted_chat_gpt.html')
os.remove('extracted_lines.txt')
