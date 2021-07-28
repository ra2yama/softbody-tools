# Environment for easy testing/visualizing
# Allows the same setup to be either manually stepped or run with the testbed

TIME_STEP = 1.0 / 60 # will not carry over into testbed
SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480

try:
    from framework import (Framework, FrameworkBase, Keys, main)
except:
    print("Unable to import TestBed Framework, so running in testbed will not work.")

class Environment: # OOP <3 ;(
    def __init__(self, world):
        self.world = world
        self.init_bodies(self.world)
    def init_bodies (self, world): # Must be implemented. This is where all world setup should occur.
        # Be careful to add things to local variable world rather than self.world.
        # It's only set up as a separate function to allow for the same objects to be added to arbritrary worlds,
        # such as when running the test bed.

        raise Exception("init_bodies must be implemented.")
    
    def tick(self, world): # An arbitrary tick function meant to work on different world, similar to init_bodies.
        # Put everything that runs each frame here, EXCEPT stepping the simulation.
        # Again mind local variable world vs self.world.
        # Also keep in mind self can be used to track data, although again calling tick won't Step the simulation.
        raise Exception("tick must be implemented.")

    def Step(self):
        self.tick(self.world)
        self.world.Step(TIME_STEP, 10, 10)

def RunTestbed(env_obj): # will not display env_obj as is, but rather reinitialize it.
    class Sample(Framework):
        def __init__(self):
            super(Sample, self).__init__()
            env_obj.init_bodies(self.world)

        def Step(self, settings):
            env_obj.tick(self.world)
            super(Sample, self).Step(settings)

    main(Sample)
