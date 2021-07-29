import Box2D  # The main library
from Box2D.b2 import (world, polygonShape, staticBody, dynamicBody, edgeShape, fixtureDef, circleShape, revoluteJointDef, distanceJointDef)
from environment import (Environment, RunTestbed)
from softbody import (SoftBody, rect_positions, make_matrix, transpose_matrix)
import math
from inspect import signature

class SampleEnv(Environment):
    def __init__(self):
        super().__init__(world(gravity=(0, -10), doSleep=True))
        self.time = 0

    def init_bodies (self, world):
        self.time = 0

        fixture = fixtureDef(shape=polygonShape(box=(5, 0.5)), density=5, friction=0)
        fixture.filter.groupIndex = -2
        fixture2 = fixtureDef(shape=polygonShape(box=(5, 0.5)), density=5, friction=0)
        fixture2.filter.groupIndex = -2

        ground = world.CreateBody(
            shapes=edgeShape(vertices=[(-40, 0), (40, 0)])
        )

        self.paddle = world.CreateBody(shapes=polygonShape(box=(5, 0.5)), position=(0, 1))
        # self.paddle = world.CreateDynamicBody(position=(0, 0.5), fixtures=fixture)
        self.pole = world.CreateDynamicBody(position=(0, 5.5), angle=math.pi / 2, fixtures=fixture2)

        dfn = revoluteJointDef(
            bodyA=self.paddle,
            bodyB=self.pole,
            anchor=(0, 1),
        )

        self.joint = world.CreateJoint(dfn)
    
    def tick (self, world):
        # print(dir(self.paddle))
        force = math.sin(self.time / 10 + 90)
        # print(force)
        # self.paddle.ApplyLinearImpulse((force * 40, 0), self.paddle.GetWorldPoint((0, 0)), True)
        x, y = self.paddle.GetWorldPoint((0, 0))
        if self.joint.angle != 0:
            self.paddle.position = (x - self.joint.angle, y)
        # print(dir(self.joint)) #
        # print(self.joint.angle)
        self.time += 1


env = SampleEnv()

# for _ in range(200):
#     env.Step()
#     print(env.bruh.GetWorldPoint((0, 0)))

RunTestbed(env)