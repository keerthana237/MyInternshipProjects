print("UNIT CONVERTER: METERS AND FEET")
while True:
    converter=input("enter target units(meters/feet): ").lower()
    if converter!="meters" and converter!="feet":
        raise ValueError("Invalid input, must enter target unit i.e meters or feet")
    try:
        value=float(input("enter the value to be converted: "))
    except ValueError:
        print("input must be a number, enter a number value")
    else:
        if(converter=="meters"):
            converted_value=value/3.28084
            print(f"{value} feet is equal to {converted_value} meters")
        elif converter=="feet":
            converted_value= value*3.28084
            print(f"{value} meters is equal to {converted_value} feet")
        break
