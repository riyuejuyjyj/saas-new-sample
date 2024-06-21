# Python 教程：使用 Django、Stripe、Neon PostgreSQL、TailwindCSS、GitHub Actions 构建 SaaS 应用

## 1.准备工作

- 创建工作目录 saas
- 在该目录下创建 src 目录，用于存放项目代码
- 创建 requirements.txt 文件，用于存放项目依赖
- 创建虚拟 python 虚拟环境，并激活

```python
python -m venv venv
source venv/Scripts/activate
# 安装django5.0
pip install -r requirements.txt
# 在src目录下创建了项目cfehome
django-admin startproject cfehome .
# 启动项目
python manage.py runserver
# 创建app
python manage.py startapp visits
```

## 2.django 模板和静态文件

### a.模板渲染

> 首先在 saas 目录下创建 templates 目录，用于存放模板文件，然后在 cfehome 目录下配置 settings.py 中的 templates
> "DIRS": [BASE_DIR / "templates"],

创建 views.py 文件，编写视图函数，并返回模板文件

```python
from django.shortcuts import render

def home_page_view(request,*args,**kwargs):
    return render(requst,'home.html')
```

创建 home.html 文件，编写模板内容

```html
<!DOCTYPE html>
<html>
  <head>
    <title>cfehome</title>
  </head>
  <body>
    <h1>欢迎来到cfehome</h1>
  </body>
</html>
```

在 urls.py 中配置路由

```python
from django.contrib import admin
from django.urls import path
from .views import home_page_view
urlpatterns = [
    # 主页
    path("", home_page_view),
    path("hello-world/", home_page_view),
    path("admin/", admin.site.urls),
]
```

模板中使用变量
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>{{page_title}}</h1>
    <p>{{request.user}}  {{request.method}}
        --{{request.user.is_authenticated}}
    </p>
</body>
</html>
```

### b.模板继承

创建 base.html 文件，作为模板的父模板

```html 
<!DOCTYPE html>
<html lang="ch">
<head>
    <title>
        {%block title%}
        saas
        {%endblock title%}
    </title>
</head>
<body>
    <h1>{{page_title}}</h1>

    {% block content %}
        replace me
    {% endblock content %}

</body>
</html>
```

在 home.html 文件中继承 base.html 文件

```html
{% extends 'base.html' %}

{% block title %}
{{page_title}}-{{block.super}}
{% endblock title%}


{% block content %}
<h1>{{page_title}}</h1>

{% include 'snipp/welcome-user-msg.html'%}

{% endblock content%}
````

### c.配置静态目录

+ 首先在src目录下创建static文件夹，在static内部再创建vendors文件夹存放我们flowbite的css和js

+ 在settins.py配置一下内容

	```python
	STATIC_URL = "static/"
	STATICFILES_BASE_DIR = BASE_DIR/'static'
	STATICFILES_VENDOR_DIR = STATICFILES_BASE_DIR/"vendors"
	
	
	# source for collects
	STATICFILES_DIRS = [
	    STATICFILES_BASE_DIR
	]
	
	# output for collects
	# local cdn
	STATIC_ROOT = BASE_DIR.parent/'local-cdn'
	```
	
+ 在templates目录下新建base文件夹，再新加上css.html,    js.html  ,   meta.html(==暂时为空==)

	

	css.html

	```html
	{% load static %}
	<link href="{% static 'vendors/flowbite.min.css' %}" rel="stylesheet" />
	```

	js.html

	```html
	{% load static %}
	<script src="{%  static 'vendors/flowbite.min.js'  %}"></script>
	```
	
