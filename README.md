# Overview
This program is a simple UI where users can log in and register. After the user is logged in, the user will be exposed to some simple features of the program.
The objective of this project is for me to learn how to use Python and create UI apps. I would continue working on the creation of UI and I will try different languages to find out to create a modern-looking UI. Another reason why I decided to create a UI is that I want to create a basic game and connect the game with a UI so that users can log in and register to play the game.
The following code is a demonstration of the Python code I wrote; the code shows how to create a class and how to build getters and setters for that class. The __init__ function is a constructor and it defines how many variables the class will have.
``` Python
class currentUser:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
    def set_user(self, username):
        self.username = username
    def get_user(self):
        return self.username
    def set_email(self, email):
        self.email = email
    def get_email(self):
        return self.email
    def set_password(self, password):
        self.password = password
    def get_password(self):
        return self.password
```
{Provide a link to your YouTube demonstration.  It should be a 4-5 minute demo of the software running and a walkthrough of the code.  Focus should be on sharing what you learned about the language syntax.}

[Software Demo Video](http://youtube.link.goes.here)

# Development Environment

The tools that I used are Visual Studio Code, Git, GitHub, and Python. I used the internet and Youtube as medias to look for extra information as well.
I created this software using Python and installed the library to Tkinter to create the UI windows. You can install Tkinter with the command: pip install tkinter. The following are the libraries that I used to create this software.

```python
import tkinter as tk
import re
from tkinter import messagebox
from tkinter.constants import END
from PIL import Image, ImageTk
```

# Useful Websites

* [Tk themed widgets](https://docs.python.org/3/library/tkinter.ttk.html)
* [Basic Widgets](https://tkdocs.com/tutorial/widgets.html)

# Future Work

* Connect the data to an online database using MySQL
* Reuse the UI to connect to a simple Python game
* Make the UI more visually appealing