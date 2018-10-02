##MARS ROVER KATA

###CONTEXT

You’re part of the engineering team of a important space agency. Currently the agency is working in a robotic rover to explore the surface of Mars. Develop an API that translates the commands sent from earth to instructions that are understood by the rover.

###REQUIREMENTS

* Starts in a given initial coordinate (x, y)
* Starts in a given initial direction (North, South, East or West)
* Receives a character array of commands
* Implements command that move the rover forward(f)
* Implements command that move the rover backwards(b)
* Implements command that turn the rover left(l)
* Implements command that turn the rover right(r)

###ADVANCED

* Simulate the surface as a sphere subdivided by 144 segments in each axis. In other words, the coordinate (0, 0) is the same as (144, 144)

###ULTRA

* Implement a obstacle detection system. If a coordinate is occupied by a obstacle the rover should report its location and move to the last free location (and never get stuck again for the same reason)
