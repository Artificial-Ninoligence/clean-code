import re

def get_file(file_path):
    if len(file_path) > 0 and file_path[len(file_path) - 1] == '/':
        return file_path

    try:
        p_location = file_path.rindex('/')
    except:
        p_location = -1
    dirName = ''

    if p_location >= 0:
        dirName = file_path[0: p_location + 1]
    else:
        dirName = ''

    return dirName

def getFilenamePart(file_name):
    try:
        file_name.rindex('/')
    except:
        return file_name

    pos = file_name.rindex('/')
    base_name = file_name[pos + 1:]
    return base_name

def get_extension_part(file_name):
    try:
        occurrences = [m.start() for m in re.finditer('\.', file_name)]
        return file_name[occurrences[-1] + 1:]
    except:
        pass

    return ''


assert(get_file("log/cups/access_log") == "log/cups/")
assert(get_file("log/cups/") == "log/cups/")
assert(get_file("cups/access_log") == "cups/")
assert(get_file("access_log") == "")
assert(getFilenamePart("log/cups/access_log") == "access_log")
assert(getFilenamePart("log/cups/") == "")
assert(getFilenamePart("cups/access_log") == "access_log")
assert(getFilenamePart("access_log") == "access_log")
assert(get_extension_part("log/cups/access_log") == "")
assert(get_extension_part("base/FileHelper.cpp") == "cpp")
assert(get_extension_part("base/FileHelper.cpp.bak") == "bak") 
