import numpy as np
import turtle as tl
from boids import Boid

width = 800
height = 600
no_of_boids = 30

wn = tl.Screen()
wn.setup(800, 600)
wn.bgcolor("black")
wn.tracer(0)

pen = tl.Turtle()
pen.hideturtle()
pen.speed(0)


flock = [Boid(np.random.randint(-200, 200), np.random.randint(-200, 200), width, height) for i in range(no_of_boids)]
boids = [tl.Turtle() for _ in range(no_of_boids)]

while True:
	wn.update()

	i = 0
	for boid in flock:
		boid.update()
		boid.draw(boids[i])
		boid.isOnLimit()
		boid.maxSpeed()
		boid.align(flock)
		boid.separation(flock)
		boid.cohesion(flock)
		i += 1

wn.mainloop()
wn.exitonclick()