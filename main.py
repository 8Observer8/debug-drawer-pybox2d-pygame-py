import math

import pygame
from Box2D import (b2_dynamicBody, b2BodyDef, b2CircleShape, b2FixtureDef,
                   b2PolygonShape, b2Vec2, b2World)

from debug_drawer import DebugDrawer

pygame.init()

window = pygame.display.set_mode((300, 300))
pygame.display.set_caption("Debug Drawer")
clock = pygame.time.Clock()
points = []
points.append((10, 20))
points.append((50, 100))

pixelsPerMeter = 30
world = b2World(gravity=b2Vec2(0, 9.8))
debugDrawer = DebugDrawer(window, pixelsPerMeter)
debugDrawer.flags = { "drawShapes": True }
world.renderer = debugDrawer

# Ground
groundBodyDef = b2BodyDef()
groundBodyDef.position = b2Vec2(150 / pixelsPerMeter, 270 / pixelsPerMeter)
groundBody = world.CreateBody(groundBodyDef)
groundShape = b2PolygonShape()
groundShape.SetAsBox(130 / pixelsPerMeter, 20 / pixelsPerMeter)
groundFixtureDef = b2FixtureDef()
groundFixtureDef.shape = groundShape
groundFixtureDef.density = 0
groundBody.CreateFixture(groundFixtureDef)

# Box
boxBodyDef = b2BodyDef()
boxBodyDef.position = b2Vec2(100 / pixelsPerMeter, 30 / pixelsPerMeter)
boxBodyDef.angle = 30 * math.pi / 180
boxBodyDef.type = b2_dynamicBody
boxBody = world.CreateBody(boxBodyDef)
boxShape = b2PolygonShape()
boxShape.SetAsBox(30 / pixelsPerMeter, 30 / pixelsPerMeter)
boxFixtureDef = b2FixtureDef()
boxFixtureDef.shape = boxShape
boxFixtureDef.density = 1
boxBody.CreateFixture(boxFixtureDef)

# Circle
circleBodyDef = b2BodyDef()
circleBodyDef.position = b2Vec2(200 / pixelsPerMeter, 50 / pixelsPerMeter)
circleBodyDef.type = b2_dynamicBody
circleBody = world.CreateBody(circleBodyDef)
circleShape = b2CircleShape()
circleShape.radius = 20 / pixelsPerMeter
circleFixtureDef = b2FixtureDef()
circleFixtureDef.shape = circleShape
circleFixtureDef.density = 1
circleFixtureDef.restitution = 0.5
circleBody.CreateFixture(circleFixtureDef)

# Platform
platformBodyDef = b2BodyDef()
platformBodyDef.position = b2Vec2(220 / pixelsPerMeter, 200 / pixelsPerMeter)
platformBodyDef.angle = -20 * math.pi / 180
platformBody = world.CreateBody(platformBodyDef)
platformShape = b2PolygonShape()
platformShape.SetAsBox(50 / pixelsPerMeter, 5 / pixelsPerMeter)
platformFixtureDef = b2FixtureDef()
platformFixtureDef.shape = platformShape
platformFixtureDef.density = 0
platformBody.CreateFixture(platformFixtureDef)

run = True

while run:
    # Limit frames per second
    dt = clock.tick(60)

    world.Step(dt / 1000, 3, 2)

    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    window.fill(0)

    world.DrawDebugData()

    # Update display
    pygame.display.flip()
