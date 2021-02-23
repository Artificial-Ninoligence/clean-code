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


def get_file_name(file_path):
    try:
        slash_index = file_path.rindex('/')
    except:
        return file_path

    file_name = file_path[slash_index + 1:]

    return file_name

def get_file_extension(file_path):
    try:
        last_dot = [m.start() for m in re.finditer('\.', file_path)]
        file_extension = file_path[last_dot[-1] + 1:]
        return file_extension
    except:
        return ''

assert(get_directory_name("log/cups/access_log") == "log/cups/")
assert(get_directory_name("log/cups/") == "log/cups/")
assert(get_directory_name("cups/access_log") == "cups/")
assert(get_directory_name("access_log") == "")
assert(get_file_name("log/cups/access_log") == "access_log")
assert(get_file_name("log/cups/") == "")
assert(get_file_name("cups/access_log") == "access_log")
assert(get_file_name("access_log") == "access_log")
assert(get_file_extension("log/cups/access_log") == "")
assert(get_file_extension("base/FileHelper.cpp") == "cpp")
assert(get_file_extension("base/FileHelper.cpp.bak") == "bak") 
