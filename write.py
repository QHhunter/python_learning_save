user_input = input("请输入访客名（q终止）")
with open("guest_book.txt", "a") as f:
    while user_input != "q":
        f.write(user_input + "\n")
        print(f"欢迎{user_input}")
        user_input = input("请输入访客名（q终止）")


"""
Python输出函数print加上 f 的作用：即print(f" ")
主要作用就是格式化字符串，加f后可以在字符串里面使用用花括号括起来的变量和表达式，
包含的{}表达式在程序运行时会被表达式的值代替。
"""