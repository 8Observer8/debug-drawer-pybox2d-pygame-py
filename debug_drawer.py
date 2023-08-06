import math

import pygame
from Box2D import b2Draw


class DebugDrawer(b2Draw):

    def __init__(self, window, pixelsPerMeter, thickness=3):
        super().__init__()
        self.window = window
        self.pixelsPerMeter = pixelsPerMeter
        self.thickness = thickness

    def DrawSolidPolygon(self, vertices, color):
        pygame.draw.line(self.window, (color.r * 255, color.g * 255, color.b * 255),
            (vertices[0][0] * self.pixelsPerMeter, vertices[0][1] * self.pixelsPerMeter),
            (vertices[1][0] * self.pixelsPerMeter, vertices[1][1] * self.pixelsPerMeter),
            self.thickness)
        pygame.draw.line(self.window, (color.r * 255, color.g * 255, color.b * 255),
            (vertices[1][0] * self.pixelsPerMeter, vertices[1][1] * self.pixelsPerMeter),
            (vertices[2][0] * self.pixelsPerMeter, vertices[2][1] * self.pixelsPerMeter),
            self.thickness)
        pygame.draw.line(self.window, (color.r * 255, color.g * 255, color.b * 255),
            (vertices[2][0] * self.pixelsPerMeter, vertices[2][1] * self.pixelsPerMeter),
            (vertices[3][0] * self.pixelsPerMeter, vertices[3][1] * self.pixelsPerMeter),
            self.thickness)
        pygame.draw.line(self.window, (color.r * 255, color.g * 255, color.b * 255),
            (vertices[3][0] * self.pixelsPerMeter, vertices[3][1] * self.pixelsPerMeter),
            (vertices[0][0] * self.pixelsPerMeter, vertices[0][1] * self.pixelsPerMeter),
            self.thickness)

    def DrawSolidCircle(self, center, radius, axis, color):
        amountOfAngles = 20
        angleStep = 360 / amountOfAngles
        startAngle = 0
        endAngle = angleStep

        for i in range(amountOfAngles):
            x0 = radius * math.cos(startAngle * math.pi / 180);
            y0 = radius * math.sin(startAngle * math.pi / 180);
            x1 = radius * math.cos(endAngle * math.pi / 180);
            y1 = radius * math.sin(endAngle * math.pi / 180);
            pygame.draw.line(self.window, (color.r * 255, color.g * 255, color.b * 255),
                ((center[0] + x0) * self.pixelsPerMeter, (center[1] + y0) * self.pixelsPerMeter),
                ((center[0] + x1) * self.pixelsPerMeter, (center[1] + y1) * self.pixelsPerMeter),
                self.thickness)
            startAngle = endAngle
            endAngle += angleStep

    def DrawPolygon(self, vertices, color):
        pass
    def DrawSegment(self, p1, p2, color):
        pass
    def DrawPoint(self, p, size, color):
        pass
    def DrawCircle(self, center, radius, color, drawwidth=1):
        pass
    def DrawTransform(self, xf):
        pass
