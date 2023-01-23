import pygame

# initialize pygame
pygame.init()

# set the screen size
size = (700, 500)
screen = pygame.display.set_mode(size)

# set the title of the window
pygame.display.set_caption("Block Game")

# set the player starting position
player_x = 350
player_y = 250

# set the block size
block_size = 50

# create a list of blocks
blocks = []
for x in range(0, size[0], block_size):
    for y in range(0, size[1], block_size):
        blocks.append((x, y))
        
# create a list of trees
trees = []
for x in range(100, size[0] - 100, block_size * 3):
    for y in range(100, size[1] - 100, block_size * 3):
        trees.append((x, y))
        
# create a list of cows
cows = []
for x in range(200, size[0] - 200, block_size * 4):
    for y in range(200, size[1] - 200, block_size * 4):
        cows.append((x, y))

# set the player's starting score
score = 0

# main game loop
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            # move the player based on the key pressed
            if event.key == pygame.K_LEFT:
                player_x -= block_size
            elif event.key == pygame.K_RIGHT:
                player_x += block_size
            elif event.key == pygame.K_UP:
                player_y -= block_size
            elif event.key == pygame.K_DOWN:
                player_y += block_size

    # fill the screen with black
    screen.fill((0, 0, 0))

    # draw the blocks
    for block in blocks:
        pygame.draw.rect(screen, (255, 255, 255), (block[0], block[1], block_size, block_size))

    # draw the trees
    for tree in trees:
        pygame.draw.polygon(screen, (0, 128, 0), [(tree[0], tree[1]), (tree[0] + block_size, tree[1] + block_size), (tree[0] - block_size, tree[1] + block_size)])

    # draw the cows
    for cow in cows:
        pygame.draw.polygon(screen, (0, 0, 0), [(cow[0], cow[1]), (cow[0] + block_size, cow[1] - block_size), (cow[0] + block_size * 2, cow[1]), (cow[0] + block_size, cow[1] + block_size), (cow[0], cow[1] + block_size * 2), (cow[0] - block_size, cow[1] + block_size), (cow[0], cow[1])])
        font = pygame.font.Font(None, 30)
        text = font.render("cow", True, (255, 255, 255))
        screen.blit(text, (cow[0] - block_size // 2, cow[1] - block_size // 2))

    # check if the player is touching a cow
    for cow in cows:
        if (cow[0] - block_size <= player_x <= cow[0] + block_size) and (cow[1] - block_size <= player_y <= cow[1] + block_size):
            score += 1
            print("Score:", score)
            cows.remove(cow)
            break

    # draw the player
    pygame.draw.circle(screen, (255, 0, 0), (player_x, player_y), block_size // 2)

    # update the display
    pygame.display.flip()

# exit pygame
pygame.quit()
