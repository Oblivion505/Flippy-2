# ---/// Flippy 2 ///---
# ~ By Joshua Abbott



import pygame, sys
from pygame.locals import QUIT

# --------------------------------------
# Sets the dimensions and colour of the background, calls the grid_create() and circles() functions when the code is first run, continously calls the click() and update() function
# --------------------------------------

def display():
  
   pygame.init()

   title_screen()

   user_1 = name_input(1)
   user_2 = name_input(2)

   background = pygame.display.set_mode((d_width, d_height))
   background.fill(b_colour)
  
   corner_x = 210
   corner_y = 40
   user_colour = white
   opp_colour = black
   valid = False
   end = False

   turn_text = pygame.font.SysFont("", 28)

   grid_create(background, "Start")
   circle_array = circles(background, corner_x, corner_y)
  
   while True:
       for event in pygame.event.get():
           if event.type == QUIT:
               pygame.quit()
               sys.exit()
       if end == False:
          valid, circle_array = click(corner_x, corner_y, valid, circle_array, user_colour, opp_colour)
          update(background, corner_x, corner_y, circle_array, "Continuous")
          if valid == True and user_colour == white:
            user_colour = black
            opp_colour = white
            valid = False
          elif valid == True and user_colour == black:
            user_colour = white
            opp_colour = black
            valid = False
          turn_indicate(background, turn_text, user_colour, user_1, user_2)
          pygame.display.update()
          end = check_end(valid, circle_array, user_colour, opp_colour, background, user_1, user_2)
       
       else:
         grid_create(background, "End")
         update(background, corner_x, corner_y, circle_array, "End")
         pygame.display.update()

# --------------------------------------
# Sets up the title screen of the game, prompts the user to press Enter to start the game
# --------------------------------------

def title_screen():

  background = pygame.display.set_mode((d_width, d_height))
  background.fill(b_colour)
  pygame.display.set_caption("Flippy 2")

  title_text = pygame.font.SysFont("dejavusansmono", 70)
  sub_text = pygame.font.SysFont("", 30)

  title = title_text.render("Flippy 2", True, d_blue)
  subtitle = sub_text.render("[ Press Enter to Start Game ]", True, d_blue)

  pygame.draw.line(background, white, (110, 0), (60, 390), 6)
  pygame.draw.line(background, white, (150, 0), (100, 390), 6)
  pygame.draw.line(background, black, (628, 0), (578, 390), 6)
  pygame.draw.line(background, black, (668, 0), (618, 390), 6)

  background.blit(title, (200, 80))
  background.blit(subtitle, (215, 220))

  pygame.display.update()

  loop = True

  while loop == True:

    for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
        if event.unicode == "\r":
          loop = False

# --------------------------------------
# Asks the user to input their name and validates it to check if it is 1 to 5 characters long
# --------------------------------------

def name_input(user):

  name = ""

  background = pygame.display.set_mode((d_width, d_height))
  background.fill(b_colour)

  rect = pygame.Rect(239, 200, 250, 60)
  pygame.draw.rect(background, d_blue, rect, 3)

  pygame.draw.line(background, d_blue, (100, 0), (100, 390), 6)
  pygame.draw.line(background, d_blue, (628, 0), (628, 390), 6)

  prompt_text = pygame.font.SysFont("dejavuserif", 30)
  name_text = pygame.font.SysFont("", 50)

  if user == 1:

    prompt_1 = prompt_text.render("Player 1,", True, white)
    prompt_2 = prompt_text.render("please enter your name:", True, white)

  if user == 2:

    prompt_1 = prompt_text.render("Player 2,", True, black)
    prompt_2 = prompt_text.render("please enter your name:", True, black)

  background.blit(prompt_1, (150, 50))
  background.blit(prompt_2, (150, 100))

  pygame.display.update()

  while True:

    for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
        if len(event.unicode) != 0:
          if (ord(event.unicode) >= 65 and ord(event.unicode) <= 90) or (ord(event.unicode) >= 97 and ord(event.unicode) <= 122):
            if len(name) < 5:
              name = name + event.unicode
        if event.unicode == "\x08":
          name = name[:-1]
        if event.unicode == "\r":
          if name != "":
            return name

    for i in range(0, len(name)):

      if user == 1:
        
        name_display = name_text.render(name[i], True, white)
      
      elif user == 2:
        
        name_display = name_text.render(name[i], True, black)

      background.blit(name_display, (260 + (i * 40), 215))

    for a in range(0, 5 - len(name)):

      blank = pygame.Rect(415 - (a * 40), 215, 40, 40)
      pygame.draw.rect(background, b_colour, blank, 1)
      background.fill(b_colour, blank)
    
    pygame.display.update()
    
