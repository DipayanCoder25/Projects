import pygame
import random
import sys

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Player vs Enemies")

background = pygame.image.load("background.jpg")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
pygame.mixer.music.load("background.mp3")
pygame.mixer.music.play(-1)

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

clock = pygame.time.Clock()
player_size = 50
player = pygame.Rect(WIDTH // 2, HEIGHT - 80, player_size, player_size)

enemy_size = 50
enemies = []
for _ in range(7):
    x = random.randint(0, WIDTH - enemy_size)
    y = random.randint(0, HEIGHT - enemy_size)
    enemies.append(pygame.Rect(x, y, enemy_size, enemy_size))

score = 0
font = pygame.font.Font(None, 36)
running = True

while running:
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.left > 0:
        player.x -= 5
    if keys[pygame.K_RIGHT] and player.right < WIDTH:
        player.x += 5
    if keys[pygame.K_UP] and player.top > 0:
        player.y -= 5
    if keys[pygame.K_DOWN] and player.bottom < HEIGHT:
        player.y += 5
    pygame.draw.rect(screen, BLUE, player)
    for enemy in enemies:
        pygame.draw.rect(screen, RED, enemy)
        if player.colliderect(enemy):
            score += 1
            enemy.x = random.randint(0, WIDTH - enemy_size)
            enemy.y = random.randint(0, HEIGHT - enemy_size)
    text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(text, (10, 10))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
