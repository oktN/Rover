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

    with it('moves forward facing North'):
        given_position = [0, 0]
        given_direction = 'North'
        rover = Rover(given_position, given_direction)

        rover.command(['f'])
        current_position = rover.broadcast_position()

        expected_position = [0, 1]
        expect(current_position).to(equal(expected_position))

    with it('moves forward facing South'):
        given_position = [0, 0]
        given_direction = 'South'
        rover = Rover(given_position, given_direction)

        rover.command(['f'])
        current_position = rover.broadcast_position()

        expected_position = [0, 143]
        expect(current_position).to(equal(expected_position))

    with it('moves forward facing East'):
        given_position = [0, 0]
        given_direction = 'East'
        rover = Rover(given_position, given_direction)

        rover.command(['f'])
        current_position = rover.broadcast_position()

        expected_position = [1, 0]
        expect(current_position).to(equal(expected_position))

    with it('moves forward facing West'):
        given_position = [0, 0]
        given_direction = 'West'
        rover = Rover(given_position, given_direction)

        rover.command(['f'])
        current_position = rover.broadcast_position()

        expected_position = [143, 0]
        expect(current_position).to(equal(expected_position))

    with it('moves backwards facing North'):
        given_position = [0, 0]
        given_direction = 'North'
        rover = Rover(given_position, given_direction)

        rover.command(['b'])
        current_position = rover.broadcast_position()

        expected_position = [0, 143]
        expect(current_position).to(equal(expected_position))

    with it('moves backwards facing South'):
        given_position = [0, 0]
        given_direction = 'South'
        rover = Rover(given_position, given_direction)

        rover.command(['b'])
        current_position = rover.broadcast_position()

        expected_position = [0, 1]
        expect(current_position).to(equal(expected_position))

    with it('moves backwards facing East'):
        given_position = [0, 0]
        given_direction = 'East'
        rover = Rover(given_position, given_direction)

        rover.command(['b'])
        current_position = rover.broadcast_position()

        expected_position = [143, 0]
        expect(current_position).to(equal(expected_position))

    with it('moves backwards Facing West'):
        given_position = [0, 0]
        given_direction = 'West'
        rover = Rover(given_position, given_direction)

        rover.command(['b'])
        current_position = rover.broadcast_position()

        expected_position = [1, 0]
        expect(current_position).to(equal(expected_position))

    with it('turns right from North to East'):
        given_position = [0, 0]
        given_direction = 'North'
        rover = Rover(given_position, given_direction)

        rover.command(['r'])

        current_direction = rover.broadcast_direction()
        expected_direction = 'East'
        expect(current_direction).to(equal(expected_direction))

    with it('turns right from East to South'):
        given_position = [0, 0]
        given_direction = 'East'
        rover = Rover(given_position, given_direction)

        rover.command(['r'])

        current_direction = rover.broadcast_direction()
        expected_direction = 'South'
        expect(current_direction).to(equal(expected_direction))

    with it('turns right from South to West'):
        given_position = [0, 0]
        given_direction = 'South'
        rover = Rover(given_position, given_direction)

        rover.command(['r'])

        current_direction = rover.broadcast_direction()
        expected_direction = 'West'
        expect(current_direction).to(equal(expected_direction))

    with it('turns right from West to North'):
        given_position = [0, 0]
        given_direction = 'West'
        rover = Rover(given_position, given_direction)

        rover.command(['r'])

        current_direction = rover.broadcast_direction()
        expected_direction = 'North'
        expect(current_direction).to(equal(expected_direction))

    with it('turns left from North to West'):
        given_position = [0, 0]
        given_direction = 'North'
        rover = Rover(given_position, given_direction)

        rover.command(['l'])

        current_direction = rover.broadcast_direction()
        expected_direction = 'West'
        expect(current_direction).to(equal(expected_direction))

    with it('turns left from West to South'):
        given_position = [0, 0]
        given_direction = 'West'
        rover = Rover(given_position, given_direction)

        rover.command(['l'])

        current_direction = rover.broadcast_direction()
        expected_direction = 'South'
        expect(current_direction).to(equal(expected_direction))

    with it('turns left from South to East'):
        given_position = [0, 0]
        given_direction = 'South'
        rover = Rover(given_position, given_direction)

        rover.command(['l'])

        current_direction = rover.broadcast_direction()
        expected_direction = 'East'
        expect(current_direction).to(equal(expected_direction))

    with it('turns left from West to North'):
        given_position = [0, 0]
        given_direction = 'East'
        rover = Rover(given_position, given_direction)

        rover.command(['l'])

        current_direction = rover.broadcast_direction()
        expected_direction = 'North'
        expect(current_direction).to(equal(expected_direction))

    with it('reset coords to 0 when surpases 143 towards North'):
        given_position = [0, 143]
        given_direction = 'North'
        rover = Rover(given_position, given_direction)

        rover.command(['f'])
        current_position = rover.broadcast_position()

        expected_position = [0, 0]
        expect(current_position).to(equal(expected_position))

    with it('reset coords to 0 when surpases 143 towards East'):
        given_position = [143, 0]
        given_direction = 'East'
        rover = Rover(given_position, given_direction)

        rover.command(['f'])
        current_position = rover.broadcast_position()

        expected_position = [0, 0]
        expect(current_position).to(equal(expected_position))

    with it('reset coords to 143 when surpases 0 towards South'):
        given_position = [0, 0]
        given_direction = 'South'
        rover = Rover(given_position, given_direction)

        rover.command(['f'])
        current_position = rover.broadcast_position()

        expected_position = [0, 143]
        expect(current_position).to(equal(expected_position))

    with it('reset coords to 143 when surpases 0 towards West'):
        given_position = [0, 0]
        given_direction = 'West'
        rover = Rover(given_position, given_direction)

        rover.command(['f'])
        current_position = rover.broadcast_position()

        expected_position = [143, 0]
        expect(current_position).to(equal(expected_position))

    with it('reset coords to 143 when surpases 0 backwards North'):
        given_position = [0, 0]
        given_direction = 'North'
        rover = Rover(given_position, given_direction)

        rover.command(['b'])
        current_position = rover.broadcast_position()

        expected_position = [0, 143]
        expect(current_position).to(equal(expected_position))

    with it('reset coords to 143 when surpases 0 backwards East'):
        given_position = [0, 0]
        given_direction = 'East'
        rover = Rover(given_position, given_direction)

        rover.command(['b'])
        current_position = rover.broadcast_position()

        expected_position = [143, 0]
        expect(current_position).to(equal(expected_position))

    with it('reset coords to 0 when surpases 143 backwards South'):
        given_position = [0, 143]
        given_direction = 'South'
        rover = Rover(given_position, given_direction)

        rover.command(['b'])
        current_position = rover.broadcast_position()

        expected_position = [0, 0]
        expect(current_position).to(equal(expected_position))

    with it('reset coords to 0 when surpases 143 backwards West'):
        given_position = [143, 0]
        given_direction = 'West'
        rover = Rover(given_position, given_direction)

        rover.command(['b'])
        current_position = rover.broadcast_position()

        expected_position = [0, 0]
        expect(current_position).to(equal(expected_position))
