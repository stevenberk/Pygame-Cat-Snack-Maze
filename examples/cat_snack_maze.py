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
        
class Speed_Boost(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        pygame.sprite.Sprite.__init__(self)
        self.active = True
        self.image = pygame.Surface([size[0], size[1]])
        self.image.fill((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.left = pos[1]
        self.rect.top = pos[0]
    def player_hit(self, player):
        if pygame.sprite.spritecollide(self, [player], False) and self.active == True:
            player.vx += 1
            player.vy += 1
            self.active = False
    



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
    player.vx = 1
    player.vy = 1
    


    cat = Cat([900, 920])
    cat_group = pygame.sprite.Group()
    cat_group.add(cat)

    speed_boosters_group = pygame.sprite.Group()


    wall_group = pygame.sprite.Group()
    # first set of values is location coordinates, second is size
    wall_group.add(Block([0, 0],[1000, 20])) #this line is the top border
    wall_group.add(Block([0, 0], [20, 1000])) #left border
    wall_group.add(Block([980, 0], [1000, 20])) #bottom border
    wall_group.add(Block([0, 980], [20, 1000])) # right border
    wall_group.add(Block([390,500], [1000, 15])) 
    wall_group.add(Block([330,308], [517, 15]))  
    wall_group.add(Block([0, 300], [15, 200]))
    wall_group.add(Block([260, 300], [15, 480]))
    wall_group.add(Block([0, 100], [15, 800]))
    wall_group.add(Block([860,20], [200, 15]))
    wall_group.add(Block([800,100], [220, 15]))
    wall_group.add(Block([730,200], [180, 15])) 
    wall_group.add(Block([730,450], [550, 15])) #other line part of above
    wall_group.add(Block([89, 200], [15, 560])) 
    wall_group.add(Block([260, 300], [300, 15]))
    wall_group.add(Block([70, 380], [15, 190])) 
    wall_group.add(Block([920,120], [200, 15])) 
    wall_group.add(Block([730,380], [15, 200])) # verticle line, has lots of speed bumps at gap
    wall_group.add(Block([815,305], [15, 120])) 
    wall_group.add(Block([790,668], [15, 140]))
    wall_group.add(Block([790,668], [330, 15]))
    wall_group.add(Block([915,538], [130, 15]))
    wall_group.add(Block([790,818], [15, 120]))
    wall_group.add(Block([860,748], [15, 120]))
    wall_group.add(Block([800,458], [15, 130]))
    wall_group.add(Block([800,458], [150, 15]))
    wall_group.add(Block([860,510], [120, 15]))
    wall_group.add(Block([450, 300], [560, 15])) #line 109 -113 a
    wall_group.add(Block([505, 420], [560, 15]))
    wall_group.add(Block([560, 300], [560, 15]))
    wall_group.add(Block([615, 420], [560, 15]))
    wall_group.add(Block([670, 300], [560, 15]))
    wall_group.add(Block([390,370], [160, 15])) 
    wall_group.add(Block([20, 450], [15, 190])) 
    wall_group.add(Block([70, 520], [15, 190])) 
    wall_group.add(Block([20, 590], [15, 190])) 
    wall_group.add(Block([70, 660], [15, 260])) 
    wall_group.add(Block([20, 740], [15, 260])) 
    wall_group.add(Block([70, 810], [15, 260])) 
    wall_group.add(Block([70, 810], [100, 15]))
    wall_group.add(Block([130, 890], [110, 15])) 
    wall_group.add(Block([190, 810], [100, 15]))
    wall_group.add(Block([260, 890], [110, 15])) 
    wall_group.add(Block([330, 810], [100, 15]))
    
     
   

    #"speed bumps", in linear oder
    speed_boosters_group.add(Speed_Boost([90, 20],[90, 20]))
    speed_boosters_group.add(Speed_Boost([815, 100],[20, 50]))
    #speed_boosters_group.add(Speed_Boost([875, 100],[20, 50]))
    speed_boosters_group.add(Speed_Boost([935, 160],[20, 50]))
    speed_boosters_group.add(Speed_Boost([745, 260],[20, 50]))
    speed_boosters_group.add(Speed_Boost([935, 380],[3, 50])) # gap begin"
    speed_boosters_group.add(Speed_Boost([935, 385],[3, 50]))
    speed_boosters_group.add(Speed_Boost([935, 389],[3, 50]))
    speed_boosters_group.add(Speed_Boost([935, 394],[3, 50]))
    speed_boosters_group.add(Speed_Boost([935, 399],[3, 50]))
    speed_boosters_group.add(Speed_Boost([935, 404],[3, 50]))
    speed_boosters_group.add(Speed_Boost([935, 409],[3, 50]))
    speed_boosters_group.add(Speed_Boost([935, 414],[3, 50]))
    speed_boosters_group.add(Speed_Boost([935, 419],[3, 50]))
    speed_boosters_group.add(Speed_Boost([935, 424],[3, 50]))
    speed_boosters_group.add(Speed_Boost([935, 429],[3, 50]))
    speed_boosters_group.add(Speed_Boost([935, 434],[3, 50]))
    speed_boosters_group.add(Speed_Boost([935, 439],[3, 50]))
    speed_boosters_group.add(Speed_Boost([935, 444],[3, 50]))
    speed_boosters_group.add(Speed_Boost([935, 449],[3, 50]))
    speed_boosters_group.add(Speed_Boost([935, 454],[3, 50]))
    speed_boosters_group.add(Speed_Boost([935, 459],[3, 50]))
    speed_boosters_group.add(Speed_Boost([935, 464],[3, 50]))
    speed_boosters_group.add(Speed_Boost([935, 469],[3, 50])) # gap end
    speed_boosters_group.add(Speed_Boost([212, 450],[10, 50]))
    speed_boosters_group.add(Speed_Boost([390, 310],[60, 10]))
    
    


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

        for speed_boost in speed_boosters_group:
            speed_boost.player_hit(player)


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

            
        speed_boosters_group.draw(screen)
        player_group.draw(screen)
        wall_group.draw(screen)
        cat_group.draw(screen)
        pygame.display.update()
        clock.tick(fps)


    pygame.quit()


if __name__ == '__main__':
    main()