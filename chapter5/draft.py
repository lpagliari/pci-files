import optimization
s = [1,4,3,2,7,3,6,3,2,4,5,3]

reload(optimization)
domain = [(0,9)] * (len(optimization.people) * 2)
s = optimization.randomoptimize(domain, optimization.schedulecost)
optimization.schedulecost(s)
optimization.printschedule(s)

s = optimization.hillclimb(domain, optimization.schedulecost)
optimization.schedulecost(s)
optimization.printschedule(s)

s = optimization.annealingoptimize(domain, optimization.schedulecost, T=10000, cool=0.95, step=3)
optimization.schedulecost(s)
optimization.printschedule(s)

s = optimization.geneticoptimize(domain, optimization.schedulecost)
optimization.printschedule(s)

#######################
import dorm
dorm.printsolution([0,0,0,0,0,0,0,0,0,0])

s = optimization.randomoptimize(dorm.domain, dorm.dormcost)
dorm.dormcost(s)
s = optimization.geneticoptimize(dorm.domain, dorm.dormcost)
dorm.printsolution(s)

#######################
import socialnetwork
import optimization
sol = optimization.randomoptimize(socialnetwork.domain, socialnetwork.crosscount)
socialnetwork.crosscount(sol)
sol = optimization.annealingoptimize(socialnetwork.domain, socialnetwork.crosscount, step = 50, cool = 0.99)
socialnetwork.crosscount( sol)

#######################
random_sol = [0, 3, 5, 7, 5, 0, 3, 8, 0, 2, 9, 5] # generated originaly randomly
reload(optimization)
s = optimization.hillclimb(domain, optimization.schedulecost, random_sol)
optimization.schedulecost(s)
optimization.printschedule(s)

