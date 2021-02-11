class RevereString(object):

    def reverse(self, chars):
        if chars is None or not chars:
            return chars

        size = len(chars)
        for i in range(size // 2):
            chars[i], chars[size - 1 - i] = chars[size - 1 - i], chars[i]
        return chars

    def reverse_alt(chars):
        if chars is None or not chars:
            return chars
        return chars[::-1]