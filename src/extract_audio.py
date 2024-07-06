"""
Author       : Senkita
Date         : 2024-05-08 12:36:43
Description  : 提取音轨
LastEditTime : 2024-05-20 14:56:01
LastEditors  : Senkita
"""

from pathlib import Path

import ffmpeg


def extract_audio(video_file: Path) -> Path:
    output_tmp_file: Path = Path("audios", video_file.stem + "_tmp.aac")

    Path("audios").mkdir(parents=True, exist_ok=True)

    ffmpeg.input(filename=video_file,hwaccel='cuda', vcodec='h264_cuvid').output(
        str(object=output_tmp_file),
        acodec="aac",  # 设置音频编码器为AAC
        audio_bitrate="192k",  # 设置音频比特率为192k
        ac=1,  # 设置音频通道为单声道
        vf='hwupload_cuda',
    ).run(overwrite_output=True)

    output_file: Path = output_tmp_file.rename(
        target=output_tmp_file.parent.joinpath(
            output_tmp_file.stem.replace("_tmp", "") + output_tmp_file.suffix
        )
    )

    return output_file
