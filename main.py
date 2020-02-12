import pyglet # import the library
win= pyglet.window.Window() # create the window

# Create a sprite
img= pyglet.image.load('sheet.png')
smol_img = img.get_region(x=112, y=96, width=32, height=32)

def update(dt):
  pass

# Start the event loop
@win.event
def on_draw():
    win.clear()
    smol_img.blit(100, 150)

# Create a sprite
Get= pyglet.image.load('Overworld.png')
smol_img = img.get_region(x=56, y=96, width=32, height=32)

def update(dt):
  pass

# Start the event loop
@win.event
def on_draw():
    win.clear()
    smol_img.blit(100, 150)

three= pyglet.image.load('cave')
smol_img = img.get_region(x=0, y=380, width=32, height=32)

def update(dt):
  pass

# Start the event loop
@win.event
def on_draw():
    win.clear()
    smol_img.blit(100, 150)

# Create the text object
text = pyglet.text.Label('Welcome', x = 100, y = 50)


# inside the loop:
def on_draw():
  text.draw()


pyglet.clock.schedule(update) 
pyglet.app.run()