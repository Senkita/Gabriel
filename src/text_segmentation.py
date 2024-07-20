from pathlib import Path


def split_text(text, token_length) -> list[str]:
    """Splits text into chunks based on token length.

    Args:
      text: The input text to be split.
      token_length: The desired length of each chunk in tokens.

    Returns:
      A list of strings, each representing a chunk of the original text.
    """

    words = text.split()
    chunks: list[str] = []
    current_chunk: list[str] = []
    current_length = 0

    for word in words:
        if current_length + len(word) <= token_length:
            current_chunk.append(word)
            current_length += len(word)
        else:
            chunks.append(" ".join(current_chunk))
            current_chunk = [word]
            current_length: int = len(word)

    if current_chunk:
        chunks.append(" ".join(current_chunk))

    return chunks


def text_segmentation(text_file: Path, token_length: int = 2048):
    title: str = Path(text_file).stem

    with open(file=text_file, mode="r", encoding="utf-8") as f:
        text = f.read()

    chunks = split_text(text=text, token_length=token_length)
    output_files: list[Path] = []

    for i, chunk in enumerate(iterable=chunks):
        output_file = Path("texts", title + f"_chunk_{i+1}" + Path(text_file).suffix)
        output_files.append(output_file)

        with open(file=output_file, mode="w", encoding="utf-8") as f:
            f.write(chunk)
    return output_files
