






import pyautogui

mouse_x, mouse_y = pyautogui.position() 
goal_x , goal_y = 600, 500

while mouse_x != goal_x or mouse_y != goal_y:
    if mouse_x < goal_x:
        mouse_x += 1
    elif mouse_x > goal_x: 
        mouse_x -= 1
    if mouse_y < goal_y:
        mouse_y += 1
    elif mouse_y > goal_y: 
        mouse_y -= 1
    pyautogui.moveTo(mouse_x, mouse_y)





































# pyautogui.typewrite("Hello, World!") 






















