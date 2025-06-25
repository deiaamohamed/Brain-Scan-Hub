# predictor_setup.py
import torch
import cv2
import numpy as np
from detectron2.engine import DefaultPredictor
from detectron2.config import get_cfg
from detectron2.data import MetadataCatalog


cfg = get_cfg()
cfg.merge_from_file(r"D:\Brain Scan Hub\Brainapp\ML\config.yaml")
cfg.MODEL.WEIGHTS = r"D:\Brain Scan Hub\Brainapp\segmentation_model\model_final.pth"
cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = 0.5
cfg.MODEL.DEVICE = "cpu"  # Or "cuda" if you have a GPU


MetadataCatalog.get(cfg.DATASETS.TRAIN[0]).thing_classes = ["Tumor"]

predictor = DefaultPredictor(cfg)
metadata = MetadataCatalog.get(cfg.DATASETS.TRAIN[0])
