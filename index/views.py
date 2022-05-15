from django.shortcuts import render,redirect
from django.http import HttpResponse
from user.models import user
from votinglist.models import Votlins
from result.models import Result
from variable.models import xyz
from temp.models import tempuser
from django.core.mail import send_mail
import random

def f():
    global a
    
    a=random.randint(10000,30000)
    print(a)
    
def Home(request):
    request.session['x']=1
    rt=Result.objects.get(id=1)
    if rt.show==123:        
    
        data={}
        k=0
        try:
            name=request.POST['name']
            email=request.POST['email']
            gender=request.POST['gender']       
            password=request.POST['password']
            phone=request.POST['phone']
            postal=request.POST['postal']
            
            #kkkk=user(name=name,email=email,password=password,gender=gender,phone=phone,postal=postal)
            request.session['n']=name
            request.session['g']=gender
            request.session['p']=password
            request.session['ph']=phone
            request.session['po']=postal
            request.session['q']=data
            request.session['e']=email
            am=user.objects.all()
            for i in am:
                if(email==i.email):
                    data["s"]="s"
                    k+=1
                if(phone==i.phone):
                    data["s"]="s"
                    k+=1
            
            f()        
            if(k==0):
                
                send_mail(
                'Votting',
                f'Your OYP:-{a}, donot shear it with anyone.',
                'mayankagrawal911900@gmail.com',
                [f'{email}'],
                fail_silently=False,
                )
                
                request.session['s']=0
                return redirect('/otp')
        except:
            pass
        return render(request,"Home2.html",data)
    else:
        return redirect('/pp')
        
d={'y':1}
def otp(request):
    request.session['x']=9
    p=request.session['s']
    if (p==0):
        try:
            otp=int(request.GET['otp'])
            
            if(a==otp):
                request.session['s']=1
                request.session['x']=1
                
                return redirect('/vote')
            
            else:
                d[k]="Invalid OTP"
                    
        except:
            pass
        if request.method=="POST":
            jj=int(request.POST['jj'])

            if jj==d['y']:
                
                e1=request.session['e']
                print(e1)
                
                f()
                d['y']+=1
                send_mail(
                'Votting',
                f'Your OYP:-{a}, donot shear it with anyone.',
                'mayankagrawal911900@gmail.com',
                [f'{e1}'],
                fail_silently=False,
                )
                
        return render(request,"otp.html",d)

def vote(request):
    p=request.session['x']
    print(p)
    if(p==1):
        if 1:
            
            voat=Votlins.objects.all()
            da={'voat':voat}
            try:
                
                hh=request.GET['hh']
                o=0
                for i in voat:
                    o+=1
                    if i.Candidates == hh:
                        print(hh,3,i.Candidates,o)
                        voat=Votlins.objects.get(id=o)
                        dd=Votlins(id=o,Candidates=voat.Candidates,votes=(1+(voat.votes)))
                        dd.save()
                        name=request.session['n']
                        gender=request.session['g']
                        password=request.session['p']
                        phone=request.session['ph']
                        postal=request.session['po']
                        email=request.session['e']
                        p=user(name=name,email=email,password=password,gender=gender,phone=phone,postal=postal)
                        p.save()
                        request.session['x']=7                    
                        return redirect('/thanks')
                   
            except:
                pass
            return render(request,"vote.html",da)
def thanks(request):
        request.session['x']=7   
        return render(request,"thanks.html")
def pp(request):
    f()
    request.session['x']=6
    request.session['s']=1
    return render(request,"timeout.html")

def result(request):
    rt=Result.objects.get(id=1)
    if rt.show==1234:        
        voat=Votlins.objects.all().order_by('votes')
        for i in voat:
            o=i.votes
        o=Votlins.objects.filter(votes=o)
        
        for i in o:
            print(i.Candidates)
        da={'voat':voat,"o":o}
        print(da["o"])
        return render(request,"chart.html",da)
    else:
        return render(request,"rrr.html")
def sed123(request):
    rt=Result.objects.get(id=1)
    if rt.show==1234:
        em=user.objects.all()
        voat=Votlins.objects.all().order_by('votes')
        for i in voat:
            o=i.votes
        o=Votlins.objects.filter(votes=o)
        
        for i in em:
            send_mail(
                'Votting',
                'result is out.!!!!!',
                'mayankagrawal911900@gmail.com',
                [f'{i.email}'],
                fail_silently=False,
                )
            print(i.email)
        for i in o:
            send_mail(
                'Votting',
                'Conguratulate,you win!!!!!',
                'mayankagrawal911900@gmail.com',
                [f'{i.email}'],
                fail_silently=False,
                )
def send123(request):
    rt=Result.objects.get(id=1)
    if rt.show==1234:
        if request.method=="POST":
            jj=int(request.POST['xyz'])
            if jj==911:
                rt=Result.objects.get(id=1)
            
                em=user.objects.all()
                voat=Votlins.objects.all().order_by('votes')
                for i in voat:
                    o=i.votes
                o=Votlins.objects.filter(votes=o)
                
                    
                for i in em:
                    send_mail(
                        'Votting',
                        'result is out.!!!!!',
                        'mayankagrawal911900@gmail.com',
                        [f'{i.email}'],
                        fail_silently=False,
                        )
                    
                for i in o:
                    print(i.email)
                    send_mail(
                        'Votting',
                        'Conguratulate, you win!!!!!',
                        'mayankagrawal911900@gmail.com',
                        [f'{i.email}'],
                        fail_silently=False,
                        )
                return render(request,"send123.html")
    return render(request,"send123.html")    
            
