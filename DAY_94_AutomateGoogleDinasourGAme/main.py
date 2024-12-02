import pyautogui
import time
from PIL import ImageGrab, ImageOps
import numpy as np

def detect_obstacle(region):
    img = pyautogui.screenshot() # Take a screenshot
    img_screen = img.getpixel((203, 290)) # Get the pixel value at the specified coordinates

    # Capture the game screen region
    screen = ImageGrab.grab(bbox=region)  # Specify the region (x1, y1, x2, y2)
    gray_screen = ImageOps.grayscale(screen)  # Convert to grayscale
    pixel_data = np.array(gray_screen)  # Convert to numpy array
    
    # Return True if an obstacle is detected
    if img_screen[0] == 255:
        return np.any(pixel_data < 200 )  # Adjust threshold as needed
    else:
        return np.any(pixel_data < 50)  # Adjust threshold as needed

def main():
    print("Starting game automation in 3 seconds...")
    time.sleep(3)
    # Show an alert message
    pyautogui.alert("Press OK to start the game automation")

                

    # Coordinates of the screen area to monitor (adjust to your screen setup)
    obstacle_region = (250, 540,300, 580)  # (x1, y1, x2,         y2)
 
    while True:
        if detect_obstacle(obstacle_region):
            pyautogui.press('space')  # Jump
            time.sleep(0.001)  # Avoid multiple jumps
        elif pyautogui.press('esc'):
            break

if __name__ == "__main__":                            
    main()


 