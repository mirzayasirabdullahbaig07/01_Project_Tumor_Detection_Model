
#%%

from ultralytics import YOLO
import os

# Specify the correct path
data_path = "C:\\Users\\HP\\Desktop\\01_Project_Tumor_Detection_Model\\data.yaml"



# Check if the file exists
if not os.path.exists(data_path):
    print(f"File not found: {data_path}")
else:
    print("File exists, proceeding with training...")

    # Load a model
    model = YOLO("yolo11n.pt")


    # Train the model
    train_results = model.train(
        data=data_path,  # path to dataset YAML
        epochs=5,  # number of training epochs
        imgsz=640,  # training image size
        device="cpu",  # device to run on
    )

# %%
from ultralytics import YOLO
model=YOLO("C:\\Users\\HP\\Desktop\\01_Project_Tumor_Detection_Model\\code\\runs\detect\\train2\\weights\\best.pt")

results=model("C:\\Users\\HP\\Desktop\\01_Project_Tumor_Detection_Model\\Test_Images",save=True)

# Process results list
for result in results:
    boxes=result.boxes
    print(boxes)


# %%

from ultralytics import YOLO
from ultralytics import SAM

# Load YOLO model
yolo_model = YOLO("C:\\Users\\HP\\Desktop\\01_Project_Tumor_Detection_Model\\code\\runs\detect\\train2\\weights\\best.pt")

# Run batched inference on list of images
results = yolo_model("C:\\Users\\HP\\Desktop\\01_Project_Tumor_Detection_Model\\Test_Images",save=True)

# Load the SAM model
sam_model = SAM("sam2_b.pt")

for result in results:
    boxes=result.boxes
    class_ids=boxes.cls.int().tolist() if boxes is not None else []

    if len(class_ids):
        bboxes = boxes.xyxy.cpu().numpy()
        sam_results=sam_model(result.orig_img, bboxes=bboxes, verbose=False, save=True, device="cpu")

# %%