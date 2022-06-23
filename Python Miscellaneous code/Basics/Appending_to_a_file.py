more_lines = ['', 'Append text lines', 'The end']

with open('readme2.txt', 'a') as f:
    f.writelines('\n'.join(more_lines))