import streamlit as st
import cv2
import requests
from ultralytics import YOLO
import time
import threading
import queue

API_KEY = "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"

story_queue = queue.Queue()

model = YOLO("best.pt")

def generate_story(obj):
    try:
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": "meta-llama/llama-3-8b-instruct",
                "messages": [
                    {
                        "role": "user",
                        "content": f"Write a very short mysterious story about a {obj} in 2 sentences (max 20 words)."
                    }
                ],
                "max_tokens": 50
            },
            timeout=10
        )
        data = response.json()
        if "choices" in data:
            return data["choices"][0]["message"]["content"].strip()
    except:
        pass
    return "Something feels strange about it..."

def generate_story_async(obj):
    def _run():
        story_queue.put(generate_story(obj))
    threading.Thread(target=_run, daemon=True).start()

st.title("🕵️ Object Story Generator")
st.write("Show an object to the camera and get a story!")

run = st.checkbox("Start Camera")

frame_box = st.empty()
story_box = st.empty()

if "last_object" not in st.session_state:
    st.session_state.last_object = None
if "story" not in st.session_state:
    st.session_state.story = "Show an object..."
if "last_story_time" not in st.session_state:
    st.session_state.last_story_time = 0  
if "story_history" not in st.session_state:
    st.session_state.story_history = []

with st.sidebar:
    st.header("📚 Story History")
    if st.session_state.story_history:
        for i, story in enumerate(reversed(st.session_state.story_history), 1):
            st.markdown(f"**{i}.** {story}")
    else:
        st.caption("No stories generated yet.")

if run:
    cap = cv2.VideoCapture(0)

    while run:
        ret, frame = cap.read()
        if not ret:
            break

        try:
            new_story = story_queue.get_nowait()
            st.session_state.story = new_story
            st.session_state.story_history.append(new_story)
        except queue.Empty:
            pass

        results = model(frame, imgsz=320, verbose=False)

        detected = []
        for r in results:
            for box in r.boxes:
                if float(box.conf[0]) > 0.6:
                    detected.append(model.names[int(box.cls[0])])

        if detected:
            obj = detected[0]
            now = time.time()

            if obj != st.session_state.last_object and (now - st.session_state.last_story_time) >= 10:
                st.session_state.story = "Generating..."
                st.session_state.last_object = obj
                st.session_state.last_story_time = now 
                generate_story_async(obj)

        annotated = results[0].plot()
        annotated = cv2.cvtColor(annotated, cv2.COLOR_BGR2RGB)

        frame_box.image(annotated, channels="RGB")
        story_box.markdown(f"### 📖 Story:\n{st.session_state.story}")

        time.sleep(0.03)

    cap.release()
