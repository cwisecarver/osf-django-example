## Getting Started:
- Clone this repo
- Create a virtual environment
- `cd osf_example/osf_project`
	- If you're using virtualenvwrapper you can set the project directory with the command `setvirtualenvproject`
- `./up.sh --reset`
	- By default it will install all requirements and run migrations
	- `--reset` will erase and recreate the database installing fixtures
	- The default username/password is `admin:123password`
- Create a new repo on github so that you're not modifying the example project
	- `git remote remove origin && git remote add https://github.com/{username}/{repo_name}.git` will switch the origin to the new repo you've created on github

## Exploring the Project
- `http://localhost:8010/admin/` is the url for the admin
- `http://localhost:8010/api/` is the root of the browseable API

## Creating your new application
- Inside your virtualenv and in the project directory:
	- `python manage.py startapp {app_name}` will create a new application skeleton
	- Lookover the zoo application in osf_example_app for how to setup models, views, serializers, and urls. They're in files named by ... what they are.
