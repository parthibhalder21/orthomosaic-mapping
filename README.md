# Orthomosaic Mixed View Mapping

This project generates an **orthomosaic map** from a drone video using both **horizontal** and **vertical** view frames.

---

## 🚀 How to Use

1. Place your drone video file in the same folder as `orthomosaic_mixed.py`.
2. Install dependencies:
   ```bash
   pip install opencv-python
   ```
3. Run the script:
   ```bash
   python orthomosaic_mixed.py
   ```
4. The script will:
   - Extract frames into the `frames/` folder.
   - Stitch them into `orthomosaic_mixed.jpg`.

---

## 📂 Files

- `orthomosaic_mixed.py` → Main Python script
- `frames/` → Extracted frames (created when script runs)
- `orthomosaic_mixed.jpg` → Final stitched orthomosaic image

---

## 📌 Notes

- If stitching fails, try fewer frames or higher quality.
- Works best with stable aerial footage.

---

## 📜 License

This project is under the MIT License.

## 📚 References

- **OpenCV Image Stitching Documentation:** [https://docs.opencv.org/4.x/d8/d19/tutorial_stitcher.html](https://docs.opencv.org/4.x/d8/d19/tutorial_stitcher.html)  
- **Orthophoto Concept:** [https://en.wikipedia.org/wiki/Orthophoto](https://en.wikipedia.org/wiki/Orthophoto)  
- **🎥 Reference Video:** [What Is An Orthomosaic? Orthomosaic Maps & Orthophotos](https://www.youtube.com/watch?v=g8mapLUXyGI)
