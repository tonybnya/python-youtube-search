#! python3
# youtube_search.py - launches a YouTube search using keywords
# from clipboard or command line

import webbrowser
import sys
import pyperclip

BASE_URL = "https://www.youtube.com/results?search_query="

if len(sys.argv) > 1:
    # Get the keywords from the command line
    keywords = "+".join(sys.argv[1:])
else:
    # Get the keywords from the clipboard
    keywords = pyperclip.paste()


if __name__ == "__main__":
    webbrowser.open(BASE_URL + keywords)
