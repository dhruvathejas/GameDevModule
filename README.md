# GameDev 🎮

A lightweight, beginner-friendly Python game development module built on top of Python's built-in `turtle` library.

The goal of **GameDev** is to make simple 2D games easier to create without requiring a large external game engine.

## 🚀 Installation

Install the latest version directly from GitHub:

```bash
python -m pip install git+https://github.com/dhruvathejas/game-dev-module.py.git
```

After installation:

```python
import gamedev
```

---

# ✨ Features

GameDev currently provides:

- 🎮 Game loop
- 🧩 Sprite system
- ⌨️ Keyboard input
- 🎨 Sprite colors
- 📏 Sprite size control
- 📍 Sprite positioning
- 🔵 Dot-based sprites
- ✏️ Drawing tools
- ▭ Rectangle drawing
- ⭕ Circle drawing
- 🧹 Screen clearing
- 🏃 Sprite movement
- 🔍 Sprite attribute getters
- ⚙️ Sprite attribute setters
- 🪶 Lightweight API
- 🐍 Built with Python and Turtle

---

# 📦 Version

Current version:

```text
1.10
```

GameDev is currently a work in progress.

---

# 🐍 Requirements

GameDev requires:

- Python 3.8 or newer
- Python's built-in `turtle` module
- Tkinter

No external game engine is required.

---

# 🎮 Basic Example

```python
import gamedev

gamedev.Sprite.create_sprite(
    "player",
    0,
    0,
    50,
    "blue",
    1,
    1
)

gamedev.GameLoop.game_loop()
```

This creates a blue player sprite and starts the game loop.

---

# 🧩 Sprites

GameDev has a simple sprite system.

A sprite contains:

1. Name
2. X position
3. Y position
4. Size
5. Color
6. Draw setting
7. Dot setting

Create a sprite:

```python
gamedev.Sprite.create_sprite(
    "player",
    0,
    0,
    50,
    "blue",
    1,
    1
)
```

The arguments are:

```text
name
x
y
size
colour
draw
dot
```

Example:

```python
gamedev.Sprite.create_sprite(
    "enemy",
    100,
    50,
    30,
    "red",
    1,
    1
)
```

---

# 📍 Sprite Movement

## Move on the X axis

```python
gamedev.Sprite.move_x("player", 10)
```

Move left:

```python
gamedev.Sprite.move_x("player", -10)
```

Move right:

```python
gamedev.Sprite.move_x("player", 10)
```

## Move on the Y axis

```python
gamedev.Sprite.move_y("player", 10)
```

Move up:

```python
gamedev.Sprite.move_y("player", 10)
```

Move down:

```python
gamedev.Sprite.move_y("player", -10)
```

## Move on both axes

```python
gamedev.Sprite.move("player", 10, 5)
```

This changes the sprite's position by:

```text
X + 10
Y + 5
```

---

# 🎯 Setting Position

Set the X position:

```python
gamedev.Sprite.set_x("player", 200)
```

Set the Y position:

```python
gamedev.Sprite.set_y("player", 100)
```

Example:

```python
gamedev.Sprite.set_x("player", 0)
gamedev.Sprite.set_y("player", 0)
```

---

# 📏 Sprite Size

Change the size of a sprite:

```python
gamedev.Sprite.set_size("player", 75)
```

Example:

```python
gamedev.Sprite.set_size("enemy", 100)
```

---

# 🎨 Sprite Colors

Change a sprite's color:

```python
gamedev.Sprite.set_colour("player", "green")
```

Examples of colors:

```text
red
blue
green
yellow
purple
orange
black
white
```

---

# ⌨️ Keyboard Input

GameDev provides the `key()` function for keyboard controls.

```python
gamedev.key("Left", left)
```

Example:

```python
def left():
    gamedev.Sprite.move_x("player", -10)

gamedev.key("Left", left)
```

You can create controls for all four arrow keys:

```python
def left():
    gamedev.Sprite.move_x("player", -10)

def right():
    gamedev.Sprite.move_x("player", 10)

def up():
    gamedev.Sprite.move_y("player", 10)

def down():
    gamedev.Sprite.move_y("player", -10)

gamedev.key("Left", left)
gamedev.key("Right", right)
gamedev.key("Up", up)
gamedev.key("Down", down)
```

