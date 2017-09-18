Provisioning a new site
=======================

## Required Packages
* nginx
* Python3.6
* virtualenv + pip
* Git

eg, on Ubuntu (and raspbian)

    sudo add-apt-repository ppa:fkrull/deadsnakes
    sudo apt-get install nginx git python36 python3.6-venv

## Nginx Virtual Host Config

* see nginx.template.conf
* replace SITENAME with new site name

## Systemd service

* see gunicorn-systemd.template.service
* replace SITENAME with, e.g., staging.my-domain.com

## Folder structure:
Assume we have a user account at /home/username

    /home/USERNAME
    └── sites
                └── SITENAME
                    ├── database
                    ├── source
                    ├── static
                    └── virtualenv