# --------------------------------------
# Creates the 6x6 grid
# --------------------------------------

def grid_create(background, type):
   if type == "Start":
     block_size = 60
     for x in range(0, d_width - 400, block_size):
         for y in range(0, d_height - 50, block_size):
           rect = pygame.Rect(x + 180, y + 10, block_size, block_size)
           pygame.draw.rect(background, d_blue, rect, 1)
           
   elif type == "End":
     block_size = 36
     for x in range(0, d_width - 512, block_size):
         for y in range(0, d_height - 174, block_size):
           rect = pygame.Rect(x + 80, y + 150, block_size, block_size)
           pygame.draw.rect(background, d_blue, rect, 1)

# --------------------------------------
# Creates a 2D array to represent the colour of the circle in each grid square, initially makes every circle the same colour as the background apart from the circles in the middle 4 squares
# --------------------------------------

def circles(background, corner_x, corner_y):

   circle_row = []
   circle_array = []
  
   for x in range(0, 6):
      for y in range(0, 6):
        if (x == 2 and y == 2) or (x == 3 and y == 3): 
         circle_row.append(white)
        elif (x == 2 and y == 3) or (x == 3 and y == 2):
          circle_row.append(black)
        else:
          circle_row.append((b_colour))
        pygame.draw.circle(background, circle_row[y], (corner_x + x * 60, corner_y + y * 60), 20, 0)
      circle_array.append(circle_row)
      circle_row = []

   return circle_array

# --------------------------------------
# Constantly checks if the user is clicking with their left mouse button inside a created grid square, calls the grid_check() function if the conditions are met
# --------------------------------------

def click(corner_x, corner_y, valid, circle_array, user_colour, opp_colour):
  
  position = pygame.mouse.get_pos()
  button1 = pygame.mouse.get_pressed()
  
  for x in range(0, 6):
    for y in range(0, 6):
      if position[0] >= (corner_x + x * 60 - 25) and position[0] <= (corner_x + x * 60 + 25) and position[1] >= (corner_y + y * 60 - 25) and position[1] <= (corner_y + y * 60 + 25) and button1[0] == True:

        click_x = x
        click_y = y

        valid, circle_array = grid_check(valid, circle_array, click_x, click_y, user_colour, opp_colour, "Move")
         
  return valid, circle_array

# --------------------------------------
# Checks the validity of the user's move by checking for circles of the opposite colour surrounding the square that was clicked, continuing if more opposite colour circles are found, and validating the move if a circle of the same colour is detected behind the circles of the opposite colour, if the move is valid then the grid_change function is called to update the 2D array by changing the colours of the opposite colour circles to the same colour as the user's circles
# --------------------------------------

