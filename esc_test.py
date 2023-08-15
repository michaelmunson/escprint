from esc import esc
from time import sleep

if __name__ == "__main__":
    print("TEST: esc.printf")
    esc.printf("Test", [" This", "red/underline", "italic"])
    esc.printf(
        "This is normal, ",
        ["But this is red and underlined", "red/underline"],
        ["And this is blue and italic", "blue/italic"]
    )

    print("TEST: esc.print")
    esc.print("Test", "red/underline", "italic")
    print("TEST: esc.input")
    input_value = esc.input("Q?: ", prompt="yellow/italic", input="red", end="")
    print(input_value)
    print("TEST: esc.create_fn")
    redund = esc.create_fn("red","underline",precall=lambda:print())
    redund("PRINT ME RED AND UNDERLINED")