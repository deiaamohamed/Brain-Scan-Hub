# ========== STEP 0: IMPORTS FOR DJANGO ==========
import os
import uuid
import cv2
import numpy as np

# Detectron2
from detectron2.config import get_cfg
from detectron2.engine import DefaultPredictor
from detectron2.data import MetadataCatalog
from detectron2.utils.visualizer import Visualizer
from Brainapp.ML.predictor_setup import predictor


# ========== STEP 2: Brightness Enhancement ==========
def enhance_brightness(image, factor=1.5):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    hsv = np.array(hsv, dtype=np.float64)
    hsv[:, :, 2] *= factor
    hsv[:, :, 2][hsv[:, :, 2] > 255] = 255
    hsv = np.array(hsv, dtype=np.uint8)
    bright_img = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
    return bright_img

# ========== STEP 3: Prediction ==========
def predict_image(image_path):
    image = cv2.imread(image_path)
    original = image.copy()
    bright_img = enhance_brightness(image)
    bright_img = cv2.resize(bright_img, (640, 640))
    
    outputs = predictor(bright_img)
    instances = outputs["instances"].to("cpu")

    # لو مفيش ماسكات أصلاً
    if not instances.has("pred_masks"):
        return  bright_img

    masks = instances.pred_masks.numpy()  # [N, H, W]

    # ماسك أحمر شفاف فوق الصورة
    mask_overlay = bright_img.copy()

    for mask in masks:
        red_mask = np.zeros_like(mask_overlay, dtype=np.uint8)
        red_mask[:, :, 2] = 255  # لون أحمر (BGR)
        mask_bool = mask.astype(bool)

        # دمج الماسك مع الصورة باستخدام الشفافية
        mask_overlay[mask_bool] = cv2.addWeighted(
            mask_overlay, 0.3, red_mask, 0.3, 0
        )[mask_bool]

    return mask_overlay
