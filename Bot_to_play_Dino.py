import time
#Import pyscreenshot and autogui. Those libraries are necessary to do this project
#The first one will capture screenshots and the seconde one will control the GUI
import pyscreenshot as ImageGrab
import pyautogui

def capture_screen():
	#This function captures a screenshot and returns it
	screen = ImageGrab.grab()
	return screen

def detect_enemy(screen):
	#This function will detect when there is a cactus close to the Dino.
	
	for x in range(590,710):
		for y in range(392,415):
			#Those values are the range of an area close to the dino
			color = screen.getpixel((x, y))
			#If There is gray tones in this area, it means that there is an cactus and the dino must jump
			if color != (247,247,247):
				print("%d, %d" %(x,y))
				return True

def jump():
	#This method makes the dino jump
	#It has the same behavior as if a human pressed the up arrow key
	pyautogui.keyDown("up")
	time.sleep(0.08)
	print('SPACE pressed!!!!')
	pyautogui.keyUp("up")

def start_program():
	#To start the game, the space or up key must be pressed. It's what this function does
	
	print('Starting in...' )
	for i in range(3, 0, -1):
		print(i)
		time.sleep(1)
	#after 3 secs, the space key is pressed
	pyautogui.press("space")


start_program()
while True:
	#When the game is started, the function "capture_screen" is called continously 
	#Then the screen captured is passed as an argument to the enemy function, which will return true if there is an enemy
	screen = capture_screen()	
	enemy = detect_enemy(screen)
	if enemy == True:
		#If there's an enemy, then jump() is called to make the dino jump
		print('JUMP!')
		jump()
		#break		
		#print('JUMP!')
