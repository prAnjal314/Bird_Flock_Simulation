import numpy as np
import turtle as tl

class Boid:
	def __init__(self, x, y, width, height):
		self.position = tl.Vec2D(x, y)
		self.max_speed = 5.1
		self.max_force = 0.2
		
		vec1 = (np.random.rand(2) - 0.5)*5
		self.velocity = tl.Vec2D(*vec1)

#		vec2 = (np.random.rand(2) - 0.5)/2
		self.acceleration = tl.Vec2D(0, 0)

	def draw(self, n):
		n.shape("circle")
		n.color("gray")
		n.shapesize(0.4)
		n.penup()
		n.setposition(self.position[0], self.position[1])

	def update(self):
		self.position += self.velocity
		self.velocity += self.acceleration

	def isOnLimit(self):
		if self.position[0] < -400:
			self.position += tl.Vec2D(800, 0)
		elif self.position[0] > 400:
			self.position += tl.Vec2D(-800, 0)

		if self.position[1] < -300:
			self.position += tl.Vec2D(0, 600)
		elif self.position[1] > 300:
			self.position += tl.Vec2D(0, -600)

	def maxSpeed(self):
		if tl.distance(self.velocity) >= 5:
			self.velocity *= self.max_speed/np.linalg.norm(self.velocity)
			self.acceleration = tl.Vec2D(0, 0)


	def align(self, boids):
		boid_in_range = 0
		average_velocity = tl.Vec2D(0, 0)
		equi_velocity = tl.Vec2D(0, 0)

		for boid in boids:
			distance = np.linalg.norm(boid.position - self.position)
			if self.position != boid.position and distance < 100:
				boid_in_range += 1
				average_velocity += boid.velocity
		
		if boid_in_range > 0:
			average_velocity *= (1/boid_in_range)
		
			if np.linalg.norm(average_velocity) > 0:
				average_velocity *= (self.max_speed/np.linalg.norm(average_velocity))
			equi_velocity = average_velocity - self.velocity
	
		self.acceleration += equi_velocity

	def separation(self, boids):
		tot = 0
		ave_vec = tl.Vec2D(0, 0)

		for boid in boids:
			distance = np.linalg.norm(boid.position - self.position)
			if boid.position != self.position and distance < 30:
				diff_vec = boid.position - self.position
				tot += 1
				ave_vec += diff_vec

				if np.linalg.norm(ave_vec) > 0:
					ave_vec *= (-self.max_force/np.linalg.norm(ave_vec))
			self.acceleration += ave_vec

	def cohesion(self, boids):
		boid_in_range = 0
		vec = tl.Vec2D(0, 0)
		tot = tl.Vec2D(0, 0)

		for boid in boids:
			distance = np.linalg.norm(boid.position - self.position)
			if boid.position != self.position and distance > 150:
				tot += boid.position - self.position
				boid_in_range += 1

		if boid_in_range > 0:
			com = tot * (1/boid_in_range)
			vec = com - self.position
			if np.linalg.norm(vec) > 0:
				vec *= (self.max_force/(2*np.linalg.norm(vec)))
		self.acceleration += vec
