
class Rover:
  def __init__(self, blockages= ()):
    self.blockages= set(blockages)
    self.x, self.y = (0,0)
    self.bearing= 0

  def chain(self, clist):
    for cmd in list(clist):
      if cmd == 'l' or cmd == 'r':
        self.turn(cmd)
      if cmd == 'f' or cmd == 'b':
        self.move(cmd)


  def turn(self, direction):
    step = 90 if direction == "l" else 270
    self.bearing = ((self.bearing + step) % 360)

  def move(self, direction):
    steps = {0: (1, 0), 90: (0,1), 180: (-1, 0), 270: (0, -1)}
    stepd = (self.bearing + (0 if direction == "f" else 180)) % 360
    print "direction= %s, stepd= %s" % (direction, str(stepd))
    incr = steps[stepd]

    x = self.x + incr[0]
    y = self.y + incr[1]
    if (x,y) in self.blockages:
      return

    print "site 1 (x, y)= (%d, %d)" % (self.x, self.y)
    self.x, self.y = (x, y)
    print "site 2 (x, y)= (%d, %d)" % (self.x, self.y)

  def run(self):
    self.chain("llfffb")

if __name__ == "__main__":
    Rover().run()

