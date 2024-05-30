"""
Author       : Senkita
Date         : 2024-05-08 12:36:43
Description  : 提取音轨
LastEditTime : 2024-05-20 14:56:01
LastEditors  : Senkita
"""

from pathlib import Path

import ffmpeg


def extract_audio(video_file: str) -> str:
    output_file: str = video_file.replace(".mp4", ".aac").replace("videos", "audios")

    Path("audios").mkdir(parents=True, exist_ok=True)

    ffmpeg.input(filename=video_file).output(
        output_file,
        acodec="aac",  # 设置音频编码器为AAC
        audio_bitrate="192k",  # 设置音频比特率为192k
        ac=1,  # 设置音频通道为单声道
    ).run(overwrite_output=True)

    return output_file
