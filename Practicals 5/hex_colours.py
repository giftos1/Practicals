COLOUR_NAMES = {"ALICEBLUE": "#f0f8ff", "ANTIQUEWHITE": "#faebd7", "AZURE1": "#f0fffff", "AZURE2": "#e0eeee",
                "AZURE3": "#c1cdcd", "AZURE4": "#838b8b",
                "BEIGE": "#f5f5dc", "BISQUE1": "#ffe4c4", "BISQUE2": "#eed5b7", "BISQUE3": "#cdb79e"}
colour_name = input("Enter a colour name").upper()
while colour_name != "":

    if colour_name in COLOUR_NAMES:
        print("{} code is {}".format(colour_name, COLOUR_NAMES[colour_name]))
    else:
        print("Invalid input")
    colour_name = input("Enter a colour name").upper()
