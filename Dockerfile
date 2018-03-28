FROM            ygh131/oh_team_docker_dev:base
MAINTAINER      ygh131test@gmail.com

ENV             BUILD_MODE             production
ENV             DJANGO_SETTINGS_MODULE config.settings.${BUILD_MODE}

COPY            . /srv/project


RUN             cp -f /srv/project/.config/${BUILD_MODE}/nginx.conf /etc/nginx/nginx.conf
RUN             cp -f /srv/project/.config/${BUILD_MODE}/nginx-app.conf /etc/nginx/sites-available/
RUN             rm -f /etc/nginx/sites-enabled/*
RUN             ln -sf /etc/nginx/sites-available/nginx-app.conf /etc/nginx/sites-enabled/

RUN             cp /srv/project/.config/${BUILD_MODE}/supervisord.conf /etc/supervisor/conf.d/


CMD             pkill nginx; supervisord -n

# eb에서 프록시로 연결할 port를 열어줌
EXPOSE          80
