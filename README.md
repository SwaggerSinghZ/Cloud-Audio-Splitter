# 🎶 CloudAudio Splitter

CloudAudio Splitter is a **serverless audio processing tool** that extracts vocals and instrumentals from MP3 files using **Spleeter** and the **AWS Free Tier**.  
It leverages **Python, AWS Lambda, S3, and Boto3** to provide a cost-effective, cloud-powered solution for music and audio enthusiasts.

---

## 📌 Features
- 🎤 **Vocal & Instrument Separation** using [Spleeter](https://github.com/deezer/spleeter).
- ☁️ **AWS S3 Integration** for input/output file storage.
- 🔒 **Serverless & Scalable** using AWS Free Tier.
- 🛠️ **Automation Ready** with Python scripts.
- ⚡ Lightweight and optimized for cloud deployment.

---

## 🏗️ Tech Stack
- **Python 3.9+** → Core scripting & orchestration.
- **Spleeter** → Pre-trained deep learning model for source separation.
- **Boto3** → AWS SDK for Python (S3 upload/download).
- **AWS S3** → File storage for inputs and outputs.
- **AWS Lambda (optional)** → Serverless function execution.
- **Docker (optional)** → For packaging dependencies.

---

## 🚀 Project Roadmap
✅ Local MP3 separation using Spleeter  
✅ Upload separated files (vocals, accompaniment) to AWS S3  
🔜 Automate workflow with AWS Lambda  
🔜 Add CI/CD & Testing integration (Gherkin + Pytest)  
🔜 Create simple web frontend (React / Flask UI) for file uploads  
🔜 Deploy complete serverless pipeline  

---

## ⚙️ Setup & Usage

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/cloudaudio-splitter.git
cd cloudaudio-splitter
2️⃣ Install Dependencies
bash
Copy code
pip install spleeter boto3
3️⃣ Configure AWS
Make sure your AWS CLI is configured:

bash
Copy code
aws configure
4️⃣ Run the Script
bash
Copy code
python split_and_upload.py
This will:

Run Spleeter on your input MP3

Save outputs in output/

Upload results to your specified S3 bucket

📂 Project Structure
bash
Copy code
CloudAudio-Splitter/
│── backend/
│   ├── split_and_upload.py   # Main script
│   ├── samples/              # Input MP3 files
│   ├── output/               # Generated stems
│── README.md
📊 Example Output
After splitting test_song.mp3, you’ll get:

Copy code
vocals.wav
accompaniment.wav
Both files are then uploaded to:

arduino
Copy code
s3://your-bucket-name/test_song_outputs/
🔮 Future Enhancements
Web-based upload & playback

Multi-cloud support (AWS + GCP)

API endpoints for integration

CI/CD with GitHub Actions

Automatic cleanup of temporary files

🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to change.
