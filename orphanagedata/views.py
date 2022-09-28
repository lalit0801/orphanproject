from django.shortcuts import render,redirect
from django.http import HttpResponse
from orphanagedata.models import NewRegister,NewRegistration,NewOrphan,AddEvents,AddDonors,RequestChildren
from django.core.files.storage import FileSystemStorage
from django.conf.urls.static import static
# Create your views here.
def home(request):
    return render(request,'template/index.html')
def contact(request):
    return render(request,'template/contact.html')
def gallery(request):
    return render(request,'template/gallery.html')
def about(request):
    return render(request,'template/about.html')
def causes(request):
    return render(request,'template/causes.html')
def causessingle(request):
    return render(request,'template/causessingle.html')
def registration(request):
    return render(request,'template/registration.html')
def newregistration(request):
    if request.method=="POST":
        a=request.POST['firstname'];
        b=request.POST['lastname'];
        c=request.POST['dob'];
        d=request.POST['fathername'];
        e=request.POST['email'];
        f=request.POST['password'];
        g=request.POST['confirmpassword'];
        h=request.POST['address'];
        i=request.POST['phone'];
        j=request.POST['pincode'];
        k=request.POST['city'];
        l=request.POST['state'];
        m=request.POST['gender'];
        n=request.FILES['user_image'];
        data=NewRegistration(firstname=a,lastname=b,dob=c,fathername=d,email=e,password=f,confirmpassword=g,address=h,phone=i,pincode=j,city=k,state=l,gender=m,user_image=n)
        data.save()
        indexmsg="NEW USER IS ADDED SUCCESSFULLY"
        return render(request,'template/indexmsg.html',{"indexmsg":indexmsg})
    else:
        return render(request,'template/registration.html')
def showregistration(request):
    data=NewRegistration.objects.all()
    return render(request,'template/showregistration.html',{"alldata":data})
def deleteuser(request):  
    id=request.POST['t1']
    data=NewRegistration.objects.filter(p_id=id).delete()
    return redirect('/showregistration/')

def addchildren(request):
    return render(request,'template/addchildren.html')
def deletechildren1(request):  
    id=request.POST['t1']
    data=NewOrphan.objects.filter(p_id=id).delete()
    return redirect('/deletechildren/')
def updatechildren1(request):  
    id=request.POST['t1']
    data=NewOrphan.objects.filter(p_id=id).all()
    return render(request,'template/updatechildren1.html',{"alldata":data})
def finalupdate(request):  
    t=request.POST['t21']
    a=request.POST['t1']
    b=request.POST['t22']
    c=request.POST['t23']
    d=request.POST['t24']
    e=request.POST['t3']
    f=request.POST['t4']
    g=request.POST['t5']
    h=request.POST['t6']
    i=request.POST['t7']
    j=request.POST['t8']
    k=request.POST['t9']
    l=request.POST['t10']
    m=request.POST['t11']
    n=request.POST['t12']
    o=request.POST['t13']
    p=request.POST['t14']
    r=request.POST['t25']

    data=NewOrphan.objects.filter(p_id=t).update(p_id=t,dateofjoining=a,firstname=b,middlename=c,lastname=d,gender=e,dob=f,religion=g,height=h,eyecolor=i,otherdescription=j,y1=k,y2=l,y3=m,y4=n,y5=o,otherdescriptions=p,haircolor=r)
    return redirect("/updatechildren/")
def updatechildren(request): 
    data=NewOrphan.objects.all()
    return render(request,'template/updatechildren.html',{"alldata":data})
def deletechildren(request):
    data=NewOrphan.objects.all()
    return render(request,'template/deletechildren.html',{"alldata":data})
def deleteorphan(request):  
    id=request.POST['t1']
    data=NewOrphan.objects.filter(p_id=id).delete()
    return redirect('/showchildren/')
