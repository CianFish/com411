def cross_bridge(flat):
    if flat < 5:
        for steps in range(0,flat,1):
            print("Crossed Step")
        print("We must keep going")
    else:
        for steps in range(0,flat,1):
            print("Crossed Step")
        print("The bridge is collapsing")

cross_bridge(3)
cross_bridge(6)

#the way below was my other attempt
#def cross_bridge(steps):

#    for steps in range(steps):
#        print("Crossed step")
#
#   if steps < 5:
 #          print("We must keep going!")
  # else:
   #        print("The bridge is collapsing")

#cross_bridge(3)
#cross_bridge(6)