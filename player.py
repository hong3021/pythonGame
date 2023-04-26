import pygame
from support import import_folder


class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()

        self.import_character_assets()
        self.frame_index = 0
        self.animations_speed = 0.15
        self.image = self.animations['idle'][self.frame_index]
        # self.image = pygame.Surface((32, 60))
        # self.image.fill("red")
        self.rect = self.image.get_rect(topleft=pos)

        # movement
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 8
        self.dash_speed = 16
        self.gravity = 0.8
        self.jump_speed = -16
        self.double_jump = 2
        self.gliding_speed = -0.16

        # player status
        self.facing_right = True
        self.on_ground = False
        self.on_ceilling = False
        self.on_left = False
        self.on_right = False
        self.status = 'idle'

    def import_character_assets(self):
        characteer_path = 'photo/characterA/'
        self.animations = {'idle': [], 'run': [], 'jump': [], 'fall': []}

        for animation in self.animations.keys():
            full_path = characteer_path + animation
            self.animations[animation] = import_folder(full_path)

    def animate(self):
        animation = self.animations[self.status]
        # loop over fram
        self.frame_index += self.animations_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0

        image = animation[int(self.frame_index)]
        if self.facing_right:
            self.image = image
        else:
            flipped_image = pygame.transform.flip(image, True, False)
            self.image = flipped_image

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

        if keys[pygame.K_c]:
            if self.direction.x > 0:
                self.direction.x = +5
            else:
                self.direction.x = -5

    def get_status(self):
        if self.direction.y < 0:
            self.status = 'jump'
        elif self.direction.y > 1:
            self.status = 'fall'
        else:
            if self.direction.x != 0:
                self.status = 'run'
            else:
                self.status = 'idle'

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jump(self):
        self.direction.y = self.jump_speed

    # def gliding(self):
    #     self.direction.y = self.gliding_speed

    def update(self):
        self.get_input()
        self.animate()
        self.get_status()



