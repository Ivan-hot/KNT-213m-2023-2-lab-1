# KNT-213m-2023-2-lab-1

## _Common steps_

### Create virtual environment using python3.10

```
python3.10 -m venv venv
```

### Activate virtual environment

```
source venv/bin/activate
```

### Upgrade pip

```
pip install -U pip
```

### Install development dependencies

```
pip install -r requirements.txt
```

## _Local deployment_

### Build docker image

```
docker build -t lab1:latest .
```

### Run docker container

```
docker run -d --name lab1 --network host lab1:latest
```

### Admin panel

http://127.0.0.1:9000/admin/ <br>
default username: admin <br>
default password: admin

### Link

http://127.0.0.1:9000/
