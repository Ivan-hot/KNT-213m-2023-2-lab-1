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

# Lab 1

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

# Lab 2

## _Weather station_

Configure BAZA_URL in weather_station.urls.py. <br>
If using djangosite in docker container with port 9000 then this port should be specified in BAZA_URL<br>
If using local runserver of djangosite with port 8000 then this port should be specified in BAZA_URL<br>

### Run weather station

```
python -m weather_station.main
```

# Lab 3

## _CSV import_

To fill up the database with data for analysis use file weather_datasetUSA.csv.
To use it run command

```
python manage.py todb -f ./model_for_predict/weather_datasetUSA.csv
```
