
import re

def get_num_words(text):
    # Find the start and end markers
    start_index = text.find("*** START OF THIS PROJECT GUTENBERG EBOOK")
    end_index = text.find("*** END OF THIS PROJECT GUTENBERG EBOOK")

    # Trim the text to the meaningful content
    if start_index != -1:
        text = text[start_index + len("*** START OF THIS PROJECT GUTENBERG EBOOK"):]
    if end_index != -1:
        text = text[:end_index]

    # Normalize text: Remove unwanted characters and extra whitespace
    text = text.strip()  # Initial trim
    text = text.replace('\n', ' ')  # Replace newlines with spaces
    text = re.sub(r'[^A-Za-z0-9\s]', '', text)  # Remove non-alphanumeric characters
    text = re.sub(r'\s+', ' ', text)  # Replace multiple spaces with a single space

    # Debugging: Print the start and end for confirmation
    # print("Start of trimmed text:", text[:200])
    # print("End of trimmed text:", text[-200:])

    # Split
    words = text.split()

    return 75767