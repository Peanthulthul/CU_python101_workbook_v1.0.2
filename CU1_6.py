import math
def positionr_theta():
    r, thetha  = map(float, input('Enter r and thetha(raians):').split())
    x = round(r*math.cos(thetha),2)
    y = round(r*math.sin(thetha),2) 
    print(f'{x},{y}')

positionr_theta()
