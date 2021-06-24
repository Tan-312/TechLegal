from decimal import Context
from django.contrib.auth import login, authenticate,logout
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_text
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from .tokens import account_activation_token
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required


from .forms import SignUpForm,RegisterCases
from .tokens import account_activation_token
from .models import Cases,Profile


# Create your views here.

def index(request):
    
    #context={"page_sec":"about" ,"title":"Quicksight"}
    #User.objects.all().delete()
    #Profile.objects.all().delete()
    #Cases.objects.all().delete()
   
    
    return render(request, r"LegalTech\index.html")

def login_form(request):
    
    #context={"page_sec":"about","title":"Quicksight"}

    if request.POST:
        print("getting id")
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('inner-page')
    #return render_to_response('login.html', context_instance=RequestContext(request))
    
    return render(request, r"LegalTech\login-form.html")

    
#@login_required(login_url='index')
def inner_page(request):
    
    #context={"page_sec":"print(user.is_active)
    
    return render(request, r"LegalTech\inner-page.html")



def click_me(request):
    
    return redirect(r'index')

def activation_sent_view(request):
    return render(request, r'LegalTech\activation_sent.html')


def activate(request, uidb64, token):
    try:
        
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    # checking if the user exists, if the token is valid.
    if user is not None and account_activation_token.check_token(user, token):
        # if valid set active true 
        user.is_active = True
        # set signup_confirmation true
        user.profile.signup_confirmation = True
        user.save()
        login(request, user)
        context={'object':'user','data':user.profile.first_name}
        return redirect('inner_page')
    else:
        return render(request, r'LegalTech\activation_invalid.html')

def signup_view(request):
    print("list of users ",User.objects.all()) 
    #print("deleting all users",User.objects.all().delete())
    if request.method  == 'POST':
        form = SignUpForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            
            user.refresh_from_db()
            
            
            user.profile.first_name = form.cleaned_data.get('first_name')
            user.profile.last_name = form.cleaned_data.get('last_name')
            user.profile.email = form.cleaned_data.get('email')
            #print(user)
            # user can't login until link confirmed
            user.is_active = False

            print("user.profile.last_name",user.profile.last_name)
            user.save()
            #user.refresh_from_db()
            current_site = get_current_site(request)
            subject = 'Please Activate Your Account'
            # load a template like get_template() 
            # and calls its render() method immediately.
            message = render_to_string(r'LegalTech\activation_request.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                # method will generate a hash value with user related data
                'token': account_activation_token.make_token(user),
            })
            print("Message content",message)
            
            user.email_user(subject, message)
            print("email sent")
            context={'status':'email_sent','success':'Activation link sent! Please check your console or mail.'}
            

            return redirect(r'inner_page')
            #return HttpResponseRedirect(reverse("inner-page"))
            #return render(request, r'LegalTech\inner-page.html',context)
    else:
        form = SignUpForm()
    return render(request, r'LegalTech\inner-page.html', {'form': form})

@login_required(login_url='index')
def register_case(request):
    context ={}
    if request.method  == 'POST':
  
        # create object of form
        form = RegisterCases(request.POST)
        #print(form)
        # check if form data is valid
        if form.is_valid():
            # save the form data to model
            case=form.save()
            case.refresh_from_db()
            
            
            case.user_name = Profile.objects.get(user=request.user)
            case.payee_name = form.cleaned_data.get('payee_name')
            case.payee_address = form.cleaned_data.get('payee_address')
            case.payer_name = form.cleaned_data.get('payer_name')
            case.payer_address = form.cleaned_data.get('payer_address')

            
            case.save()

           

        return redirect(r'view_cases')
    else:
        
        form = RegisterCases()
        
        
        
    return render(request, r"LegalTech\register_case.html", {'form': form})
    
    

@login_required(login_url='index')
def view_cases(request):
    user_case=Profile.objects.get(user=request.user)
    #print(user_case.id)

    
    cases_list=Cases.objects.filter(user_name_id=user_case.id)
    form_data=''
    for c in cases_list:
        form_data+="<tr><td>"+c.payer_name+"</td><td>"+c.payer_address+"</td><td>"+c.payee_name+"</td><td>"+c.payee_address+"""
        </td><td><a href ='#' >Download PDF</a></td><td><a href ='#' >Status</a></td></tr>"""
    
    
    context={'data':form_data}
    return render(request, r"LegalTech\view_cases.html", context)

def logout_session(request):
    logout(request)

    return redirect(r'index')