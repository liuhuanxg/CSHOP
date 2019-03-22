from django.shortcuts import reverse ,HttpResponseRedirect

def check_user(func):
    def inner(request,*args,**kwargs):
        if request.session.get('user'):
            return func(request,*args,**kwargs)
        else:
            return HttpResponseRedirect(reverse('users:login'))
    return inner