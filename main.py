import sys
import os
# allows to randomly place sprites on screen
import random
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

#initiate class pet
class Pet(pg.sprite.Sprite):

# This class represents the pet and derives from the "Sprite" class in Pygame.

  def __init__(self):
    # Constructor. Pass in the color of the block,
    # and its x and y position. 

    # Call the parent class (Sprite) constructor
    super().__init__()

    # Create an image loaded from the disk.
    self.image = pg.image.load('images/Cartoon_Border_Collie.png')
    # self.image.fill(color)

    # Fetch the rectangle object that has the dimensions of the image
    # image.
    # Update the position of this object by setting the values
    # of rect.x and rect.y
    self.rect = self.image.get_rect()

#initiate class flea

# image = py.image.load('images/Cartoon_Border_Collie.png')

# def run_game():
#Initialize and set up screen.
pg.init()
screenWidth = 1280
screenHeight = 948
screen = pg.display.set_mode((screenWidth, screenHeight))
pg.display.set_caption("Petopia: Pet Rescue!")

# This is a list of 'sprites.' Each block in the program is
# added to this list. The list is managed by a class called 'Group.'
pet_list = pg.sprite.Group()

#This is a list of all sprites
all_sprites_list = pg.sprite.Group()

# for loop for pets
for i in range(10):
  #this represents a pet
  pet = Pet()

# Set a random location for the block
  pet.rect.x = random.randrange(screenWidth)
  pet.rect.y = random.randrange(screenHeight)

  # Add the block to the list of objects
  pet_list.add(pet)
  all_sprites_list.add(pet)  

# create catcher for player
player = Pet()
all_sprites_list.add(player)

##loop until user clicks close (will update to timer)
done = False

# Used to manage how fast the screen updates
clock = pg.time.Clock()

score = 0

#load background image
background_image = pg.image.load("picnic-area-149153_1280.png").convert()
#get dog image for now without using the get_image function
# husky = screen.blit(get_image('images/Cartoon_Border_Collie.png'), (20, 30))
#get rect object from an image
# husky_rect = husky.get_rect(topleft=(100, 300))

#Start main loop.
while not done: 
  #start event loop.
  for event in pg.event.get():
    if event.type == pg.QUIT:
      done = True #same thing as sys.exit
      # sys.exit()
  #set background image
  screen.blit(background_image, [0, 0])
  
  # Get the current mouse position. This returns the position as a list of two numbers.
  pos = pg.mouse.get_pos()

  # Fetch the x and y out of the list like we fetch letters out of a string.
  # Set the player object to the mouse location
  player.rect.x = pos[0]
  player.rect.y = pos[1]

  # See if the player block has collided with anything.
  pets_hit_list = pg.sprite.spritecollide(player, pet_list, True)

  # Check the list of collisions.
  for pet in pets_hit_list:
      score += 1
      print(score)
      # return score

  # Draw all the spites
  all_sprites_list.draw(screen)

  #Refresh screen.
  pg.display.flip()

  # Limit to 60 frames per second
  clock.tick(60)

# run_game()
pg.quit()

