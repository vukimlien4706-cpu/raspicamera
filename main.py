#!/usr/bin/env python3

import time
from pathlib import Path

try:
    from picamera2 import Picamera2
except ImportError as exc:
    raise SystemExit(
        "picamera2 is not installed. On Raspberry Pi OS, install it with: "
        "sudo apt install python3-picamera2"
    ) from exc


OUTPUT_DIR = Path(__file__).resolve().parent / "output"
OUTPUT_DIR.mkdir(exist_ok=True)


def main() -> None:
    camera = Picamera2()
    config = camera.create_still_configuration(
        main={"size": (1920, 1080)},
        lores={"size": (640, 480)},
    )
    camera.configure(config)
    camera.start()
    time.sleep(2)

    output_path = OUTPUT_DIR / "capture.jpg"
    camera.capture_file(str(output_path))
    print(f"Saved image to: {output_path}")
    camera.stop()


if __name__ == "__main__":
    main()
