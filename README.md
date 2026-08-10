# GameDev v1.0

A simple Python game-development module built with Turtle.

## Installation

Install directly from GitHub:

```powershell
python -m pip install git+https://github.com/dhruvathejas/game-dev-module.py.git
```

Then import it:

```python
import gamedev
```

---

# Basic Functions

## `paint()`

Draw a line from `(x1, y1)` to `(x2, y2)`.

```python
gamedev.paint(x1, y1, x2, y2)
```

Example:

```python
gamedev.paint(-100, 0, 100, 0)
```

Arguments:

```text
x1, y1, x2, y2
```

## `paint_start()`

Turns the pen on.

```python
gamedev.paint_start()
```

## `paint_stop()`

Turns the pen off.

```python
gamedev.paint_stop()
```

Use this when you want to move without drawing.

## `paint_color()`

Changes the drawing colour.

```python
gamedev.paint_color("red")
```

Examples:

```python
gamedev.paint_color("blue")
gamedev.paint_color("green")
gamedev.paint_color("yellow")
```

## `paint_size()`

Changes the pen thickness.

```python
gamedev.paint_size(10)
```

A larger number makes a thicker line.

## `paint_rectangle()`

Draws a rectangle.

```python
gamedev.paint_rectangle(x, y, width, height)
```

Example:

```python
gamedev.paint_rectangle(-100, 100, 200, 100)
```

## `paint_move()`

Moves to an exact position.

```python
gamedev.paint_move(x, y)
```

Example:

```python
gamedev.paint_move(50, 100)
```

## `move_by_x()`

Changes the current X position.

```python
gamedev.move_by_x(20)
```

Negative values move left:

```python
gamedev.move_by_x(-20)
```

## `move_by_y()`

Changes the current Y position.

```python
gamedev.move_by_y(20)
```

Negative values move down:

```python
gamedev.move_by_y(-20)
```

## `paint_circle()`

Draws a circle.

```python
gamedev.paint_circle(x, y, size)
```

Example:

```python
gamedev.paint_circle(0, 0, 50)
```

## `clear()`

Clears the drawing.

```python
gamedev.clear()
```

---

# Sprites

Sprites store game objects and their properties.

## Creating a Sprite

First create the Sprite object:

```python
player = gamedev.Sprite()
```

Then register it:

```python
gamedev.Sprite.create_sprite(
    player,
    0,
    0,
    30,
    "blue",
    1,
    1
)
```

The argument order is:

```text
name, x, y, size, colour, draw, dot
```

So the example creates:

```text
name   = player
x      = 0
y      = 0
size   = 30
colour = blue
draw   = 1
dot    = 1
```

---

# Sprite Properties

Sprite properties can be changed directly.

## X

Move right:

```python
player.x += 5
```

Move left:

```python
player.x -= 5
```

## Y

Move up:

```python
player.y += 5
```

Move down:

```python
player.y -= 5
```

## Size

```python
player.size = 50
```

## Colour

```python
player.colour = "red"
```

## Draw

Enable drawing:

```python
player.draw = 1
```

Disable drawing:

```python
player.draw = 0
```

## Dot

Enable the dot:

```python
player.dot = 1
```

Disable the dot:

```python
player.dot = 0
```

---

# `game_frame()`

`game_frame()` renders the sprites.

```python
gamedev.game_frame()
```

It goes through the sprite list and uses each sprite's:

```text
x
y
size
colour
draw
dot
```

to decide what to render.

A basic game loop looks like:

```python
while True:
    # Change game variables

    gamedev.game_frame()
```

The basic idea is:

```text
change game state
       ↓
game_frame()
       ↓
draw sprites
       ↓
update screen
       ↓
repeat
```

---

# Complete Tiny Game

```python
import gamedev

player = gamedev.Sprite()

gamedev.Sprite.create_sprite(
    player,
    0,
    0,
    40,
    "blue",
    1,
    1
)

while True:
    player.x += 2

    if player.x > 300:
        player.x = -300

    gamedev.game_frame()
```

This creates a blue player sprite that moves across the screen and wraps around when it reaches the edge.

---

# GameDev Toolbox

| Function | What it does |
|---|---|
| `paint()` | Draw a line |
| `paint_start()` | Start drawing |
| `paint_stop()` | Stop drawing |
| `paint_color()` | Change pen colour |
| `paint_size()` | Change pen size |
| `paint_rectangle()` | Draw a rectangle |
| `paint_move()` | Move to a position |
| `move_by_x()` | Move relative to X |
| `move_by_y()` | Move relative to Y |
| `paint_circle()` | Draw a circle |
| `clear()` | Clear the drawing |
| `Sprite.create_sprite()` | Create/register a sprite |
| `game_frame()` | Render all sprites |
| Manual sprite variables wit h an operater.| Change sprite.x, sprite.y, sprite.size, sprite.colour, sprite.draw, or sprite.dot directly |
---

# Core Game Pattern

The main GameDev idea is simple:

```python
while True:
    player.x += 5
    enemy.x -= 3

    gamedev.game_frame()
```

Change your game variables, then render the frame.

