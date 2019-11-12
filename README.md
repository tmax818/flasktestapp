
- Create a virtual environment. Be sure to change <name of virutal environment> to a name you will remember!

```bash
conda create -n <name of virtual environment>
```

- Activate the virtual environment.

```bash
activate <name of virutal environment>
```

- Install flask in the virtual environment you just created.

```bash
conda install flask
```

- Use pip to install the 'gunicorn' package.

```bash
pip install gunicorn
```

- Make the directory where your project will live. 

```bash
mkdir <dir name>
```

- Change into the directory you created in step 5 above.

```bash
cd <dir name>
```

- Open VS code or the IDE of your choice.

```bash
code .
```

- Create `app.py` and paste in the following:

```python
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hello_world():
    return "It Works!!!"

if __name__ == '__main__':
    app.run()
```

- Create a new file in the root directory called: `Procfile` and paste in the following:

```
web: gunicorn app:app
```

- ??? I don't know, just do it.

```bash
pip freeze > requirements.txt
```

- Set up your directory as a git repository.

```bash
git init
```

- Add your changes to the git repository.

```bash
git add .
```

- Commit your changes.

```bash
git commit -m "init commit"
```

- Log into Heroku. You must have an account and have downloaded the Heroku CLI.

```bash
heroku login
```

- Create the Heroku repo for your project

```bash
heroku create
```

- Cross your fingers and type:

```bash
git push heroku master
```

- If the last step did not generate errors, type:

```bash
heroku open
```

hi
