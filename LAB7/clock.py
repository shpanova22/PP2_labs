import pygame
import datetime

pygame.init()

screen=pygame.display.set_mode((800,600))

clock=pygame.time.Clock()




image=pygame.image.load(r"C:\Users\Lenovo\Desktop\PP2_labs\clock.png")
imageL=pygame.image.load(r"C:\Users\Lenovo\Desktop\PP2_labs\sec_hand.png")
imageR=pygame.image.load(r"C:\Users\Lenovo\Desktop\PP2_labs\min_hand.png")


running=True

while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
            
    screen.blit(image,(0,0))
    
    curr_date=datetime.datetime.now()
    curr_min=curr_date.minute
    curr_sec=curr_date.second
    minute_angle=(curr_min/60) * (-360)
    second_angle=(curr_sec/60) * (-360)
    
    rotated_Rhand=pygame.transform.rotate(imageR,minute_angle)
    Rhand_move=rotated_Rhand.get_rect(center=(400,300))
    screen.blit(rotated_Rhand,Rhand_move)
    
    
    rotated_Lhand=pygame.transform.rotate(imageL,second_angle)
    Lhand_move=rotated_Lhand.get_rect(center=(400,300))
    screen.blit(rotated_Lhand,Lhand_move)
    
    pygame.display.flip()
    clock.tick(60)
    
pygame.quit()
        


