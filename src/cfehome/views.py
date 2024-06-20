from django.http import HttpResponse
from django.shortcuts import render
from visits.models import PageVisit

def home_page_view(request,*args,**kwargs):
    # request.path 就是访问的页面的路径 /
    queryset = PageVisit.objects.filter(path = request.path)
    my_title = "my page"
    my_context = {
        "page_title": my_title,
        "querycount": queryset.count()
    }
    # 创建了一个新的访
    PageVisit.objects.create(path = request.path)
    return render(request,"home.html",my_context)
    



def old_home_page_view(request,*args,**kwargs):
    my_title = "my page"
    my_context = {
        "page_title": my_title
    }
    html_ = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>{page_title}</h1>
</body>
</html>
""".format(**my_context)
    return HttpResponse(html_)