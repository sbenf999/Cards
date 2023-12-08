class Person:
    def __init__(self, forname, surname, gender, height, weight):
        self.forname = forname
        self.surname = surname
        self.gender = gender
        self.height = height
        self.weight = weight
        self.fullname = self.forname + " " + self.surname
        
    def give_info(self, item):
        item = item.lower()
        attributes: dict = {
            "forname": self.forname,
            "surname": self.surname,
            "gender": self.gender,
            "height": self.height,
            "weight": self.weight,
            "fullname": self.fullname,
        }
        
        return attributes[item]
        
    def set_forname(self, new):
        self.forname = new
        
    def set_surname(self, new):
        self.surname = new
    
    def set_gender(self, new):
        self.gender = new
    
    def set_height(self, new):
        self.height = new
        
    def set_weight(self, new):
        self.weight = new
        
    def __str__(self):
        return f"{self.forname}, {self.surname}, {self.gender}, {self.height}, {self.weight}"

        
Josh = Person("Josh", "Seddon", "Male", "5'11", "70")
forname = Josh.give_info("forname")
print(forname)
Josh.set_forname("Holmes")
forname = Josh.give_info("forname")
print(forname)
print(Josh)