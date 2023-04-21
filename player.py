import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((32, 60))
        self.image.fill("red")
        self.rect = self.image.get_rect(topleft=pos)

        # movement
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 8
        self.dash_speed = 16
        self.gravity = 0.8
        self.jump_speed = -16
        self.gliding = -0.16
        self.facing_right = True
        self.on_ground = False
        self.on_ceilling = False
        self.on_left = False
        self.on_right = False
        self.status = 'idle'


    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.direction.x = 0.8
            self.facing_right = True
        elif keys[pygame.K_LEFT]:
            self.direction.x = -0.8
            self.facing_right = False
        else:
            self.direction.x = 0

        if keys[pygame.K_SPACE] and self.on_ground:
            self.jump()
        # if keys[pygame.K_c]:
        #     if self.direction.x > 0:
        #         self.direction.x = +5
        #     else:
        #         self.direction.x = -5

    def get_status(self):
        if self.direction.y < 0:
            self.status = 'jump';
        elif self.direction.y > 0:
            self.status = 'fall'
        else:
            if self.direction.x != 0:
                self.status = 'run'
            else:
                self.status = 'ilde'



    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jump(self):
        self.direction.y = self.jump_speed

    def update(self):
        self.get_input()
        self.get_status()



