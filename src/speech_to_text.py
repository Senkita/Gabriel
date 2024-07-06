"""
Author       : Senkita
Date         : 2024-05-08 12:56:31
Description  : insanely-fast-whisper
LastEditTime : 2024-05-20 14:53:31
LastEditors  : Senkita
"""

from pathlib import Path

import torch
from transformers import pipeline
from transformers.pipelines.base import Pipeline


def speech_to_text(audio_file: Path) -> Path:
    output_file: Path = Path("texts", audio_file.stem + ".txt")

    Path("texts").mkdir(parents=True, exist_ok=True)

    pipe: Pipeline = pipeline(
        "automatic-speech-recognition",
        model="openai/whisper-large-v3",
        torch_dtype=torch.float16,
        device="cuda:0" if torch.cuda.is_available() else "cpu",
        model_kwargs={
            "attn_implementation": "flash_attention_2"
            if torch.cuda.is_available()
            else "sdpa"
        },
    )

    outputs = pipe(
        str(object=audio_file),
        chunk_length_s=30,
        batch_size=24,
        return_timestamps=False,
    )

    with open(file=output_file, mode="w", encoding="utf-8") as f:
        f.write(outputs["text"])

    return output_file
