from django.shortcuts import get_object_or_404,render
from django.http import HttpResponseRedirect
from django.views import generic
from lyrify.models import Post
from lyrify.forms import PostForm
from lyrify.parser import place_lyrics, parse_lyrics
import random

def home(req):

    tmpl_vars = {
        'all_posts': Post.objects.reverse(),
        'form': PostForm()
    }
    return render(req, 'lyrify/index.html', tmpl_vars)

class DetailView(generic.DetailView):
    model = Post
    template_name = 'lyrify/test.html'


def test(request, post_id):
    p = get_object_or_404(Post, pk=post_id)
    originalL = p.text
    lyrics = parse_lyrics(originalL)
    #remove empty words
    length = len(lyrics)
    blanks = random.sample(xrange(0, length), int(length/8))
    for x in blanks: lyrics[x] = '-'

    return render(request, 'lyrify/test.html', {'lyrics': lyrics, 'index': blanks, 'post_id': post_id})    

def create_post(request):

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            data = form.cleaned_data
            place_lyrics(data['text'])
            #import pdb; pdb.set_trace()
            post.author = request.user
            post.save()
            return HttpResponseRedirect('/')
    else:
        form = PostForm()


    return render(request, 'post.html', {'form': form})


def check_answer(request):
    raw_index = request.POST["index"]
    post_id = request.POST["post_id"]
    index = [int(y) for y in str(raw_index)[1:-1].split(",")]; #convert unicode list to int list
    p = get_object_or_404(Post, pk=post_id)
    originalL = p.text
    lyrics = parse_lyrics(originalL)
    answers= []

    total = 0
    for i in index:
        answer = request.POST[str(i)]
        answers.append((i, answer))
        if (answer == lyrics[i]):
            total += 1

    return render(request, 'lyrify/results.html', {'lyrics': lyrics, 'answers': answers, 'total': total})    
   

    # if request.method == 'POST':
    #     form = AnswerForm(request.POST, length)
    #     if form.is_valid():
    #         form = form.cleaned_data
    #         answers = []
    #         for (answer, user) in form.answers(): 
    #             pass
    #             #compare answeres
    #     return HttpResponseRedirect('/');
    # else:
    #     form = PostForm()


