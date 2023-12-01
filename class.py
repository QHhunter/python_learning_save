class CuteCat:
    def __init__(self,cat_name,cat_age,cat_color):
        self.name = cat_name
        self.age = cat_age
        self.color = cat_color

    def speak(self):
        print("喵" * self.age)

    def think(self, content):
        print(f"小猫{self.name}在思考{content}...")


cat1 = CuteCat("小白", 5, "绿色")
cat1.think("逗猫棒还是作妖")
cat1.speak()