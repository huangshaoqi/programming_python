# -*- coding:utf-8 -*-
import os
import pprint


def find_py(path, py_files=[]):
    if os.path.exists(path):
        root_path = os.path.abspath(path)
        # print(root_path)
        root_files = os.listdir(root_path)
        for file in root_files:
            filename = os.path.join(root_path, file)
            if os.path.isfile(filename):
                if os.path.splitext(file)[1] == ".py":
                    py_files.append(filename)
                else:
                    pass
            else:
                path = os.path.join(root_path, file)
                # print(path)
                find_py(path)
    else:
        print("找不到路径！")
    return py_files


if __name__ == "__main__":
    pprint.pprint(find_py("./.."))
