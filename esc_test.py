from esc import esc
from time import sleep

def printtest(test):
    print()
    print(f"<<< TEST {test} >>>")
    print("------------------------")

class Test(dict):
    def __init__(self) -> None:
        self["print"] = Test.print
        self["printf"] = Test.printf
        self["create_fn"] = Test.create_fn
        self["input"] = Test.input
        self["cursor"] = Test.cursor
        self["erase_prev"] = Test.erase_prev
    @staticmethod
    def print():
        printtest("esc.print")
        esc.print("WHITE & UNDERLINE", "underline", fg=(255,255,255))
    @staticmethod
    def printf():
        printtest("esc.printf")
        esc.printf(
            "This is normal, ",
            ["but this is red and underlined, ", "red/underline"],
            ["and this is blue and italic", "blue/italic"]
        )
        esc.printf("These are separated by a new line", ("OKAY?", "red"), end="\n")
    @staticmethod
    def create_fn():
        printtest("esc.create_fn")
        fn = esc.create_fn("red","italic", prefix="#")
        fn("red and italic with a # in front.")
    @staticmethod
    def input():
        printtest("esc.input")
        esc.input("Yellow prompt, red/underline input: ", prompt="yellow", input="red/underline", end="")
    @staticmethod
    def cursor():
        esc.erase_screen()
        esc.cursor_up(10)
        esc.print("Cursor moved up ten", "cyan")
        sleep(1)
        esc.cursor_down(10)
        esc.print("Cursor moved down ten", "cyan")
        sleep(1)
        esc.cursor_up(5)
        esc.cursor_right(10)
        esc.print("Cursor moved up five right ten", "cyan")
        sleep(1)
        esc.erase_screen()
    @staticmethod
    def erase_prev():
        esc.erase_prev()

if __name__ == "__main__":
    esc.enable_alt_buffer()
    tester = Test()
    try:
        t_inp = "..."
        while t_inp != "":
            t_inp = input("Enter test: ")
            if t_inp in tester:
                tester[t_inp]()
                print()
            else:
                print("Invalid test.")
    except:
        pass
    finally:
        esc.disable_alt_buffer()

    # print("Hello World")
    # esc.print("Hello World", fg=(255,255,255), bg=(32,132,255))
    # myprt = esc.create_fn("blue/italic")

    # esc.printf(
    #     "Normal, ",
    #     ("Colored, ", "red/underline"),
    #     "Normal again."
    # )

    # esc.input("Enter: ", prompt="red", input="blue", end="")

    # print("TEST: esc.printf")
    # esc.printf("Test", [" This", "red/underline", "italic"])
    # esc.printf(
    #     "This is normal, ",
    #     ["But this is red and underlined", "red/underline"],
    #     ["And this is blue and italic", "blue/italic"]
    # )
    # print("TEST: esc.print")
    # esc.print("Print me with color code", bg=(255,255, 255))
    # esc.print("Test", "red/underline", "italic")
    # print("TEST: esc.input")
    # input_value = esc.input("Q?: ", prompt="yellow/italic", input="red", end="")
    # print(input_value)
    # print("TEST: esc.create_fn")
    # redund = esc.create_fn("red","underline",precall=lambda:print())
    # redund("PRINT ME RED AND UNDERLINED")
    