def tensnum(x):
    if x<100:
        print(x//10)
    elif x>99 and x<1000:
        print((x//10)%10)
    else:
        print(0)
tensnum(99)
tensnum(765)
tensnum(9)