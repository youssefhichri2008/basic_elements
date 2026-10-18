
import pygame

pygame.init()

taille = 60

carte = [
    ["S", ".", ".", "#", "."],
    ["#", "#", ".", "#", "."],
    [".", ".", ".", ".", "."],
    [".", "#", "#", "#", "."],
    [".", ".", ".", ".", "E"]
]

fenetre = pygame.display.set_mode((len(carte[0]) * taille, len(carte) * taille))
pygame.display.set_caption("Labyrinthe")

joueur_x = 0
joueur_y = 0

jeu = True

while jeu:
    for evenement in pygame.event.get():
        if evenement.type == pygame.QUIT:
            jeu = False

        if evenement.type == pygame.KEYDOWN:
            nx = joueur_x
            ny = joueur_y

            if evenement.key == pygame.K_UP:
                ny -= 1
            elif evenement.key == pygame.K_DOWN:
                ny += 1
            elif evenement.key == pygame.K_LEFT:
                nx -= 1
            elif evenement.key == pygame.K_RIGHT:
                nx += 1

            if 0 <= nx < len(carte[0]) and 0 <= ny < len(carte):
                if carte[ny][nx] != "#":
                    joueur_x = nx
                    joueur_y = ny

    fenetre.fill((255, 255, 255))

    for y in range(len(carte)):
        for x in range(len(carte[y])):
            rectangle = (x * taille, y * taille, taille, taille)

            if carte[y][x] == "#":
                pygame.draw.rect(fenetre, (40, 40, 40), rectangle)
            elif carte[y][x] == "E":
                pygame.draw.rect(fenetre, (0, 200, 0), rectangle)

            pygame.draw.rect(fenetre, (180, 180, 180), rectangle, 1)

    pygame.draw.circle(
        fenetre,
        (30, 100, 255),
        (joueur_x * taille + taille // 2,
         joueur_y * taille + taille // 2),
        taille // 3
    )

    if carte[joueur_y][joueur_x] == "E":
        pygame.display.set_caption("Bravo, tu as gagné !")

    pygame.display.flip()

pygame.quit()
