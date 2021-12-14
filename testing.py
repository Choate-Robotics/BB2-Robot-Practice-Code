def tank_drive(speed_y, speed_turn):
            
    if speed_turn < .1 and speed_turn > -.1:
        sL = speed_y
        sR = speed_y
    # elif speed_turn == 1:
    #     sL = speed_y
    #     sR = -speed_y
    # elif speed_turn == -1:
    #     sL = -speed_y
    #     sR = speed_y
    else:
        rT = (1/speed_turn) * 3
        print(rT)
        vDiff = abs((speed_y*2)/rT)
        rL = rT + .5 * 2
        rR = rT - .5 * 2
        if abs(rL) > abs(rR):
            sL = speed_y
            sR = speed_y - vDiff
        else:
            sL = speed_y - vDiff
            sR = speed_y

    return sL, sR

print(tank_drive(1, -1))