def registerchildren(request):
    if request.method=="POST":
        s=request.FILES['childimage'];
        a=request.POST['orphanid'];
        b=request.POST['dateofjoining'];
        c=request.POST['firstname'];
        d=request.POST['middlename'];
        e=request.POST['lastname'];
        f=request.POST['gender'];
        g=request.POST['dob'];
        h=request.POST['religion'];
        i=request.POST['height'];
        j=request.POST['haircolor'];
        k=request.POST['eyecolor'];
        l=request.POST['otherdescription'];
        m=request.POST['y1'];
        n=request.POST['y2'];
        o=request.POST['y3'];
        p=request.POST['y4'];
        q=request.POST['y5'];
        r=request.POST['otherdescriptions'];
        data=NewOrphan(orphanid=a,dateofjoining=b,firstname=c,middlename=d,lastname=e,gender=f,dob=g,religion=h,height=i,haircolor=j,eyecolor=k,otherdescription=l,y1=m,y2=n,y3=o,y4=p,y5=q,otherdescriptions=r,childimage=s)
        data.save()
        msg="NEW ORPHAN IS ADDED"
        return render(request,'template/msg.html',{"abc":msg})
    else:
        return render(request,'template/addchildren.html')
def showchildren(request):
    data=NewOrphan.objects.all()
    return render(request,'template/showchildren.html',{"alldata":data})     
def addevent(request):
    return render(request,'template/addevent.html')  
def registerevent(request):
    if request.method=="POST":
        a=request.POST['eventtype'];
        b=request.POST['name'];
        c=request.POST['eventdate'];
        d=request.POST['eventtime'];
        e=request.POST['place'];
        f=request.POST['organizer'];
        g=request.POST['description'];
        h=request.FILES['eimg'];
        data=AddEvents(eventtype=a,name=b,eventdate=c,eventtime=d,place=e,organizer=f,description=g,eventimg=h)
        data.save()
        msg="EVENT IS ADDED"
        return render(request,'template/msg.html',{"abc":msg})
    else:
        return render(request,'template/addevent.html') 
def adminshowevent(request):
    data=AddEvents.objects.all()
    return render(request,'template/adminshowevent.html',{"alldata":data}) 
def editevent1(request):  
    id=request.POST['t21']
    data=AddEvents.objects.filter(p_id=id).all()
    return render(request,'template/editevent1.html',{"dATA":data})
def finaleditevent(request):  
        t=request.POST['t21'];
        a=request.POST['eventtype'];
        b=request.POST['name'];
        c=request.POST['eventdate'];
        d=request.POST['eventtime'];
        e=request.POST['place'];
        f=request.POST['organizer'];
        g=request.POST['description'];
        data=AddEvents.objects.filter(p_id=t).update(p_id=t,eventtype=a,name=b,eventdate=c,eventtime=d,place=e,organizer=f,description=g)    
        return redirect("/adminshowevent/")
def editevent(request):  
    data=AddEvents.objects.all()
    return render(request,'template/editevent1.html',{"alldata":data})
def deleteevent(request):  
    id=request.POST['t1']
    data=AddEvents.objects.filter(p_id=id).delete()
    return redirect('/adminshowevent/')   
def showevent(request):
    data=AddEvents.objects.all()
    return render(request,'template/showevent.html',{"alldata":data})
def donationform(request):
    return render(request,'template/donationform.html')    
def adddonor(request):
    if request.method=="POST":
        a=request.POST['amount'];
        b=request.POST['firstname'];
        c=request.POST['lastname'];
        d=request.POST['email'];
        e=request.POST['phone'];
        f=request.POST['address'];
        g=request.POST['state'];
        h=request.POST['city'];
        i=request.POST['pincode'];
        j=request.POST['note'];
        k=request.POST['cardno'];
        l=request.POST['cvv'];
        m=request.POST['expirydate'];
           
        data=AddDonors(amount=a,firstname=b,lastname=c,email=d,phone=e,address=f,state=g,city=h,pincode=i,note=j,cardno=k,cvv=l,expirydate=m)
        data.save()
        msg="THANK YOU FOR YOUR DONATION"
        return render(request,'template/msg.html',{"abc":msg})
    else:
        return render(request,'template/donationform.html')
def showdonor(request):
    data=AddDonors.objects.all()
    return render(request,'template/showdonor.html',{"alldata":data})
def deletedonor(request):  
    id=request.POST['t1']
    data=AddDonors.objects.filter(p_id=id).delete()
    return redirect('/showdonor/')
def login(request):
    return render(request,'template/login.html')
