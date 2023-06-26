import nbformat as nbf
import os
import glob


def main():
    dir_path = "/home/chunibyo/workspace/thorough-pytorch/source/第三章"  # 替换成你的目录路径
    pattern = os.path.join(dir_path, "*.md")
    files = glob.glob(pattern)

    # 按前缀字典顺序排序
    sorted_files = sorted(files, key=lambda x: os.path.basename(x))

    nb = nbf.v4.new_notebook()

    for file in sorted_files:
        flag = False
        with open(file, "r") as file:
            lines = file.read().split("\n")
            tmp = ""
            for line in lines:
                if line.startswith("```"):
                    if flag:
                        nb["cells"].append(nbf.v4.new_code_cell(tmp))
                    else:
                        nb["cells"].append(nbf.v4.new_markdown_cell(tmp))
                    tmp = ""
                    flag = not flag
                else:
                    tmp += line + "\n"
        nbf.write(nb, "example.ipynb")


if __name__ == "__main__":
    main()

"""
# 创建一个空的Notebook对象

    
       """
