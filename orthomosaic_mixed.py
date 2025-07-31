
import cv2
import os

# === Input video file ===
video_path = "VIDEO-2025-07-31-12-25-43.mp4"  # Change this to your video file path
frames_dir = "frames"
os.makedirs(frames_dir, exist_ok=True)

# === Extract frames ===
cap = cv2.VideoCapture(video_path)
frame_rate = int(cap.get(cv2.CAP_PROP_FPS))
frame_interval = frame_rate * 2  # every 2 seconds

count = 0
saved_count = 0
while True:
    ret, frame = cap.read()
    if not ret:
        break
    if count % frame_interval == 0:
        frame = cv2.resize(frame, (1280, 720))  # resize for faster processing
        cv2.imwrite(f"{frames_dir}/frame_{saved_count:04d}.jpg", frame)
        saved_count += 1
    count += 1
cap.release()
print(f"[INFO] Extracted {saved_count} frames into '{frames_dir}' folder.")

# === Load frames for stitching ===
images = []
for fname in sorted(os.listdir(frames_dir)):
    img = cv2.imread(os.path.join(frames_dir, fname))
    if img is not None:
        images.append(img)

print(f"[INFO] Loaded {len(images)} frames for stitching.")

# === Stitch frames ===
stitcher = cv2.Stitcher_create(cv2.Stitcher_PANORAMA)
status, stitched = stitcher.stitch(images)

if status == cv2.Stitcher_OK:
    output_path = "orthomosaic_mixed.jpg"
    cv2.imwrite(output_path, stitched)
    print(f"✅ Orthomosaic saved as {output_path}")
else:
    print(f"❌ Stitching failed. Error code: {status}")
