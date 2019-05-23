import pygame

def control(player):

  for event in pygame.event.get():

      if event.type == pygame.QUIT:
          done = True

      if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_LEFT:
              player.changespeed(-5, 0)
          if event.key == pygame.K_RIGHT:
              player.changespeed(5, 0)
          if event.key == pygame.K_UP:
              player.changespeed(0, -5)
          if event.key == pygame.K_DOWN:
              player.changespeed(0, 5)

      if event.type == pygame.KEYUP:
          if event.key == pygame.K_LEFT:
              player.changespeed(5, 0)
          if event.key == pygame.K_RIGHT:
              player.changespeed(-5, 0)
          if event.key == pygame.K_UP:
              player.changespeed(0, 5)
          if event.key == pygame.K_DOWN:
              player.changespeed(0, -5)