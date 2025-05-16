# python-nbody

## Setup

### Getting the Skeleton Files

To get started, fork the repository by using the GitHub interface. This will allow you to push your changes to your own version of the repository hosted on GitHub.

Then, clone **your** fork by copying the SSH URL and running

`git clone <SSH URL>`

in a directory of your choice.

If it's your first time using `git` on your machine, you may have to set up an SSH key--just follow the instructions in any error messages you get.

You should now be able to use `git add`, `git commit`, `git push` and (unlikely) `git pull`.

#### Merges 

If at any point you encounter an automated merge (e.g. from `git pull`), this section may be helpful.

Depending on the settings on the computer you’re using, you will possibly find yourself in one of three command line text editors:

    nano
    vim
    emacs

~~Fortunately~~ Unfortunately, `git` will likely default to one of these text editors, meaning that the simple act of providing a merge message may cause you considerable consternation. Don’t worry, this is normal! One of the goals of 61B is to teach you to handle these sorts of humps. Indeed, one of the reasons we’re making you use a powerful real-world version control system like `git` this semester is to have you hit these common hurdles now in a friendly pedagogical environment instead of the terrifying real world. However, this also means we’re going to suffer sometimes, particularly at this early point in the semester. Don’t panic!

For reference, this is what `vim` looks like:

vim

