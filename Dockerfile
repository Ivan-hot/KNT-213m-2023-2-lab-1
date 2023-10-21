FROM ubuntu:22.04

RUN apt update
RUN apt install -y supervisor
RUN apt install -y nginx
RUN apt install -y python3 
RUN apt install -y python3-pip 

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

COPY . /app/

RUN mkdir logs

COPY ./djangosite.conf /etc/supervisor/conf.d/
COPY ./djangosite-nginx.conf /etc/nginx/sites-available/djangosite-nginx.conf
RUN ln -s /etc/nginx/sites-available/djangosite-nginx.conf /etc/nginx/sites-enabled/djangosite-nginx
RUN rm /etc/nginx/sites-enabled/default

ENTRYPOINT ["/bin/bash", "-c", "python3 /app/djangosite/manage.py migrate --no-input && python3 /app/djangosite/manage.py collectstatic --no-input && python3 /app/djangosite/manage.py createadmin -u admin -e admin@admin.admin -p admin && service supervisor start && service nginx start && supervisorctl tail -f djangosite"]