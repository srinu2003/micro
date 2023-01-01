from menu import flavors,weights,decorations;
from cake import Cake
def generateReceipt(l):
    print("Please Review your order...")
    print('| %s | %s | %s | %s | %s | %s | %s |'%('S.no'.center(4),'Flavor'.center(15),'Weight'.center(6),'Cool'.center(5),'Decoration'.center(12),'Steps'.center(5),'Cost'.center(5)))
    print('-'*68)
    totalCost = 0
    for i,cake in enumerate(l):
        print('| %s'%str(i+1).center(4),end=' ')
        cake.printCake()
        totalCost += cake.calculateCost()
    print('Total Cost : ',totalCost)

orderList = []
# Chocolatey v1.1.0
# Chocolatey detected you are not running from an elevated command shell
#  (cmd/powershell).

#  You may experience errors!! - many functions/packages
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
    sno = 'S.no'
    fl = 'Flavor'
    cos = 'Cost / kg'
    print('| %s| %s| %s |' %(sno.center(4),fl.center(15),cos.center(10)))
    print('-'*38)
    for index,flavor in flavors.items():
        print('| %s| %s| %s |'%(str(index).center(4),flavor[0].center(15) ,str(flavor[1]).center(10)))
    flavor = int(input('Enter your choice:'))
    
    #Quantity
    print('Please choose the quantity:')
    print('| %s| %s |'%(sno.center(4),'weight'.center(6)))
    print('-'*16)
    for index,weight in enumerate(weights):
        print('| %s| %s | '%(str(index).center(4),str(weight).center(6)))
    weight = weights[int(input('Weight:'))-1]

    #cool
    cool = input('Do you prefer your cake cool?([Y]es/[N]o): ')
    isCool = False
    if cool == 'y' or cool =='Y':
        isCool = True
    
    #steps
    step = input('Do you need a step cake?([Y]es/[N]o): ').lower()
    steps = 0
    if step == 'y':
        steps = int(input('Enter number of steps(Available:[1,2,3]): '))
    
    #decaarations
    print('Choose any decoration:')
    print('| %s| %s| %s |'%(sno.center(4),'Decoration'.center(12),'cost'.center(5)))
    print('-'*30)
    for index,decoration in decorations.items():
        print('| %s| %s| %s |'%(str(index).center(4),decoration[0].center(12),str(decoration[1]).center(5)))
    decoration = int(input('Decoration: '))

    #ordering 
    orderList.append(Cake(weight,flavors[flavor],isCool,decorations[decoration],steps))
    orderMore = input('Thank you for the order. Would you like to order more?[Y/N] ')
    if orderMore == 'n':
        break

generateReceipt(orderList)#Final step

