from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Article


# Create your views here.
def index(request):
	articless = Article.objects.all()
	paginator = Paginator(articless, 2) # Show 25 contacts per page
	page = request.GET.get('page')
	try:
		article = paginator.page(page)
	except PageNotAnInteger:
		article = paginator.page(1)
	except EmptyPage:
		article = paginator.page(paginator.num_pages)





	# article = Article.objects.filter(isreviewed=True)
	#article = Article.objects.all()
	toplast = Article.objects.all()[:3]
	return render(request,'blog/index.html', {'article' : article , 'toplast' : toplast})


def login(request):
	pass