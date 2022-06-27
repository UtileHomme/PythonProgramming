class Request:
    def send(self):
        print('Sent')

# This is a function
print(Request.send)

http_request = Request()

# This is a method
print(http_request.send)

# <class 'function'>
print(type(Request.send))

# <class 'method'>
print(type(http_request.send))

class Request1:
    def send(*args):
        print('Sent', args)

http_request1 = Request1()

# Sent ()
# None
# Here args is empty
print(Request1.send())

# Sent (<__main__.Request1 object at 0x000001E934BC3BB0>,)
# None
# Here args is not empty
print(http_request1.send())



