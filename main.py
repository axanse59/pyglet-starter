import pyglet # import the library
win= pyglet.window.Window() # create the window

# Create a sprite
img= pyglet.image.load('sheet.png')
smol_img = img.get_region(x=112, y=96, width=32, height=32)
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
    


pyglet.clock.schedule(update) 
pyglet.app.run()