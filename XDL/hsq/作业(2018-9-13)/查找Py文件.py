# -*- coding:utf-8 -*-
import os


def find(path):
    py_files = []

    def find_py(path):
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
                    find_py(filename)
        else:
            print("找不到路径！")
        return py_files

    return find_py(path)


if __name__ == "__main__":
    print(find("./"))
    print(find("./"))
