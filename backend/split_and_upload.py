import subprocess
import boto3
import os
import sys

# === CONFIGURATION ===
mp3_file = os.path.join(os.getcwd(), "..", "samples", "test_song.mp3")
output_dir = os.path.join(os.getcwd(), "output")
bucket_name = "cloudaudio-splitter-bucket-test1"
s3_folder = "test_song_outputs"

# === Step 1: Run Spleeter ===
def run_spleeter():
    print("Running Spleeter...")

    if not os.path.exists(mp3_file):
        print(f"❌ MP3 file not found at: {mp3_file}")
        sys.exit(1)

    command = [
        "spleeter",
        "separate",
        "-p", "spleeter:2stems",
        "-o", output_dir,
        mp3_file
    ]

    try:
        subprocess.run(command, check=True)
        print("✅ Spleeter separation done!")
    except subprocess.CalledProcessError as e:
        print("❌ Spleeter failed:", e)
        sys.exit(1)

# === Step 2: Upload to S3 ===
def upload_to_s3():
    print("Uploading to S3...")

    s3 = boto3.client('s3')
    track_name = os.path.splitext(os.path.basename(mp3_file))[0]
    spleeter_output_path = os.path.join(output_dir, track_name)

    if not os.path.exists(spleeter_output_path):
        print(f"❌ Output folder not found: {spleeter_output_path}")
        sys.exit(1)

    for filename in os.listdir(spleeter_output_path):
        full_path = os.path.join(spleeter_output_path, filename)
        s3_key = f"{s3_folder}/{filename}"
        try:
            s3.upload_file(full_path, bucket_name, s3_key)
            print(f"✅ Uploaded: {filename} → s3://{bucket_name}/{s3_key}")
        except Exception as e:
            print(f"❌ Failed to upload {filename}: {e}")

# === Run ===
if __name__ == "__main__":
    run_spleeter()
    upload_to_s3()
