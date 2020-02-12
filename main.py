import pyglet # import the library
win= pyglet.window.Window() # create the window
win.blit()


text = pyglet.text.Label('Hello, world', x = 200, y = 200)


# inside the loop:
def on_draw():
  text.draw()

# Create a sprite
img= pyglet.image.load('assets/hero/Old hero.png')

def update(dt):
  pass

# Start the event loop
@window.event
def on_draw():
    win.clear()
    img.blit(100, 150)

pyglet.clock.schedule(update) 
pyglet.app.run()