import copy
import random

class Hat:
    def __init__(self, **kwargs):
        self.contents=[]
        for key, value in kwargs.items():
            for i in range(value):
                self.contents.append(key)
    
    def draw(self, num):
        if num >= len(self.contents):
            ret=self.contents.copy()
            self.contents=[]
            return ret
        ret=[]
        for i in range(num):
            random_ball=random.choice(self.contents)
            ret.append(random_ball)
            self.contents.remove(random_ball)
        return ret


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    # Store the number of successful experiments
    successful_experiments = 0

    for _ in range(num_experiments):
        # Make a copy of the hat to keep the original intact
        hat_copy = copy.deepcopy(hat)

        # Draw the specified number of balls
        drawn_balls = hat_copy.draw(num_balls_drawn)

        # Count the number of each color drawn
        drawn_ball_counts = {color: drawn_balls.count(color) for color in set(drawn_balls)}

        # Check if the drawn counts meet or exceed the expected counts
        if all(drawn_ball_counts.get(color, 0) >= count for color, count in expected_balls.items()):
            successful_experiments += 1

    # Calculate the probability
    probability = successful_experiments / num_experiments
    return probability