+ 在templates创建nav文件夹，新建navbar.html

	```html
	
	<nav class="bg-white border-gray-200 dark:bg-gray-900">
	    <div class="max-w-screen-xl flex flex-wrap items-center justify-between mx-auto p-4">
	      <a href="https://flowbite.com/" class="flex items-center space-x-3 rtl:space-x-reverse">
	          <img src="https://flowbite.com/docs/images/logo.svg" class="h-8" alt="Flowbite Logo" />
	          <span class="self-center text-2xl font-semibold whitespace-nowrap dark:text-white">Flowbite</span>
	      </a>
	      <button data-collapse-toggle="navbar-default" type="button" class="inline-flex items-center p-2 w-10 h-10 justify-center text-sm text-gray-500 rounded-lg md:hidden hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-gray-200 dark:text-gray-400 dark:hover:bg-gray-700 dark:focus:ring-gray-600" aria-controls="navbar-default" aria-expanded="false">
	          <span class="sr-only">Open main menu</span>
	          <svg class="w-5 h-5" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 17 14">
	              <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M1 1h15M1 7h15M1 13h15"/>
	          </svg>
	      </button>
	      <div class="hidden w-full md:block md:w-auto" id="navbar-default">
	        <ul class="font-medium flex flex-col p-4 md:p-0 mt-4 border border-gray-100 rounded-lg bg-gray-50 md:flex-row md:space-x-8 rtl:space-x-reverse md:mt-0 md:border-0 md:bg-white dark:bg-gray-800 md:dark:bg-gray-900 dark:border-gray-700">
	          <li>
	            <a href="#" class="block py-2 px-3 text-white bg-blue-700 rounded md:bg-transparent md:text-blue-700 md:p-0 dark:text-white md:dark:text-blue-500" aria-current="page">Home</a>
	          </li>
	          <li>
	            <a href="#" class="block py-2 px-3 text-gray-900 rounded hover:bg-gray-100 md:hover:bg-transparent md:border-0 md:hover:text-blue-700 md:p-0 dark:text-white md:dark:hover:text-blue-500 dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent">About</a>
	          </li>
	          <li>
	            <a href="#" class="block py-2 px-3 text-gray-900 rounded hover:bg-gray-100 md:hover:bg-transparent md:border-0 md:hover:text-blue-700 md:p-0 dark:text-white md:dark:hover:text-blue-500 dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent">Services</a>
	          </li>
	          <li>
	            <a href="#" class="block py-2 px-3 text-gray-900 rounded hover:bg-gray-100 md:hover:bg-transparent md:border-0 md:hover:text-blue-700 md:p-0 dark:text-white md:dark:hover:text-blue-500 dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent">Pricing</a>
	          </li>
	          <li>
	            <a href="#" class="block py-2 px-3 text-gray-900 rounded hover:bg-gray-100 md:hover:bg-transparent md:border-0 md:hover:text-blue-700 md:p-0 dark:text-white md:dark:hover:text-blue-500 dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent">Contact</a>
	          </li>
	        </ul>
	      </div>
	    </div>
	  </nav>
	  
	```
	
+ 在base.html中include,效果如下

	```html
	{% include 'nav/navbar.html' %}
	```

	![image-20240620172714153](C:/Users/桐/AppData/Roaming/Typora/typora-user-images/image-20240620172714153.png)

## 3 .上传到GitHub

配置python .gitignore文件

```
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# PyInstaller
#  Usually these files are written by a python script from a template
#  before PyInstaller builds the exe, so as to inject date/other infos into it.
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.nox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
*.py,cover
.hypothesis/
.pytest_cache/
cover/

# Translations
*.mo
*.pot

# Django stuff:
*.log
local_settings.py
db.sqlite3
db.sqlite3-journal

# Flask stuff:
instance/
.webassets-cache

# Scrapy stuff:
.scrapy

# Sphinx documentation
docs/_build/

# PyBuilder
.pybuilder/
target/

# Jupyter Notebook
.ipynb_checkpoints

# IPython
profile_default/
ipython_config.py

# pyenv
#   For a library or package, you might want to ignore these files since the code is
#   intended to run in multiple environments; otherwise, check them in:
# .python-version

# pipenv
#   According to pypa/pipenv#598, it is recommended to include Pipfile.lock in version control.
#   However, in case of collaboration, if having platform-specific dependencies or dependencies
#   having no cross-platform support, pipenv may install dependencies that don't work, or not
#   install all needed dependencies.
#Pipfile.lock

# poetry
#   Similar to Pipfile.lock, it is generally recommended to include poetry.lock in version control.
#   This is especially recommended for binary packages to ensure reproducibility, and is more
#   commonly ignored for libraries.
#   https://python-poetry.org/docs/basic-usage/#commit-your-poetrylock-file-to-version-control
#poetry.lock

# PEP 582; used by e.g. github.com/David-OConnor/pyflow
__pypackages__/

# Celery stuff
celerybeat-schedule
celerybeat.pid

# SageMath parsed files
*.sage.py

# Environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# Spyder project settings
.spyderproject
.spyproject

# Rope project settings
.ropeproject

# mkdocs documentation
/site

# mypy
.mypy_cache/
.dmypy.json
dmypy.json

# Pyre type checker
.pyre/

# pytype static type analyzer
.pytype/

# Cython debug symbols
cython_debug/

# PyCharm
#  JetBrains specific template is maintainted in a separate JetBrains.gitignore that can
#  be found at https://github.com/github/gitignore/blob/main/Global/JetBrains.gitignore
#  and can be added to the global gitignore or merged into this file.  For a more nuclear
#  option (not recommended) you can uncomment the following to ignore the entire idea folder.
#.idea/

```

