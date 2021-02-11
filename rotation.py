class Rotation(object):

    def is_substring(self, str1, str2):
        return str1 in str2

    def is_rotation(self, str1, str2):
        if str1 is None or str2 is None:
            return False
        if len(str1) != len(str2):
            return False
        return self.is_substring(str1, str2 + str1)
