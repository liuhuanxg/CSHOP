from django.shortcuts import reverse ,HttpResponseRedirect,render
from django.core.paginator import Paginator
def check_user(func):
	def inner(request,*args,**kwargs):
		if request.session.get('user'):
			return func(request,*args,**kwargs)
		else:
			return HttpResponseRedirect(reverse('users:login'))
	return inner

def page(r,data,pagenum,path,**kwargs):
	count=data.count()
	print(kwargs)
	paginator = Paginator(data, pagenum)
	p = int(r.GET.get('p', 1))
	pagedata = paginator.page(p)
	pagecount = paginator.num_pages
	pagerange = paginator.page_range
	if p < 1:
		p = 1
	if p > pagecount:
		p = pagecount
	if p <= 5:
		page_list = pagerange[:10]
	elif p + 5 > pagecount:
		page_list = pagerange[-10:]
	else:
		page_list = pagerange[p - 5:p + 4]
	return render(r, path, {'pagedata': pagedata, 'page_list': page_list, 'p': p,'kwargs':kwargs['kwargs']})