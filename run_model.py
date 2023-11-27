from ultralytics import YOLO

# Load a pretrained YOLOv8n model
model = YOLO("yolov8m_custom.pt")

# Run inference on an image
results = model.predict(
    source="/Users/dhruv-goyal/Desktop/head_counting/akgec",
    show=True,
    save=True,
    conf=0.5,
    show_conf=True,
    save_txt=True,
    line_width=1,
    show_labels=False,
)


"""
yolo task=detect mode=predict model=yolov8m_custom.pt 
conf=0.10 
source=/Users/dhruv-goyal/HeadCount/akgec 
save_txt=True 
show_labels=False 
show_conf=True 
save_conf=True 
line_width=1
"""
