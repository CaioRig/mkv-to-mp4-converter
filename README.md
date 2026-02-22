
# MKV Converter

A Python utility to convert MKV video files to MP4 format using FFmpeg.

## Features

- Batch convert all MKV files in the current directory
- Fast stream copying (no re-encoding)
- Simple command-line interface

## Requirements

- Python 3.x
- FFmpeg installed and available in PATH

## Installation

1. Clone or download this project
2. Ensure FFmpeg is installed on your system
3. Run the script:

```bash
python main.py
```

## Usage

Place the script in a folder containing MKV files and run it. All MKV files will be converted to MP4 format in the same directory.

```bash
python main.py
```

## How It Works

- Scans the current directory for `.mkv` files
- Uses FFmpeg to copy video and audio streams without re-encoding
- Outputs MP4 files with the same base filename
- Overwrites existing files automatically

## Notes

- Conversion is fast since streams are copied, not re-encoded
- Requires FFmpeg to be installed and accessible from command line
# mkv-to-mp4-converter
