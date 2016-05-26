
# 9. Given a string, compute recursively a new string where all the
# adjacent chars are now separated by a "*".
def get_xeverywhere(text):
    if len(text) == 0:
        return ''
    else:
        return get_xeverywhere(text[0:len(text)-1]) + text[len(text)-1] + '*'
print(get_xeverywhere('xmenxe'))
