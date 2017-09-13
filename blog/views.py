from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Article, Catecory


# Create your views here.
def index(request):
	articless = Article.objects.all()
	catecory = Catecory.objects.all()
	
	page = request.GET.get('page')
	cat = request.GET.get('cat')

	if cat:
		cat = Catecory.objects.get(name=cat)
		articless = Article.objects.filter(catecory=cat)
	paginator = Paginator(articless, 2) # Show 25 contacts per page	
	try:
		article = paginator.page(page)
	except PageNotAnInteger:
		article = paginator.page(1)
	except EmptyPage:
		article = paginator.page(paginator.num_pages)
		
	# TODO: admin valid article before add it to the blog
	# article = Article.objects.filter(isreviewed=True)
	toplast = Article.objects.all()[:3]
	return render(request,'blog/index.html', {'article' : article , 'toplast' : toplast, 'catecory' : catecory })


def contact(request):
	return render(request,'blog/contact.html')