#!/usr/bin/env python
"""geometry.py: defines the shapes that can represent the area of clouds"""
__author__ = 'Max Penrose'


import numpy
import coordinates

class otherrect:
	def __init__(self, constructPoints):
		self.constructPoints = constructPoints
		self.corners = []
		# corners[] format: [top-right, bottom-right, bottom-left, top-left]
		self.corners.append(coordinates.Coords((constructPoints[1].x, constructPoints[0].y), inputType='tuple'))
		self.corners.append(coordinates.Coords((constructPoints[2].x, constructPoints[1].y), inputType='tuple'))
		self.corners.append(coordinates.Coords((constructPoints[3].x, constructPoints[2].y), inputType='tuple'))
		self.corners.append(coordinates.Coords((constructPoints[0].x, constructPoints[3].y), inputType='tuple'))

		self.width = self.corners[0].x - self.corners[3].x
		self.height = self.corners[0].y - self.corners[1].y
		self.area = self.width * self.height

	#def getPointsInside():

class rect:
	def __init__(self, img, startcorner):
		