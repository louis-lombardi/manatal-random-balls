import random as rd

def lottery():
    chosen_balls = []
    chosen_balls_amount = 0
    while chosen_balls_amount < 10:   # repeat until we find 10 distinct numbers
        ball = rd.randint(1,50)
        if ball not in chosen_balls:   # check if we don't already have this ball
            chosen_balls.append(ball)
            chosen_balls_amount += 1
    chosen_balls.sort()
    return(chosen_balls)


##### TEST #####
    
print(lottery())


##### UNIT TESTS #####

""" To test if the balls are actually chosen in a random way, we could generate a 
large amount of 10 balls-sets and count the frequency of each number. They should
all be around 0.02 (see following function).
We would also have to look if every output is a list of size 10
with only integers between 1 and 50, and if the list is sorted. """


def lottery_frequency_test():
    balls_count = 50 * [0] # counts the frequency of balls
    for i in range(1000000):
        balls=lottery()
        for ball in balls:
            balls_count[ball-1] = balls_count[ball-1] + 1  # increment the elements of balls_count
    for j in range(50):
        balls_count[j] = balls_count[j] / 10000000
    if max(balls_count)<0.021 and min(balls_count)>0.019:
        return(True)
    else:
        return(False)
        
print("The unit test returned "+str(lottery_frequency_test()))  # can take a few seconds to compute
    



 