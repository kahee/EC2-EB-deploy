FROM            ygh131/oh_team_docker_dev:base
MAINTAINER      ygh131test@gmail.com


RUN             apt-get -y update
RUN             apt-get -y dist-upgrade
RUN             apt-get -y install nginx supervisor build-essential

COPY            .requirements /srv/.requirements

WORKDIR         /srv
RUN             pip install -r /srv/.requirements/production.txt

ENV             BUILD_MODE             production
ENV             DJANGO_SETTINGS_MODULE config.settings.${BUILD_MODE}

COPY            . /srv/project


RUN             cp -f /srv/project/.config/${BUILD_MODE}/nginx.conf /etc/nginx/nginx.conf
RUN             cp -f /srv/project/.config/${BUILD_MODE}/nginx-app.conf /etc/nginx/sites-available/
RUN             rm -f /etc/nginx/sites-enabled/*
RUN             ln -sf /etc/nginx/sites-available/nginx-app.conf /etc/nginx/sites-enabled/

RUN             cp /srv/project/.config/${BUILD_MODE}/supervisord.conf /etc/supervisor/conf.d/

CMD             pkill nginx; supervisord -n

EXPOSE          80
