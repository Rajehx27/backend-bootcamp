### where is the interacticity? how to I use the funcitons?


# the main problem in this soltution is to try the compistion and to know when to use it.

category = {
    "None": 0,
    "Electronics": 1,
    "Priced": 2,
    "Foreign": 3,
    "Colored": 4,
}


class Item:
    def __init__(self, name, weight, category="None"):
        self.name = name
        self.weight = weight
        self.category = category

    def get_weight(self):
        return self.weight

    def get_category(self):
        return self.category

    def print_item(self):
        print(self.name)

    def print_item_and_category(self):
        print(self.name, ", ", self.category)


class Electronics(Item):
    def __init__(self, name, weight, category, brand, feature):
        # if category != "Electronics":
        #     print("category mismatch")
        #     return None
        super().__init__(name=name, weight=weight, category=category)
        self.brand = brand
        self.feature = feature


class Priced(Item):
    def __init__(self, name, weight, category, price):
        super().__init__(name, weight, category)
        self.price = price


class Foreign(Item):
    def __init__(self, name, weight, category, origin):
        super().__init__(name, weight, category)
        self.origin = origin


class Colored(Item):
    def __init__(self, name, weight, category, color):
        super().__init__(name, weight, category)
        self.color = color


# solution compistion
class Charger(Item):
    def __init__(self, name, weight, category, color, price, size, brand):
        ### interesting implementation!
        p1 = Priced(name, weight, category, price)
        p2 = Colored(name, weight, category, color)
        p3 = Electronics(name, weight, category, brand, feature="None")
        self.color = p2.color
        self.price = p1.price
        self.size = size
        self.brand = p3.brand
        self.weight = weight


class Bag:
    def __init__(self):
        self.items = []
        self.weight = 0
        ### why private?
        self.__maxItmesNum = 6
        self.__maxWeight = 80

    def add_item(self, item):
        if len(self.items) >= self.__maxItmesNum or (item.getWeight() + self.weight > self.__maxWeight):
            print("can't add this item, Bag is full")
        else:
            self.items.append(item)
            self.weight += item.getWeight()
            # we could sort list by category if needed

    def remove_item(self, item):
        if item in self.items:
            self.weight -= item.getWeight()
            self.items.remove(item)

    def print_all(self):
        if len(self.items) == 0:
            print("Bag is empty")
        else:
            for item in self.items:
                item.print_item()

    def print_item_and_category(self):
        if len(self.items) == 0:
            print("Bag is empty")
        else:
            for item in self.items:
                item.print_item_and_category()

    def print_items_from_category(self, category):
        if len(self.items) == 0:
            print("Bag is empty")
        else:
            temp = 0
            for item in self.items:
                if item.get_category() == category:
                    item.print_item()
                    temp += 1
            if temp == 0:
                print("no items in bag from this category")


my_bag = Bag()
# print(my_bag.print_all())

# charger = Electronics(name="Charger", weight=12, category="Electronics", brand="Lenovo", feature="Medium size")

passport = Colored(name="Passport", weight=1, category="Colored", color="blue")
sunglasses = Colored(name="Sunglasses", weight=10, category="Colored", color="black")
sneakers = Foreign(name="Sneakers", weight=10, category="Foreign", origin="Spain")
smartphones = Electronics(name="smartphones", weight=9, category="Electronics", brand="Apple", feature="AMOLED Display")
laptop = Electronics(name="laptop", weight=60, category="Electronics", brand="Dell", feature="I7 Processor")
smartwatch = Electronics(name="smartwatch", weight=44, category="Electronics", brand="Samsung", feature="Fitness")
campus = Electronics(name="campus", weight=4, category="Electronics", brand="Samsung", feature="high accuracy")

charger = Charger("universal", 12, "Electronics", "black", 50, "Medium", "Lenovo")

print(isinstance(charger, Electronics))
