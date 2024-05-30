from pathlib import Path

from .extract_audio import extract_audio
from .revise_text import revise_text
from .speech_to_text import speech_to_text
from .summarize_text import summarize_text


def process_video(video_file: str) -> None:
    file_name: str = Path(video_file).name

    print(f"🚀 「{file_name}」开始处理...")

    audio_file: str = (
        extract_audio(video_file=video_file)
        if not Path(
            video_file.replace(".mp4", ".aac").replace("videos", "audios")
        ).exists()
        else video_file.replace(".mp4", ".aac").replace("videos", "audios")
    )

    raw_text_files: str = (
        speech_to_text(audio_file=audio_file)
        if not Path(
            audio_file.replace(".aac", ".txt").replace("audios", "texts")
        ).exists()
        else audio_file.replace(".aac", ".txt").replace("audios", "texts")
    )

    revised_text_files: str = (
        revise_text(raw_text_file=raw_text_files)
        if not Path(raw_text_files.replace(".txt", ".md")).exists()
        else raw_text_files.replace(".txt", ".md")
    )

    if not Path(revised_text_files.replace(".md", "_summary.md")).exists():
        summarize_text(revised_text_file=revised_text_files)

    print(f"🎉 「{file_name}」处理完成！")
