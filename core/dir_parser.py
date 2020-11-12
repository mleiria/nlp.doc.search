import os

ext_ok = set()
# Init set with allowed extensions
ext_ok.update(['pdf', 'docx', 'txt', 'doc', 'jpg', 'eml', 'tif'])

ext_nok = set()

files_to_parse = list()
files_to_not_parse = list()


def get_list_of_files(dir_name):
    # create a list of file and sub directories
    # names in the given directory
    list_of_files = os.listdir(dir_name)
    all_files = list()
    # Iterate over all the entries
    for entry in list_of_files:
        # Create full path
        full_path = os.path.join(dir_name, entry)
        # If entry is a directory then get the list of files in this directory
        if os.path.isdir(full_path):
            all_files = all_files + get_list_of_files(full_path)
        else:
            all_files.append(full_path)
    return all_files


def save_txt(file_to_save, text):
    if text.strip() != "":
        # if the text is not empty
        f = open(file_to_save, "w")
        f.write(text)
        f.close()