def grid_check(valid, circle_array, click_x, click_y, user_colour, opp_colour, type):

 if circle_array[click_x][click_y] != white and circle_array[click_x][click_y] != black:

    

    for x in range(click_x - 1, click_x + 2):
       for y in range(click_y - 1, click_y + 2):
         
         if type == "Move":
           #print(x, y) ####
           flip_list = []

         if (x == click_x and y == click_y) or x > len(circle_array) - 1 or x < 0 or y > len(circle_array[0]) - 1 or y < 0: 
           continue

         if circle_array[x][y] == opp_colour: 
           if type == "Move":
             #print("path found") ####
             pass
           if x + x - click_x > len(circle_array) - 1 or x + x - click_x < 0 or y + y - click_y > len(circle_array[0]) - 1 or y + y - click_y < 0:
             continue
           if type == "Move":
             flip_list.append((x, y))
           end = False
           count_x = 0
           count_y = 0
           
           while end == False:
             if type == "Move":
               #print(count_x, count_y, ":", x + x - click_x + count_x, y + y - click_y + count_y) ####
               pass
             if circle_array[x + x - click_x + count_x][y + y - click_y + count_y] == opp_colour:
               
                if x + x - click_x + count_x + (x - click_x) > len(circle_array) - 1 or x + x - click_x + count_x + + (x - click_x) < 0 or y + y - click_y + count_y + (y - click_y) > len(circle_array[0]) - 1 or y + y - click_y + count_y + (y - click_y) < 0 or circle_array[x + x - click_x + count_x][y + y - click_y + count_y] == b_colour:
                   end = True
                   continue

                else:

                  if type == "Move":
                     flip_list.append((x + x - click_x + count_x, y + y - click_y + count_y))
                  count_x = count_x + (x - click_x)
                  count_y = count_y + (y - click_y)
                  if type == "Move":
                    #print("count_x, count_y increment:", count_x, count_y) ####
                    pass

             if circle_array[x + x - click_x + count_x][y + y - click_y + count_y] == user_colour:
                if type == "Move":
                  flip_list.append((click_x, click_y))
                  circle_array = grid_change(circle_array, flip_list, user_colour)
                valid = True
                end = True

             elif circle_array[x + x - click_x + count_x][y + y - click_y + count_y] == b_colour:
               end = True

    if type == "Move":
      #print("---------- end ----------") ####
      pass

    return valid, circle_array

 else:

    return valid, circle_array

# --------------------------------------
# Changes the colour of the circles that are flipped by the user's move by iterating through the flip_list to identify the indexes in the 2D array that need their colour changed
# --------------------------------------

def grid_change(circle_array, flip_list, user_colour):

  #print("appending:", flip_list) ####

  for x in range(0, len(flip_list)):
      circle_array[flip_list[x][0]][flip_list[x][1]] = user_colour

  return circle_array

# --------------------------------------
# Constantly iterates through the 2D array and makes any colour changes to the circles in the grid by redrawing them
# --------------------------------------

def update(background, corner_x, corner_y, circle_array, type):

    for x in range(0, 6):
      for y in range(0, 6):

        if type == "Continuous":
          pygame.draw.circle(background, circle_array[x][y], (corner_x + x * 60, corner_y + y * 60), 20, 0)
          
        elif type == "End":
          corner_x = 98
          corner_y = 168
          
          pygame.draw.circle(background, circle_array[x][y], (corner_x + x * 36, corner_y + y * 36), 12, 0)

# --------------------------------------
# Displays text at the top left of the screen to show if it is White's turn or Black's turn
# --------------------------------------

def turn_indicate(background, turn_text, user_colour, user_1, user_2):

  if user_colour == white:

    cover_surface = turn_text.render("It is " + user_2 + "'s" + " turn.", False, b_colour)

    text_surface = turn_text.render("It is " + user_1 + "'s" + " turn.", False, white)

  elif user_colour == black:

    cover_surface = turn_text.render("It is " + user_1 + "'s" + " turn.", False, b_colour)

    text_surface = turn_text.render("It is " + user_2 + "'s" + " turn.", False, black)

  background.blit(cover_surface, (5, 10))
  background.blit(text_surface, (5, 10))

# --------------------------------------
# Checks if any more valid moves can be made in the current turn, if not then the game is ended and the point_count() function is called
# --------------------------------------

def check_end(valid, circle_array, user_colour, opp_colour, background, user_1, user_2):

  end = False

  for x in range(0, len(circle_array)):
    for y in range(0, len(circle_array[0])):
      valid, circle_array = grid_check(valid, circle_array, x, y, user_colour, opp_colour, "End")
      if valid == True:

        end = False
        
        return end

  if valid == False:

    end = True

    points_w, points_b = point_count(circle_array)

    end_screen(background, points_w, points_b, user_1, user_2)

    return end

# --------------------------------------
# Counts up the points for each colour by iterating through the colour values in circle_array and returns the point totals
# --------------------------------------

def point_count(circle_array):

  points_w = 0
  points_b = 0

  for x in range(0, len(circle_array)):
    for y in range(0, len(circle_array[0])):
      if circle_array[x][y] == white:
        points_w += 10
      elif circle_array[x][y] == black:
        points_b += 10

  return points_w, points_b

