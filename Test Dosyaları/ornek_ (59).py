def colorize(text, color):
    colors = ("blue", "red", "white", "black", "orange")
    if type(text) is not str:
        raise TypeError("text parameter have to be str type ")
    if type(color) is not str:
        raise TypeError("color parameter type have to be str type ")
    if color not in colors:
        raise ValueError(f"colors does not have {color} color ")
    print(f"\n{text} {color}\n")


try:
    colorize("merhaba", "red")
    colorize("merhaba", 10)
    colorize("selam", "yellow")
except Exception as ex:
    print(ex)