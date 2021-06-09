class Mobile:
    def __init__(self, name):
        self.name = name

class MobileStore:
    def __init__(self):
        self.mobiles = []

    def add_mobile(self, new_mobile): 
        if isinstance(new_mobile, Mobile):
            self.mobiles.append(new_mobile)
        else:
            raise TypeError("Mobile must be a object of Mobile class")

oneplus = Mobile("Oneplus 6T")
samsung = "Samsung galaxy g8"
mobostore = MobileStore()
mobostore.add_mobile(oneplus)
print(mobostore.mobiles)
# mobostore.add_mobile(samsung)
# print(mobostore.mobiles)



