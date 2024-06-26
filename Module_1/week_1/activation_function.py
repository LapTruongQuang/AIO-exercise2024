import math 
def calc_activation_func(x, act_name):
    if act_name == 'sigmoid':
        return 1/(1 + math.exp(-x))
    elif act_name == 'elu':
        if x > 0:
            return x
        else:
            return 0.01*(math.exp(x) - 1)
    else:
        if x > 0:
            return x
        else:
            return 0

if __name__=="main":
    assert calc_activation_func(x = 1, act_name ='relu') == 1
    print (round(calc_activation_func(x = 3, act_name ='sigmoid'), 2))