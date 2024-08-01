def bouncing_ball(h, bounce, window):
    bounces = 0
    if (bounce >= 1) or (bounce <=0) or (h <0) or (window<0) or (window==h):
        return -1
    while h > window:
        h = bounce*h
        if h > window:
            bounces += 2
    return bounces + 1

print(bouncing_ball(int(input()), int(input()), int(input())))