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

## 2.django 模板

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