See [this link](http://stackoverflow.com/questions/11828270/how-to-exit-the-vim-editor) if you are stuck in `vim`. If you are in `emacs`, type something and then press `ctrl-x` then `ctrl-s` to save, then `ctrl-x` then `ctrl-c` to exit.

If you somehow end up having a merge conflict, consult the [git weird technical failures guide](https://sp19.datastructur.es/materials/guides/git-wtfs).

If you get some sort of error, STOP and either figure it out by carefully reading the git guide or seek help from an instructor. You’ll potentially save yourself a lot of trouble vs. guess-and-check with git commands. If you find yourself trying to use commands you Google like `force push`, don’t.

### Python

To start, you'll need a modern version of Python ([download if necessary](https://www.python.org/downloads/)). We suggest version 3.12.3 (check with `python3 --version`). This should come with `pip`, but you may have to ensure this separately depending on your system.

If using Windows, we recommend using Ubuntu through the Windows Subsystem for Linux so you can follow along with standard commands.

Unfortunately, various ways to install Python may result in you lacking the package manager `pip` and/or `venv`. Try Googling to see if you can resolve this, or ask course staff.

**We will assume in these instructions that `python3` resolves to the correct version of Python.** Depending on how you installed it, you may need to use just `python`. Similarly, `pip` and `pip3` may also need to be switched around.

### Virtual environment

Let's set up a Python virtual environment. This will ensure you get only the right dependencies and don't pollute your Python environment.
You may also use another environment manager like `Anaconda`, but here's how to do it with just Python:

First, navigate to your home directory or some other location outside of this git repository.

Assuming you're using a UNIX shell, you can follow along:

`cd ~/`

Then, create a directory (folder) to house our new environment:

`mkdir nbody-env`

and create a new virtual environment with

`python3 -m venv nbody-env`.

To activate the environment, use

`source ~/nbody-env/bin/activate`.

To deactivate, just type `deactivate` at any time. Remember to re-activate whenever you come back to work on this project!

### Packages

We'll need some packages to help with parts of the project we don't want to do ourselves, like drawing.

Navigate back to this git repository using `cd`, and then

`pip install -r requirements.txt`

This should install all the necessary packages into your virtual environment.

If you don't have the `pip` alias available, you may equivalently try

`python3 -m pip install -r requirements.txt`

## Introduction

Your goal for this project is to write a program simulating the motion of `N` objects in a plane, accounting for the gravitational forces mutually affecting each object as demonstrated by Sir Isaac Newton’s [Law of Universal Gravitation](http://en.wikipedia.org/wiki/Newton%27s_law_of_universal_gravitation).

Ultimately, you will be creating a program nbody.py that draws an animation of bodies floating around in space tugging on each other with the power of gravity.

Throughout the instructions, we will be using Python's [type hinting syntax](https://docs.python.org/3/library/typing.html), e.g. `values: List[float]`. While it is optional to use type hinting in your project, it is considered a best practice and [strongly recommended](https://google.github.io/styleguide/pyguide.html#221-type-annotated-code).
You may check your code with [mypy](https://mypy.readthedocs.io/en/stable/getting_started.html) or another linter like [pytype](https://github.com/google/pytype).

## The Body Class and Its Constructor

You’ll start by creating a `Body` class. In your favorite text editor, create a new file called `Body.py`. If you haven’t picked a text editor, we recommend [VSCode](https://code.visualstudio.com/download) or [Sublime Text](https://www.sublimetext.com/download). Remember that your `.py` files should have the same name as the class it contains.

Begin by creating a basic version of the `Body` class with the following 6 instance variables:

```python
xx_pos: float  # Its current x position
yy_pos: float  # Its current y position
xx_vel: float  # Its current velocity in the x direction
yy_vel: float  # Its current velocity in the y direction
mass: float  # Its mass
img_filename: str  # The name of the file that corresponds to the image that depicts the body (for example, jupiter.gif)
```

Your instance variables must be named exactly as above. The reason we call them by double letters, e.g. `xx_pos` rather than `x_pos` is to reduce the chance of typos. In past semesters, students have accidentally pressed `x` when they meant `y`, and this has caused significant debugging hassle. After adding the 6 instance variables above, add in a `Body` constructor (`__init__`) that can initialize an instance of the `Body` class. Later on, an instance of the `Body` class can represent a planet, star, or various objects in this universe. The signature of the constructor should be:

```python
def __init__(self, xx_pos: float, yy_pos: float, xx_vel: float,
              yy_vel: float, mass: float, img_filename: str):
```

We will also provide a factory method that takes in a `Body` and initializes an identical `Body` object
(i.e. a copy). The signature of this method should be:

```python
@staticmethod
def copy(b: Body) -> Body:
```

All of the numbers for this project will be `float`s. We’ll go over what exactly a float is later in the course, but for now, think of it is a real number, e.g. `x = 3.5`.

Once you have filled in the constructors, you can test it out by running `body_test.py`.

You can run our provided test with the command
`python -m unittest --verbose body_test`

If you pass this test, you’re ready to move on to the next step. Do not proceed until you have passed this test.

## Understanding the Physics

Let’s take a step back now and look at the physics behind our simulations. Our Body objects will obey the laws of Newtonian physics. In particular, they will be subject to:

- Pairwise Force: Newton’s _law of universal gravitation_ asserts that the strength of the gravitational force between two particles is given by the product of their masses divided by the square of the distance between them, scaled by the gravitational constant $G = 6.67 \cdot 10^{-11} \dfrac{\text{Nm}^2}{\text{kg}^2}$. The gravitational force exerted on a particle is along the straight line between them (we are ignoring here strange effects like the curvature of space). Since we are using Cartesian coordinates to represent the position of a particle, it is convenient to break up the force into its $x$- and $y$-components ($F_x$, $F_y$). The relevant equations are shown below. We have not derived these equations, and you should just trust us.

    - $F = \dfrac{G \cdot m_1 \cdot m_2}{r^2}$

    - $r^2 = dx^2 + dy^2$

    - $F_x = \dfrac{F \cdot dx}{r}$

    - $F_y = \dfrac{F \cdot dy}{r}$

Look at the image below and make sure you understand what each variable represents!

Note that force is a vector (i.e., it has direction). In particular, be aware that $dx$ and $dy$ are signed (positive or negative).

- Net Force: The _principle of superposition_ says that the net force acting on a particle in the $x$- or $y$-direction is the sum of the pairwise forces acting on the particle in that direction.

In addition, all bodies have:

- Acceleration: Newton’s _second law of motion_ says that the accelerations in the $x$- and $y$-directions are given by:
    - $a_x = \dfrac{F_x}{m}$
    - $a_y = \dfrac{F_y}{m}$

Check your understanding!

Consider a small example consisting of two celestial objects: Saturn and the Sun. Suppose the Sun is at coordinates ($1.0 \cdot 10^{12}, 2.0 \cdot 10^{11}$) and Saturn is at coordinates ($2.3 \cdot 10^{12}, 9.5 \cdot 10^{11}$). Assume that the Sun’s mass is $2.0 \cdot 10^{30} \text{ kg}$ and Saturn’s mass is $6.0 \cdot 10^{26} \text{ kg}$. Here’s a diagram of this simple solar system:

Let’s run through some sample calculations. First let’s compute $F_1$, the force that Saturn exerts on the Sun. We’ll begin by calculating $r$, which we’ve already expressed above in terms of $dx$ and $dy$. Since we’re calculating the force exerted by Saturn, dx is Saturn’s $x$-position minus Sun’s $x$-position, which is $1.3 \times 10^{12} \text{ m}$. Similarly, dy is $7.5 \cdot 10^{11} \text{ m}$.

So, $r^2 = dx^2 + dy^2 = (1.3 \cdot 10^{12})^2 + (7.5 \cdot 10^{11})^2$. Solving for $r$ gives us $1.5 \cdot 10^{12} \text{ m}$. Now that we have $r$, computation of $F$ is straightforward:

$$F = \dfrac{G \cdot (2.0 \cdot 10^{30} \text{ kg}) \cdot (6.0 \cdot 10^{26} \text{kg})}{(1.5 \cdot 10^{12} \text{ m})^2} = 3.6 \cdot 10^{22} \text{ N}$$

Note that the magnitudes of the forces that Saturn and the Sun exert on one another are equal; that is, $|F| = |F_1| = |F_2|$. Now that we’ve computed the pairwise force on the Sun, let’s compute the x- and y-components of this force, denoted with $F_{1,x}$ and $F_{1, y}$, respectively. Recall that dx is $1.3 \cdot 10^{12}$ meters and dy is $7.5 \cdot 10^{11}$ meters. So,

$$F_{1,x} = \dfrac{F_1 \cdot (1.3 \cdot 10^{12} \text{ m})}{1.5 \cdot 10^{12} \text{ m}} = 3.1 \cdot 10^{22} \text{ N}$$
$$F_{1, y} = \dfrac{F_1 \cdot (7.5 \cdot 10^{11} \text{ m})}{1.5 \cdot 10^{12} \text{ m}} = 1.8 \cdot 10^{22} \text{ N}$$

Note that the sign of dx and dy is important! Here, $dx$ and $dy$ were both positive, resulting in positive values for $F_{1, x}$ and $F_{1, y}$. This makes sense if you look at the diagram: Saturn will exert a force that pulls the Sun to the right (positive $F_{1, x}$ ) and up (positive $F_{1, y}$).

Next, let’s compute the $x$ and $y$-components of the force that the Sun exerts on Saturn. The values of $dx$ and $dy$ are negated here, because we’re now measuring the displacement of the Sun relative to Saturn. Again, you can verify that the signs should be negative by looking at the diagram: the Sun will pull Saturn to the left (negative $dx$) and down (negative $dy$).

$$F_{2, x} = \dfrac{F_2 \cdot (-1.3 \cdot 10^{12} \text{ m})}{1.5 \cdot 10^{12} \text{ m}} = -3.1 \cdot 10^{22} \text{ N}$$
$$F_{2, y} = \dfrac{F_2 \cdot(-7.5 \cdot 10^{11} \text{ m})}{1.5 \cdot 10^{12} \text{ m}} = -1.8 \cdot 10^{22} \text{ N}$$

Let’s add Neptune to the mix and calculate the net force on Saturn. Here’s a diagram illustrating the forces being exerted on Saturn in this new system:


We can calculate the $x$-component of the net force on Saturn by summing the $x$-components of all pairwise forces. Likewise, $F_{\text{net}, y}$ can be calculated by summing the $y$-components of all pairwise forces. Assume the forces exerted on Saturn by the Sun are the same as above, and that $F_{2,x} = 1.1 \cdot 10^{22} \text{ N}$ and $F_{2,y} = 9.0 \cdot 10^{21} \text{N}$.

$$F_{\text{net}, x} = F_{1, x} + F_{2, x} = -3.1 \cdot 10^{22} \text{ N} + 1.1 \cdot 10^{22} \text{ N} = -2.0 \cdot 10^{22} \text{ N}$$
$$F_{\text{net}, y} = F_{1, y} + F_{2, y} = -1.8 \cdot 10^{22} \text{ N} + 9.0 \cdot 10^{21} \text{ N} = -9.0 \cdot 10^{21} \text { N}$$

### Double check your understanding!

Suppose there are three bodies in space as follows:

- Samh: $x = 1, y = 0, \text{mass} = 10$
- Aegir: $x = 3, y = 3, \text{mass} = 5$
- Rocinante: $x = 5, y = -3, \text{mass} = 50$

Calculate $F_{\text{net}, x}$ and $F_{\text{net}, y}$ exerted on Samh. To check your answer, click [here](http://www.wolframalpha.com/input/?i=%286.67+*+10%5E-11+*+10+*+5%29+%2F+13+*+2+%2F+sqrt%2813%29+%2B+%286.67+*+10%5E-11+*+10+*+50%29+%2F25+*+4+%2F+sqrt%2825%29) for $F_{\text{net}, x}$ and [here](http://www.wolframalpha.com/input/?i=%2810+*+5+*+6.67+*+10%5E-11%29+%2F13+*+3+%2F+sqrt%2813%29+-+%2850+*+10+*+6.67+*+10%5E-11%29+%2F+25+*+3+%2F+sqrt%2825%29) for $F_{\text{net}, y}$.

## Writing the Body Class

In our program, we’ll have instances of the `Body` class do the job of calculating all the numbers we learned about in the previous example. We’ll write helper methods, one by one, until our `Body` class is complete.

### calc_distance

Start by adding a method called `calc_distance` that calculates the distance between two `Body`s. This method will take in a single `Body` and should return a `float` equal to the distance between the supplied body and the body that is doing the calculation, e.g.

`samh.calc_distance(rocinante)`

It is up to you this time to figure out the signature of the method. Once you have completed this method, go ahead and recompile and run the next unit test to see if your code is correct.

Test with:
`python -m unittest --verbose calc_distance_test`

Note: you may import default libraries like `math`.

### calc_force_exerted_by 

The next method that you will implement is `calc_force_exerted_by`. The `calc_force_exerted_by` method takes in a `Body`, and returns a `float` describing the force exerted on this body by the given body. You should be calling the `calc_distance` method inside this method. As an example, `samh.calc_force_exerted_by(rocinante)` for the numbers in "Double Check Your Understanding" return `1.334⋅10−9`

.

Once you’ve finished `calc_force_exerted_by`, re-compile and run the next unit test.

`python -m unittest --verbose calc_force_exerted_by`

Hint: It is good practice to declare any constants as a class or module (file)-level variable, and to use that variable anytime you wish to use the constant.

Hint 2: Python supports scientific notation. For example, I can write `some_number = 1.03e-7`.

### calc_force_exerted_by_x and calc_force_exerted_by_y 

The next two methods that you should write are `calc_force_exerted_by_x`  and `calc_force_exerted_by_y`. Unlike the `calc_force_exerted_by` method, which returns the total force, these two methods describe the force exerted in the X and Y directions, respectively. Remember to check your signs! Once you’ve finished, you can recompile and run the next unit test. As an example, `samh.calc_force_exerted_by_x(rocinante)` in "Double Check Your Understanding" should return `1.0672⋅10−9`

.

NOTE: Do not use `abs` to fix sign issues with these methods. This will cause issues later when drawing planets.

`python -m unittest --verbose calc_force_exerted_by_xy`

### calc_net_force_exerted_by_x and calc_net_force_exerted_by_y

Write methods `calc_net_force_exerted_by_x` and `calc_net_force_exerted_by_y` hat each take in a list of `Body`s and calculates the net X and net Y force exerted by all bodies in that array upon the current `Body`. For example, consider the code snippet below:

```python
all_bodys = [samh, rocinante, aegir]
samh.calc_net_force_exerted_by_x(all_bodys)
samh.calc_net_force_exerted_by_y(all_bodys)
```

The two calls here would return the values given in "Double Check Your Understanding."

As you implement these methods, remember that `Body`s cannot exert gravitational forces on themselves! Can you think of why that is the case (hint: the universe will possibly collapse in on itself, destroying everything including you)?

To avoid this problem, ignore any body in the array that is equal to the current body.
To compare two bodies, you may use `is` or `==`, provided you have not implemented `__eq__()` for your `Body`.
The default implementation of `__eq__` (for which `==` is just [syntactic sugar](https://en.wikipedia.org/wiki/Syntactic_sugar)) is to compare with `is`.
This checks if the two objects being compared are precisely the same object in memory (not just constructed with the same values).

When you are done go ahead and run:

`python -m unittest --verbose calc_net_force_exerted_by_xy`

### update

Next, you’ll add a method that determines how much the forces exerted on the body will cause that body to accelerate, and the resulting change in the body’s velocity and position in a small period of time $dt$. For example, `samh.update(0.005, 10, 3)` would adjust the velocity and position if an $x$-force of $10 \text{ Newtons}$ and a y-force of $3 \text{ Newtons}$ were applied for $0.005 \text{ seconds}$.

You must compute the movement of the `Body` using the following steps:

  - Calculate the acceleration using the provided $x$- and $y$-forces.
  - Calculate the new velocity by using the acceleration and current velocity. Recall that acceleration describes the change in velocity per unit time, so the new velocity is $(v_x + dt \cdot a_x, v_y + dt \cdot a_y)$.
  - Calculate the new position by using the velocity computed in step 2 and the current position. The new position is $(p_x + dt \cdot v_x, p_y + dt \cdot v_y)$.

Let’s try an example! Consider a squirrel initially at position $(0, 0)$ with a $v_x$ of $3 \dfrac{\text{m}}{\text{s}}$ and a $v_y$ of $5 \dfrac{\text{m}}{\text{s}}$. $F_{\text{net}, x}$ is $-5 \text{ N}$ and $F_{\text{net}, y}$ is $-2 \text{ N}$. Here’s a diagram of this system:

squirrelforce

We’d like to update with a time step of $1 \text{ second}$. First, we’ll calculate the squirrel’s net acceleration:

$$a_{\text{net}, x} = \dfrac{F_{\text{net}, x}}{m} = \dfrac{-5 \text{ N}}{1 \text{ kg}} = -5 \dfrac{\text{m}}{\text{s}^2}$$

$$a_{\text{net}, y} = \dfrac{F_{\text{net}, y}}{m} = \dfrac{-2 \text{ N}} {1 \text{ kg}} = -2 \dfrac{\text{m}}{\text{s}^2}$$

With the addition of the acceleration vectors we just calculated, our system now looks like this:

squirrelacc

Second, we’ll calculate the squirrel’s new velocity:

$$v_{\text{new}, x} = v_{\text{old}, x} + dt \cdot a_{\text{net}, x} = 3 \dfrac{\text{m}}{\text{s}} + 1 \text{ s} \cdot -5 \dfrac{\text{m}}{\text{s}^2} = -2 \dfrac{\text{m}}{\text{s}}$$

$$v_{\text{new}, y} = v_{\text{old}, y} + dt \cdot a_{\text{net}, y} = 5 \dfrac{\text{m}}{\text{s}} + 1 \text{ s} \cdot -2 \dfrac{\text{m}}{\text{s}^2} = 3 \dfrac{\text{m}}{\text{s}}$$

Third, we’ll calculate the new position of the squirrel:

$$p_{\text{new}, x} = p_{\text{old}, x} + dt \cdot v_{\text{new}, x} = 0 \text{ m} + 1 \text{ s} \cdot -2 \dfrac{\text{m}}{\text{s}} = -2 \text{ m}$$

$$p_{\text{new}, y} = p_{\text{old}, y} + dt \cdot v_{\text{new}, y} = 0 \text{ m} + 1 \text{ s} \cdot 3 \dfrac{\text{m}}{\text{s}} = 3 \text{ m}$$

Here’s a diagram of the updated system:

squirrelupdated

For math/physics experts: You may be tempted to write a more accurate simulation where the force gradually increases over the specified time window. Don’t! Your simulation must follow exactly the rules above.

Write a method `update(self, dt, f_xx, f_yy)` that uses the steps above to update the body’s position and velocity instance variables (this method does not need to return anything).

Once you’re done, recompile and test your method with:

`python -m unittest --verbose update_test.py`

Once you’ve done this, you’ve finished implementing the physics. Hoorah! You’re halfway there.

## Testing Your Body Class

As the semester progresses, we’ll be giving you fewer and fewer tests, and it will be your responsibility to write your own tests. Writing tests is a good way to improve your workflow and be more efficient.

Some people find the rush of test-driven development (TDD) addictive. You basically set up a little game for yourself to solve. Some people hate it. Your mileage may vary. Whether you personally enjoy the TDD flow or not, writing tests will be one of the most important skills you learn here at Berkeley, and getting "[test-infected](https://wiki.c2.com/?TestInfected)" will save you and your future colleagues an enormous amount of time and misery.

### The \_\_str\_\_ method

Go ahead and try writing your own test for a `__str__(self)` method in the `Body` class.
This is a [dunder method](https://www.pythonmorsels.com/what-are-dunder-methods/) that is called, among other places, when we call `print()` and `str()` on an object.

First, make a `body_test.py` file and write a `unittest` test that creates a body and checks that

```python
Body b = ...
str(b)
```

returns a string with its state information in a human-readable format of your choosing.
Feel free to copy the structure from the provided tests.

An example output might look like  
```
Body at (1.5, 2.6) with velocity (3.7, 4.1) and mass 1.239812e+08
```
but feel free to change the formatting as you see fit. Check out the [format specification documentation](https://docs.python.org/3/library/string.html#formatspec) for information on using scientific notation or limiting decimal places.

Then, go and implement `__str__` in `body.py`. Run your test to see if your implementation is working correctly!

For bonus points, consider: how you might check that `print(b: Body)` is working properly?
This is beyond the scope of the course, but an important [real-world consideration](https://stackoverflow.com/questions/33767627/write-unittest-for-console-print).

## Getting Started with the Simulator (nbody.py)

Create a file named `nbody.py`. `NBody` is a class that will actually run your simulation. This class will have no (explicit) constructor to start off with. The goal of this class is to simulate a universe specified in one of the data files. For example, if we look inside `data/planets.txt` (using the command line `more` command), we see the following:

```bash
$ more planets.txt
5
2.50e+11
1.4960e+11  0.0000e+00  0.0000e+00  2.9800e+04  5.9740e+24    earth.gif
2.2790e+11  0.0000e+00  0.0000e+00  2.4100e+04  6.4190e+23     mars.gif
5.7900e+10  0.0000e+00  0.0000e+00  4.7900e+04  3.3020e+23  mercury.gif
0.0000e+00  0.0000e+00  0.0000e+00  0.0000e+00  1.9890e+30      sun.gif
1.0820e+11  0.0000e+00  0.0000e+00  3.5000e+04  4.8690e+24    venus.gif
```

The input format is a text file that contains the information for a particular universe (in SI units). The first value is an integer `N` which represents the number of planets. The second value is a real number `R` which represents the radius of the universe, used to determine the scaling of the drawing window. Finally, there are `N` rows, and each row contains 6 values. The first two values are the $x$- and $y$-coordinates of the initial position; the next pair of values are the $x$- and $y$-components of the initial velocity; the fifth value is the mass; the last value is a `string` that is the name of an image file used to display the planets. Image files can be found in the images directory. The file above contains data for our own solar system (up to Mars).

### read_radius

Your first method is `read_radius`. Given a file name as a `string`, it should return a `float` corresponding to the radius of the universe in that file, e.g. `read_radius("./data/planets.txt")` should return `2.50e+11`.

You can test this method using the supplied test.

`python -m unittest --verbose read_radius_test.py`

### read_bodies 

Your next method is `read_bodies`. Given a file name, it should return an array of `Body`s corresponding to the bodies in the file, e.g. `read_bodies("./data/planets.txt")` should return an array of five planets.

You can test this method using the supplied test.

`python -m unittest --verbose read_bodies_test.py`

## Drawing the Initial Universe State (main)

Next, build the functionality to draw the universe in its starting position. You’ll do this in four steps. Because all code for this part of the assignment is in `main`, this part of the assignment will NOT have automated tests to check each little piece.

### Collecting All Needed Input

Create a main block in `nbody.py` by adding the following, **outside of the `NBody` class**:

```python
if __name__ == "__main__":
    print("Running NBody")
```

Note that this is _not_ a `main` function. It is generally recommended to define a `main` function and call it here, but to keep things simple we'll just put our (very minimal) code here directly.

When we call `python3 nbody.py`, you should see the output `Running NBody`.

Write code so that your `main` function performs the following steps:

- Store the first and second command line arguments as `float`s named `T` and `dt`. Hint: the arguments come in as `strings`. You will have to convert the `strings` to `floats`!

- Store the third command line argument as a `string` named `filename`.
    
- Create an `NBody` object. You may further test that your `main` block is working by having the `NBody` object parse the file and print out some results.

Feel free to reference the [docs](https://docs.python.org/3/tutorial/stdlib.html#command-line-arguments) on reading command line arguments.

### Animation basics

Python is not known for its powerful graphics applications, but we will make do with one of the most common drawing libraries you will encounter: `matplotlib`.

The logistics of setting up a `FuncAnimation` object and using it are a little unintuitive and tedious, so we've provided an example for you in `examples/squirrel_renderer.py`

Go ahead and run the example with `python3 examples/squirrel_renderer.py`. It should display a window with an animation.
**If this doesn't work, you may have to install additional packages related to PyQt!**. While we try to include all the dependencies in `requirements.txt`, some students may lack operating system-level dependencies. Reach out to course staff if you're having trouble getting the example to work.

To terminate the example, you can close the window or use `Ctrl+C` at the command line where you launched it.

`SquirrelRenderer` provides most of the code you'll need to render the simulation, but you must read it to understand what to do. Reading other people's code is a critical skill in the real world!
Warning: it may not be perfect or easy to understand. This is definitely for educational purposes and not laziness on the instructors' part.

Copy the relevant parts of `SquirrelRenderer` into `NBody`. You may now choose to add a constructor `__init__` to `NBody`, or add some methods to allow us to populate the universe after construction.

A reasonable implementation could look like this:
```python
    def __init__(self, T: float, dt: float, filename: str):
        ...
```

Either way, you will need to do the following:

### Draw the Background

First, set the scale of your plot so that it matches the radius of the universe. Then draw the image `starfield.jpg` as the background. This is more or less already done for you in the example.

Note that `starfield.jpg` is referred to with the relative path `images/starfield.jpg` in the example. This assumes that the working directory is the main folder for this repository. If you're getting errors, check that you're running from the correct folder! 

### Drawing One Body

Next, we’ll want a `Body`, such as a planet, to be able to draw itself at its appropriate position.

To do this, take a brief detour back to the `body.py` file. Add one last method to the `Body` class, `draw(self, ax: matplotlib.pyplot.Axes, img: matplotlib.AxesImage)`, that sets the image data and transform to show the `Body`’s image at the `Body`’s position. There's no need to return anything from this method.

Hint: you will need the `Axes`, otherwise the `Body` won't show up in the right place. Check the example to figure out how to configure the transform.

Tip: It can be very resource-intensive to load the image from disk every frame, slowing down your animation. Is there some way we can load the image once so it can be re-used each time we draw?

Be careful to not break existing test cases that might not provide valid file paths! You may find the [`try` and `except` keywords](https://www.w3schools.com/python/python_try_except.asp) helpful.

### Initialize all the objects to be drawn

The `FuncAnimation` paradigm requires that we create all the objects that will be animated up-front.
`NBody` should hold on to a list (or similar) of `Body`s as well as a list of `AxesImage`s. `AxesImage` is the object that is [returned from `imshow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html).

As long as we have enough `AxesImage`s to go around, it doesn't particularly matter which one is used for which planet in each frame (we can simply overwrite the image data each time). That being said, depending on your implementation, you may want to somehow keep track of which image object corresponds with which `Body`.

### Drawing More than One Body

Now implement an `update` method that draws all the `Body`s in the simulation. Hopefully this is very clean, thanks to all the prep work we've done! The instructor implementation is only a handful of lines. 

Lastly, update your `main` block to pass the appropriate command-line arguments to `NBody` and "run" the simulation (we have not added the physics yet).

Test that your `main` block and drawing code works by running:

`python3 nbody.py 157788000.0 25000.0 data/planets.txt`

You should see the sun and four planets sitting motionless. You are almost done.

Tip: if you see an empty window, check your units! Some `matplotlib` arguments are given in inches, while others will be in terms of the axis units.

Note: there are ways to unit test graphical output, and ways we could test the generated plotting objects directly. This is beyond the scope of the course, but sometimes important in applications like web development and computer graphics.

## Creating an Animation

Everything you’ve done so far is leading up to this moment. With only a bit more code, we’ll get something very cool.

To create our simulation, we will discretize time (please do not mention this to Stephen Hawking). The idea is that at every discrete interval, we will be doing our calculations and once we have done our calculations for that time step, we will then update the values of our `Body`s and then redraw the universe.

Finish your `update` method by adding the following:

For each call, do the following:
- Calculate the net $x$ and $y$ forces for each `Body`, and store them in a `net_x_forces` and `net_y_forces` list respectively.
- After calculating the net forces for every `Body`, call `update` (`Body.update`) on each of the `Body`s. This will update each body’s position, velocity, and acceleration.
- Draw all of the `Body`s.

Important: For each time through the main loop, do not make any calls to `Body.update` until all forces have been calculated and safely stored `net_x_forces` and `net_y_forces`. For example, don’t call `self.bodies[0].update()` until after the entire `net_x_forces` and `net_y_forces` lists are done! The difference is subtle, but the autograder will be upset if you call `bodies[0].update` before you calculate `net_x_forces[1]` and `net_y_forces[1]`.

Test your program:

`python3 nbody.py 157788000.0 25000.0 data/planets.txt`

Make sure to also try out some of the other simulations, which can all be found in the `data` directory. Some of them are very cool.

## Printing the Universe

When the simulation is over, i.e. when you’ve reached time `T` **and manually closed the animation window**, you should print out the final state of the universe in the same format as the input, e.g.:

```
5
2.50e11
1.4925e+11 -1.0467e+10  2.0872e+03  2.9723e+04  5.9740e+24    earth.gif
-1.1055e+11 -1.9868e+11  2.1060e+04 -1.1827e+04  6.4190e+23    mars.gif
-1.1708e+10 -5.7384e+10  4.6276e+04 -9.9541e+03  3.3020e+23 mercury.gif
2.1709e+05  3.0029e+07  4.5087e-02  5.1823e-02  1.9890e+30      sun.gif
6.9283e+10  8.2658e+10 -2.6894e+04  2.2585e+04  4.8690e+24    venus.gif
```

You are welcome to try to figure this out on your own, but if you’d prefer not to, the solution is right below:

```python
def print_universe(self):
    """
    Print the universe.
    """
    print(f"{len(self.bodies)}")
    print(f"{self.radius:.2e}")
    for b in self.bodies:
        print(f"{b.xx_pos:.2e} {b.yy_pos:.2e} {b.xx_vel:.2e} {b.yy_vel:.2e} {b.mass:.2e} {b.img_file_name}")
```

Here, `bodies` is our filler variable name for reading in the bodies. You may have a different variable name.

This isn’t all that exciting (which is why we’ve provided a solution), but we’ll need this method to work correctly to autograde your assignment.

# Submission

Run
```
python3 nbody.py 500000.0 25000.0 data/kevin.txt
```

Once the simulation stops, close the window and copy the output into a text file `out.txt`. Submit this for grading!

## Going Above and Beyond (Gold Points)

For those of you who finish early and want to try something wild, crazy, and new, create new files `nbody_extreme.py` and `body_extreme.py`. You may also add additional classes as needed. Please include "Extreme" at the end of the filenames for clarity.

In the Extreme version of your `NBody` simulator, you should do something fundamentally new. There are a number of other interesting possibilities:

- Support elastic (or inelastic) collisions.
- Add the ability to programmatically generate planet images (rather than relying on input image files).
- Add the ability to control a spacecraft that is subject to the gravitational forces of the objects in the solar system.

No tips are provided here in the spec. If you want to know how to do any of the things listed above (or something else of your own imagining), try using search engines to learn how to do the thing you want to do.

## Frequently Asked Questions

### I’m passing all the local tests, but failing even easy tests like `read_radius_test` in the autograder.

Make sure you’re actually using the string argument that `read_radius_test` takes as input. Your code should work for ANY valid data file, not just `planets.txt`.

### The test demands 133.5, and I’m giving 133.49, but it still fails!

Sorry, our sanity check tests have flaws. But you should ensure that your value for `G` is $6.67 \cdot 10^{-11} \dfrac{\text{Nm}^2}{\text{kg}^2}$ exactly, and not anything else (don’t make it more accurate).

### When I run the simulation, my planets start rotating, but then quickly accelerate and disappear off of the bottom left of the screen.

Look at the way you’re calculating the force exerted on a particular planet in one time step. Make sure that the force doesn’t include forces that were exerted in past time steps.
Make sure you did not use `abs(...)` when calculating `calc_force_exerted_by_x(...)` and `calc_force_exerted_by_y(...)`.
Also ensure that you are using a `float` to keep track of summed forces (not `int`), although Python makes this pretty hard to mess up!

# Acknowledgements
This project is more or less a direct transcription of [Spring 2019 CS 61B Project 0](https://sp19.datastructur.es/materials/proj/proj0/proj0) from Java into Python. The assignment `README` is also largely identical. Thanks to Josh Hug, Matthew Chow, and Daniel Nguyen, and the original authors Robert Sedgewick and Kevin Wayne from Princeton University.