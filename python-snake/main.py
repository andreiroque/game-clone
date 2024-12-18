import pygame
import random

pygame.init()
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Snake Clone")
clock = pygame.time.Clock()

running = True
score_counter = 0
grid_size = 10
move_delay = 50 #delay between movements in milliseconds 
last_move_time = 0
tail = []
has_eaten = False

text = ""


font = pygame.font.Font("DejaVuSansMono.ttf", 20)

def renderScore():
  text = font.render(f"Score: {score_counter}",  True, (255, 255, 255), (0, 0, 0))
  textRect = text.get_rect()
  textRect.center = (60, 30)
  screen.blit(text, textRect)

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
direction = pygame.Vector2(grid_size, 0) # Initialize moving to rigth by 10px

def summonFood():
   return  pygame.Vector2(random.randrange(0, screen.get_width(), 10), random.randrange(0, screen.get_height(), 10))

food_pos = summonFood()

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  current_time = pygame.time.get_ticks()
  if current_time - last_move_time > move_delay:

    previous_pos = player_pos.copy()

    player_pos += direction

    if len(tail) > 0:
      tail.insert(0, previous_pos)
      tail.pop()
      has_eaten = True
      for i in range(0, len(tail)):
        if player_pos.x == tail[i].x and player_pos.y == tail[i].y :
          running = False
    last_move_time = current_time
    has_eaten = False
  screen.fill("black")

  #Draw grid
  # for col in range(40):
  #   for row in range(40):
  #     pygame.draw.rect(screen, (33, 33, 33),pygame.Rect(row * 10, col * 10, 10, 10), 1)

  #Check if snake eats the food
  if player_pos == food_pos:
    score_counter += 1
    food_pos = summonFood()
    tail.append(player_pos.copy())

  renderScore()

  pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(player_pos.x, player_pos.y, 10, 10))
  pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(food_pos.x, food_pos.y, 10, 10))

  for i in range(0, len(tail)):
    pygame.draw.rect(screen, (255 - i * 5, 255 - i * 5, 255 - i * 5), pygame.Rect(tail[i].x, tail[i].y, 10, 10))


  if player_pos.x <= 0:
    player_pos.x = screen.get_width()
  elif player_pos.x >= screen.get_width():
    player_pos.x = 0
  elif player_pos.y <= 0:
    player_pos.y = screen.get_height()
  elif player_pos.y >= screen.get_height():
    player_pos.y = 0


  keys = pygame.key.get_pressed()
  if keys[pygame.K_w] or keys[pygame.K_UP]:
    if direction.y == 0: #prevent reversing direction
      direction = pygame.Vector2(0, -grid_size)
  elif keys[pygame.K_s] or keys[pygame.K_DOWN]:
    if direction.y == 0:
      direction = pygame.Vector2(0, grid_size)
  elif keys[pygame.K_a] or keys[pygame.K_LEFT]:
    if direction.x == 0:
      direction = pygame.Vector2(-grid_size, 0)
  elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
    if direction.x == 0:
      direction = pygame.Vector2(grid_size, 0)


  


  pygame.display.flip()

  clock.tick(60)

print("Game Over!")
print(f"Total Score: {score_counter}")

pygame.quit()