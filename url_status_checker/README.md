## URL STATUS CHECKER

This script goes through each line in a file and prints out the http status code including redirects.

Run `pip install -r requirements.txt` to install the requirements preferably in a virtual environment.

Run the script with `python checker.py NAME_OF_FILE` where `NAME_OF_FILE` is the name of the file containing the urls.
This would print the status codes to the terminal.

If you want to write them to a file, run it this way instead.
`python checker.py NAME_OF_FILE > FILE_TO_WRITE_TO` where `FILE_TO_WRITE_TO` is the name of the file or path to the file you want to write the status codes to.
