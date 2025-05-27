# 🧠 Tumor Detection Model with YOLOv11 and SAM2

**Author:** Mirza Yasir Abdullah Baig  
**Email:** yasirabdullah4549@gmail.com  
**LinkedIn:** [linkedin.com/in/mirzayasirabdullahbaig](https://www.linkedin.com/in/mirza-yasir-abdullah-baig)  
**GitHub:** [github.com/mirzayasirabdullahbaig07](https://github.com/mirzayasirabdullahbaig07)

---

## 📌 Overview

This project implements a tumor detection system using **YOLOv11** for real-time object detection and **SAM2 (Segment Anything Model 2)** for precise image segmentation.  
It was developed as part of an internship at **Arch Technologies** from **May 1, 2025, to July 30, 2025**.  
The system aims to assist in early diagnosis and analysis of tumors in medical imaging.

---

## 📁 Project Structure

tumor-detection/
├── code/
│ ├── train.py
│ ├── inference.py
│ └── weights/
│ └── best.pt
├── data/
│ └── data.yaml
├── Test_Images/
├── requirements.txt
└── README.md

---

## 🚀 Features

- ✅ **Real-Time Tumor Detection** with YOLOv11  
- 🧩 **Precise Tumor Segmentation** with SAM2  
- 📁 **Custom Dataset Support**  
- 🔌 **Easy Integration** into medical imaging workflows  

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/tumor-detection.git
cd tumor-detection

python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate

pip install -r requirements.txt

python code/train.py --data data.yaml --epochs 5 --img-size 640 --device cpu

python code/inference.py --weights code/weights/best.pt --source Test_Images/ --save

📧 Email: yasirabdullah4549@gmail.com

💼 LinkedIn: linkedin.com/in/mirzayasirabdullahbaig

💻 GitHub: github.com/mirzayasirabdullahbaig07

---

### ✅ How to Use:

1. Copy all the content above.
2. Open your project folder.
3. Create or open a file called `README.md`.
4. Paste the content into it and save.
5. Push it to GitHub to display it on your repo.

Let me know if you want to add sample images, badge icons, or project demo links!

