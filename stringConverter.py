def uniqueChar(string, char):
    lpos = string.find(char)
    rpos = string.rfind(char)
    if lpos == rpos:
        return True
    return False

def ConvertString(string):
    result = ""
    for character in string:
        if uniqueChar(string, character):
            result += "("
        else:
            result += ")"
    return result

while(1):
    testString = input().lower()
    print(ConvertString(testString))
