import pygame

# Initialize Pygame
pygame.init()

# Set the size of each cell
taille = 60

# Create the maze
# S = Start, E = Exit, # = Wall, . = Empty space
carte = [
    ["S", ".", ".", "#", "."],
    ["#", "#", ".", "#", "."],
    [".", ".", ".", ".", "."],
    [".", "#", "#", "#", "."],
    [".", ".", ".", ".", "E"]
]

# Create the game window
fenetre = pygame.display.set_mode((len(carte[0]) * taille, len(carte) * taille))
pygame.display.set_caption("Maze")

# Set the player's starting position
joueur_x = 0
joueur_y = 0

# Main game loop
jeu = True

while jeu:
    # Handle game events
    for evenement in pygame.event.get():
        if evenement.type == pygame.QUIT:
            jeu = False

        # Check for keyboard input
        if evenement.type == pygame.KEYDOWN:
            nx = joueur_x
            ny = joueur_y

            # Move the player
            if evenement.key == pygame.K_UP:
                ny -= 1
            elif evenement.key == pygame.K_DOWN:
                ny += 1
            elif evenement.key == pygame.K_LEFT:
                nx -= 1
            elif evenement.key == pygame.K_RIGHT:
                nx += 1

            # Check if the new position is inside the maze
            if 0 <= nx < len(carte[0]) and 0 <= ny < len(carte):
                # Prevent the player from crossing walls
                if carte[ny][nx] != "#":
                    joueur_x = nx
                    joueur_y = ny

    # Clear the window
    fenetre.fill((255, 255, 255))

    # Draw the maze
    for y in range(len(carte)):
        for x in range(len(carte[y])):
            rectangle = (x * taille, y * taille, taille, taille)

            # Draw walls in dark gray
            if carte[y][x] == "#":
                pygame.draw.rect(fenetre, (40, 40, 40), rectangle)

            # Draw the exit in green
            elif carte[y][x] == "E":
                pygame.draw.rect(fenetre, (0, 200, 0), rectangle)

            # Draw the grid lines
            pygame.draw.rect(fenetre, (180, 180, 180), rectangle, 1)

    # Draw the player in blue
    pygame.draw.circle(
        fenetre,
        (30, 100, 255),
        (joueur_x * taille + taille // 2,
         joueur_y * taille + taille // 2),
        taille // 3
    )

    # Check if the player has reached the exit
    if carte[joueur_y][joueur_x] == "E":
        pygame.display.set_caption("Congratulations, you won!")

    # Update the display
    pygame.display.flip()

# Close Pygame
pygame.quit()
