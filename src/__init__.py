from pathlib import Path

from .extract_audio import extract_audio
from .revise_text import revise_text
from .speech_to_text import speech_to_text
from .summarize_text import summarize_text
from .text_segmentation import text_segmentation


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

    # 分段
    raw_chunk_files: list[Path] = text_segmentation(text_file=raw_text_file)

    revised_text_file: Path = (
        revise_text(
            raw_chunk_files=raw_chunk_files, raw_text_file_stem=raw_text_file.stem
        )
        if not Path("texts", raw_text_file.stem + ".md").exists()
        else Path("texts", raw_text_file.stem + ".md")
    )

    for raw_chunk_file in raw_chunk_files:
        if raw_chunk_file.exists():
            raw_chunk_file.unlink()

    # 分段
    revised_chunk_files: list[Path] = text_segmentation(text_file=revised_text_file)

    if not Path("texts", revised_text_file.stem + "_summary.md").exists():
        summarize_text(
            revised_chunk_files=revised_chunk_files,
            revised_text_file_stem=revised_text_file.stem,
        )

    for revised_chunk_file in revised_chunk_files:
        if revised_chunk_file.exists():
            revised_chunk_file.unlink()

    print(f"🎉 「{video_file.name}」处理完成！")
