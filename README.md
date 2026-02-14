#I'm using Python 3.12.7 for this project\

Reccommended:\
#create a Python virtual environment to install only Python libraries needed for this project\
python -m venv myenv\
myenv\Scripts\activate\

Required:\
pip3 install -U "huggingface_hub[cli]"\
hf download Qwen/Qwen3-TTS-12Hz-1.7B-Base --local-dir ./Qwen3-TTS-12Hz-1.7B-Base\
#find the NVIDIA cuda compiler version\
nvcc --version\
#use that version to find the correct command to run to install torch\
https://pytorch.org/get-started/locally/\
#for cuda 13.0, this is the command to install torch\
pip3 install torch torchvision --index-url https://download.pytorch.org/whl/cu130\
pip3 install soundfile\
pip3 install qwen_tts\
