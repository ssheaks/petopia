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
    # Constructor.

    # Call the parent class (Sprite) constructor
    super().__init__()

    # Create an image loaded from the disk.
    pet_path_list = ['images/Sprite_Border_Collie.png', 'images/Sprite_Tabby_Cat.png', 'images/Sprite_Rabbit.png', 'images/Sprite_Parrot.png']

    self.image = pg.image.load(random.choice(pet_path_list))

    # Fetch the rectangle object that has the dimensions of the image, update the position of this object by setting the values of rect.x and rect.y
    self.rect = self.image.get_rect()

#initiate class flea
class Flea(pg.sprite.Sprite):

# This class represents the pet and derives from the "Sprite" class in Pygame.

  def __init__(self):
    # Constructor. 

    # Call the parent class (Sprite) constructor
    super().__init__()

    # Create an image loaded from the disk.
    self.image = pg.image.load('images/Sprite_Flea.png')

    # Fetch the rectangle object that has the dimensions of the image, update the position of this object by setting the values of rect.x and rect.y
    self.rect = self.image.get_rect()

  def reset_pos(self):
    # Reset position to the top of the screen, at a random x location. Called by update() or the main program loop if there is a collision.
        self.rect.y = random.randrange(-300, -20)
        self.rect.x = random.randrange(0, screenWidth - 97)
 
  def update(self):
    #  Called each frame.

    # Move block down one pixel
    self.rect.y += 1

    # If block is too far down, reset to top of screen.
    if self.rect.y > screenHeight + 10:
        self.reset_pos()

#initiate class player
class Player(pg.sprite.Sprite):

# This class represents the player and derives from the "Sprite" class in Pygame.

  def __init__(self):
    # Constructor. 

    # Call the parent class (Sprite) constructor
    super().__init__()

    # Create an image loaded from the disk.
    self.image = pg.image.load('images/Sprite_fly_swatter.png')

    # Fetch the rectangle object that has the dimensions of the image, update the position of this object by setting the values of rect.x and rect.y
    self.rect = self.image.get_rect()
  
  def update(self):
    # Get the current mouse position. This returns the position
    # as a list of two numbers.
    pos = pg.mouse.get_pos()

    # Fetch the x and y out of the list, just like we'd fetch letters out of a string. Set the player object to the mouse location
    self.rect.x = pos[0]
    self.rect.y = pos[1]


# def run_game():
#Initialize and set up screen.
pg.init()
screenWidth = 1100
screenHeight = 815
screen = pg.display.set_mode((screenWidth, screenHeight))
pg.display.set_caption("Petopia: Pet Rescue!")

# This is a list of pet sprites and each pet is added to this list. The list is managed by a class called 'Group.'
pet_list = pg.sprite.Group()

# This is a list of flea sprites and each flea is added to this list. The list is managed by a class called 'Group.'
flea_list = pg.sprite.Group()

#This is a list of all sprites
all_sprites_list = pg.sprite.Group()

# for loop for pets
for i in range(10):
  #this represents a pet
  pet = Pet()

# Set a random location for the pet
  pet.rect.x = random.randrange(screenWidth - 97)
  pet.rect.y = random.randrange(screenHeight - 100)

  # Add the pet to the list of objects
  pet_list.add(pet)
  all_sprites_list.add(pet)  

# for loop for fleas
for i in range(30):
  #this represents a pet
  flea = Flea()

# Set a random location for the flea
  flea.rect.x = random.randrange(screenWidth - 97)
  flea.rect.y = random.randrange(screenHeight - 100)

  # Add the flea to the list of objects
  flea_list.add(flea)
  all_sprites_list.add(flea)  

# create catcher for player
player = Player()
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
  
  #Can move code below to player class
  # Get the current mouse position. Returns position as a list of two numbers.
  # pos = pg.mouse.get_pos()

  # # Fetch the x and y out of the list like we fetch letters out of a string.
  # # Set the player object to the mouse location
  # player.rect.x = pos[0]
  # player.rect.y = pos[1]

  # Calls update() method on every sprite in the list
  all_sprites_list.update()

  # See if the player block has collided with fleas. True removes the block and returns a list of all colliding blocks
  flea_hit_list = pg.sprite.spritecollide(player, flea_list, False)

  # Check the list of collisions.
  for flea in flea_hit_list:
      score += 1
      print(score)
      # return score
      #reset fleas to fall again
      flea.reset_pos()

  # Draw all the spites
  all_sprites_list.draw(screen)

  # Limit to 60 frames per second
  clock.tick(60)

  #Refresh screen.
  pg.display.flip()

# run_game()
pg.quit()

