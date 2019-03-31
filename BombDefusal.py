######################################################
#           Project: RaspPi Bomb Defusal             #
# Names: Alex Anderson, Shawn Chauvin, Karey Higuera #
# Description: A real life implementation of KTANE   #
#       (Keep Talking and Nobody Explodes)           #
######################################################

#Base class for the bomb. This will handle all major game functions.
class Bomb(object):
    def __init__(self, timer=60):
        self.timer = timer
        self.strikes = 0
        self.modules = [0,0,0]

    @property
    def timer(self):
        return self._timer

    @property
    def strikes(self):
        return self._strikes

    @property
    def modules(self):
        return self._modules

    @timer.setter
    def timer(self, time):
        self._timer = time

    @strikes.setter
    def strikes(self, strikes):
        self._strikes = strikes
        #if the bomb has reached 3 strikes, game over
        if (self._strikes >= 3):
            self.explode()

    @modules.setter
    def modules(self, modules):
        self._modules = modules
        #if all the modules are solved, finish the game
        if self._modules == [1,1,1]:
            self.win()

    def moduleComplete(self, modNumber):
        #pull a copy of the list of module states
        updatedModules = self.modules
        #set the indicated module to complete
        updatedModules[modNumber] = 1
        #push this updated list to the Bomb
        self.modules = updatedModules

    def explode(self):
        print "BOOM!"

    def win(self):
        print "You win!"

#Abstract Module class. All sub-modules extend this.
class Module(object):

    def __init__(self, modNumber, bomb):
        #This modNumber is the spot in the Bomb modules array that marks whether this module is complete or not.
        self.modNumber = modNumber
        #This is a reference to the main bomb instance, the owner of this module
        self.bomb = bomb

    @property
    def modNumber(self):
        return self._modNumber

    @property
    def bomb(self):
        return self._bomb

    @modNumber.setter
    def modNumber(self, modNumber):
        self._modNumber = modNumber

    @bomb.setter
    def bomb(self, bomb):
        self._bomb = bomb

    #add a strike to the main bomb instance
    def strike(self):
        self.bomb.strikes += 1

    #let the bomb know that this module is complete
    def solve(self):
        self.bomb.moduleComplete(self.modNumber)


##SAMPLE CODE##

#This is our bomb, it has a timer of 60 seconds (though obviously there isn't a real timer yet)
bomb = Bomb(60)

#Here we create a cut the wires module (we give it a module number and tell it which bomb it's a part of)
cutTheWires = Module(0, bomb)

#then we can mess up and get a strike on it
cutTheWires.strike()

#we can see that we now have a strike
print "You have {} strike(s).".format(bomb.strikes)

#Let's create two more cut the wires modules
cutTheWires2 = Module(1, bomb)
cutTheWires3 = Module(2, bomb)

#Let's see which modules are complete
print "Here's the state of the modules: {}".format(bomb.modules)

#we can solve the first module
cutTheWires.solve()

#let's check the state of the modules one more time
print "Here's the state of the modules: {}".format(bomb.modules)

#let's solve the other two modules
cutTheWires2.solve()
cutTheWires3.solve()