---

# ✏️ Drawing

GameDev includes basic drawing functions.

## Draw a line

```python
gamedev.paint(0, 0, 100, 100)
```

This draws a line between two coordinates.

---

# 🖊️ Drawing Mode

Start drawing:

```python
gamedev.paint_start()
```

Stop drawing:

```python
gamedev.paint_stop()
```

---

# 🎨 Drawing Color

Change the drawing color:

```python
gamedev.paint_color("red")
```

Then draw:

```python
gamedev.paint(0, 0, 100, 0)
```

---

# 📏 Drawing Size

Change the pen size:

```python
gamedev.paint_size(5)
```

---

# ▭ Rectangles

Draw a rectangle:

```python
gamedev.paint_rectangle(
    0,
    0,
    100,
    50
)
```

Arguments:

```text
x
y
width
height
```

---

# ⭕ Circles

Draw a circle:

```python
gamedev.paint_circle(
    0,
    0,
    50
)
```

---

# 🚶 Turtle Movement

Move the drawing position along the X axis:

```python
gamedev.move_by_x(10)
```

Move along the Y axis:

```python
gamedev.move_by_y(10)
```

---

# 🧹 Clear the Screen

Clear the Turtle screen:

```python
gamedev.clear()
```

---

# 🔍 Getting Sprite Information

GameDev provides functions for reading sprite properties.

Get X:

```python
x = gamedev.Sprite.get_x("player")
```

Get Y:

```python
y = gamedev.Sprite.get_y("player")
```

Get size:

```python
size = gamedev.Sprite.get_size("player")
```

Get color:

```python
colour = gamedev.Sprite.get_colour("player")
```

Get draw setting:

```python
draw = gamedev.Sprite.get_draw("player")
```

Get dot setting:

```python
dot = gamedev.Sprite.get_dot("player")
```

Example:

```python
x = gamedev.Sprite.get_x("player")

print(x)
```

---

# ⚙️ Changing Sprite Properties

Sprite properties can be changed after creation.

```python
gamedev.Sprite.set_x("player", 100)
gamedev.Sprite.set_y("player", 50)
gamedev.Sprite.set_size("player", 80)
gamedev.Sprite.set_colour("player", "yellow")
gamedev.Sprite.set_draw("player", 1)
gamedev.Sprite.set_dot("player", 1)
```

---

# 🗑️ Deleting Sprites

Delete a sprite using its name:

```python
gamedev.Sprite.delete_sprite("enemy")
```

---

# 🔄 Game Loop

Start the GameDev game loop with:

```python
gamedev.GameLoop.game_loop()
```

The game loop continuously:

1. Clears the screen
2. Reads sprite information
3. Draws the sprites
4. Updates the screen
5. Repeats

Conceptually:

```text
START
  ↓
Clear screen
  ↓
Read sprite data
  ↓
Draw sprites
  ↓
Update screen
  ↓
Repeat
  ↓
∞
```

---

# 🕹️ Complete Example

```python
import gamedev

gamedev.Sprite.create_sprite(
    "player",
    0,
    0,
    50,
    "blue",
    1,
    1
)

def left():
    gamedev.Sprite.move_x("player", -10)

def right():
    gamedev.Sprite.move_x("player", 10)

def up():
    gamedev.Sprite.move_y("player", 10)

def down():
    gamedev.Sprite.move_y("player", -10)

gamedev.key("Left", left)
gamedev.key("Right", right)
gamedev.key("Up", up)
gamedev.key("Down", down)

gamedev.GameLoop.game_loop()
```

This creates a controllable player using the arrow keys.

---

# 🧠 How Sprites Are Stored

GameDev uses two lists for its sprite system:

```python
names = []
attributes = []
```

Sprite names are stored in `names`.

Sprite properties are stored in `attributes`.

For example:

```python
names = [
    "player",
    "enemy"
]
```

The corresponding attributes could be:

```python
attributes = [
    [0, 0, 50, "blue", 1, 1],
    [100, 50, 30, "red", 1, 1]
]
```

The indexes correspond to each other.

