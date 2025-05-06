from image_lane_detector import process_image
from video_lane_detector import process_video
import cv2

# Image processing
image = cv2.imread('input/road2.jpg')
processed_image = process_image(image)
cv2.imwrite('output/processed_road.jpg', processed_image)

# Video processing
process_video('input/road.mp4', 'output/processed_video.avi')