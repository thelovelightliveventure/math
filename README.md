# Welcome to ```math```!
This is a repository that holds my most useful project to date: __The Statistics Program__!

## What does ``The Statistics Program``` do?
It calculates Measures of Central Tendency (```MCT```) and Method of Least Squares (```MLS```). 
For ```MCT```, there are a couple of options: ```mean```, ```median```, and ```mode```.
For ```MLS```, there are also a couple of options: ```Linear Regression``` and ```Non-linear Regression```. [^note]

## How is this project useful?
If you've ever calculated mean, median, or mode, you know that it takes a lot of time and a lot of steps. The more steps, the more errors there will be! As a result,
I've built this project so that no one needs to do it by hand.
Linear regression and non-linear regression take even more time! And it's mostly done by hand, which makes it a very strenous process. Because of my dislike of them in 
Precalculus class, I decided to build this program, to make life easier for you all. Also, AI's notoriously bad at linear regression and non-linear regression (it's also bad at 
standard deviation, something I might add to this project in the future).

## What files are in this project?
Currently, there are only a couple of files:

```python.py``` has all the main scripts for the program. It welcomes the user, finds the program the user needs, receives the user's input, and calculates what the output
should be. 

```db_setup.py``` sets up the database for the ```python.py``` script and defines it for the rest of the script. It's a helper script, if you will.

```script.sql``` has all the tables for ```python.py```. This is the database that ```db_setup.py``` is pulling from. As of right now, it's not very useful, but once I write the MLS programs, this will be hugely helpful!

[^note]: __This project is still underway.__
