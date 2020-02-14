import pyglet # import the library
win= pyglet.window.Window() # create the window

# Create a sprite
img= pyglet.image.load('characters.png')
smol_img = img.get_region(x=0, y=0, width=25, height=16)
spr = pyglet.sprite.Sprite(smol_img, x = 200, y = 200)

keys = pyglet.window.key.KeyStateHandler()

def update(dt):
  win.push_handlers(keys)
  if keys[pyglet.window.key.LEFT]:
    spr.x -= 1
  if keys[pyglet.window.key.RIGHT]:
    spr.x += 1
  if keys[pyglet.window.key.DOWN]:
    spr.y -= 1
  if keys[pyglet.window.key.UP]:
    spr.y += 1

# Start the event loop
@win.event
def on_draw():
    win.clear()
    smol_img.blit(100,100)
    spr.draw()
    

# Create a sprite
the= pyglet.image.load('characters.png')
smol_the = the.get_region(x=0, y=25, width=25, height=32)
yr = pyglet.sprite.Sprite(smol_the, x = 100, y = 100)

keys = pyglet.window.key.KeyStateHandler()

def villiankeys(dt):
  win.push_handlers(keys)
  if keys[pyglet.window.key.LEFT]:
    spr.x -= 1
  if keys[pyglet.window.key.RIGHT]:
    spr.x += 1
  if keys[pyglet.window.key.DOWN]:
    spr.y -= 1
  if keys[pyglet.window.key.UP]:
    spr.y += 1

# Start the event loop
@win.event
def on_draw():
    win.clear()
    smol_the.blit(100,100)
    spr.draw()

pyglet.clock.schedule(update) 
pyglet.app.run()