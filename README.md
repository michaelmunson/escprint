# escprint
Library for Escape Printing

## Usage
```python
from escprint import esc
```

### esc.print
This is useful for a basic print statement
```python
esc.print("Hello World!", "red","underline", end="")
```
Different Escape Arguments can be deliminated by a "/"
```python
esc.print("Hello World!", "red/underline", end="")
```
Prefixes are also valid
```python
esc.print("World!", "red/underline", prefix="Hello ")
```
**precall** & **postcall** keyword arguments can be passed as well. These are functions that will be called before and after the print statement, respectively.
```python
esc.print("World", "red", precall=lambda:print("Hello"), postcall=lambda:print("!"))
``` 


### esc.printf
Sometimes, we want different characters/words to have different styles.
```python
esc.printf(
    "This is normal, ",
    ["but this is red and underlined, ", "red/underline"],
    ["and this is blue and italic", "blue/italic"]
)
```

### esc.create_fn
If we are constantly printing the same styles over and over, we might want to create a printing function to do it for us.
```python
print_yellow_italic = esc.create_fn("yellow","italic")

print_yellow_italic("This will be yellow and italic", end="")
```
Note that the keyword arguments allowed with **esc.print** are valid when creating the function.
```python
print_yellow_italic = esc.create_fn("yellow","italic",precall=print("'Ello Govna"))
```

### esc.input
We also might want to format our inputs as well.

Here, the prompt is "What is your name? ", which is colored yellow. 
The user's input will be on the same line, but will be colored red and underlined. 
```python
esc.input("What is your name? ", prompt="yellow/italic", input="red/underline", end="")
```