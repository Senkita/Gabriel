"""
Author       : Senkita
Date         : 2024-05-08 16:33:52
Description  : 修订讲稿
LastEditTime : 2024-05-20 14:54:55
LastEditors  : Senkita
"""

import os
from pathlib import Path
from typing import Sequence

import cohere
from cohere import ChatConnector, ChatMessage
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env")

co = cohere.Client(api_key=os.getenv("COHERE_API_KEY"))

prompts: Sequence[ChatMessage] = [
    {
        "role": "SYSTEM",
        "message": "# 角色\n\n你作为一名卓越的全栈专家, 对全科领域有着深厚理解和实践经验。\n\n## 技能\n\n### 技能1: 修订讲演稿\n\n- 用户会给你提供发送一份由insanely-fast-whisper转录的讲演稿, 其中可能存在由于发言人的能力、口音、语言表达等问题, 或者转录模型的准确性不足等因素引起的错误和错别字。\n\n- 请你利用你的专业知识和网络检索能力来修正转录稿, 确保内容准确无误。\n\n## 约束\n\n- 使用简体中文回复。\n\n- 直接输出修订稿。\n\n- 遵循Markdown格式排版。\n\n- 围绕讲稿主题，逐字逐词逐句逐段修正讲稿内容。",
    }
]

connectors: Sequence[ChatConnector] = [{"id": "web-search"}]


def revise_text(raw_text_file: Path) -> Path:
    output_file: Path = Path("texts", raw_text_file.stem + ".md")

    title: str = Path(raw_text_file).stem

    with open(file=raw_text_file, mode="r", encoding="utf-8") as f:
        content: str = f.read()

    response = co.chat(
        chat_history=prompts,
        message=f"讲稿主题: 《{title}》\n讲稿内容: 「{content}」",
        connectors=connectors,
        model="command-r-plus",
        temperature=0,
    )

    with open(file=output_file, mode="w", encoding="utf-8") as f:
        f.write(response.text)

    return output_file
