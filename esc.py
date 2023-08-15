import sys
from typing import Callable



# https://gist.github.com/fnky/458719343aabd01cfb17a3a4f7296797
ESCMAP = {
    "reset" : "\x1b[0m",
    "bold" : "\x1b[1m",
    "dim" : "\x1b[2m",
    "blink" : "\033[5m",
    "italic" : "\033[3m",
    "underline" : "\x1b[4m",
    "u" : "\x1b[4m",
    "reverse" : "\x1b[7m",
    "hidden" : "\x1b[8m",
    "strike" : "\033[9m",
    "strikethrough" : "\033[9m",
    "delete" : '\x1b[2K',
    "home" : "\x1b[H",
    "request" : "\x1b[6n",
    "upscroll" : "\x1b[8",
    "savecursor" : "\x1b[s",
    "restorecursor" : "\x1b[u",
    "black" : "\x1b[30m",
    "red" : "\x1b[31m",
    "green" : "\x1b[32m",
    "yellow" : "\x1b[33m",
    "blue" : "\x1b[34m",
    "magenta" : "\x1b[35m",
    "cyan" : "\x1b[36m",
    "white" : "\x1b[37m",
    "Black" : "\x1b[90m",
    "Red" : "\x1b[91m",
    "Green" : "\x1b[92m",
    "Yellow" : "\x1b[93m",
    "Blue" : "\x1b[94m",
    "Magenta" : "\x1b[95m",
    "Cyan" : "\x1b[96m",
    "White" : "\x1b[97m",
    "bblack" : "\x1b[40m",
    "bred" : "\x1b[41m",
    "bgreen" : "\x1b[42m",
    "byellow" : "\x1b[43m",
    "bblue" : "\x1b[44m",
    "bmagenta" : "\x1b[45m",
    "bcyan" : "\x1b[46m",
    "bwhite" : "\x1b[47m",
    "bBlack" : "\x1b[100m",
    "bRed" : "\x1b[101m",
    "bGreen" : "\x1b[102m",
    "bYellow" : "\x1b[103m",
    "bBlue" : "\x1b[104m",
    "bMagenta" : "\x1b[105m",
    "bCyan" : "\x1b[106m",
    "bWhite" : "\x1b[107m",
    # erase from cursor until end of screen
    "del2end" : "\x1b[J",
    # erase from cursor to beginning of screen
    "del2beg" : "\x1b[1J",
    # erase entire screen
    "delall" : "\x1b[2J",
    # erase saved lines
    "delsaved" : "\x1b[3J",
    # erase from cursor to end of line
    "del2endln" : "\x1b[KJ",
    # erase start of line to the cursor
    "del2startln" : "\x1b[0K",
    # erase the entire line
    "delln" : "\x1b[1K",
    "nocursor" : "\x1b[?25l",
    "showcursor" : "\x1b[?25h",
    "altbuffer" : "\x1b[?1049h",
    "disablealtbuffer" : "\x1b[?1049l",
    "savescreen" : "\x1b[?47h",
    "restorescreen" : "\x1b[?47l"
}

