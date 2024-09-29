#Install Project using penv

## STEPS to INSTALL ON YOUR LOCAL COMPUTER

1. Clone This Project
```sh
git clone git@github.com:
```

2. Make sure that you've been already install pyenv on your computer

3. Create a Virtual Environment
```sh
python -m venv venv
```

4. Activate the Virtual Environment
```sh
source venv/bin/activate
```

5. Install Project Dependencies
```sh
pip install -r requirements.txt
```

6. Running this project
```sh
python main.py
```

## STEPS to INSTALL ON YOUR Docker
1. Build Docker Image with Dockerfile
```sh
docker build -t ${your-image-name} .
```

2. Create The Container from Docker Image
```sh
docker run -it -p ${8000:8000} --name ${your-container-name} ${your-image-name}
```