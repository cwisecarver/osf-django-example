## Getting Started:
- Clone this repo
- Create a virtual environment
- `cd osf_example/osf_project`
	- If you're using virtualenvwrapper you can set the project directory with the command `setvirtualenvproject`
- `./up.sh`
	- By default it will install all requirements and run migrations
	- It accepts a `--reset` argument that will erase and recreate the database