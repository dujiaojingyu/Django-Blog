from django.shortcuts import render,HttpResponse,HttpResponsePermanentRedirect
from .models import UserInfo,UserProfile
from django.contrib.auth.models import User
from .forms import RegistrationForm,UserProfileForm,UserForm,UserInfoForm
from django.contrib.auth.decorators import login_required
# Create your views here.


def register(request):
    if request.method == "POST":
        user_form = RegistrationForm(request.POST)
        userprofile_form = UserProfileForm(request.POST)

        if user_form.is_valid() and userprofile_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            new_profile = userprofile_form.save(commit=False)
            new_profile.user = new_user
            new_profile.save()
            UserInfo.objects.create(user=new_user)
            # return HttpResponse("你已经成功注册！")
            username = user_form.cleaned_data['username']
            return render(request,'account/register_done.html',{'username':username})
        else:
            return HttpResponse("对不起你不能注册")
    else:
        user_form = RegistrationForm()
        userprofile_form = UserProfileForm()
        return render(request,
                      'account/register.html',
                      {'form':user_form,'profile':userprofile_form},
                      )


@login_required(login_url='account/login/')
def myself(request):
    user = User.objects.get(username=request.user.username)
    print(user)
    userinfo = UserInfo.objects.get(user=user)
    userprofile = UserProfile.objects.get(user=user)
    return render(request,'account/myself.html',{'user':user,
                                                 'userinfo':userinfo,
                                                 'userprofile':userprofile})

@login_required(login_url='account/login/')
def myself_edit(request):
    user = User.objects.get(username=request.user.username)
    userinfo = UserInfo.objects.get(user=user)
    userprofile = UserProfile.objects.get(user=user)

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        userinfo_form = UserInfoForm(request.POST)
        userprofile_form = UserProfileForm(request.POST)
        if user_form.is_valid() and userinfo_form.is_valid() and userprofile_form.is_valid():
            user_cd = user_form.cleaned_data
            userprofile_cd = userprofile_form.cleaned_data
            userinfo_cd = userinfo_form.cleaned_data
            print(user_cd['email'])
            user.email = user_cd['email']
            userprofile.birth = userprofile_cd['birth']
            userprofile.phone = userprofile_cd['phone']
            userinfo.school = userinfo_cd['school']
            userinfo.company = userinfo_cd['company']
            userinfo.aboutme = userinfo_cd['aboutme']
            userinfo.address = userinfo_cd['address']
            userinfo.profession = userinfo_cd['profession']
            user.save()
            userinfo.save()
            userprofile.save()
        return HttpResponsePermanentRedirect('/account/my-information')
    else:
        user_form = UserForm(instance=user)
        userprofile_form = UserProfileForm(initial={'birth':userprofile.birth,
                                                    'phone':userprofile.phone})
        userinfo_form = UserInfoForm(initial={'school':userinfo.school,
                                              'address':userinfo.address,
                                              'aboutme':userinfo.aboutme})
        return render(request,'account/myself_edit.html',{'user_form':user_form,
                                                      'userprofile_form':userprofile_form,
                                                      'userinfo_form':userinfo_form})


@login_required(login_url='account/login/')
def my_image(request):
    if request.method == 'POST':
        img = request.POST['img']
        userinfo = UserInfo.objects.get(user=request.user.id)
        userinfo.photo = img
        userinfo.save()
        return HttpResponse('1')
    else:
        return render(request,'account/imagecrop.html',)