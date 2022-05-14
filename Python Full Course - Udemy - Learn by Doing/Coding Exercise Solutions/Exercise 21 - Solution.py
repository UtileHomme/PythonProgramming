import re
"""
Our definition of a secure filename is:
- The filename must start with an English letters or a number (a-zA-Z0-9).
- The filename can **only** contain English letters, numbers and symbols among these four: `-_()`.
- The filename must end with a proper file extension among `.jpg`, `.jpeg`, `.png` and `.gif`
"""


def is_filename_safe(filename):
    # you only need to change the regular expression (regex) below
    regex = '^[a-zA-Z0-9][a-zA-Z0-9_()-]*(\.jpg|\.jpeg|\.png|\.gif)$'
    # ^[a-zA-Z0-9]      start with a-zA-Z0-9
    # [a-zA-Z0-9_()-]*      then only contains a-zA-Z0-9_()- for any number of times
    # (\.jpg|\.jpeg|\.png|\.gif)$       at last, it must end with one of the four extensions, remember to escape the dot
    # since we check from start to end, it can either match the whole string or none
    return re.match(regex, filename) is not None
