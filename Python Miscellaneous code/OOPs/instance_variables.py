from pprint import pprint


class HtmlDocument:
    version = 5
    extension = 'html'


pprint(HtmlDocument.__dict__)

# Class variables
print(HtmlDocument.extension)
print(HtmlDocument.version)


home = HtmlDocument()

# checking instance variables
pprint(home.__dict__)

home.version = 6

# Now instance dict will have a value
pprint(home.__dict__)

# If you change the class variables, this change will also reflect in the instance variables
HtmlDocument.media_type = 'text/html'
print(home.media_type)



