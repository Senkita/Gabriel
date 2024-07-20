from pathlib import Path

from requests import Response, post

url: str = "http://localhost:11434/api/generate"


def get_summarize_response(title: str, content: str) -> str:
    data = {
        "model": "qwen2",
        "system": "# 角色\n\n你作为一名卓越的全栈专家，对软硬件开发有着深厚理解和实践经验，尤为擅长从繁杂的讯息中抽丝剥茧，提纲挈领。\n\n## 技能\n\n### 技能1: 总结讲稿\n\n- 用户会给你提供一份讲演稿，请你使用列表罗列出其中的全部知识点，并展开细节\n\n## 约束\n\n- 使用简体中文回复\n\n- 仅罗列知识点及其细节即可，其他无关信息都不要有\n\n- 不得遗漏相关知识点细节\n\n- 作为最后一道审验，你必须利用你的专业知识、现有知识库和网络搜索能力进行再三校对",
        "prompt": f"讲演主题：《{title}》\n\n讲演内容：【{content}】",
        "stream": False,
    }

    summarize_response: Response = post(url=url, json=data)

    if summarize_response.status_code == 200:
        return summarize_response.json()["response"]


def summarize_text(
    revised_chunk_files: list[Path], revised_text_file_stem: str
) -> None:
    output_file: Path = Path("texts", f"{revised_text_file_stem}_summary.md")
    text: str = ""

    for revised_chunk_file in revised_chunk_files:
        title: str = Path(revised_chunk_file).stem

        with open(file=revised_chunk_file, mode="r", encoding="utf-8") as f:
            content: str = f.read()

        summarize_response: str = get_summarize_response(title=title, content=content)
        text += summarize_response

    with open(file=output_file, mode="w", encoding="utf-8") as f:
        f.write(text)
