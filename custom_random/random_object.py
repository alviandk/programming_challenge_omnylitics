class MyDefineObject():
    def __init__(self, object):
        self.object = str(object)

    def is_integer(self):
        try:
            int(self.object)
            return True
        except ValueError:
            return False

    def is_real_number(self):
        try:
            float(self.object)
            return True
        except ValueError:
            return False

    def is_alphanumeric(self):
        return any(char.isdigit() for char in self.object)

    def define_object_type(self):
        if self.is_integer():
            return "integer"
        elif self.is_real_number():
            return "real numbers"
        elif self.is_alphanumeric():
            return "alphanumeric"
        else:
            return "alphabetical strings"
