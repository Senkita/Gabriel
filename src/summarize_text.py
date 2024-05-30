"""
Author       : Senkita
Date         : 2024-05-08 16:46:51
Description  : 总结文稿
LastEditTime : 2024-05-20 14:45:07
LastEditors  : Senkita
"""

import os

from dotenv import load_dotenv
from groq import Groq
from groq.types.chat.chat_completion import ChatCompletion

load_dotenv(dotenv_path=".env")

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def summarize_text(revised_text_file: str) -> None:
    output_file: str = revised_text_file.replace(".md", "_summary.md")

    title: str = revised_text_file.removeprefix("texts/").removesuffix(".md")

    with open(file=revised_text_file, mode="r", encoding="utf-8") as f:
        content: str = f.read()

    chat_completion: ChatCompletion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "# 角色\n\n你作为一名卓越的全栈专家, 对全科领域有着深厚理解和实践经验。\n\n## 技能\n\n### 技能1: 总结文稿\n\n- 用户会给你提供发送一份文稿, 请你结合专业知识对其提纲挈领, 给出概述性总结。\n\n## 约束\n\n- 使用简体中文回复。\n\n- 不得遗漏相关技术细节。\n\n- 遵循Markdown格式排版。",
            },
            {
                "role": "user",
                "content": f"讲稿主题: 《{title}》\n讲稿内容: 「{content}」",
            },
        ],
        temperature=0,
        model="llama3-70b-8192",
        max_tokens=32768,
        stream=False,
    )

    with open(file=output_file, mode="w", encoding="utf-8") as f:
        f.write(chat_completion.choices[0].message.content)
