class MyCustomError(TypeError):
    """
    Exception raised when a specific error code is needed
    """
    def __init__(self, message, code):
        super().__init__(f'Error code {code} : {message}')
        self.code = code


err =  MyCustomError('An error occurred.', 500)
# raise MyCustomError('An error occurred.', 500)

# The below code prints the content of triple string
print(err.__doc__)