### a.命令 git status

当你运行 `git status` 命令时，Git 会显示当前工作目录和暂存区的状态。这个命令非常有用，因为它可以帮助你了解哪些文件已被修改、哪些文件已暂存准备提交，以及哪些文件未被跟踪。

以下是 `git status` 命令的一些常见输出示例：

#### 未跟踪的文件

如果你有新添加的文件，但这些文件还没有被 Git 跟踪，`git status` 会显示这些文件。

```bash
$ git status
On branch main
Your branch is up to date with 'origin/main'.

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        newfile.txt

nothing added to commit but untracked files present (use "git add" to track)
```

#### 已修改但未暂存的文件

如果你修改了已跟踪的文件，但还没有将这些修改暂存起来，`git status` 会显示这些文件。

```bash
$ git status
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)
        modified:   modifiedfile.txt

no changes added to commit (use "git add" and/or "git commit -a")
```

#### 已暂存准备提交的文件

如果你已经将修改的文件暂存起来，准备提交，`git status` 会显示这些文件。

```bash
$ git status
On branch main
Your branch is up to date with 'origin/main'.

Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)
        modified:   stagedfile.txt
```

#### 分支信息

`git status` 还会显示当前分支的信息，以及与远程分支的同步情况。

```bash
$ git status
On branch main
Your branch is ahead of 'origin/main' by 1 commit.
  (use "git push" to publish your local commits)

nothing to commit, working tree clean
```

#### 总结

`git status` 是一个非常有用的命令，可以帮助你了解当前 Git 仓库的状态。通过查看这个命令的输出，你可以清楚地知道哪些文件已被修改、哪些文件已暂存准备提交，以及哪些文件未被跟踪。

### b.命令git add

`git add` 命令用于将文件的更改从工作目录添加到暂存区（也称为索引）。这是 Git 工作流程中的一个重要步骤，因为只有在文件被添加到暂存区后，才能将其提交到版本库。

以下是一些常见的 `git add` 用法：

#### 添加单个文件

要将单个文件添加到暂存区，可以使用以下命令：

```bash
git add <文件名>
```

例如：

```bash
git add README.md
```

#### 添加多个文件

如果要添加多个文件，可以在命令中列出所有文件名：

```bash
git add <文件名1> <文件名2> <文件名3>
```

例如：

```bash
git add file1.txt file2.txt file3.txt
```

#### 添加所有更改

如果要将工作目录中的所有更改（包括新文件、修改的文件和删除的文件）添加到暂存区，可以使用以下命令：

```bash
git add .
```

或者使用 `-A` 选项：

```bash
git add -A
```

#### 交互式添加

Git 还提供了交互式添加的功能，允许你选择性地添加文件的某些部分。可以使用以下命令启动交互式添加：

```bash
git add -p
```

这将打开一个交互式界面，让你选择要添加的更改块。

#### 添加删除的文件

如果你删除了一个文件，并希望将这个删除操作也添加到暂存区，可以使用以下命令：

```bash
git add -u
```

这将添加所有已跟踪文件的更改，包括删除的文件。

#### 示例

假设你有一个包含以下文件的 Git 仓库：

```
README.md
file1.txt
file2.txt
```

你修改了 `README.md` 和 `file1.txt`，并添加了一个新文件 `file3.txt`。你可以使用以下命令将这些更改添加到暂存区：

```bash
git add README.md file1.txt file3.txt
```

或者使用以下命令一次性添加所有更改：

```bash
git add .
```

通过这些命令，你可以将文件的更改从工作目录添加到暂存区，为下一步的提交做好准备

### c.命令git commit

`git commit` 命令用于将暂存区中的更改提交到本地仓库。每次提交都会生成一个新的提交记录，包含提交的作者、时间戳、提交信息以及更改的内容。

以下是一些常见的 `git commit` 用法：

#### 基本提交

要提交暂存区中的更改，可以使用以下命令：

```bash
git commit -m "提交信息"
```

例如：

```bash
git commit -m "修复了登录页面的 bug"
```

#### 添加并提交

如果你希望在一次操作中完成添加和提交，可以使用 `-a` 选项。这将自动将所有已跟踪文件的更改添加到暂存区，然后进行提交：

