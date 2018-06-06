import sys
import os
import pygame as pg
from pygame.locals import *

_image_library = {}
def get_image(path):
        global _image_library
        image = _image_library.get(path)
        # image = pg.Surface((29, 30))
        if image == None:
                canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
                image = pg.image.load(canonicalized_path)
                #this rescales images
                image = pg.transform.scale(image, (97, 100))
                _image_library[path] = image
        return image

# image = py.image.load('images/Cartoon_Border_Collie.png')

def run_game():
  #Initialize and set up screen.
  pg.init()
  screen = pg.display.set_mode((1280, 948))
  pg.display.set_caption("Petopia: Pet Rescue!")
  #load background image
  background_image = pg.image.load("picnic-area-149153_1280.png").convert()
  #Start main loop.
  while True: 
    #start event loop.
    for event in pg.event.get():
      if event.type == pg.QUIT:
        sys.exit()
    #set background image
    screen.blit(background_image, [0, 0])
    #get dog image 
    screen.blit(get_image('images/Cartoon_Border_Collie.png'), (20, 30))
    #Refresh screen.
    pg.display.flip()

run_game()