#!/usr/bin/env bash
export DJANGO_SETTINGS_MODULE=config.settings.dev

# Nginx에 존재하던 모든 enabled서버 설정 링크 삭제
sudo rm -rf /etc/nginx/sites-enabled/*
# 프로젝트의 Nginx 설정 (nginx-app.conf)
sudo cp -f /srv/ec2-deploy/.config/nginx-app.conf /etc/nginx/sites-available/nginx-app.conf
sudo ln -sf /etc/nginx/sites-available/nginx-app.conf /etc/nginx/sites-enabled/nginx.conf
sudo cp -f /srv/ec2-deploy/.config/uwsgi.service /etc/systemd/system/uwsgi.service

cd /srv/ec2-deploy/app
# ubuntu 유저로 collectstatic  명령어를 실행 (deploy 스크립트가 root로 설정되서)
/bin/bash -c \
'/home/ubuntu/.pyenv/versions/fc-ec2-deploy/bin/python \
 /srv/ec2-deploy/app/manage.py collectstatic --noinput' ubuntu
sudo systemctl enable uwsgi
sudo systemctl daemon-reload
sudo systemctl restart uwsgi nginx