```text
names[0]       → attributes[0]
"player"       → player attributes

names[1]       → attributes[1]
"enemy"        → enemy attributes
```

This keeps the sprite system simple and easy to understand.

---

# 🏗️ Project Structure

A typical project using GameDev can look like:

```text
my_game/
│
├── main.py
│
└── gamedev/
    ├── __init__.py
    └── core.py
```

Your game's code can be placed in `main.py`.

The GameDev engine itself can be contained inside the package.

---

# ⚠️ Importing GameDev

When GameDev is installed as a package, importing it should not automatically start the game loop.

This:

```python
import gamedev
```

should simply load the module.

The game loop can then be started manually:

```python
gamedev.GameLoop.game_loop()
```

This makes GameDev easier to use as a normal Python package.

---

# 🚧 Development Status

GameDev is currently a **work in progress**.

The API may change as development continues.

Possible future features include:

- 💥 Collision detection
- 🖼️ Sprite images
- 🎞️ Animation
- 🔊 Sound
- 🖱️ Mouse input
- 🌍 Physics
- 🪂 Gravity
- 💨 Velocity
- ⏱️ Timers
- 📝 Text rendering
- 🎬 Scenes
- 📷 Camera movement
- 🧱 Boundaries
- 🔷 More shapes
- 🚀 Improved rendering

These features are planned ideas and may not currently be implemented.

---

# 📜 License

No license has been specified yet.

Until a license is added, the project's default copyright applies.

---

# 👨‍💻 Author

**Dhruva Thejas**

GameDev is an experimental Python game-development project designed to make creating simple games easier.

---

# ⭐ GitHub

GameDev is developed on GitHub.

Install it directly with:

```bash
python -m pip install git+https://github.com/dhruvathejas/game-dev-module.py.git
```

---

# 🎮 The Idea

GameDev is built around a simple concept:

```text
Python
   ↓
Turtle
   ↓
GameDev
   ↓
Sprites + Input + Drawing
   ↓
Game Loop
   ↓
🎮 GAME
```

The project is small, simple, and still evolving.

---

# 🧠 How GameDev Works

GameDev is built on top of Python's built-in `turtle` module.

Instead of being a huge game engine, GameDev provides a small layer of functions that makes common game-development tasks easier.

The basic architecture is:

```text
Your Game
   ↓
GameDev
   ↓
Python Turtle
   ↓
Tkinter Window
   ↓
Your Screen
```

## 🎮 The Game Loop

The game loop is the part that keeps the game running.

GameDev repeatedly:

```text
1. Clears the previous frame
        ↓
2. Reads the sprite lists
        ↓
3. Draws each sprite
        ↓
4. Updates the Turtle screen
        ↓
5. Repeats
```

This happens continuously while:

```python
gamedev.GameLoop.game_loop()
```

is running.

Because the loop runs repeatedly, changing a sprite's position can make it appear to move across the screen.

---

# 🧩 How Sprites Work

GameDev stores sprite information using two lists:

```python
names = []
attributes = []
```

The `names` list stores the sprite names.

The `attributes` list stores the properties of each sprite.

For example:

```python
names = [
    "player",
    "enemy"
]
```

The corresponding attributes could be:

```python
attributes = [
    [0, 0, 50, "blue", 1, 1],
    [100, 50, 30, "red", 1, 1]
]
```

The information is connected by its index:

```text
names[0]       → attributes[0]
"player"       → [0, 0, 50, "blue", 1, 1]

names[1]       → attributes[1]
"enemy"        → [100, 50, 30, "red", 1, 1]
```

Each attribute has a specific meaning:

```text
attributes[i][0] → X position
attributes[i][1] → Y position
attributes[i][2] → Size
attributes[i][3] → Colour
attributes[i][4] → Draw setting
attributes[i][5] → Dot setting
```

This simple structure makes the sprite system easy to modify.

---

# 🔧 How To Tweak GameDev

GameDev is designed to be modified.

You can edit the source code to add your own features, change existing behavior, or experiment with the engine.

## 📍 Change Sprite Movement

The normal X movement function is:

```python
attributes[i][0] += amount
```

You could change how movement works by modifying this part of the source code.

For example, you could add a movement multiplier:

