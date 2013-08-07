#This program might be getting a little to hot to handle
#I'm going to want to add some sort of logging feature soon, I'm going to want
#to find some way to export the list out, and import it again.
#Also find a way to display the robot list

from catsMod import *

class Core():
    def __init__(self):
        #Handles the objects so they don't have to
        self.mainForm = Form()
        self.roboRegister = RobotList()

    def main(self):
        #Super simple main loop menu, if it doesn't see something it likes it complains
        #but doesn't crash
        quitApp = False
        while not quitApp:
            whatdo = self.mainForm.menu()
            if whatdo == "1":
                self.addNewBot()
            elif whatdo == "2":
                self.removeBot()
            elif whatdo == "3":
                self.displayBots()
            elif whatdo == "4":
                quitApp = True
            else:
                self.mainForm.typeError()
            
        
    def addNewBot(self):
        robotData = self.mainForm.askNewBot()
        tmpRobot = Robot(robotData)
        self.roboRegister.addRobot(tmpRobot)
        if tmpRobot in self.roboRegister:
            self.mainForm.addBotConfirm()
        else:
            self.mainForm.generalError()

    def removeBot(self):
        robotNum = self.mainForm.deleteBot(self.roboRegister)
        self.roboRegister.removeRobotNum(robotNum)

    def displayBots(self):
        self.mainForm.robotListHeader()
        for robot in self.roboRegister:
            self.mainForm.printRobot(robot)
        input()
        
    def test(self):
        #I don't think this needs to be in here anymore, but we'll see what may come of it.
        i = True
        while i:
            self.addNewBot()
            print(self.roboRegister)
            end = input("Do you want to add another robot?")
            if end.lower().strip() != "yes" and end.lower().strip() != "y":
                i = False

if __name__ == "__main__":
    newSession = Core()
    newSession.main()
