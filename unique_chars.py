class UniqueChars(object):

    def has_unique_chars(self, str):
        if str is None:
            return False
        char_set = set()
        for char in str:
            if char in char_set:
                return False
            else:
                char_set.add(char)
        return True