# conversion_type = input("what is your conversion type?:  \n 1. temperature \n 2. speed \n 3. weight \n")
# source_value = float(input("what is your source value?:  "))
# (Celsius * 1.8) + 32
# 1 mph =  1.609344 km/h
# 1 kg = 1/6.35 stone = 1*2.205 lbs

def temperature():
    temp_conv = input("what is the temperature conversion type you want: \n 1. F to C \n 2. C to F")
    match temp_conv:
        case '1':
            value = float(input("what is your temperature value in F?:  "))
            new_value = (value - 32) / 1.8
            print("the temperature value in C is : " + str(new_value))
        case '2':
            value = float(input("what is your temperature value in C?:  "))
            new_value = (value * 1.8) + 32
            print("the temperature value in F is : " + str(new_value))
        case _:
            print("invalid input, try again")
            temperature()


def speed():
    speed_conv = input("what is the speed conversion type you want: \n 1. MPH to KPG \n 2. KPH to MPH")
    match speed_conv:
        case '1':
            value = float(input("what is your speed value in MPH?:  "))
            new_value = value * 1.609344
            print("the speed value in KPH is : " + str(new_value))
        case '2':
            value = float(input("what is your speed value in KPH?:  "))
            new_value = value / 1.609344
            print("the speed value in MPH is : " + str(new_value))
        case _:
            print("invalid input, try again")
            speed()


def weight():
    weight_conv = input(
        "what is the weight conversion type you want: \n 1. kg to stone \n 2. stone to kg \n 3. stone to lbs \n 4. "
        "lbs to stone \n 5. lbs to kg \n 6. kg to lbs")
    match weight_conv:
        case '1':
            value = float(input("what is your weight value in kg?:  "))
            new_value = value / 6.35
            print("the weight value in stone is : " + str(new_value))
        case '2':
            value = float(input("what is your weight value in stone?:  "))
            new_value = value * 6.35
            print("the weight value in kg is : " + str(new_value))
        case '3':
            value = float(input("what is your weight value in stone?:  "))
            new_value = value * 14
            print("the weight value in lbs is : " + str(new_value))
        case '4':
            value = float(input("what is your weight value in lbs?:  "))
            new_value = value / 14
            print("the weight value in stone is : " + str(new_value))
        case '5':
            value = float(input("what is your weight value in lbs?:  "))
            new_value = value * 2.205
            print("the weight value in kg is : " + str(new_value))
        case '6':
            value = float(input("what is your weight value in kg?:  "))
            new_value = value / 2.205
            print("the weight value in lbs is : " + str(new_value))
        case _:
            print("invalid input, try again")
            weight()


def convert():
    conversion_type = input("what is your conversion type?:  \n 1. temperature \n 2. speed \n 3. weight \n")
    match conversion_type:
        case '1':
            temperature()
        case '2':
            speed()
        case '3':
            weight()
        case _:
            print("invalid input, try again")
            convert()


convert()
