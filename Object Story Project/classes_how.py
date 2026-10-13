from ultralytics import YOLO
model = YOLO("best.pt")
#print(len(model.names))
print(model.names)
#model.info()
#print(model.model)
#results = model("C:/Users/91892/Downloads/dogboi.webp")