```bash
git commit -a -m "提交信息"
```

例如：

```bash
git commit -a -m "更新了配置文件"
```

#### 修改最后一次提交

如果你刚刚提交了一次更改，但发现遗漏了一些内容或者提交信息有误，可以使用 `--amend` 选项来修改最后一次提交：

```bash
git commit --amend -m "新的提交信息"
```

例如：

```bash
git commit --amend -m "修复了登录页面的 bug，并更新了配置文件"
```

#### 交互式提交

Git 还提供了交互式提交的功能，允许你选择性地提交文件的某些部分。可以使用以下命令启动交互式提交：

```bash
git commit -p
```

这将打开一个交互式界面，让你选择要提交的更改块。

#### 示例

假设你已经将一些更改添加到暂存区，可以使用以下命令进行提交：

```bash
git commit -m "修复了登录页面的 bug"
```

如果你希望在一次操作中完成添加和提交，可以使用以下命令：

```bash
git commit -a -m "更新了配置文件"
```

通过这些命令，你可以将暂存区中的更改提交到本地仓库，生成一个新的提交记录。

### d.git push

```
git remote add origin https://github.com/riyuejuyjyj/saas-rnd-sample.git
git push -u origin main
```

## 4.配置环境变量和远程postgresql数据库

在requirements.txt中新增一下依赖

```txt
gunicorn
python-decouple
psycopg[binary]
dj-database-url
```

在根目录下创建.env文件==数据的链接下面展示==

```python
# dotenv
DJANGO_DEBUG=True
DJANGO_SECRET_KEY='django-insecure-(k=ht&acl(yf56cxxi(&dv#u-!^0nu^x@-3rtvro3&y811-e!('
#(生产数据库)DATABASE_URL='postgresql://neondb_owner:XiAv0WZBm6fd@ep-wispy-smoke-a1f8lrb9.ap-southeast-1.aws.neon.tech/neondb?sslmode=require'
#测试数据库dev
DATABASE_URL ='postgresql://neondb_owner:XiAv0WZBm6fd@ep-empty-forest-a1ks4jcq.ap-southeast-1.aws.neon.tech/neondb?sslmode=require'
CONN_MAX_AGE=60
```

进入到src目录下cfehome的settings.py中添加一下内容

```python
# 导入
from decouple import config
import dj_database_url

SECRET_KEY = config('DJANGO_SECRET_KEY')
DEBUG = config("DJANGO_DEBUG", default=True, cast=bool)

CONN_MAX_AGE = config("CONN_MAX_AGE", default=60, cast=int)
DATABASE_URL = config("DATABASE_URL",default=None,cast=str)
if DATABASE_URL is not None:
    import dj_database_url
    DATABASES = {
    "default": dj_database_url.config(
        default=DATABASE_URL,
        conn_health_checks=True,
        conn_max_age=CONN_MAX_AGE,
    )
}
```

进入https://console.neon.tech/，创建后数据库以后将其url粘贴到DATABASE_URL，再创建一个dev分支用于本地测试使用，main用于部署使用

## 5.配置静态文件下载命令

为了方便以后下载静态文件js，css之类。

```shell
python manage.py startapp commando
```

创建一个用于新建命令的模块，在生成的模块根目录中创建management\commands两个文件夹，再创建__init__.py文件，==别忘了在settins.py中添加commando模块==

在commands下创建hello_world.py，用于测试

```python
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    def handle(self, *args, **options):
        print("Hello World!")
```

此时在命令行运行,可以看到多了个commando模块下的hello_world模块

````shell
python manage.py
output:
[auth]
    changepassword
    createsuperuser

[commando]
    hello_world
    vendor_pull

[contenttypes]
    remove_stale_contenttypes

[django]
    check
    compilemessages
    createcachetable
    dbshell
    diffsettings
    dumpdata
    flush
    inspectdb
    loaddata
    makemessages
    makemigrations
    migrate
    optimizemigration
    sendtestemail
    shell
    showmigrations
    sqlflush
    sqlmigrate
    sqlsequencereset
    squashmigrations
    startapp
    startproject
    test
    testserver

[sessions]
    clearsessions

[staticfiles]
    collectstatic
    findstatic
    runserver
````

然后在src目录下创建我们的helpers文件夹，在其中创建init.py，downloader.py

init.py

```python
from .downloader import download_to_local

__all__ = ["download_to_local"]
```

downloader.py