```python
attributes[i][0] += amount * 2
```

Now the same movement command moves a sprite twice as far.

---

# 🏃 Add Speed

You could add a speed value to each sprite.

For example, your attributes could eventually become:

```python
[x, y, size, colour, draw, dot, speed]
```

Then movement could use:

```python
attributes[i][0] += amount * attributes[i][6]
```

This could allow different sprites to have different speeds.

---

# 💥 Adding Collision Detection

Collision detection can be added by comparing sprite positions.

A simple distance-based check could use:

```python
dx = Sprite.get_x("player") - Sprite.get_x("enemy")
dy = Sprite.get_y("player") - Sprite.get_y("enemy")
```

Then calculate the distance:

```python
distance = (dx ** 2 + dy ** 2) ** 0.5
```

You could use that distance to determine whether two sprites are close enough to interact.

---

# 🌍 Adding Physics

GameDev can also be extended with physics.

For example, a future physics system could store:

```text
X position
Y position
X velocity
Y velocity
Gravity
Acceleration
```

A game could then update a sprite's position every frame.

Conceptually:

```text
Velocity
   ↓
Position
   ↓
Draw sprite
   ↓
Next frame
```

---

# 🖼️ Adding Images

The current sprite system is based around Turtle drawing.

A future version could support image-based sprites.

For example:

```python
Sprite.create_sprite(
    "player",
    0,
    0,
    50,
    "blue",
    1,
    1
)
```

could eventually be extended with an image parameter.

This would allow games to use custom artwork instead of only simple shapes.

---

# 🛠️ Modifying The Source Code

If you have downloaded or cloned the repository, you can edit the GameDev source code directly.

A typical structure could look like:

```text
game-dev-module.py/
│
├── gamedev/
│   ├── __init__.py
│   └── core.py
│
├── pyproject.toml
├── README.md
└── LICENSE
```

The main GameDev implementation can be edited inside the package source files.

After making changes, reinstall your local version if necessary:

```bash
python -m pip install .
```

You can then test your modified version.

---

# 🧪 Experimenting

GameDev is intended to be experimented with.

You can:

- Add new functions
- Change sprite behavior
- Add new attributes
- Create new drawing functions
- Add collision detection
- Add physics
- Add animations
- Add new input methods
- Improve the game loop
- Create your own systems

If you modify the source, make sure you understand which parts of the engine depend on the data structures you change.

For example, adding a new item to `attributes` means the code that reads `attributes` may also need to be updated.

---

# 📜 Copyright & Permission

GameDev is copyrighted by its author.

**Copyright © 2026 Dhruva Thejas**

Unless a license or written permission says otherwise, copyright law applies to the source code.

That means users should **not assume that they automatically have permission to redistribute, relicense, or publish modified copies of the project.**

## ✅ What You Can Do

You may use the project for personal learning and experimentation.

You may also modify your own copy for testing and development.

## ⚠️ Redistribution

Do not redistribute the GameDev source code, publish modified copies, or claim the project as your own unless you have permission from the copyright holder or a license has been added that allows it.

## 🧑‍💻 Want To Modify It?

You can experiment with your own local copy.

If you want to distribute your modified version publicly, obtain permission from the copyright holder first unless a future license explicitly permits it.

## 🏷️ Attribution

If permission is granted to use or distribute the project, keep the original copyright and author information unless the permission explicitly says otherwise.

---

# 🔐 Copyright Notice

```text
Copyright © 2026 Dhruva Thejas

GameDev is currently distributed without an open-source license.

Permission to use, modify, copy, publish, or redistribute the
source code beyond personal use has not been granted unless
explicitly stated by the copyright holder.
```

---

# 📌 Important

The copyright section describes the project's current status.

If a license is added to the repository in the future, the license included with the project should be used to determine what permissions are granted.

---

# 🚀 Keep Building

GameDev is designed to grow.

Start with:

```text
Sprites
   ↓
Movement
   ↓
Input
   ↓
Game Loop
```

Then build:

```text
Physics
   ↓
Collision
   ↓
Animation
   ↓
Images
   ↓
Sound
   ↓
Bigger Games
```

The engine starts small, but the code is yours to explore, understand, and improve within the permissions that apply to the project.