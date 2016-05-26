# 7. Given a string, compute recursively (no loops) a new string where all the
# lowercase 'x' chars have been changed to 'y' chars.
def get_x2yintext(text):
    if len(text) == 0:
        return ''
    elif text[len(text)-1] == 'x':
        return get_x2yintext(text[0:len(text)-1]) + 'y'
    else:
        return get_x2yintext(text[0:len(text)-1]) + text[len(text)-1]
print(get_x2yintext('xmenxe'))