class esc:
    reset = "\x1b[0m"    
    bold = "\x1b[1m"    
    dim = "\x1b[2m"    
    blink = "\033[5m"
    italic = "\033[3m"     
    underline = "\x1b[4m"    
    u = "\x1b[4m"      
    reverse = "\x1b[7m"    
    hidden = "\x1b[8m"    
    strike = "\033[9m"
    strikethrough = "\033[9m"       
    delete = '\x1b[2K'    
    home = "\x1b[H"    
    request = "\x1b[6n"    
    upscroll = "\x1b[8"    
    savecursor = "\x1b[s"    
    restorecursor = "\x1b[u"     
    black = "\x1b[30m"    
    red = "\x1b[31m"    
    green = "\x1b[32m"    
    yellow = "\x1b[33m"    
    blue = "\x1b[34m"    
    magenta = "\x1b[35m"    
    cyan = "\x1b[36m"    
    white = "\x1b[37m"    
    Black = "\x1b[90m"    
    Red = "\x1b[91m"    
    Green = "\x1b[92m"    
    Yellow = "\x1b[93m"    
    Blue = "\x1b[94m"    
    Magenta = "\x1b[95m"    
    Cyan = "\x1b[96m"    
    White = "\x1b[97m"    
    bblack = "\x1b[40m"    
    bred = "\x1b[41m"    
    bgreen = "\x1b[42m"    
    byellow = "\x1b[43m"    
    bblue = "\x1b[44m"    
    bmagenta = "\x1b[45m"    
    bcyan = "\x1b[46m"    
    bwhite = "\x1b[47m"    
    bBlack = "\x1b[100m"    
    bRed = "\x1b[101m"    
    bGreen = "\x1b[102m"    
    bYellow = "\x1b[103m"    
    bBlue = "\x1b[104m"    
    bMagenta = "\x1b[105m"    
    bCyan = "\x1b[106m"    
    bWhite = "\x1b[107m"
    # erase from cursor until end of screen
    del2end = "\x1b[J"
    # erase from cursor to beginning of screen
    del2beg = "\x1b[1J"
    # erase entire screen
    delall = "\x1b[2J"
    # erase saved lines
    delsaved = "\x1b[3J"
    # erase from cursor to end of line
    del2endln = "\x1b[KJ"
    # erase start of line to the cursor
    del2startln = "\x1b[0K"
    # erase the entire line
    delln = "\x1b[1K"
    nocursor = "\x1b[?25l"
    showcursor = "\x1b[?25h"
    altbuffer = "\x1b[?1049h"
    disablealtbuffer = "\x1b[?1049l"
    savescreen = "\x1b[?47h"
    restorescreen = "\x1b[?47l"
    
    @staticmethod
    def set(*esc_args):
        for esc_arg in esc_args:
            esc_arg = esc_arg.replace(",","/")
            for e in esc_arg.split("/"):
                e = e.strip()
                if e in ESCMAP:
                    print(ESCMAP[e],end="")

    @staticmethod
    def print(string:str,*esc_args,**kwargs):        
        def passme():
            pass

        esc.set(*esc_args)
    
        if "precall" in kwargs:
            precall = kwargs["precall"]
            del kwargs["precall"]
        else:
            precall = passme

        if "postcall" in kwargs:
            postcall = kwargs["postcall"]
            del kwargs["postcall"]
        else:
            postcall = passme

        prefix=""
        if "prefix" in kwargs:
            prefix=kwargs["prefix"]
            del kwargs["prefix"]

        precall()
        print(prefix, end="")
        print(string, **kwargs)
        postcall()
        esc.clear()
        
    @staticmethod
    def printf(*args) -> None:
        for arg in args:
            if (isinstance(arg,tuple) or isinstance(arg, list)):
                string = arg[0]
                if len(arg) > 1:
                    escs = arg[1:]
                    esc.set(*escs)
            elif (isinstance(arg, str)):
                string = arg
                esc.clear()
            print(string, end="")
            esc.clear()
        print()
    
    @staticmethod
    def create_fn(*args, **kwargs) -> Callable:
        def print_fn(string, **print_kwargs):
            kwargs.update(print_kwargs)
            esc.print(string, *args, **kwargs)
        return print_fn
    
    @staticmethod
    def input(string:str, *args, **kwargs) -> str:
        escinput = ""
        if "input" in kwargs:
            escinput = kwargs["input"]
            del kwargs["input"]
        escprompt = ""
        if "prompt" in kwargs:
            escprompt = kwargs["prompt"]
            del kwargs["prompt"]
        esc.set(escprompt)
        esc.print(string, *args, **kwargs)
        esc.set(escinput)
        input_value = input()
        esc.clear()
        return input_value

    @staticmethod 
    def clear() -> None:
        print(esc.reset,end="")

    @staticmethod
    def cursor_up(n:int=1) -> None:
        sys.stdout.write("\033["+str(n)+"F")
        sys.stdout.flush()

    @staticmethod
    def cursor_down(n:int=1) -> None:
        sys.stdout.write("\033["+str(n)+"E")
        sys.stdout.flush()
    
    @staticmethod
    def cursor_left(n:int=1) -> None:
        sys.stdout.write("\033["+str(n)+"D")
        sys.stdout.flush()

    @staticmethod
    def cursor_right(n:int=1) -> None:
        sys.stdout.write("\033["+str(n)+"C")
        sys.stdout.flush()

    @staticmethod
    def erase_to_endln() -> None:
        sys.stdout.write("\033[K")
        sys.stdout.flush()

    @staticmethod
    def erase_screen() -> None:
        sys.stdout.write("\033[2J")
        sys.stdout.flush()

    @staticmethod
    def erase_line() -> None:
        sys.stdout.write("\033[2K")
        sys.stdout.flush()

    @staticmethod
    def erase_prev(n:int=1) -> None:
        if n > 1:
            for i in range(n):
                esc.cursor_up(1)
                esc.erase_line()
        else:
            esc.cursor_up(1)
            esc.erase_line()

    @staticmethod
    def hide_cursor() -> None:
        print(esc.nocursor, end="")

    @staticmethod
    def show_cursor() -> None:
        print(esc.showcursor, end="")

    @staticmethod
    def enable_alt_buffer() -> None:
        print(esc.altbuffer, end="")
    
    @staticmethod
    def disable_alt_buffer() -> None:
        print(esc.disablealtbuffer, end="")

    @staticmethod
    def save_screen() -> None:
        print(esc.savescreen, end="")

    @staticmethod
    def restore_screen() -> None:
        print(esc.restorescreen, end="")

    @staticmethod
    def fg_code(code:int) -> None:
        print(f"\x1b[38;5;{code}m", end="")

    @staticmethod
    def bg_code(code:int) -> None:
        print(f"\x1b[48;5;{code}m", end="")
    
    @staticmethod
    def fg_rgb(r:int,g:int,b:int) -> None:
        print(f"\x1b[38;2;{r};{g};{b}m", end="")
    
    @staticmethod
    def bg_rgb(r:int,g:int,b:int) -> None:
        print(f"\x1b[48;2;{r};{g};{b}m", end="")
    
    
    

    