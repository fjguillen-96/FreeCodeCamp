import random

class Hat():
    def __init__(self, **colors):
        # Initialize the hat with the given colors and their respective counts
        self.contents = [color for color, num_color in colors.items() for _ in range(num_color)]

    def draw(self, n):
        # Draw n balls randomly from the hat
        num_balls = len(self.contents)

        # If n is less than the total number of balls, draw n balls randomly
        if n < num_balls:
            rng = random.sample(range(0, num_balls - 1), n)
            rng.sort(reverse=True)
        # Otherwise, draw all the balls in the hat
        else:
            rng = list(range(0, num_balls - 1))

        # Remove and return the drawn balls
        return [self.contents.pop(i) for i in rng]

    def return_balls(self, colors):
        # Return the given colors and their counts back to the hat
        [self.contents.append(color) for color, num_color in colors.items() for _ in range(num_color)]


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    M = 0  # Initialize the count of successful experiments

    # Perform the experiment num_experiments times
    for _ in range(num_experiments):
        # Draw balls from the hat
        drawn_balls = hat.draw(num_balls_drawn)

        # Count the occurrences of each color in the drawn balls
        drawn_balls_dict = dict.fromkeys(list(set(drawn_balls)))
        for color in drawn_balls_dict:
            cnt = 0
            for color_i in drawn_balls:
                if color == color_i:
                    cnt += 1
            drawn_balls_dict[color] = cnt

        # Check if the drawn balls match the expected balls
        match = True
        for color in expected_balls:
            if color in drawn_balls_dict.keys() and not (expected_balls[color] <= drawn_balls_dict[color]):
                match = False
                break

        # If the balls match, increment the successful experiment count
        if match:
            M += 1

        # Return the drawn balls back to the hat
        hat.return_balls(drawn_balls_dict)

    # Calculate and return the probability of a successful experiment
    return M / num_experiments
