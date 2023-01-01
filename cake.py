from menu import flavors,weights,decorations;
class Cake:
    def __init__(this,weight,flavor,isCool,decoration,steps):
        this.weight = weight
        this.flavor = flavor
        this.isCool = isCool
        this.decoration = decoration
        this.steps = steps

    def printCake(this):
        if this.isCool:
            cool = "Yes"
        else:
            cool = "No"
        if this.steps == 0:
            this.steps = 'N/A'
        else:
            this.steps = str(this.steps)
        print('| %s | %s | %s | %s | %s | %s |'%(this.flavor[0].center(15),str(this.weight).center(6),cool.center(5),this.decoration[0].center(12),this.steps.center(5),str(this.calculateCost()).center(5))
        )

    def calculateCost(this):
        cost = this.flavor[1] * this.weight + this.decoration[1]
        if this.isCool:
            cost += cost + (cost * 0.2)
        return cost