```python
import requests
from pathlib import Path

def download_to_local(url:str,out_path:Path,parent_mkdir:bool=True):
    if not isinstance(out_path,Path):
        raise ValueError(
            f"{out_path} must be a pathlib.Path object"
        )
    if parent_mkdir:
        out_path.parent.mkdir(parents=True,exist_ok=True)
    try:
        response = requests.get(url)
        response.raise_for_status()
        out_path.write_bytes(response.content)
        return True
    except requests.RequestException as e:
        print(f"Error downloading {url} to {out_path}: {e}")
        return False
```

然后回到commands文件夹再创建vendor_pull.py

```python
from django.core.management.base import BaseCommand
import helpers
from django.conf import settings

import helpers.downloader
VENDOR_STATICFILES = {
    "flowbite.min.css":"https://cdnjs.cloudflare.com/ajax/libs/flowbite/2.3.0/flowbite.min.css",
    "flowbite.min.js":"https://cdnjs.cloudflare.com/ajax/libs/flowbite/2.3.0/flowbite.min.js"
}


STATICFILES_VENDOR_DIR = getattr(
    settings,
    'STATICFILES_VENDOR_DIR'
)

class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Downloading vendor static files")
        completed_urls = []
        for name,url in VENDOR_STATICFILES.items():
            out_path = STATICFILES_VENDOR_DIR / name
            dl_success = helpers.downloader.download_to_local(url, out_path)
            print(f"Downloading {name} from {url} ot {out_path}")
            if dl_success:
                completed_urls.append(url)
            else:
                self.stdout.write(
                    self.style.ERROR(f"Failed to download {name} from {url}")
                )
        if set(completed_urls) == set(VENDOR_STATICFILES.values()):
            self.stdout.write(
                self.style.SUCCESS("All vendor static files downloaded")
            )
        else:
            self.stdout.write(
                self.style.WARNING("Some vendor static files failed to download")
            )    
```

此时为防止我们的目录不存在，所以在settins.py修改代码如下

```python
STATIC_URL = "static/"
STATICFILES_BASE_DIR = BASE_DIR/'static'
STATICFILES_BASE_DIR.mkdir(exist_ok=True,parents=True)
STATICFILES_VENDOR_DIR = STATICFILES_BASE_DIR/"vendors"
```

此时我们可以删掉static目录，然后在命令行输入

```py
python manage.py vendor_pull
```

可以看见它会自动创建statit目录并下载css，js文件

然后在dockerfile文件中

```dockerfile
# Set the python version as a build-time argument
# with Python 3.12 as the default
ARG PYTHON_VERSION=3.12-slim-bullseye
FROM python:${PYTHON_VERSION}

# Create a virtual environment
RUN python -m venv /opt/venv

# Set the virtual environment as the current location
ENV PATH=/opt/venv/bin:$PATH

# Upgrade pip
RUN pip install --upgrade pip

# Set Python-related environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install os dependencies for our mini vm
RUN apt-get update && apt-get install -y \
    # for postgres
    libpq-dev \
    # for Pillow
    libjpeg-dev \
    # for CairoSVG
    libcairo2 \
    # other
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Create the mini vm's code directory
RUN mkdir -p /code

# Set the working directory to that same code directory
WORKDIR /code

# Copy the requirements file into the container
COPY requirements.txt /tmp/requirements.txt

# copy the project code into the container's working directory
COPY ./src /code

# Install the Python project requirements
RUN pip install -r /tmp/requirements.txt

# database isn't available during build
# run any other commands that do not need the database
# such as:
RUN python manage.py vendor_pull
RUN python manage.py collectstatic --noinput

# set the Django default project name
ARG PROJ_NAME="cfehome"

# create a bash script to run the Django project
# this script will execute at runtime when
# the container starts and the database is available
RUN printf "#!/bin/bash\n" > ./paracord_runner.sh && \
    printf "RUN_PORT=\"\${PORT:-8000}\"\n\n" >> ./paracord_runner.sh && \
    printf "python manage.py migrate --no-input\n" >> ./paracord_runner.sh && \
    printf "gunicorn ${PROJ_NAME}.wsgi:application --bind \"0.0.0.0:\$RUN_PORT\"\n" >> ./paracord_runner.sh

# make the bash script executable
RUN chmod +x paracord_runner.sh

# Clean up apt cache to reduce image size
RUN apt-get remove --purge -y \
    && apt-get autoremove -y \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Run the Django project via the runtime script
# when the container starts
CMD ./paracord_runner.sh
```

