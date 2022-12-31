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
        print(
            f'''    {this.flavor[0]}       {this.weight}       {this.decoration[0]}       {this.steps}        {cool}'''
        )

    def calculateCost(this):
        cost = this.flavor[1] * this.weight + this.decoration[1]
        if this.isCool:
            cost += cost + (cost * 0.2)
        return cost