import cv2
import numpy as np

# Usage
def solution(image_path):
    # image= cv2.imread(image_path)
    ######################################################################
    ######################################################################
    '''
    The pixel values of output should be 0 and 255 and not 0 and 1
    '''
    #####  WRITE YOUR CODE BELOW THIS LINE ###############################
    image= cv2.imread(image_path)
    ######################################################################
    ######################################################################
    '''
    The pixel values of output should be 0 and 255 and not 0 and 1
    '''
    #####  WRITE YOUR CODE BELOW THIS LINE ###############################

    image = cv2.convertScaleAbs(image, alpha=1.4, beta=9)

    blurred_image = cv2.GaussianBlur(image, (10,10), 0)
    hsv_image = cv2.cvtColor(blurred_image, cv2.COLOR_BGR2HSV)

    lower_orange_red = np.array([0, 90, 100])
    upper_orange_red = np.array([30, 255, 255])

    mask = cv2.inRange(hsv_image, lower_orange_red, upper_orange_red)

    red_orange_image = cv2.bitwise_and(blurred_image, image, mask=mask)

    grayscale_image = cv2.cvtColor(red_orange_image, cv2.COLOR_RGB2GRAY)

    _, thresholded_image = cv2.threshold(grayscale_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    contours, _ = cv2.findContours(thresholded_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    max_contour = max(contours, key=cv2.contourArea)
    # Find the largest contour
    for contour in contours:
        cv2.drawContours(thresholded_image, max_contour, -1, (0, 255, 0), 3)

    # Fill the white regions with white pixels
    for contour in contours:
        cv2.fillPoly(thresholded_image, [max_contour], (255, 255, 255))

    # Fill the largest contour with white pixels
    masked_image = cv2.bitwise_and(thresholded_image, thresholded_image, mask=cv2.fillPoly(np.zeros(image.shape[:2], dtype=np.uint8), [max_contour], 255))

    cv2.imshow('final', masked_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    a, b = masked_image.shape

# Create a blank 3-channel image with the shape (a, b, 3)
    final_image = np.zeros((a, b, 3), dtype=np.uint8)

    # Copy the grayscale image to all three color channels
    final_image[:, :, 0] = masked_image
    final_image[:, :, 1] = masked_image
    final_image[:, :, 2] = masked_image

    # Display the final image
    # cv2.imshow('ans', final_image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    ################################################################### 
    return final_image
