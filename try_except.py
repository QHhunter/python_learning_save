try:
    user_weight = float(input("请输入体重（kg）"))
    user_height = float(input("请输入身高（m）"))
    user_BMI = user_weight / user_height ** 2
except ValueError:
    print("输入不合理，请重新运行，并输入正确数字")
except ZeroDivisionError:
    print("身高不能为零，请重新运行，并输入正确数字")
except:
    print("发生未知错误，请重新运行")
else:
    print("您的BMI:" + str(user_BMI))