import os


def tool_spec_ext_file(root_path, target_ext):
    # target_ext: txt, py, csv... (without ".")
    if "." not in target_ext:
        target_ext = "." + target_ext

    target_list = []
    for root, dirs, files in os.walk(root_path):
        for file in files:
            ext = file[file.find("."):]
            if target_ext == ext:
                target_list.append(os.path.join(root, file))

    return target_list


def tool_spec_name_folder(root_path, target):
    target_list = []
    files = os.listdir(root_path)
    for f in files:
        file_path = os.path.join(root_path, f)
        if os.path.isdir(file_path):
            if target in f:
                target_list.append(file_path)
    return target_list




