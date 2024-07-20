from pathlib import Path

from src import process_video


def main() -> None:
    video_files: list[Path] = sorted(
        [
            video_file
            for video_file in Path("videos").iterdir()
            if video_file.suffix == ".mp4" or ".wmv"
        ]
    )

    for video_file in video_files:
        process_video(video_file=video_file)


if __name__ == "__main__":
    main()
