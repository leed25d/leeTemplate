import unittest
from rover import Rover

class RoverTest(unittest.TestCase):

    def testCreation(self):
      self.assertIsNotNone(Rover())

    def testStartsAtOrigin(self):
      rover = Rover()
      self.assertEquals(0,rover.x)
      self.assertEquals(0,rover.y)

    def testBlockedMoveForward_2(self):
        rover= Rover(((2,0),))
        self.assertEquals(0, rover.bearing)
        rover.move("f")
        rover.move("f")
        self.assertEquals(1, rover.x)
        self.assertEquals(0, rover.y)
        
    def testMoveForward_2(self):
        rover= Rover()
        self.assertEquals(0, rover.bearing)
        rover.move("f")
        rover.move("f")
        self.assertEquals(2, rover.x)
        self.assertEquals(0, rover.y)

        
    def testMoveDiametricForward_2(self):
        rover= Rover()
        self.assertEquals(0, rover.bearing)
        rover.turn("l")
        rover.turn("l")
        rover.move("f")
        rover.move("f")
        self.assertEquals(180, rover.bearing)
        self.assertEquals(-2, rover.x)
        self.assertEquals(0, rover.y)
        
    def testMove_270_Forward_2(self):
        rover= Rover()
        self.assertEquals(0, rover.bearing)
        rover.turn("right")
        rover.move("f")
        rover.move("f")
        self.assertEquals(270, rover.bearing)
        self.assertEquals(0, rover.x)
        self.assertEquals(-2, rover.y)
        
    def testTurnLeft(self):
        rover= Rover()
        self.assertEquals(0, rover.bearing)
        rover.turn("l")
        self.assertEquals(90, rover.bearing)
        
    def testTurnRight(self):
        rover= Rover()
        self.assertEquals(0, rover.bearing)
        rover.turn("right")
        self.assertEquals(270, rover.bearing)

    def testTurnRightRightLeft(self):
        rover= Rover()
        self.assertEquals(0, rover.bearing)
        rover.turn("r")
        rover.turn("r")
        rover.turn("l")
        self.assertEquals(270, rover.bearing)
        
    def testTurnLeftLeft(self):
        rover= Rover()
        self.assertEquals(0, rover.bearing)
        rover.turn("l")
        rover.turn("l")
        self.assertEquals(180, rover.bearing)
        
    def testChain(self):
        rover= Rover()
        self.assertEquals(0, rover.bearing)
        rover.chain("llfffb")
        self.assertEquals(180, rover.bearing)
        self.assertEquals(-3, rover.x)
        self.assertEquals(0, rover.y)

        

