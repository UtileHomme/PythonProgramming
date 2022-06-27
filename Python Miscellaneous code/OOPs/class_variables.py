class HtmlDocument:
    extension = 'html'
    version = '5'

#1.a Accessing class variables
print(HtmlDocument.extension, HtmlDocument.version)

#1.b Another way of accessing class variables
extension = getattr(HtmlDocument, 'extension')
version = getattr(HtmlDocument, 'version')

print(extension, version)

# In case the class variable doesn't exist, one can assign a default value as well

mediaType = getattr(HtmlDocument, 'mediaType', 'application/json')

print(mediaType)

#2. How to set value of a variable or add a new variable to class at runtime

# Set the value of an existing variable
HtmlDocument.mediaType = 'text/html'

# Add a new variable to class named mediatype
setattr(HtmlDocument, 'mediatype', 'text/html')

print(HtmlDocument.mediaType)
print(HtmlDocument.mediatype)

#3. How to delete a class variable

del HtmlDocument.mediaType

# OR

delattr(HtmlDocument, 'mediatype')

