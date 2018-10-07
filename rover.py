class Rover:
    STEP = 1
    SURFACE_AXIS = [0, 143]
    POSITION_OPERATORS = {
    'North': [0,STEP],
    'East': [STEP,0],
    'South': [0,-STEP],
    'West': [-STEP,0]
    }
    TURN_REFERENCES = {
    'North': ['West','East'],
    'East': ['North','South'],
    'South': ['East','West'],
    'West': ['South','North']
    }

    def __init__(self, given_position, given_direction):
            self.position = given_position
            self.direction = given_direction

    def broadcast_position(self):
        return self.position

    def broadcast_direction(self):
        return self.direction

    def command(self, commands):
        for command in commands:
            if command == 'f':
                self.position[0] += self.POSITION_OPERATORS.get(self.direction)[0]
                if self.position[0] >= self.SURFACE_AXIS[1]:
                    self.position[0] = self.SURFACE_AXIS[0]

                elif self.position[0] < self.SURFACE_AXIS[0]:
                    self.position[0] = self.SURFACE_AXIS[1]

                self.position[1] += self.POSITION_OPERATORS.get(self.direction)[1]
                if self.position[1] >= self.SURFACE_AXIS[1]:
                    self.position[1] = self.SURFACE_AXIS[0]

                elif self.position[1] < self.SURFACE_AXIS[0]:
                    self.position[1] = self.SURFACE_AXIS[1]

            elif command == 'b':
                self.position[0] -= self.POSITION_OPERATORS.get(self.direction)[0]
                if self.position[0] >= self.SURFACE_AXIS[1]:
                    self.position[0] = self.SURFACE_AXIS[0]

                elif self.position[0] < self.SURFACE_AXIS[0]:
                    self.position[0] = self.SURFACE_AXIS[1]

                self.position[1] -= self.POSITION_OPERATORS.get(self.direction)[1]
                if self.position[1] >= self.SURFACE_AXIS[1]:
                    self.position[1] = self.SURFACE_AXIS[0]

                elif self.position[1] < self.SURFACE_AXIS[0]:
                    self.position[1] = self.SURFACE_AXIS[1]

            elif command == 'r':
                self.direction = self.TURN_REFERENCES.get(self.direction)[1]

            elif command == 'l':
                self.direction = self.TURN_REFERENCES.get(self.direction)[0]

            else:
                print('Wrong command, doing nothing.')
