from django.shortcuts import render


# Create your views here.
def index(request):
    article = "most scientists define the Arctic as the area within the Arctic Circle, a line of latitude about 66.5° north of the Equator. Within this circle are the Arctic ocean basin and the northern parts of Scandinavia, Russia, Canada, Greenland, and the U.S. state of Alaska.\
 The Arctic is almost entirely covered by water, much of it frozen. Some frozen features, such as glaciers and icebergs, are frozen freshwater. In fact, the glaciers and icebergs in the Arctic make up about 20% of Earth’s supply of freshwater.\
 Most of the Arctic, however, is the liquid saltwater of the Arctic ocean basin. Some parts of the ocean’s surface remain frozen all or most of the year. This frozen seawater is called sea ice. Often, sea ice is covered with a thick blanket of snow."
    context = {"name": "Sagar Neupane", "age": 24, "job": "teacher", "salary": 28750, "article": article,
               "heading": "Dynamic Heading"}
    return render(request, "index.html", context)


def dateFilter(request):
    from datetime import datetime
    context = {"value": "myValue", "datetime": datetime.now}
    return render(request, "filterDateTime.html", context)


def TemplatesTag(request):
    context = {"name": "sagar", "age": 24}
    return render(request, "TemplatesTag.html", context)


def loopDTL(request):
    age = {"age1": 24, "age2": 42, "age3": 78, "age4": 90}
    list1 = [14, 45, 46, 85, "sagar"]
    student = {"stu1": {"name": "Sagar Neupane", "age": 24, "level": "Bachelor's", "Course": "CSIT"},
               "stu2": {"name": "Aashish Adhikari", "age": 14, "level": "District Level", "Course": "BLE"},
               "stu3": {"name": "Jamuna Neupane", "age": 65, "level": "Old Level", "Course": "No Study"},
               }
    context = {"age": age, "list": list1, "student": student}
    return render(request, 'forloopDTL.html', context)
