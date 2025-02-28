import pygame
from circleshape import *
from constants import *
from shot import *


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 180
        self.x = x
        self.y = y
        self.timer = 0
        self.shots_group = None

    def set_shots_group(self, shots):
        self.shots_group = shots

        
        
    
    
    
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw (self, screen):
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), 2)
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(dt * -1)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(dt * -1)
        if keys[pygame.K_SPACE]:
            self.shoot()
        

        if self.timer > 0:
            self.timer -= dt


    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        if self.timer <= 0 and self.shots_group is not None:
        
            new_shot = Shot(self.position.x, self.position.y)

            direction = pygame.Vector2(0, 1)
            direction = direction.rotate(self.rotation)
            new_shot.velocity = direction * PLAYER_SHOOT_SPEED

            self.shots_group.add (new_shot)
            self.timer = PLAYER_SHOOT_COOLDOWN





        
        