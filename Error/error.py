class myCustomError(TypeError):
    """
    hi hi hi
    """
    def __init__(self, message, code):
        super().__init__(f'Error code: {code}, Error message: {message}')
        self.code = code

err = myCustomError("THis is an error.", 500)
print(err)
