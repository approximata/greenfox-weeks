# 8. Given a string, compute recursively a new string where all the 'x' chars have been removed.
def get_x2noneintext(text):
    if len(text) == 0:
        return ''
    elif text[len(text)-1] == 'x':
        return get_x2noneintext(text[0:len(text)-1]) + ''
    else:
        return get_x2noneintext(text[0:len(text)-1]) + text[len(text)-1]
print(get_x2noneintext('xmenxe'))
