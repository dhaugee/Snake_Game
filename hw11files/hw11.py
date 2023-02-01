# Problem A.
class Item:
    '''
    Purpose: An item of clothing
    Instance variables: The item's price in USD, category (where it's worn),
    name and store in which it's sold
    Methods: A string method to return neatly printed info regarding an item and
    an inequality method to determine which items cost more than others
    '''
    def __init__(self, csv_string, store):
        csv_list = csv_string.split(',')
        self.name = csv_list[0]
        self.price = float(csv_list[1])
        self.category = csv_list[2]
        self.store = store

    def __str__(self):
        return f'{self.name} ({self.category}): ${self.price}'

    def __lt__(self, other):
        return self.price < other.price

# Problem B.
class Store:
    '''
    Purpose: A store where items are sold
    Instance variables: The name of the store and a list of their items w/ info
    Methods: A string method that returns the store name and a list of the items
    sold there with relevant info (name of item, price, category)
    '''
    def __init__(self, name, filename):
        inventory = open(filename)
        inventory_list = inventory.readlines()
        inventory_list = inventory_list[1:]
        self.name = name
        self.items = []
        for i in range(len(inventory_list)):
            inventory_list[i] = inventory_list[i].strip()
            self.items.append(Item(inventory_list[i], name))

    def __str__(self):
        store_name = f'{self.name}\n'
        for i in range(len(self.items)):
            store_name += f'{self.items[i]}\n'
        return store_name

    # Problem C.
    def cheapest_outfit(self):
        fitdict = {}
        for i in range(len(self.items)):
            if self.items[i].category in fitdict:
                if self.items[i].price > fitdict[self.items[i].category]:
                    fitdict[self.items[i].category] = fitdict[self.items[i].category]
                elif self.items[i].price < fitdict[self.items[i].category]:
                    fitdict[self.items[i].category] = self.items[i].price
            else:
                fitdict[self.items[i].category] = self.items[i].price
        return fitdict

# Problem D.
def choose_store(store_list):
    tcosts_list = []
    stores_list = []
    for store in store_list:
        fitdict = store.cheapest_outfit()
        total_cost = 0
        if len(fitdict.keys()) == 4:
            for cost in fitdict.values():
                total_cost += cost
            tcosts_list.append(total_cost)
            stores_list.append(store.name)
            print(f'{store.name}: ${round(total_cost, 2)}')
        else:
            print(f'{store.name}: Outfit Incomplete')
    return stores_list[tcosts_list.index(min(tcosts_list))]
