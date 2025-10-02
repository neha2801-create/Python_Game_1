# Snake Game in different board types
import pygame
# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Shapes")

x=int(input(f"Enter how many times you want to guess the shape?"))
i = 0
while i <=x:
    
    if i % 2==0:
        pygame.draw.rect(screen, (255, 0, 0), (100, 100, 50, 50))
    else:
         pygame.draw.circle(screen, (0, 255, 0), (65 + i*40, 200), 15)
    i+=1
    
pygame.display.flip()
running = True

while running:
    for event in pygame.event.get():
        if pygame.event == pygame.QUIT:
            running = False
    

