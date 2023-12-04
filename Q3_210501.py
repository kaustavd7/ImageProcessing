import cv2
import numpy as np

def find_left_end(image):
    h, w, _ = image.shape
    for y in range(h-1, -1, -1):
        for x in range(w):
            if not np.all(image[y, x] == [255, 255, 255]):
                return x, y  # (x, y) coordinates of the first non-white pixel

def find_right_end(image):
    h, w, _ = image.shape
    for y in range(h-1, -1, -1):
        for x in range(w-1, -1, -1):
            if not np.all(image[y, x] == [255, 255, 255]):
                return x, y  # (x, y) coordinates of the first non-white pixel
            
def find_skin(left_roi, right_roi):
    
    # Define the lower and upper bounds for skin color in HSV
    lower_skin = np.array([10, 20, 40], dtype=np.uint8)
    upper_skin = np.array([30, 200, 200], dtype=np.uint8)
    
    # Create binary masks for skin color in left and right regions
    left_mask = cv2.inRange(left_roi, lower_skin, upper_skin)
    right_mask = cv2.inRange(right_roi, lower_skin, upper_skin)
    
    # Calculate the number of skin color pixels in left and right regions
    left_skin_pixels = cv2.countNonZero(left_mask)
    right_skin_pixels = cv2.countNonZero(right_mask)
    
    ratio_skin = right_skin_pixels / (left_skin_pixels + 1e-8)
    
    return ratio_skin
           


def solution(audio_path):
    ############################
    ############################

    ############################
    ############################
    ## comment the line below before submitting else your code wont be executed##
    
    image = cv2.imread(audio_path)
    
    rotated_image1 = cv2.rotate(image, cv2.ROTATE_180)

    # Rotate the rotated image by 180 degrees again
    image = cv2.rotate(rotated_image1, cv2.ROTATE_180)
    
    right_end = find_right_end(image)
    left_end = find_left_end(image)
    
    center = np.mean([left_end, right_end], axis=0)
    
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
    # Convert HSV to RGB
    image_rgb = cv2.cvtColor(hsv_image, cv2.COLOR_HSV2BGR)

# Convert RGB back to HSV
    hsv_image = cv2.cvtColor(image_rgb, cv2.COLOR_BGR2HSV)
    
    x, y = center
    x, y = int(x), int(y)

    roi_width = 50
    
    # Define the region of interest (ROI) for the left and right sides
    left_roi = hsv_image[:, :x-roi_width, :]
    right_roi = hsv_image[:, x+roi_width:, :]
    
    # # Define the lower and upper bounds for skin color in HSV
    # lower_skin = np.array([10, 20, 40], dtype=np.uint8)
    # upper_skin = np.array([30, 200, 200], dtype=np.uint8)
    
    # Define the lower and upper bounds for black color in HSV
    lower_black = np.array([0, 0, 0], dtype=np.uint8)
    upper_black = np.array([0, 0, 0], dtype=np.uint8)
    
    # Define the HSV range for yellow
    lower_yellow = np.array([20, 93, 0])
    upper_yellow = np.array([40, 255, 255])
    
    # # Create binary masks for skin color in left and right regions
    # left_mask = cv2.inRange(left_roi, lower_skin, upper_skin)
    # right_mask = cv2.inRange(right_roi, lower_skin, upper_skin)
    
    # # Calculate the number of skin color pixels in left and right regions
    # left_skin_pixels = cv2.countNonZero(left_mask)
    # right_skin_pixels = cv2.countNonZero(right_mask)
    
    # Create binary masks for skin color in left and right regions
    left_mask_black = cv2.inRange(left_roi, lower_black, upper_black)
    right_mask_black = cv2.inRange(right_roi, lower_black, upper_black)
    
    left_mask_yellow = cv2.inRange(left_roi, lower_yellow, upper_yellow)
    right_mask_yellow = cv2.inRange(right_roi, lower_yellow, upper_yellow)

    # cv2_imshow(left_mask_black)
    # cv2_imshow(right_mask_black)
    # Calculate the number of skin color pixels in left and right regions
    left_black_pixels = cv2.countNonZero(left_mask_black)
    right_black_pixels = cv2.countNonZero(right_mask_black)
    
    left_yellow_pixels = cv2.countNonZero(left_mask_yellow)
    right_yellow_pixels = cv2.countNonZero(right_mask_yellow)

    # Calculate the ratio of skin color pixels in the left and right regions
    black_ratio = right_black_pixels / (left_black_pixels + 1e-8)  # Avoid division by zero
    # ratio_skin = right_skin_pixels / (left_skin_pixels + 1e-8)
    ratio_skin = find_skin(left_roi, right_roi)
    ratio_yellow = right_yellow_pixels/(left_yellow_pixels + 1e-8)
    # print(black_ratio)
    
    class_name = 'fake'
    
    if(ratio_skin < 1.18 and ratio_skin > 1.00 and black_ratio > 0.97 and black_ratio < 1.22 and ratio_yellow < 1.22 and ratio_yellow > 1.02):
        class_name = 'real'
    else:
        class_name = 'fake'
    
    return class_name
