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
def CopyBody(b: Body) -> Body:
```


All of the numbers for this project will be `float`s. We’ll go over what exactly a double is later in the course, but for now, think of it is a real number, e.g. `x = 3.5`.

Once you have filled in the constructors, you can test it out by running `body_test.py`.

You can run our provided test with the command
`python -m unittest body_test`

If you pass this test, you’re ready to move on to the next step. Do not proceed until you have passed this test.

# Acknowledgements
This project is more or less a direct transcription of [Spring 2019 CS 61B Project 0](https://sp19.datastructur.es/materials/proj/proj0/proj0) from Java into Python. Thanks to Josh Hug, Matthew Chow, and Daniel Nguyen, and the original authors Robert Sedgewick and Kevin Wayne from Princeton University.