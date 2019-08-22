from django.shortcuts import render
from .form import RegistrationForm1, empdetail
from myapp.models import tb_registration
from myapp.form import empdetail
from myapp.models import tb_emp
from myapp.form import loginform1
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound


def register(request):
    if request.method=='POST':
        data = request.POST
        form = RegistrationForm1(data)
        if form.is_valid():
            name1=form.cleaned_data['name']
            email1=form.cleaned_data['email']
            contact1 = form.cleaned_data['contact']
            password1 = form.cleaned_data['password']
            address1= form.cleaned_data['address']

            p=tb_registration(name=name1,email=email1,contact=contact1,password=password1,address=address1)
            p.save()
            return HttpResponseRedirect('welcome/emp')
            print("\n this is valid data from form",email1)

            print("1111111111")
            return render(request,"myapp/done.html" ,{'name':name1,'email':email1,'contact':contact1,'password':password1,'address':address1})





        else:
            #form = UserCreationForm()
            #args = {'form':form}
            print("2222222222")
            return render(request,"myapp/form.html" ,{'form':form})
    else:
        form = RegistrationForm1()
        #args = form
        print("2333333333")
        return render(request,"myapp/form.html" ,{'form':form})



def employee(request):
    if request.method=='POST':
        data = request.POST
        form = empdetail(data)
        if form.is_valid():
            e_name1=form.cleaned_data['e_name']
            email1=form.cleaned_data['email']
            jobtitle1=form.cleaned_data['jobtitle']
            specialization1=form.cleaned_data['specialization']
            Experince1=form.cleaned_data['Experince']
            p = tb_emp(e_name=e_name1,email=email1, jobtitle=jobtitle1, specialization=specialization1, Experince=Experince1)
            p.save()
            return render(request, "myapp/emp.html",{'e_name': e_name1,'email':email1, 'jobtitel':jobtitle1, 'specialization': specialization1, 'Experince': Experince1})

            return HttpResponseRedirect('welcome/thanks')



        else:
            # form = UserCreationForm()
            # args = {'form':form}
            print("2222222222")
            return render(request, "myapp/emp.html", {'form': form})
    else:
        form = empdetail()
        # args = form
        print("2333333333")
        return render(request, "myapp/emp.html", {'form': form})



# Create your views here.
def login(request):
    if request.method == 'POST':
        form = loginform1(request.POST)
        if form.is_valid():
            u_email=form.cleaned_data["email"]
            u_password = form.cleaned_data["password"]
            p=tb_registration.objects.filter(email=u_email,password=u_password)
            if(p.count()>0):
                request.session['username']=u_email
                uname = None
                if request.session.has_key('username'):
                    uname = request.session['username']
                    print(uname)
                print("valid username",p)
                return HttpResponseRedirect('welcome/thanks')
            else:
                print('try again',p)
                return HttpResponseNotFound('<h1>no page here</h1>')
        else:
            print("\n\n this is else block:{0}\n\n")
            return render(request,"myapp/login.html",{'form':form})
    else:
        form=loginform1()
        print("\n\n tis is else block:{0}\n\n")
        return render(request,"myapp/login.html",{"form":form})

def template_thanks(request):
    return render(request,"myapp/thanks.html")

