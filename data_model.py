
# a = 'Real Python'

# b = ['Real','Python']

# print(a.__len__())

# print(b[0])

# print(b.__getitem__(0))

# print(dir(a))


# Giving the length of your objects using len()

class Order:
    def __init__(self, cart, customer):
        self.cart = cart 
        self.customer = customer

    def __len__(self):
        return len(self.cart)
    
order = Order(['banana','apple','mango'],'Real Python')

print(len(order))




