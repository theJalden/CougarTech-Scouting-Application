#This is to be the frame work for my most epic project yet, the
#Scouting Program Framework.  I may not know what I'm doing
#But I have the end in mind.  I think that perhaps I could start
#With makeing a module to simplify the program.  Then model out the
#Program, and then find some way to make it all fit together


class RobotList():
    #This class I intend to just be an object containing all of the robots in
    #play. To make my life easier I am making this a sorted list
    def __init__(self):
        self.robotList = []
        self.robotKeys = []


    def __str__(self):
        return str([robot.robotNum for robot in self.robotList])

    def addRobot(self, robot):
        """
        if the list is empty it just adds the robot, like wise if it is
        the largest member of the list.  Otherwise it places the robot before
        the next greatest number through a binary search
        """
        #at this point if two different robots share the same number,
        #it will try to add the robot, but may end up freaking out.
        if robot in self.robotList:
            return False
        elif self.robotList == []:
            self.robotList.append(robot)
            return True
        elif robot.robotNum >= self.robotList[-1].robotNum:
            self.robotList.append(robot)
        else:
            index = self._binSearchIndex(robot.robotNum)
            self.robotList.insert(index, robot)
        self.robotKeys = [robot.robotNum for robot in self.robotList]
        #update the key List


    def getRobot(self, robotNum):
        #get a robot specified by it's id (number)
        pass

    def removeRobot(self, robot):
        #Try statement scheduled to be removed, will take care of error handly in Form
        try: self.robotList.remove(robot)

        except:
            "I need to look up what goes here"
            pass

    def removeRobotNum(self, robotNum):
        #removes a robot based on it's number
        robotVar = self.getRobot(robotNum)
        self.removeRobot(robotVar)

    def _binSearchIndex(self, robotNum):
        #after much consternation this works!, it returns the index of the lowest
        #roboNum above the given one
        import math
        tmpRoboList = self.robotList[:]
        while len(tmpRoboList) != 1:
            tmpIndex = math.ceil(len(tmpRoboList)/2) - 1 #Splits the list in half, bias towards lower number, just what I need!
            if robotNum < tmpRoboList[tmpIndex].robotNum:
                tmpRoboList = tmpRoboList[:(tmpIndex+1)]

            elif robotNum > tmpRoboList[tmpIndex].robotNum:
                tmpRoboList = tmpRoboList[(tmpIndex+1):]
                
        return self.robotList.index(tmpRoboList[0]) #returns the index of the robot just greater than the tested one, I hope


class Robot():
    def __init__(self, number):
        self.robotNum = number
        
        self.weight = None
        self.height = None
        self.length = None
        self.width  = None
        
        self.R = 0 #number of rounds robot has been in

        self.data = {} #A dictionary of lists of length R (the number of Rounds robot has played in)
    def update(self, stats):
        #This function gets a list of new stats to add
        #maybe stats should be a dictionary, so we can iterate over the same keys as self.data
        self.R += 1
        pass

    def edit(self, stats, R):
        pass


class Form():
    #I/O class, This class receives data, then passes it to the core class as a tuple
    def __init__(self):
        pass

    def askNewBot(self):
        #asks the user what the Number for the robot is

        #TODO: Type checking, and more data points (weight dimensions, etc)
        robotNum = int(input("What Number is the robot?: "))
        return robotNum

    def deleteBot(self, botList):
        robotNum = int(input("What Number is the robot?: "))
        if roboNum not in botList.robotKeys:
            print("Error: Robot not in list")
            return False
        #most of the stuff I'm putting in this function should go into core
        else:
            return robotNum
        
    def submit(self, robot):
        #gives the robot the stats tuple, I'll assemble it myself, It will be idiot proof. (with the exception of myself)
        #This needs to change, I'm going to let the core handle this one
        stats = ()
        robot.update(stats) 

class Core():
    def __init__(self):
        self.mainForm = Form()
        self.roboRegister = RobotList()

    def main(self):
        quitApp = False
        while not quitApp:
            whatdo = self.mainForm.menu()
            if whatdo == 1:
                self.addNewBot()
            elif whatdo == 2:
                self.removeBot()
            else:
                quitApp = True
            
        
    def addNewBot(self):
        robotNum = self.mainForm.askNewBot()
        tmpRobot = Robot(robotNum)
        self.roboRegister.addRobot(tmpRobot)

    def removeBot(self):
        robotNum = self.mainForm.deleteBot()
        self.roboRegister.removeRobotNum(robotNum)
    
    
    def test(self):
        i = True
        while i:
            self.addNewBot()
            print(self.roboRegister)
            end = input("Do you want to add another robot?")
            if end.lower().strip() != "yes" and end.lower().strip() != "y":
                i = False

if __name__ == "__main__":
    #This is just for developing purposes, I want a check to make sure the module is working as expected
    newSession = Core()
    newSession.test()
