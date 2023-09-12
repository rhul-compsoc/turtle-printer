# turtle-printer

Print your Turtle creations

## usage

Write a turtle script in .tpy in scripts

Run the program with `$ make` or `$ python3 ./src/main.py`

## dependencies

- turtle
- curses

## example

```py
# Set cursor shape
shape("turtle")
color("blue")
speed(1)  # You can adjust the speed (1 is slowest, 10 is fastest)

# Draw a square
for _ in range(4):
    forward(100)  # Move the turtle forward by 100 units
    left(90)  # Turn the turtle left by 90 degrees
```
