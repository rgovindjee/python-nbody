# python-nbody

## Setup

### Python

To start, you'll need a modern version of Python. We suggest version 3.12.3 (check with `python3 --version`). This should come with `pip`, but you may have to ensure this separately depending on your system.

If using Windows, we recommend using Ubuntu through the Windows Subsystem for Linux so you can follow along with standard commands.

You will also want to have `git` installed, although the project can technically be completed without it.

### Virtual environment

Let's set up a Python virtual environment. This will ensure you get only the right dependencies and don't pollute your Python environment.
You may also use another environment manager like Anaconda, but here's how to do it with just Python:

First, navigate to your home directory or some other location outside of this git repository:

`cd ~/`

Then, create a directory (folder) to house our new environment:

`mkdir nbody-env`

and create a new virtual environment with

`python3 -m venv nbody-env`.

To activate the environment, use

`source ~/nbody-env/bin/activate`.

To deactivate, just type `deactivate` at any time.

### Packages

We'll need some packages to help with parts of the project we don't want to do ourselves, like drawing.

Navigate back to this git repository using `cd`, and then

`pip install -r requirements.txt`

This should install all the necessary packages into your virtual environment.

## Introduction

Your goal for this project is to write a program simulating the motion of `N` objects in a plane, accounting for the gravitational forces mutually affecting each object as demonstrated by Sir Isaac Newton’s [Law of Universal Gravitation](http://en.wikipedia.org/wiki/Newton%27s_law_of_universal_gravitation).

Ultimately, you will be creating a program nbody.py that draws an animation of bodies floating around in space tugging on each other with the power of gravity.

## The Body Class and Its Constructor

You’ll start by creating a Body class. In your favorite text editor, create a new file called `Body.py`. If you haven’t picked a text editor, we recommend VSCode or Sublime Text. Remember that your `.py` files should have the same name as the class it contains.

Begin by creating a basic version of the `Body` class with the following 6 instance variables:

```python
    float xx_pos  # Its current x position
    float yy_pos  # Its current y position
    float xx_vel  # Its current velocity in the x direction
    float yy_vel  # Its current velocity in the y direction
    float mass # Its mass
    str img_filename # The name of the file that corresponds to the image that depicts the body (for example, jupiter.gif)
```

Your instance variables must be named exactly as above. The reason we call them by double letters, e.g. `xx_pos` rather than `x_pos` is to reduce the chance of typos. In past semesters, students have accidentally pressed x when they meant y, and this has caused significant debugging hassle. After adding the 6 instance variables above, add in a Body constructor (`__init__`) that can initialize an instance of the Body class. Later on, an instance of the Body class can represent a planet, star, or various objects in this universe. The signature of the first constructor should be:

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


All of the numbers for this project will be `float`s. We’ll go over what exactly a double is later in the course, but for now, think of it is a real number, e.g. `x = 3.5`.

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

Note that force is a vector (i.e., it has direction). In particular, be aware that dx and dy are signed (positive or negative).

- Net Force: The _principle of superposition_ says that the net force acting on a particle in the x- or y-direction is the sum of the pairwise forces acting on the particle in that direction.

In addition, all bodies have:

- Acceleration: Newton’s _second law of motion_ says that the accelerations in the x- and y-directions are given by:
    - $a_x = \dfrac{F_x}{m}$
    - $a_y = \dfrac{F_y}{m}$

Check your understanding!

Consider a small example consisting of two celestial objects: Saturn and the Sun. Suppose the Sun is at coordinates ($1.0 \cdot 10^{12}, 2.0 \cdot 10^{11}$) and Saturn is at coordinates ($2.3 \cdot 10^{12}, 9.5 \cdot 10^{11}$). Assume that the Sun’s mass is $2.0 \cdot 10^{30} \text{ kg}$ and Saturn’s mass is $6.0 \cdot 10^{26} \text{ kg}$. Here’s a diagram of this simple solar system:

Let’s run through some sample calculations. First let’s compute $F_1$, the force that Saturn exerts on the Sun. We’ll begin by calculating $r$, which we’ve already expressed above in terms of dx and dy. Since we’re calculating the force exerted by Saturn, dx is Saturn’s $x$-position minus Sun’s $x$-position, which is $1.3 \times 10^{12} \text{ m}$. Similarly, dy is $7.5 \cdot 10^{11} \text{ m}$.

So, $r^2 = dx^2 + dy^2 = (1.3 \cdot 10^{12})^2 + (7.5 \cdot 10^{11})^2$. Solving for $r$ gives us $1.5 \cdot 10^{12} \text{ m}$. Now that we have $r$, computation of F$ is straightforward:

$$F = \dfrac{G \cdot (2.0 \cdot 10^{30} \text{ kg}) \cdot (6.0 \cdot 10^{26} \text{kg})}{(1.5 \cdot 10^{12} \text{ m})^2} = 3.6 \cdot 10^{22} \text{ N}$$

Note that the magnitudes of the forces that Saturn and the Sun exert on one another are equal; that is, $|F| = |F_1| = |F_2|$. Now that we’ve computed the pairwise force on the Sun, let’s compute the x- and y-components of this force, denoted with $F_{1,x}$ and $F_{1, y}$, respectively. Recall that dx is $1.3 \cdot 10^{12}$ meters and dy is $7.5 \cdot 10^{11}$ meters. So,

$$F_{1,x} = \dfrac{F_1 \cdot (1.3 \cdot 10^{12} \text{ m})}{1.5 \cdot 10^{12} \text{ m}} = 3.1 \cdot 10^{22} \text{ N}$$
$$F_{1, y} = \dfrac{F_1 \cdot (7.5 \cdot 10^{11} \text{ m})}{1.5 \cdot 10^{12} \text{ m}} = 1.8 \cdot 10^{22} \text{ N}$$

Note that the sign of dx and dy is important! Here, dx and dy were both positive, resulting in positive values for $F_{1, x}$ and $F_{1, y}$. This makes sense if you look at the diagram: Saturn will exert a force that pulls the Sun to the right (positive $F_{1, x}$ ) and up (positive $F_{1, y}$).

Next, let’s compute the x and y-components of the force that the Sun exerts on Saturn. The values of dx and dy are negated here, because we’re now measuring the displacement of the Sun relative to Saturn. Again, you can verify that the signs should be negative by looking at the diagram: the Sun will pull Saturn to the left (negative dx) and down (negative dy).

$$F_{2, x} = \dfrac{F_2 \cdot (-1.3 \cdot 10^{12} \text{ m})}{1.5 \cdot 10^{12} \text{ m}} = -3.1 \cdot 10^{22} \text{ N}$$
$$F_{2, y} = \dfrac{F_2 \cdot(-7.5 \cdot 10^{11} \text{ m})}{1.5 \cdot 10^{12} \text{ m}} = -1.8 \cdot 10^{22} \text{ N}$$

Let’s add Neptune to the mix and calculate the net force on Saturn. Here’s a diagram illustrating the forces being exerted on Saturn in this new system:


We can calculate the $x$-component of the net force on Saturn by summing the $x$-components of all pairwise forces. Likewise, $F_{\text{net}, y}$ can be calculated by summing the y-components of all pairwise forces. Assume the forces exerted on Saturn by the Sun are the same as above, and that $F_{2,x} = 1.1 \cdot 10^{22} \text{ N}$ and $F_{2,y} = 9.0 \cdot 10^{21} \text{N}$.

$$F_{\text{net}, x} = F_{1, x} + F_{2, x} = -3.1 \cdot 10^{22} \text{ N} + 1.1 \cdot 10^{22} \text{ N} = -2.0 \cdot 10^{22} \text{ N}$$
$$F_{\text{net}, y} = F_{1, y} + F_{2, y} = -1.8 \cdot 10^{22} \text{ N} + 9.0 \cdot 10^{21} \text{ N} = -9.0 \cdot 10^{21} \text {N}$$

Double check your understanding!

Suppose there are three bodies in space as follows:

- Samh: $x = 1, y = 0, \text{mass} = 10$
- Aegir: $x = 3, y = 3, \text{mass} = 5$
- Rocinante: $x = 5, y = -3, \text{mass} = 50$

Calculate $F_{\text{net}, x}$ and $F_{\text{net}, y}$ exerted on Samh. To check your answer, click [here](http://www.wolframalpha.com/input/?i=%286.67+*+10%5E-11+*+10+*+5%29+%2F+13+*+2+%2F+sqrt%2813%29+%2B+%286.67+*+10%5E-11+*+10+*+50%29+%2F25+*+4+%2F+sqrt%2825%29) for $F_{\text{net}, x}$ and [here](http://www.wolframalpha.com/input/?i=%2810+*+5+*+6.67+*+10%5E-11%29+%2F13+*+3+%2F+sqrt%2813%29+-+%2850+*+10+*+6.67+*+10%5E-11%29+%2F+25+*+3+%2F+sqrt%2825%29) for $F_{\text{net}, y}$.

# Acknowledgements
This project is more or less a direct transcription of [Spring 2019 CS 61B Project 0](https://sp19.datastructur.es/materials/proj/proj0/proj0) from Java into Python. Thanks to Josh Hug, Matthew Chow, and Daniel Nguyen, and the original authors Robert Sedgewick and Kevin Wayne from Princeton University.