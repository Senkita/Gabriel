from pathlib import Path

from requests import Response, post

url: str = "http://localhost:11434/api/generate"


def get_revised_response(title: str, content: str) -> str:
    data = {
        "model": "gemma2:27b",
        "system": "# 角色\n\n你作为一名卓越的全栈专家，对软硬件开发有着深厚理解和实践经验。\n\n## 技能\n\n### 技能1: 修正转录稿\n\n- 用户会给你提供一份由insanely-fast-whisper转录的讲演稿，可能存在由于发言人的能力、口音、语言表达等问题，或者转录模型的准确性不足等因素引起的错误和错别字\n\n- 请你利用你的专业知识、现有知识库和网络搜索能力来修正转录稿，确保内容准确无误\n\n- 输出修订稿\n\n## 约束\n\n- 使用简体中文回复\n\n- 直接输出修订稿\n\n- 遵循Markdown格式排版\n\n- 围绕讲稿主题，逐字逐词逐句逐段修正讲稿内容",
        "prompt": f"讲演主题：《{title}》\n\n讲演内容：【{content}】",
        "stream": False,
    }

    revised_response: Response = post(url=url, json=data)

    if revised_response.status_code == 200:
        return revised_response.json()["response"]


def revise_text(raw_chunk_files: list[Path], raw_text_file_stem: str) -> Path:
    output_file: Path = Path("texts", f"{raw_text_file_stem}.md")
    text: str = ""

    for raw_chunk_file in raw_chunk_files:
        title: str = Path(raw_chunk_file).stem

        with open(file=raw_chunk_file, mode="r", encoding="utf-8") as f:
            content: str = f.read()

        revised_response: str = get_revised_response(title=title, content=content)
        text += revised_response

    with open(file=output_file, mode="w", encoding="utf-8") as f:
        f.write(text)

    return output_file
