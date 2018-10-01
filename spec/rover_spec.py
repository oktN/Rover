from mamba import *
from expects import *

from rover import Rover

with description('Rover') as self:
    with it('starts in a given position'):
        given_position = [0, 0]
        given_direction = 'North'
        rover = Rover(given_position, given_direction)

        current_position = rover.broadcast_position()

        expect(current_position).to(equal(given_position))

    with it('starts in a given direction'):
        given_position = [0, 0]
        given_direction = 'North'
        rover = Rover(given_position, given_direction)

        current_direction = rover.broadcast_direction()

        expect(current_direction).to(equal(given_direction))

    with it('moves forward'):
        given_position = [0, 0]
        given_direction = 'North'
        rover = Rover(given_position, given_direction)

        rover.command(['f'])
        current_position = rover.broadcast_position()

        expected_position = [0, 1]
        expect(current_position).to(equal(expected_position))

    with it('moves backwards'):
        given_position = [0, 0]
        given_direction = 'North'
        rover = Rover(given_position, given_direction)

        rover.command(['b'])
        current_position = rover.broadcast_position()

        expected_position = [0, -1]
        expect(current_position).to(equal(expected_position))

"""
    with it('turns right'):
        given_position = [0, 0]
        given_direction = 'South'
        rover = Rover(given_position, given_direction)

        rover.command(['r'])

        current_direction = rover.broadcast_direction()
        expected_direction = 'West'
        expect(current_direction).to(equal(expected_direction))

    with it('turns left'):
        given_position = [0, 0]
        given_direction = 'South'
        rover = Rover(given_position, given_direction)

        rover.command(['l'])

        current_direction = rover.broadcast_direction()
        expected_direction = 'East'
        expect(current_direction).to(equal(expected_direction))
"""
