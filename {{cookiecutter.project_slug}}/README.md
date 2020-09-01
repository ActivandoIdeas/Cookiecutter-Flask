<div align="center">
  <img width="64" src="https://avatars1.githubusercontent.com/u/66532658?s=400&u=f2457dec96897c5dbc843372ec8b325589ab84d5&v=4" alt="cookiecutter-django-rest">
  <h3 align="center">{{cookiecutter.project_name}}</h3>
  <p align="center">
    {{cookiecutter.description}}
  </p>
  <p align="center">
    <a href="https://github.com/ActivandoIdeas/Cookiecutter-Django-AppEngine-GitLab/blob/master/LICENSE">
      	<img src="https://img.shields.io/badge/License-BSD3-blue.svg"  alt="license badge"/>
    </a>
    <a href="https://travis-ci.org/ActivandoIdeas/Cookiecutter-Django-AppEngine-GitLab">
        <img src="https://img.shields.io/travis/ActivandoIdeas/Cookiecutter-Django-AppEngine-GitLab.svg?label=django-cookiecutter" alt="Build Status">
    </a>
    <a href="https://www.python.org/">
        <img src="https://img.shields.io/pypi/pyversions/Django.svg?style=flat-square"  alt="python badge">
    </a>
  </p>
</div>

## Demo

Your demo project

## How to clone

You can clone this repository

    git clone https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}

## Use on local
To install this project just type

Create virtual enviroment:

    $ python -m venv env

Active your enviroment

Install dependencies

    $ pip install -r requirements.txt

Run the project

    $ flask run
    
## Dockerized app

Building

## File structure

* **core** (Flask configurations project)
  * **init** (Base config app)
  * **database** (Settings for SQLAlchemy)
  * **settings** (Injectable settings app)
* **{{cookiecutter.project_slug}}** Your project modules
  * **root** (Main blueprint Flask module) 

## Development configuration

Rename .env.example to .env file

And add your configurations

## Preview

Your image project previews

## How to contribute

* Review our code of conduct

# License

View in https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/blob/master/LICENSE