# Whisper STT Docker Example App

This application demonstrates how to use the Whisper speech-to-text (STT) model within a Docker container. It allows you to transcribe audio files to text using [Whisper's pre-trained Whisper model](https://github.com/openai/whisper).


## Usage


1. [Download Docker for Desktop](https://www.docker.com/products/docker-desktop/)
2. Create an audio file (.wav) and save it in your Desktop folder. Example: ~/Desktop/sample-audio.wav
3. Clone the repo

```shell
git clone https://github.com/UsableSystemsLab/whisper-stt-docker.git
```

4. Build the Docker image and transcribe the audio


```shell
docker build -t whisper-app .
docker run -it --rm -v ~/Desktop:/app/audio whisper-app python transcribe.py /app/audio/sample-audio.wav
```

Explanation:
The command `docker run --rm -v ~/Desktop:/app/audio -m 4g whisper-stt python transcribe.py /app/audio/sample-audio.wav` does the following:

- `docker run`: Runs a new Docker container.
- `--rm`: Automatically removes the container when it exits.
- `-v ~/Desktop:/app/audio`: Mounts the `~/Desktop` directory on your host machine to the `/app/audio` directory in the container to allow the container to access files from your Desktop.
- `-m 4g`: Limits the container's memory usage to 4GB.
- `whisper-stt`: Specifies the Docker image we already built and will use to run the model.
- `python transcribe.py /app/audio/sample-audio.wav`: Runs the `transcribe.py` script inside the container, passing the path to the audio file inside the container as an argument.

5. You may load a different model in the `transcribe.py` and rebuild the docker image and re-run the docker container. Please be sure to increase the memory limit limit using the `-m` option.


## License
MIT License