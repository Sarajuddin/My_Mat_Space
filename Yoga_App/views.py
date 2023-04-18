from django.shortcuts import render
from django.http import HttpResponse
from .models import Members
from django.template import loader


def index(request):
    return render(request, 'index.html')

# def intermediate(request):
#     global user
#     print(f'\nIntermediate Page : {user}\n')
#     template = loader.get_template('intermediate.html')
#     if user:
#             context = {
#                 'data':user,
#             }
#             return HttpResponse(template.render(context, request))
#     return render(request, 'intermediate.html')

# def advanced(request):
#     global user
#     print(f'\nAdvanced Page : {user}\n')
#     template = loader.get_template('advanced.html')
#     if user:
#             context = {
#                 'data':user,
#             }
#             return HttpResponse(template.render(context, request))
#     return render(request, 'advanced.html')

def yogaPoses(request):
    template = loader.get_template('yoga_poses.html')
    if user:
        context = {'title':"Different Yoga Poses", 'logo':"My Mat Space"}
        return HttpResponse(template.render(context, request))
    return render(request, 'yoga_poses.html')

def yogaForWomen(request):
    template = loader.get_template('yoga-for-women.html')
    if user:
        context = {'title':"Yoga for Women", 'logo':"My Mat Space"}
        return HttpResponse(template.render(context, request))
    return render(request, 'yoga-for-women.html')

def yogaForMen(request):
    template = loader.get_template('yoga-for-men.html')
    if user:
        context = {'title':"Yoga for Men", 'logo':"My Mat Space"}
        return HttpResponse(template.render(context, request))
    return render(request, 'yoga-for-men.html')

def profile(request):
    global user
    template = loader.get_template('profile.html')
    if user:
        context = {'title':"My Profile", 'logo':"My Mat Space", 'data':user}
        return HttpResponse(template.render(context, request))
    return render(request, 'profile.html')

def beginner(request):
    global user
    print(f'\nBeginner Page : {user}\n')
    template = loader.get_template('beginner.html')
    if user:
            context = {
                'title':"Beginner Section",
                'logo':"My Mat Space",
                'data':user,
            }
            return HttpResponse(template.render(context, request))
    return render(request, 'beginner.html')

def register(request):
    return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')

def fetchData(email):
    data = Members.objects.filter(email=email).values()
    return data

def getRegisterData(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        mobile = request.POST['mobile']
        age = request.POST['age']
        gender = request.POST['gender']
        disease = request.POST['disease']

        data = fetchData(email)
        print(data)
        if data:
            print("The user with this email already exists\n")
        else:
            member = Members(firstname=firstname, lastname=lastname, email=email, mobile=mobile, age=age, gender=gender, disease=disease)
            member.save()
    return render(request, 'register.html')

def help(request):
    template = loader.get_template('help.html')
    if user:
        context = {'title':"Help Desk", 'logo':"My Mat Space"}
        return HttpResponse(template.render(context, request))
    return render(request, 'help.html')

def contact(request):
    template = loader.get_template('contact.html')
    if user:
        context = {'title':"Contact Us", 'logo':"My Mat Space"}
        return HttpResponse(template.render(context, request))
    return render(request, 'contact.html')

def about(request):
    template = loader.get_template('about.html')
    if user:
        context = {'title':"About Us", 'logo':"My Mat Space"}
        return HttpResponse(template.render(context, request))
    return render(request, 'about.html')

def courses(request):
    global user
    print(f'\nCourses.html Page : {user}\n')
    template = loader.get_template('courses.html')
    if user:
            context = {
                'title':"Our Free Courses",
                'logo':"My Mat Space",
                'data':user,
            }
            return HttpResponse(template.render(context, request))
    return render(request, 'courses.html')

def home(request):
    global user
    print(f'\nHome Page : {user}\n')
    template = loader.get_template('dashboard.html')
    if user:
            context = {
                'title':"Home",
                'logo':"My Mat Space",
                'data':user,
            }
            return HttpResponse(template.render(context, request))
    return render(request, 'dashboard.html')

def dashboard(request):
    if request.method == 'POST':
        email = request.POST['email']
        # password = request.POST['password']
        print(f'\n{email}\n')
        global user
        user = Members.objects.filter(email=email).values()
        print(user)
        template = loader.get_template('dashboard.html')
        if user:
            context = {
                'title':'Dashboard',
                'logo':'My Mat Space',
                'data':user,
            }
            return HttpResponse(template.render(context, request))
    return render(request, 'login.html')
    