# Python YouTube Search

## Explanation

A simple Python script which launches a YouTube search, with keywords pasted to the clipboard, or by arguments in a command line.

## Usage

A. Use this command line

`python3 youtube_search.py keywords`

B. Use the clipboard (for macOS users)

- create a shell script, a file with `.command` extension
- add the following two lines

`#!/usr/bin/env bash`

`python3 /path/to/python_script.py`

- make the file executable

`chmod u+x your_script.command`

- Now, you can copy a keyword to the clipboard
- open the Spotlight `(⌘-SPACE)`, enter `your_script.command` to run the Python script