# --------------------------------------
# Displays the end screen of the game, including the total points of both colours and the winner
# --------------------------------------
        
def end_screen(background, points_w, points_b, user_1, user_2):

  background = pygame.display.set_mode((d_width, d_height))
  background.fill(b_colour)

  end_text = pygame.font.SysFont("", 35)
  wpoints_text = end_text.render(user_1 + "'s" + " Points: " + str(points_w), True, white)
  bpoints_text = end_text.render(user_2 + "'s" + " Points: " + str(points_b), True, black)

  if points_w > points_b:

    winner = (user_1, white)
    win_points = points_w
    win_text = end_text.render("The Winner is: " + winner[0], True, white)

  elif points_w < points_b:

    winner = (user_2, black)
    win_points = points_b
    win_text = end_text.render("The Winner is: " + winner[0], True, black)

  else:

    winner = "Tie"
    win_points = (points_w)
    win_text = end_text.render("It is a Tie.", True, purple)

  background.blit(wpoints_text, (80, 20))
  background.blit(bpoints_text, (80, 60))
  background.blit(win_text, (80, 100))

  scoreboard(background, winner, win_points, user_1, user_2)

# --------------------------------------
# Reads the high scoreboard from flippy_scoreboard.txt and puts it into a list with the new score of the winner of the game, then updates the scoreboard by writing back to the text file
# --------------------------------------

def scoreboard(background, winner, win_points, user_1, user_2):

  f = open("flippy_scoreboard.txt", "r")

  score_list = []
  end = False

  while end == False:
    
    name = f.readline().strip()
    colour = f.readline().strip()
    score = f.readline().strip()

    if name != "":

      score_list.append((name, colour, score))

    else:

      if winner != "Tie":
        
        score_list.append((winner[0], winner[1], win_points))
        
      else:
        
        score_list.append((user_1, white, win_points))
        score_list.append((user_2, black, win_points))
        
      end = True

  f.close()

  for x in range(1, len(score_list)):
    for y in range(0, len(score_list) - 1):
      if int(score_list[x][2]) > int(score_list[y][2]) and x > y:
        temp_1 = score_list[x]
        temp_2 = score_list[y]
        score_list.pop(x)
        score_list.pop(y)
        score_list.insert(y, temp_1)
        score_list.insert(x, temp_2)

  if len(score_list) > 8:
    for i in range(0, len(score_list) - 8, -1):
      score_list.pop(i)

  f = open("flippy_scoreboard.txt", "w")

  for l in range(0, len(score_list)):

    f.write(str(score_list[l][0]) + "\n")
    f.write(str(score_list[l][1]) + "\n")
    f.write(str(score_list[l][2]) + "\n")

  f.close()

  score_table(background, score_list)

# --------------------------------------
# Draws the Scoreboard on the end screen using the updated scoreboard list
# --------------------------------------

def score_table(background, score_list):
  
  score_title = pygame.font.SysFont("", 45)
  score_text = pygame.font.SysFont("", 30)

  pygame.draw.line(background, d_blue, (400, 0), (400, 390), 4)
  pygame.draw.line(background, d_blue, (400, 50), (728, 50), 2)

  scoreboard_title = score_title.render("Scoreboard:", True, d_blue)
  background.blit(scoreboard_title, (420, 10))

  for i in range(0, len(score_list)):

    if str(score_list[i][1]) == str(white):
       score_colour = white
    elif str(score_list[i][1]) == str(black):
       score_colour = black

    scoreboard_text = score_text.render("Name: " + score_list[i][0], True, score_colour)
    scoreboard_score = score_text.render("Score: " + str(score_list[i][2]), True, score_colour)
    background.blit(scoreboard_text, (420, 70 + (i * 40)))
    background.blit(scoreboard_score, (600, 70 + (i * 40)))

# Screen Dimensions
d_width = 728
d_height = 390

# Colours
black = (0, 0, 0)
white = (200, 200, 200)
purple = (75, 0, 130)
d_blue = (0, 0, 139)
b_colour = (0, 150, 180)

display()