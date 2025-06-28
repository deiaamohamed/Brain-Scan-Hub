import torch
import open_clip
from PIL import Image

model_name = "hf-hub:microsoft/BiomedCLIP-PubMedBERT_256-vit_base_patch16_224"
model, preprocess = open_clip.create_model_from_pretrained(model_name)
tokenizer = open_clip.get_tokenizer(model_name)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = model.to(device)

# === Label Set ===
labels = [
    # Tumor
    "Glioma tumor identified in the brain MRI.",
    "Meningioma tumor detected in the brain MRI.",
    "Pituitary mass lesion observed in the pituitary gland region of the brain MRI.",
    "MRI suggests abnormal tumor growth in the brain.",
    "Focal lesion consistent with tumor presence in the brain MRI.",
    "Tumor region segmented in the brain MRI.",
    "Localized brain tumor visible in the MRI scan.",
    "Abnormal mass present in the brain MRI.",
    "Potential tumor area identified in the brain MRI.",
    "Abnormal tissue formation observed in the brain MRI.",
    "Aggressive tumor appearance noted on the MRI scan.",
    "Focal tumor-like lesion seen in the brain MRI.",
    "Lesion detected in the brain MRI consistent with focal pathology.",
    "Brain tumor region clearly segmented in the MRI.",
    "Abnormal mass visualized in the brain MRI.",
    "Tumor site identified in contrast-enhanced brain MRI.",
    "Localized tumor detected with strong signal intensity in the brain MRI.",
]

# === Pre-encode all text features ===
text_inputs = tokenizer(labels).to(device)
with torch.no_grad():
    text_features = model.encode_text(text_inputs)
    text_features /= text_features.norm(dim=-1, keepdim=True)

def generate_caption(image_path):
    image = Image.open(image_path).convert("RGB")
    image_tensor = preprocess(image).unsqueeze(0).to(device)

    with torch.no_grad():
        image_features = model.encode_image(image_tensor)
        image_features /= image_features.norm(dim=-1, keepdim=True)

        similarities = (image_features @ text_features.T).squeeze(0)
        top_idx = similarities.argmax().item()
        caption = labels[top_idx]
        
        return caption
