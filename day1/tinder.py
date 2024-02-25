class Person:
    def __init__(self, name, gender, age, profession, fav_show, fav_food):
        self.name = name
        self.gender = gender
        self.age = age
        self.profession = profession
        self.fav_show = fav_show
        self.fav_movie = fav_food


person1 = Person("john", "male", 30, "doctor", "HouseMD", "hamburger")
person2 = Person("marry", "female", 24, "lawyer", "suits", "hamburger")
person3 = Person("mike", "male", 35, "engineer", "friends", "pizza")
person4 = Person("rachel", "female", 28, "fashion", "espn", "salad")
data = [person1, person2, person3, person4]

print("creating a new user:")
name = input("what is your name: ")
gender = input("male / female: ")
age = int(input("how old are you: "))
profession = input("what is your profession: ")
fav_show = input("what is your favorite TV show: ")
fav_food = input("what are your favorite food: ")

user = Person(name, gender, age, profession, fav_show, fav_food)
print("all set, now we need you to till us about the one you would like to meet ")
match_found = False

while not match_found:
    rule1 = input("do you like to meet a male/female : ")
    rule2 = int(input("what is the max age you would like to meet: "))
    for p in data:
        if rule1 == p.gender and rule2 >= p.age:
            match_found = True
            print(f"good news, we have a match for you, the name is  {p.name} ")
    if match_found:
        break
    print("sorry, not match for this data. try again please: ")


print("we will send you data soon, good luck ;) ")
