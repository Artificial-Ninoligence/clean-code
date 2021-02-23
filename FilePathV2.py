import re

#* Retrieve all directories in the given file path
def get_directory_name(file_path):
    dir_name = ""

    if len(file_path) > 0 and file_path[len(file_path) - 1] == '/':
        return file_path

    try:
        slash_index = file_path.rindex('/')
    except:
        slash_index = -1

    if slash_index >= 0:
        dir_name = file_path[0: slash_index + 1]
    else:
        dir_name = ''

    return dir_name


def get_file_name(file_name):
    try:
        slash_index = file_name.rindex('/')
    except:
        return file_name

    base_name = file_name[slash_index + 1:]
    return base_name

def get_extension_part(file_name):
    try:
        occurrences = [m.start() for m in re.finditer('\.', file_name)]
        return file_name[occurrences[-1] + 1:]
    except:
        pass

    return ''


assert(get_directory_name("log/cups/access_log") == "log/cups/")
assert(get_directory_name("log/cups/") == "log/cups/")
assert(get_directory_name("cups/access_log") == "cups/")
assert(get_directory_name("access_log") == "")
assert(getFilenamePart("log/cups/access_log") == "access_log")
assert(getFilenamePart("log/cups/") == "")
assert(getFilenamePart("cups/access_log") == "access_log")
assert(getFilenamePart("access_log") == "access_log")
assert(get_extension_part("log/cups/access_log") == "")
assert(get_extension_part("base/FileHelper.cpp") == "cpp")
assert(get_extension_part("base/FileHelper.cpp.bak") == "bak") 
