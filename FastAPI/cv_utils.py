from ultralytics import YOLO

model=YOLO("yolov8n.pt")
def detect_image(image_path):
    results=model(image_path)
    detections=[]
    for r in results:
        for box in r.boxes:
            class_id=int(box.cls[0])
            label=model.names[class_id]
            conf =float(box.conf[0])
            
            detections.append({
                "object": label,
                "confidence": round(conf, 2)
            })
    return detections
