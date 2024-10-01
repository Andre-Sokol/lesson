from pprint import pprint


class Product:
    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}.'


class Shop(Product):

    def __init__(self, name, weight, category, __file_name='products.txt'):
        super().__init__(name, weight, category)
        self.__file_name = __file_name

    def get_products(self):
        file = open(self.__file_name, 'r')
        print(f'{file.read()}')
        file.close()


    def add(self, *products):
        for i in products:
            file = open(self.__file_name, 'r')
            if str(i.name) and str(i.weight) not in file.read():
                file.close()
                file = open(self.__file_name, 'a')
                file.write(f'\n{str(i)}')
                file.close()
            else:
                print(f'Продукт {str(i)} уже есть в магазине.')





s1 = Shop('', '', '')
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)
print(s1.get_products())
