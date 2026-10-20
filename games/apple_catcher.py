
import pygame
import random

pygame.init()

# Fenetre du jeu
WIDTH = 600
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Attrape les pommes")

# Joueur : le panier
basket = pygame.Rect(250, 520, 100, 30)
basket_speed = 6

# Pommes
apple = pygame.Rect(random.randint(0, WIDTH - 20), 0, 20, 20)
apple_speed = 4

# Score
score = 0
font = pygame.font.SysFont(None, 36)

# Couleurs
WHITE = (255, 255, 255)
RED = (220, 0, 0)
BROWN = (139, 69, 19)
BLACK = (0, 0, 0)

# Boucle principale
running = True
clock = pygame.time.Clock()

while running:
    clock.tick(60)

    # Evenements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Deplacement du panier
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and basket.left > 0:
        basket.x -= basket_speed

    if keys[pygame.K_RIGHT] and basket.right < WIDTH:
        basket.x += basket_speed

    # Deplacement de la pomme
    apple.y += apple_speed

    # Pomme attrapee
    if basket.colliderect(apple):
        score += 1
        apple.x = random.randint(0, WIDTH - apple.width)
        apple.y = 0
        apple_speed += 0.2

    # Pomme ratee
    if apple.top > HEIGHT:
        apple.x = random.randint(0, WIDTH - apple.width)
        apple.y = 0

    # Dessiner le fond
    screen.fill(WHITE)

    # Dessiner le panier
    pygame.draw.rect(screen, BROWN, basket)

    # Dessiner la pomme
    pygame.draw.ellipse(screen, RED, apple)

    # Afficher le score
    score_text = font.render(f"Score : {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

    # Mettre a jour l'ecran
    pygame.display.flip()

pygame.quit()
