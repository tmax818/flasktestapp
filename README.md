
1. Create a virtual environment. Be sure to change <name of virutal environment> to a name you will remember!

```bash
conda create -n <name of virtual environment>
```

2. Activate the virtual environment.

```bash
activate <name of virutal environment>
```

3. Install flask in the virtual environment you just created.

```bash
conda install flask
```

4. Use pip to install the 'gunicorn' package.

```bash
pip install gunicorn
```



5. Make the directory where your project will live. 

```bash
mkdir <dir name>
```

6. Change into the directory you created in step 5 above.

```bash
cd <dir name>
```

7. Open VS code or the IDE of your choice.

```bash
code .
```

1. Create `app.py` and paste in the following:

```python
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hello_world():
    return "It Works!!!"

if __name__ == '__main__':
    app.run()
```

1. Create a new file in the root directory called: `Procfile` and paste in the following:

```
web: gunicorn app:app
```

8. Set up your directory as a git repository.

```bash
git init
```

9. Add your changes to the git repository.

```bash
git add .
```

10. Commit your changes.

```bash
git commit -m "init commit"
```

11. ??? I don't know, just do it.

```bash
pip freeze > requirements.txt
```

12. Log into Heroku. You must have an account and have downloaded the Heroku CLI.

```bash
heroku login
```

13. Create the Heroku repo for your project

```bash
heroku create
```

14. Cross your fingers and type:

```bash
git push heroku master
```

15. If the last step did not generate errors, type:

```bash
heroku open
```

