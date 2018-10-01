class Rover:
    STEP = 1
    # Relación entre la orientación cardinal y los operadores a utilizar. (Considerar el uso de tupla)
    DIRECTION_AXIS = {'North': [0,STEP], 'East': [STEP,0], 'South': [0,-STEP], 'West': [-STEP,0]}
    def __init__(self, given_position, given_direction):
        self.position = given_position
        self.direction = given_direction

    def broadcast_position(self):
        return self.position

    def broadcast_direction(self):
        return self.direction

    def command(self, commands):
        for command in commands:
        #Dabamos por hecho que el Rover se orientaba al norte, intento implementar la funcionalidad capaz de evaluar la dirección.
        #Operamos sobre la posicion actual del objeto con el dict (DIRECTION_AXIS) de axis definididos segun la orientación del Rover (Codigo demasiado complejo, pendiente de mejora)
        #Norte [0, +1], Sur [0, -1], Este [+1, 0], Oeste [-1, 0]
            if command == "f":
                self.position[0] += self.DIRECTION_AXIS.get(self.direction)[0]
                self.position[1] += self.DIRECTION_AXIS.get(self.direction)[1]

            elif command == "b":
                self.position[0] -= self.DIRECTION_AXIS.get(self.direction)[0]
                self.position[1] -= self.DIRECTION_AXIS.get(self.direction)[1]

            elif command == "r":
                pass

            elif command == "l":
                pass

            else:
                print("Wrong command, doing nothing.")
