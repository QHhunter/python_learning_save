"""
f = open("./learning_python.txt", "r", encoding="utf-8")
content = f.read()
print(content)
f.close()
"""
"""
读练习
"""


"""
with open("./learning_python.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print(content)

"""





"""
read第二种写法
"""


"""
with open("./learning_python.txt", "r", encoding="utf-8") as f:
    print(f.readlines())
"""
"""
with open("./learning_python.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line)
 """
with open("./learning_python.txt", "r", encoding="utf-8") as f:
    line_list = f.readlines()
print(line_list)