import os
import subprocess


def convert_mkv_to_mp4(input_file):
    output_file = os.path.splitext(input_file)[0] + ".mp4"

    command = [
        "ffmpeg",
        "-i",
        input_file,
        "-c:v",
        "copy",
        "-c:a",
        "copy",
        "-y",  # overwrite without asking
        output_file,
    ]

    try:
        subprocess.run(command, check=True)
        print(f"[OK] {input_file} -> {output_file}")
    except subprocess.CalledProcessError:
        print(f"[ERROR] Failed to convert {input_file}")


def convert_all_in_current_folder():
    files = [f for f in os.listdir() if f.lower().endswith(".mkv")]

    if not files:
        print("No .mkv files found in this folder.")
        return

    for file in files:
        convert_mkv_to_mp4(file)


if __name__ == "__main__":
    convert_all_in_current_folder()
