help = [
"""Welcome to the Turtle art game! This is an easy way to get into some basic coding, or just to have a bit of fun.

In the box on the left, you can write code. You can then use the "Run Code" button to see the results of your code on the right hand side.

This game lets you code in a language called Python. You can use Python to give commands to a "turtle" which will draw pictures for you.

Give it a try! Enter "turtle.forward(100)" into the code box on the left and hit "Run Code" to see the turtle draw you a line.""",
"""Making a line is pretty cool, but all good drawings need more than one line.

To add more drawing commands to your program, add them in order on a new line. For example, to draw a square, you can try:
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)

This will cause the turtle to make 4 identical lines, turning 90 degrees between each one.
""",
"""You may be wondering what the numbers in our commands mean. These numbers are called "arguments", and they specify a number relative to the command.

For example, turtle.forward(100) means "move the turtle forward 100 units". Likewise, turtle.right(90) means "turn the turtle right 90 degrees".

Try changing the arguments in your program and see what it does to your shape
""",
"""You will hopefully now understand the basics of programming your Turtle in Python. You can now try to use these commands to make a drawing of your own!

Here are some turtle commands you may find helpful, maybe try some out and see what they do:
turtle.forward(<distance>)
turtle.backward(<distance>)
turtle.right(<angle>)
turtle.left(<angle>)
turtle.circle(<radius>)
turtle.width(<thickness>)
turtle.color(<color>)
turtle.penup()
turtle.pendown()
turtle.begin_fill()
turtle.end_fill()

See what you can come up with by combining these commands. Once you've made something you're proud of, hit "Submit Image" to submit it to our Discord gallery!

You can continue this help tutorial for some more advanced Python concepts if you wish.
""",
"""So, you've stuck around for the fun stuff. One useful Python concept that makes turtle drawings much easier is a loop. A loop repeats a set of commands a certain number of times.

To create a loop, start by writing "for i in range(10):". Here, the number 10 can be changed to the number of times you want the loop to run.
Next, any commands inside the loop need to be indented with a tab. You can add a set of commands to your loop, an example is below:

for i in range(4):
    turtle.forward(100)
    turtle.right(90)

This will repeat the indented instructions 4 times in order. Running this code will draw the 4 sides of a square, without having to write the commands 4 times.

The letter i here will represent the number of loop that you are on, starting with 0. So during this loop, i will have the values 0, 1, 2 and 3 as the loop repeats.
You can see this in action by writing print(i) inside your loop. This will display the value of i in the console within your window each time the loop repeats.
You can also use i inside your turtle commands, for example, "turtle.forward(100 + (i * 10))" will increase the distance that the turtle travels forward by 10 each time the loop repeats.

See what else you can come up with using loops.
"""
]