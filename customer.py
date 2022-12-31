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
# Chocolatey v1.1.0
# Chocolatey detected you are not running from an elevated command shell
#  (cmd/powershell).

#  You may experience errors - many functions/packages
#  require admin rights. Only advanced users should run choco w/out an
#  elevated shell. When you open the command shell, you should ensure
#  that you do so with "Run as Administrator" selected. If you are
#  attempting to use Chocolatey in a non-administrator setting, you
#  must select a different location other than the default install
#  location. See
#  https://docs.chocolatey.org/en-us/choco/setup#non-administrative-install
#  for details.


#  Do you want to continue?([Y]es/[N]o):
print(
'''
SR Cakes v1.0
Hello!!! Welcome to Srinivas' Cake Store..😋
Pleasure to have you..😊
'''
)
while True:
    print('Here is the list of flavors available:')
    
    #flavours
    print('s.no    flavor   cost/kg')
    for index,flavor in flavors.items():
        print(f'{index}   {flavor[0]}    {flavor[1]}')
    flavor = int(input('Enter your choice:'))
    
    #Quantity
    print('Please choose the quantity:')
    print('s.no    weight')
    for index,weight in enumerate(weights):
        print(f'{index+1}   {weight}')
    weight = weights[int(input('Weight:'))-1]

    #cool
    cool = input('Do you prefer your cake cool?([Y]es/[N]o): ')
    isCool = False
    if cool == 'y'or'Y':
        isCool = True
    
    #steps
    step = input('Do you need a step cake?([Y]es/[N]o): ').lower()
    steps = 0
    if step == 'y':
        steps = int(input('Enter number of steps(Avilable:[1,2,3]): '))
    
    #decaarations
    print('Choose any decoration:')
    print('s.no    decoration   cost')
    for index,decoration in decorations.items():
        print(f'{index}   {decoration[0]}    {decoration[1]}')
    decoration = int(input('Decoration: '))

    #ordering 
    orderList.append(Cake(weight,flavors[flavor],isCool,decorations[decoration],steps))
    orderMore = input('Thank you for the order. Would you like to order more?[Y/N] ')
    if orderMore == 'n':
        break

generateReceipt(orderList)#Final step

