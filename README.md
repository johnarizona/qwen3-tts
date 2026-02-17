**I'm using Python 3.12.7 for this project**\
**Watch the video [tutorial](https://www.youtube.com/watch?v=1HIMgeJ51Vw) for how to use the repo**

### Reccommended:
**Create a Python virtual environment to install only Python libraries needed for this project**\
python -m venv myenv\
myenv\Scripts\activate

### Required:
cd models \
pip3 install -U "huggingface_hub[cli]"\
hf download Qwen/Qwen3-TTS-12Hz-1.7B-Base --local-dir ./Qwen3-TTS-12Hz-1.7B-Base\
cd .. \
### Find your NVIDIA cuda compiler version
nvcc --version\
#use that version and go to [pytorch.org](https://pytorch.org/get-started/locally/) to find the correct command to run to install torch\

### For cuda 13.0, this is the command to install torch
pip3 install torch torchvision --index-url https://download.pytorch.org/whl/cu130 \
pip3 install soundfile\
pip3 install qwen_tts

### Optional
Enable flash attn. Here are [instructions](https://github.com/johnarizona/flash-attn2-wheels) I used to compile wheels on my Windows machine as well as my pre-compiled [wheel](https://github.com/johnarizona/flash-attn2-wheels/releases/tag/0.1.0).
