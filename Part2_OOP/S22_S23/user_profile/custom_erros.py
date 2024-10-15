class EnvalidEmailError(Exception):
    def __init__(self, msg="Invalid email!"):
        self.msg = msg 
        super().__init__(self.msg)