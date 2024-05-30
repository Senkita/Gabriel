from pathlib import Path

from .extract_audio import extract_audio
from .revise_text import revise_text
from .speech_to_text import speech_to_text
from .summarize_text import summarize_text


def process_video(video_file: Path) -> None:
    print(f"🚀 「{video_file.name}」开始处理...")

    audio_file: Path = (
        extract_audio(video_file=video_file)
        if not Path("audios", video_file.stem + ".aac").exists()
        else Path("audios", video_file.stem + ".aac")
    )

    raw_text_file: Path = (
        speech_to_text(audio_file=audio_file)
        if not Path("texts", audio_file.stem + ".txt").exists()
        else Path("texts", audio_file.stem + ".txt")
    )

    revised_text_file: Path = (
        revise_text(raw_text_file=raw_text_file)
        if not Path("texts", raw_text_file.stem + ".md").exists()
        else Path("texts", raw_text_file.stem + ".md")
    )

    if not Path("texts", revised_text_file.stem + "_summary.md").exists():
        summarize_text(revised_text_file=revised_text_file)

    print(f"🎉 「{video_file.name}」处理完成！")