def logindata(request):
    if request.method=="POST":
        email=request.POST['email']
        password=request.POST['password']
        if email=="admin@gmail.com" and password=="admin":
            request.session['admin']=email
            return redirect("/admin1/")
        else:
            user=NewRegistration.objects.filter(email=email,password=password).count()
            if(user==0):
                user="NO MATCH"
                return render(request,"template/indexmsg.html",{"indexmsg":user})
            else:
                request.session['email']=email
                return redirect("/user/")
    else:
        return render(request,'template/login.html')
def admin(request):
    if request.session.has_key('admin'):
        email=request.session['admin']
        return render(request,"template/admin.html",{"username":email})
    else:
        return redirect('/login/')
def user(request):
    if request.session.has_key('email'):
        email=request.session['email']
        data=NewOrphan.objects.all()
        return render(request,"template/user.html",{"username":email,"children":data})
    else:
        return redirect('/login/')
def changepassword(request):
    email=request.session['email']
    data=NewRegistration.objects.filter(email=email).all()
    return render(request,"template/changepassword.html",{"all":data})

    
def changepassword1(request):
    if request.method=="POST":
        a=request.POST['t2'];
        b=request.POST['t11'];  
        data=NewRegistration.objects.filter(email=b).update(password=a)
        msg="Password Changed Successfully"
        email=request.session['email']
        data=NewRegistration.objects.filter(email=email).all()
        return render(request,"template/changepassword.html",{"all":data,"abc":msg})
    else:
        return render(request,'template/registration.html')


def showorphan(request):
    data=NewOrphan.objects.all()
    return render(request,'template/showorphan.html',{"children":data})
    
def alldetail(request):
    data=NewOrphan.objects.all()
    return render(request,'template/alldetail.html',{"children":data})
def showmydata(request):
    id=request.POST['t1']
    email=request.session['email']
    data=NewOrphan.objects.filter(p_id=id).all()
    data2=NewRegistration.objects.filter(email=email).all()
    return render(request,'template/singledetail.html',{"children":data,"children2":data2})
def addrequest(request):
    data=NewOrphan.objects.all()
    return render(request,'template/showorphan.html',{"children":data})
def requestchild(request):
    if request.method=="POST":
        a=request.POST['t1'];
        b=request.POST['t2'];
        c=request.POST['t3'];
        d=request.POST['t4'];
        e=request.POST['t5'];
        f=request.POST['t6'];
        g=request.POST['t7'];
        h=request.POST['t8'];
        i=request.POST['t9'];
        j=request.POST['t10'];
        k="pending"
        data=RequestChildren(user_id=a,firstname=b,lastname=c,email=d,address=e,user_image=f,child_id=g,orphanid=h,orphan_name=i,gender=j,status=k)
        data.save()
        msg2="REQUEST IS SENT SUCCESSFULLY"
        return render(request,'template/msg2.html',{"msg":msg2})
    else:
        return render(request,'template/singledetail.html')
def showrequest(request):
    data=RequestChildren.objects.filter(status="pending").all()
    return render(request,'template/showrequests.html',{"alldata":data})   
def sendresponse(request):
    data=RequestChildren.objects.filter(status="Accepted").all()
    return render(request,'template/sendresponse.html',{"alldata":data})
def deleterequest(request):  
    id=request.POST['t1']
    data=RequestChildren.objects.filter(p_id=id).delete()
    return redirect('/showrequest/')
def deleteresponse(request):  
    id=request.POST['t1']
    data=RequestChildren.objects.filter(p_id=id).delete()
    return redirect('/sendresponse/')
def final(request):
    id=request.POST['t1']
    email=request.session['email']
    data=RequestChildren.objects.filter(p_id=id).all()
    data=RequestChildren.objects.filter(p_id=id).update(status="Accepted")
    return redirect("/showrequest/")
def logout(request):
    if request.session.has_key('email'):
        del request.session['email']
    if request.session.has_key('admin'):
        del request.session['admin']
    return redirect("/login/")
def showresponse(request):
    email=request.session['email']
    data=RequestChildren.objects.filter(email=email).all()
    return render(request,'template/showrequests2.html',{"alldata":data})   
