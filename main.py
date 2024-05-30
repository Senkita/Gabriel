from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from src import process_video


def main() -> None:
    video_files: list[str] = sorted(
        [
            str(object=video_file)
            for video_file in Path("videos").iterdir()
            if video_file.suffix == ".mp4"
        ]
    )

    with ThreadPoolExecutor(max_workers=2) as executor:
        executor.map(process_video, video_files)


if __name__ == "__main__":
    main()
