# Oomck-Bot

## Getting Started

### Dependencies

- [Docker](https://www.docker.com/get-started)
- [Python 3](https://www.python.org/downloads/)

### Setup Project

1. Ensure that [Docker](https://www.docker.com/get-started) is currently running on your machine with an up-to-date version.
2. Install python dependencies with: `pip install -r requirements.txt`.
3. Download [data.json](https://drive.google.com/file/d/137MJNQTUUswp4bv_Y8368o5lzAbW8y52/view?usp=sharing) and place in `data/data.json`.
4. Run `python main.py`.
    - This will create the required ElasticSearch container in [Docker](https://www.docker.com/get-started), if not already set up.
5. Load this data into the ElasticSearch container by running `python load_data.py`.
    - This only needs to be done once upon initial setup.
6. Again, run the `python main.py` to run Oomck-Bot.
7. Enjoy!
