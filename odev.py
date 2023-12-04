import cv2
import numpy as np

def preprocess_image(image_path):
    image = cv2.imread(image_path)

    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    _, thresholded_image = cv2.threshold(gray_image, 180, 255, cv2.THRESH_BINARY)

    kernel = np.ones((5, 5), np.uint8)
    morph_image = cv2.morphologyEx(thresholded_image, cv2.MORPH_OPEN, kernel)

    return image, thresholded_image, morph_image

def count_and_display_rice_grains(original_image, thresholded_image, morph_image):
    _, labels, stats, _ = cv2.connectedComponentsWithStats(morph_image, connectivity=8)

    rice_count = len(stats) - 1  
    print(f"Pirinç Tanelerinin Sayısı: {rice_count}")

    cv2.imshow('orjinal goruntu', original_image)
    cv2.imshow('esiklenmis goruntu', thresholded_image)
    cv2.imshow('arka plani temizlenmis goruntu', morph_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if _name_ == "_main_":
    image_path = r"C:\Users\abdulkadir\Downloads\apo.jpg"
    
    original_image, thresholded_image, morph_image = preprocess_image(image_path)
    count_and_display_rice_grains(original_image, thresholded_image, morph_image)
