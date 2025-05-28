## local test
python -m venv skl

pip install -r requirements.txt

## docker

docker build --no-cache -t skeleton:1.0.0 .\
docker compose up -d