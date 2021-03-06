import sys
import os
import math
# allows to randomly place sprites on screen
import random
import pygame as pg
from pygame.locals import *

#store images in dictionary so don't have to continuously load
_image_library = {}
def get_image(path):
  global _image_library
  image = _image_library.get(path)
  # image = pg.Surface((29, 30))
  if image == None:
    canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
    image = pg.image.load(canonicalized_path)
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

    # self.image = pg.image.load(random.choice(pet_path_list))
    self.image = get_image(random.choice(pet_path_list))

    # Fetch the rectangle object that has the dimensions of the image, update the position of this object by setting the values of rect.x and rect.y
    self.rect = self.image.get_rect()

    # The "center" the sprite will orbit
    self.center_x = 0
    self.center_y = 0

    # Current angle in radians
    self.angle = 0

    # How far away from the center to orbit, in pixels
    self.radius = 0

    # How fast to orbit, in radians per frame
    self.speed = 0.05
 
  def update(self):
      #Update the pet's position, calculate a new x, y
      self.rect.x = self.radius * math.sin(self.angle) + self.center_x
      self.rect.y = self.radius * math.cos(self.angle) + self.center_y

      # increase angle 
      self.angle += self.speed

#initiate class flea
class Flea(pg.sprite.Sprite):

# This class represents the pet and derives from the "Sprite" class in Pygame.
  def __init__(self):
    # Constructor. 

    # Call the parent class (Sprite) constructor
    super().__init__()

    # Create an image loaded from the disk.
    self.image = get_image('images/Sprite_Flea.png')

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
    if self.rect.y > screenHeight + 20:
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
screenWidth = 900
screenHeight = 667
screen = pg.display.set_mode((screenWidth, screenHeight))
pg.display.set_caption("Petopia: Pet Rescue!")

# This is a list of pet sprites and each pet is added to this list. The list is managed by a class called 'Group.'
pet_list = pg.sprite.Group()

# This is a list of flea sprites and each flea is added to this list. The list is managed by a class called 'Group.'
flea_list = pg.sprite.Group()

#This is a list of all sprites
all_sprites_list = pg.sprite.Group()

# for loop for pets
for i in range(15):
  #this represents a pet
  pet = Pet()
  # sets a random center location for the pet to orbit
  pet.center_x = random.randrange(screenWidth - 97)
  pet.center_y = random.randrange(screenHeight - 100)
  # random radius from 10 to 200
  pet.radius = random.randrange(10, 200)
  # random start angle from 0 to 2pi
  pet.angle = random.random() * 2 * math.pi
  # radians per frame
  pet.speed = 0.008

  # Add the pet to the list of objects
  pet_list.add(pet)
  all_sprites_list.add(pet)  

# for loop for fleas
for i in range(30):
  #this represents a pet
  flea = Flea()

# Set a random location for the flea
  flea.rect.x = random.randrange(screenWidth - 97)
  flea.rect.y = random.randrange(screenHeight - 500)

  # Add the flea to the list of objects
  flea_list.add(flea)
  all_sprites_list.add(flea)  

# create catcher for player
player = Player()
all_sprites_list.add(player)

# This is a font we use to draw text on the screen (size 36)
font = pg.font.Font(None, 36)

#will trigger game over when set to true
game_over = False
#loop until user clicks close (will update to timer)
done = False
#will display instructions when set to True
display_instructions = True
instruction_page = 1

# Used to manage how fast the screen updates
clock = pg.time.Clock()

score = 0

#load background image
background_image = pg.image.load("picnic-area-149153_1280.png").convert()

#starter tick
start_ticks=pg.time.get_ticks() 
print(start_ticks)

#Start main loop.
while not done: 
  #calculate how many seconds
  seconds = (pg.time.get_ticks() - start_ticks)/1000 
  #start event loop.
  for event in pg.event.get():
    if event.type == pg.QUIT:
      done = True #same thing as sys.exit
    #   # sys.exit()
    elif seconds > 40:
      game_over = True

  #set background image
  screen.blit(background_image, [0, 0])

  #Render score to screen
  msg = "Score: %d" % (score)
  text = font.render(msg, True, (255, 255, 255))
  text_rect = text.get_rect()
  screen.blit(text, [10, 10])

  if not game_over:
    pg.mouse.set_visible(False)
    # Calls update() method on every sprite in the list
    all_sprites_list.update()

    # See if the player has collided with fleas. True removes the flea and returns a list of all colliding blocks
    flea_hit_list = pg.sprite.spritecollide(player, flea_list, False)

    # Check the list of collisions.
    for flea in flea_hit_list:
        score += 1
        print(score)
        #reset fleas to fall again
        flea.reset_pos()

    for flea in flea_list:
      if flea.rect.y > screenHeight + 10:
        score -=1
        print(score)

  # Draw all the spites
  all_sprites_list.draw(screen)

  if game_over:
        # If game over is true, draw game over
        pg.mouse.set_visible(True)
        text = font.render("Game Over", True, (255, 255, 255))
        text_rect = text.get_rect()
        text_x = screen.get_width() / 2 - text_rect.width / 2
        text_y = screen.get_height() / 2 - text_rect.height / 2
        screen.blit(text, [text_x, text_y])

  # Limit to 60 frames per second
  clock.tick(60)

  #Refresh screen.
  pg.display.flip()

# run_game()
pg.quit()

