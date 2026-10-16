# Slide Content: Deep Learning in Our Object Story Generator Project

## Slide 1: Title Slide
**Project Title:** Object Story Generator  
**Topic:** Application of Deep Learning in Object Detection & Story Generation  
**Project Members:** [Your Team Details]  
**Minor Project Presentation**

---

## Slide 2: Project Overview
- **Aim:** To create an interactive application that detects real-time objects using a camera and generates a creative short story about them.
- **Objective:** Bridge Computer Vision (Object Detection) with Natural Language Processing (Story Generation).
- **Technology Stack:** Python, Streamlit, YOLOv8, OpenCV, OpenRouter LLM API.
- **Outcome:** A fun, AI-powered application demonstrating the practical use of Deep Learning in real-world scenarios.

---

## Slide 3: What is Deep Learning?
- **Definition:** A subset of Machine Learning that uses Artificial Neural Networks with multiple layers to learn patterns directly from data.
- **Key Feature:** Automatic feature extraction without manual intervention.
- **Why Deep Learning?** 
  - Excels at image recognition & object detection
  - Handles complex, high-dimensional data (images, videos)
  - Achieves state-of-the-art accuracy in computer vision tasks
- **In Our Project:** Used for **Object Detection** via Convolutional Neural Networks (CNNs).

---

## Slide 4: Deep Learning Component - YOLOv8
- **Model Used:** YOLOv8 (You Only Look Once, Version 8) by Ultralytics
- **Type:** Real-time object detection and image segmentation model
- **Why YOLOv8?**
  - Fast & lightweight (YOLOv8n variant used)
  - High accuracy with real-time inference
  - Easy to train, fine-tune & deploy
  - Pre-trained on COCO dataset with 80+ classes
- **File:** `best.pt` - Our custom-trained YOLOv8 model

---

## Slide 5: How YOLOv8 Works (Deep Learning Perspective)
- **Single-Pass Detection:** Unlike R-CNNs, YOLO processes the entire image in one forward pass through the neural network.
- **Convolutional Neural Network (CNN):** Extracts hierarchical features (edges → shapes → objects).
- **Grid-Based Approach:** Divides image into grids, predicting bounding boxes + class probabilities for each cell.
- **Non-Maximum Suppression (NMS):** Eliminates duplicate detections to keep the most confident ones.
- **Real-Time Capability:** Optimized for speed without compromising much accuracy.

---

## Slide 6: Dataset & Model Training
- **Dataset Source:** COCO 2017 (Common Objects in Context) via Roboflow
- **Total Classes:** 85 object categories (e.g., person, car, dog, cat, laptop, phone, etc.)
- **Training Details:**
  - Model: `yolov8n.pt` (nano variant) - lightweight & efficient
  - Image Size: 640x640
  - Batch Size: 16
  - Framework: Ultralytics YOLOv8 built on PyTorch
- **Output:** Fine-tuned weights saved as `best.pt` for inference

---

## Slide 7: Deep Learning in Action (Implementation)
**In `main.py`, the deep learning workflow is:**

1. **Load Model:** `model = YOLO("best.pt")` - Loads trained neural network weights
2. **Capture Frames:** OpenCV captures real-time webcam frames
3. **Inference:** `model(frame, imgsz=320, verbose=False)` runs forward pass on each frame
4. **Filter Detections:** Confidence threshold `> 0.6` to ensure reliable predictions
5. **Extract Class:** `model.names[int(box.cls[0])]` gives the detected object name
6. **Visualize:** `results[0].plot()` draws bounding boxes & labels on the frame

---

## Slide 8: Integration with Story Generation
- **Trigger Logic:** When a new object is detected (different from last) with 10s cooldown
- **Async Processing:** Threading prevents UI freeze during story generation
- **LLM Integration:** Detected object name is sent to OpenRouter API (LLaMA 3-8B)
- **Prompt Engineering:** `"Write a very short mysterious story about a {obj} in 2 sentences (max 20 words)."`
- **Result:** Combines Computer Vision (DL) + Generative AI for an engaging experience

---

## Slide 9: Key Takeaways
- **Practical DL Application:** Demonstrates real-time object detection using state-of-the-art CNN architecture.
- **End-to-End System:** Seamlessly integrates deep learning inference with web UI & LLM.
- **Efficiency:** YOLOv8n ensures real-time performance even on modest hardware.
- **Scalability:** Can be extended to more classes, different models, or edge deployment.
- **Learning Outcome:** Gained hands-on experience in model training, inference, and DL deployment.

---

## Slide 10: References
- **Ultralytics YOLOv8:** [https://docs.ultralytics.com/](https://docs.ultralytics.com/)
- **YOLO Research Paper:** Redmon et al., "You Only Look Once: Unified, Real-Time Object Detection"
- **COCO Dataset:** [https://cocodataset.org/](https://cocodataset.org/)
- **Streamlit Docs:** [https://docs.streamlit.io/](https://docs.streamlit.io/)
- **OpenRouter:** [https://www.openrouter.ai/](https://www.openrouter.ai/)
- **PyTorch:** [https://pytorch.org/](https://pytorch.org/)