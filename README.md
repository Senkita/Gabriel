# Gabriel

## Introduction

- ffmpeg 提取视频音轨
- insanely-fast-whisper 语音转文本
- ollama 修正转录稿及输出总结稿

## Installation

```bash
docker run -d --gpus=all -v ollama:/root/.ollama -p 11434:11434 --name ollama --restart always ollama/ollama:latest

conda env create -f environments.yaml
```

> Optional: [Open WebUI](https://github.com/open-webui/open-webui)和[stable-diffusion-webui-docker](https://github.com/AbdBarho/stable-diffusion-webui-docker)

```bash
docker run -d -p 3000:8080 --gpus=all --add-host=host.docker.internal:host-gateway -e "WEBUI_AUTH=False" -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:main
 
git clone https://github.com/AbdBarho/stable-diffusion-webui-docker.git
cd stable-diffusion-webui-docker
docker compose --profile download up --build
docker compose --profile comfy up --build
```

## Usage

```bash
python main.py
```

## Maintainers

[Senkita](https://github.com/Senkita)

## License

[MIT](LICENSE) &copy; [Senkita](https://github.com/Senkita)

## References

- [ffmpeg-python](https://github.com/kkroening/ffmpeg-python)
- [Insanely Fast Whisper](https://github.com/Vaibhavs10/insanely-fast-whisper)
- [Ollama](https://github.com/ollama/ollama)
