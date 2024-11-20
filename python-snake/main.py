import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Snake Clone")
clock = pygame.time.Clock()
running = True
dt = 0
score_counter = 0

font = pygame.font.Font("DejaVuSansMono.ttf", 20)
text = font.render(f"Score: {score_counter}",  True, (255, 255, 255), (0, 0, 0))

textRect = text.get_rect()

textRect.center = (60, 30)

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  screen.fill("black")

  screen.blit(text, textRect)

  pygame.draw.rect(screen, "white", pygame.Rect(player_pos.x, player_pos.y, 10, 10))

  keys = pygame.key.get_pressed()
  if keys[pygame.K_w]:
    player_pos.y -= 300 * dt
  elif keys[pygame.K_s]:
    player_pos.y += 300 * dt
  elif keys[pygame.K_a]:
    player_pos.x -= 300 * dt
  elif keys[pygame.K_d]:
    player_pos.x += 300 * dt

  pygame.display.flip()

  dt = clock.tick(60) / 1000

pygame.quit()