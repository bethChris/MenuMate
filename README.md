# Python Library

This is the start of my own self-guided learning on how to make a python library from concept to creation to maintenence.

## Goals

1. Consolidate helpful code/functions I've created in the past for my own previous projects.
2. Clean and polish up this code to make it easy to read and use
3. Make it into a library that can be hosted on Pypi
4. Create a CI/CD pipeline for maintence
5. Make the documentation easily accessible and useful
 
## Tenetive Plans to Reach These Goals

1. Research how creating a library works
	- What tools will I need?
	- What skills will I need to brush up on?

2. Research what makes a library useful
	- What libraries are in use currently?
	- What are popular libraries? Why are they popular?

3. Research the CI/CD pipeline
	- What does this look like? How are they created?
	- What purpose/goal does this have in my project?

4. Comb through all projects, identify useful/not useful parts
	- What functions of my previous projects could be used elsewhere?
	- What made this project frustrating? What code did I create to ease that frustration?

5. Combine functions, freshen up logic and create supporting functions
	- What is the goal of this code?
	- What usefulness does it have? How could we improve it's impact?

6. (Continuous) Document!
	- What struggles did I have? (educational)
	- What pieces are unclear? (usability)
	- What's the structure of this library? (usability)
	- What are some examples of use? (usability)

7. Setup maintence pipeline
	- How do I plan to improve the project?
	- How will I update the project? 
	- What tests will it need to pass each iteration?
	- How will I set up these tests?


## Creating a Library
When creating a library, it's important to decide which **version** of python we should build in. We're thinking of this library not only as a cool collection of code, but also a *useful* collection of code. We need to go back a few versions from what's currently out to make it usuable for already created projects.

The most important thing to remember is that a library is meant to simplify and consolidate processes. The end result should be an easier way to do it than just creating the functionality from scratch. 

Creating a libarary is:
- creating a bunch of functions/features
- putting them into a folder with an empty `__init__.py` file
- using `setuptools`, `twine`, and `wheel` to set the project up for Pypi


### Tools/Needs
- Libraries: `setuptools`, `twine`, `wheel`
- Github
- Pypi and Test Pypi accounts
- Python version 3.9
- Virtual environment probably



## CI/CD Pipeline

### What is it?
- CI: Continuous Integration
- CD: Continuous Development

Basically, a processes to always be integrating new fixs/features and pushing out new releases. It is usually streamlined through workflows or steps for each change. For example:

- make fixes to a library
- push library to github
- github actions run several tests defined by us
- if tests pass, integrate changes
- if integrate new changes push up to Pypi

### How to Set Up?
For the most part we will be utilizing Github Action Templates to set this processes up for our own project. So far i've identified the following info about getting that set up:

- should be free for personal public repos
- they have templates to choose from based on your repos contents
- it will require setting up a YML file and a /workflows folder
- we can define what terminal commands to run and possibly set up tests to run/pass with pytest?

> NOTE: Check out the bookmarks tab for this project! (Study/Python Library). I found a good tutorial for how to set up the continous integration/deployment pipeline through github actions. 


## Implementation Notes
- I'm gonna need to learn how to call **handler functions** for the functionality I want to incorporate
- setuptools require a `setup.py` with the package information to work
- the code is split into 3 objects, splitting the functionality of the original `Menu` object into `Menu` and `MenuManager`.
- `MenuManager` will be the main controller of the selections and keeping track of the chaining menus.
- chaining Menus will work as long as there is no reference to a previous menu in a menu down the line. There's a "history" of where the user was last that the `MenuManager` will keep track of (via a stack). And a "back" button is included on Menus traveled to from another menu
