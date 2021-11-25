import copy
import random
# Consider using the modules imported above.


class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for (k, v) in kwargs.items():
            for i in range(v):
                self.contents.append(k)

    # draw set number of balls from the hat
    def draw(self, draw_number):
        drawn_balls = []
        if draw_number > len(self.contents):
            return self.contents
        for _ in range(draw_number):
            # -1 because randint takes a<=N<=b
            ball = self.contents.pop(random.randint(0, len(self.contents)-1))
            drawn_balls.append(ball)
        return drawn_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    count = 0
    for _ in range(num_experiments):
        expected_balls_copy = copy.deepcopy(expected_balls)
        hat_copy = copy.deepcopy(hat)
        drawn_balls = hat_copy.draw(num_balls_drawn)
        # checks if drawn ball are in expected_balls
        for ball in drawn_balls:
            if ball in expected_balls_copy:
                expected_balls_copy[ball] -= 1
        # if they are count +1
        if all(i <= 0 for i in expected_balls_copy.values()):
            count += 1
    return count/num_experiments


random.seed(95)
# hat = Hat(blue=4, red=2, green=6)
# probability = experiment(
#     hat=hat,
#     expected_balls={"blue": 3,
#                     "green": 1},
#     num_balls_drawn=4,
#     num_experiments=30)
hat = Hat(blue=3,red=2,green=6)
probability = experiment(hat=hat,
                         expected_balls={"blue":2,"green":1},
                         num_balls_drawn=4,
                         num_experiments=1000)
print("Probability:", probability)