from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post, PC


def home(request):
	context = {
		'posts': Post.objects.all()
	}
	return render(request, 'review/Home.html', context)
	
class PostListView(ListView):
	model = Post
	template_name = 'review/home.html'
	context_object_name = 'posts'
	ordering = ['-date_posted']


class PostDetailView(DetailView):
	model = Post

def about(request):
	return render(request, 'review/About.html', {'title': 'About'})
	
def pcs(request):
	pcs = PC.objects.all()
	return render(request, 'review/pcs.html', {'pcs': pcs})

class PCSDetailView(DetailView):
	model = PC
	template_name = 'review/pcs_about.html'
