# Lifted from: https://stackoverflow.com/a/40338475

import pygame

class Snack(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('../images/cake.png').convert_alpha()
        self.rect = self.image.get_rect()

        self.rect.center = pos 

class Cat(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('../images/kitty.png').convert_alpha()
        self.rect = self.image.get_rect()

        self.rect.center = pos

class Block(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([size[0], size[1]])
        self.image.fill((255, 0, 255))
        self.rect = self.image.get_rect()
        self.rect.left = pos[1]
        self.rect.top = pos[0]
        




def main():
    win_flag = False
    loose_flag = False
    win_timer = 0
    loose_timer = 0
    pygame.init()
    clock = pygame.time.Clock()
    fps = 50
    bg = [255, 255, 255]
    size =[1000, 1000]



    
    text1 = pygame.font.Font(pygame.font.get_default_font(),56)


    screen = pygame.display.set_mode(size)

    player = Snack([40, 50])
    player.move = [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]
    player.vx = 5
    player.vy = 5


    cat = Cat([900, 920])
    cat_group = pygame.sprite.Group()
    cat_group.add(cat)

    wall_group = pygame.sprite.Group()
    # first set of values is location coordinates, second is size
    wall_group.add(Block([0, 0],[1000, 20])) #this line is the top border
    wall_group.add(Block([0, 0], [20, 1000])) #left border
    wall_group.add(Block([980, 0], [1000, 20])) #bottom border
    wall_group.add(Block([0, 980], [20, 1000])) # right border
    wall_group.add(Block([390,600], [1000, 20]))
    wall_group.add(Block([330,258], [500, 20]))
    wall_group.add(Block([0, 300], [20, 218]))
    wall_group.add(Block([260, 300], [20, 480]))
    wall_group.add(Block([0, 100], [20, 800]))
    wall_group.add(Block([860,20], [200, 20]))
    wall_group.add(Block([800,100], [200, 20]))
    wall_group.add(Block([730,200], [500, 20]))
    wall_group.add(Block([59, 200], [20, 600]))
    wall_group.add(Block([260, 300], [300, 20]))
    wall_group.add(Block([60, 360], [20, 200]))


    player_group = pygame.sprite.Group()
    player_group.add(player)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

        key = pygame.key.get_pressed()

        for i in range(2):
            if key[player.move[i]]:
                player.rect.x += player.vx * [-1, 1][i]

        for i in range(2):
            if key[player.move[2:4][i]]:
                player.rect.y += player.vy * [-1, 1][i]

        screen.fill(bg)

        wallhit = pygame.sprite.spritecollide(player, wall_group, False)

        if wallhit:
            # if collision is detected, calls a function to end game
        
            screen.blit(text1.render('You Lose',0,(0, 0, 0)),(500,500))
            loose_flag = True
        
        if loose_flag:
            loose_timer += 1
            if loose_timer >= 101:
                pygame.quit()

        cathit = pygame.sprite.spritecollide(player, cat_group, True)


        if cathit:
            
            win_flag = True
        if win_flag:
            screen.blit(text1.render('You Win!',0,(0, 0, 0)),(500,500))
            win_timer += 1 
            if win_timer >= 241:
                pygame.quit()  

            

        player_group.draw(screen)
        wall_group.draw(screen)
        cat_group.draw(screen)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()


if __name__ == '__main__':
    main()