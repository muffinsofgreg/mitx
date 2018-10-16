class Food:

    def __init__(self, n, v, w):
        self.name = n
        self.value = v
        self.calories = w

    def getValue(self):
        return self.value

    def getCost(self):
        return self.calories

    def density(self):
        return self.getValue() / self.getCost()

    def __repr__(self):
        return self.name + ': <' + str(self.value) \
            + ', ' + str(self.calories) + '>'


# Should probably build a menu class, else menu dies with function
# def buildMenu(names, values, calories):
#    """names, values, calories lists of same length.
#       name a list of strings
#       values and calories lists of numbers
#       returns list of Foods"""
#
#    menu = []
#
#    for i in range(len(values)):
#        menu.append(Food(names[i], values[i], calories[i]))
#    return menu


class Menu:

    def __init__(self, names, values, calories):
        self.names = names
        self.values = values
        self.calories = calories
        self.menu = self.buildMenu(self.names, self.values,
                                   self.calories)

    def buildMenu(self, names, values, calories):
        menu = []
        for i in range(len(self.values)):
            menu.append(Food(names[i], values[i],
                             calories[i]))
        return menu

    def __repr__(self):
        """appends Food objects to list, then calls str()
           on each for __str__, and returns string object"""

        items = []
        for item in self.menu:
            items.append(item)
        s = '\n'.join([str(element) for element in items])
        return s


def greedy(items, maxCost, keyFunction):
    """Assumes items a list, maxCost >= 0,
        keyfunction maps elements of items to numbers"""
    # Copy bc "sorted() returns copy, no mutation"
    itemsCopy = sorted(items, key=keyFunction, reverse=True)

    result = []
    totalValue, totalCost = 0.0, 0.0

    for i in range(len(itemsCopy)):
        if (totalCost + itemsCopy[i].getCost()) <= maxCost:
            result.append(itemsCopy[i])
            totalCost += itemsCopy[i].getCost()
            totalValue += itemsCopy[i].getValue()

    return (result, totalValue)


def testGreedy(items, constraint, keyFunction):
    taken, val = greedy(items, constraint, keyFunction)
    print('Total value of items taken =', val)
    for item in taken:
        print(' ', item)


def testGreedys(foods, maxUnits):
    print('Use greedy by value to allocate', maxUnits, 'calories')
    testGreedy(foods, maxUnits, Food.getValue)
    print('\nUse greedy by cost to allocate', maxUnits, 'calories')
    testGreedy(foods, maxUnits,
               lambda x: 1 / Food.getCost(x))
    print('\nUse greedy by density to allocate', maxUnits, 'calories')
    testGreedy(foods, maxUnits, Food.density)


if __name__ == "__main__":
    names = ['wine', 'beer', 'pizza', 'burger', 'fries', 'cola', 'apple',
             'donut', 'cake']
    values = [89, 90, 95, 100, 90, 79, 50, 10]
    calories = [123, 154, 258, 354, 365, 150, 95, 195]
    foods = Menu(names, values, calories)

    testGreedys(foods.menu, 750)
