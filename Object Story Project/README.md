# Slide: Use of Deep Learning in Our Project

**Title:** *Use of Deep Learning in Object Story Generator*

- **Object Detection using YOLOv8:** We used YOLOv8, a state-of-the-art deep learning model based on Convolutional Neural Networks (CNNs), to detect and classify objects in real-time from the webcam feed.
- **Fine-Tuned Model:** Our system uses `best.pt`, a fine-tuned YOLOv8n model trained on the COCO dataset (85 object classes).
- **Automatic Feature Extraction:** Unlike traditional methods, CNNs in YOLOv8 automatically learn visual features such as edges, shapes, and textures directly from images.
- **Real-Time Performance:** YOLOv8 follows a single-pass detection approach, processing the entire frame at once for fast and accurate results.
- **Reliable Detection:** We apply a confidence threshold of > 0.6 to filter out weak or incorrect detections.
- **Integration with AI:** The detected object name is sent to LLaMA 3-8B via the OpenRouter API to generate a short story, combining Computer Vision with Generative AI.
- **Purpose:** Deep learning enables our project to "see" objects and intelligently create stories, making it interactive and AI-driven.