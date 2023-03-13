import random

class Hat():
    def __init__(self,**colors):
        self.contents = [color for color,num_color in colors.items() for _ in range(num_color)]
    def draw(self,n):
        num_balls = len(self.contents)
        if n < num_balls:
            rng = random.sample(range(0,num_balls-1),n)
            rng.sort(reverse=True)           
        else:
            rng = list(range(0,num_balls-1))
        return [self.contents.pop(i) for i in rng]
    def return_balls(self,colors):
        [self.contents.append(color) for color,num_color in colors.items() for _ in range(num_color)]


def experiment(hat,expected_balls,num_balls_drawn,num_experiments):
    M = 0
    for _ in range(num_experiments):
        drawn_balls = hat.draw(num_balls_drawn)
        drawn_balls_dict = dict.fromkeys(list(set(drawn_balls)))
        for color in drawn_balls_dict:
            cnt = 0
            for color_i in drawn_balls:
                if color==color_i:
                    cnt+=1
            drawn_balls_dict[color] = cnt
        match = True
        for color in expected_balls:
            if color in drawn_balls_dict.keys() and not (expected_balls[color] <= drawn_balls_dict[color]):
                match = False
                break
        if match:
            M+=1
        hat.return_balls(drawn_balls_dict)
    return M/num_experiments
