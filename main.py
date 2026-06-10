class Adult:
    def __init__(self, name, age, weight, height):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height


    def calculate_bmi(self):
        return self.weight / (self.height ** 2)

    def get_bmi_category(self):
        bmi = self.calculate_bmi()

        if bmi < 18.5:
            return "Underweight"
        elif bmi < 24.9:
            return "Normal weight"
        elif bmi < 29.9:
            return "Overweight"
        else:
            return "Obese"


    def print_info(self):
        print("Name:", )
        print("Age:", )
        print("Weight:",self.weight , "kg")
        print("Height:", self.height, "m")





person1=Adult("Resa",18,55,1.69)

print(person1.calculate_bmi())
print(person1.get_bmi_category())
