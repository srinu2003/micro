from menu import flavors,weights,decorations;
from cake import Cake
def generateReceipt(l):
    print("Please Review your order...")
    totalCost = 0
    for cake in l:
        cake.printCake()
        totalCost += cake.calculateCost()
    print('Total Cost : ',totalCost)

orderList = []
print(
'''
Hello!
Welcome to Srinivas' Cake Store.Pleasure to have you
'''
)
while True:
    print('Here are the list of flavors available:')
    print('s.no    flavor   cost/kg')
    for index,flavor in flavors.items():
        print(f'{index}   {flavor[0]}    {flavor[1]}')
    flavor = int(input('Enter your choice:'))
    print('Please choose the quantity:')
    print('s.no    weight')
    for index,weight in enumerate(weights):
        print(f'{index+1}   {weight}')
    weight = weights[int(input('Weight:'))-1]
    cool = input('Do you prefer your cake cool?[Y/N] ').lower()
    isCool = False
    if cool == 'y':
        isCool = True
    step = input('Do you need a step cake?[Y/N] ').lower()
    steps = 0
    if step == 'y':
        steps = int(input('Number of steps:[1,2,3] '))
    print('Choose any decoration:')
    print('s.no    decoration   cost')
    for index,decoration in decorations.items():
        print(f'{index}   {decoration[0]}    {decoration[1]}')
    decoration = int(input('Decoration: ')) 
    orderList.append(Cake(weight,flavors[flavor],isCool,decorations[decoration],steps))
    orderMore = input('Thank you for the order. Would you like to order more?[Y/N] ').lower()
    if orderMore == 'n':
        break

generateReceipt(orderList)
