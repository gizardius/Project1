from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . import models, forms

def blog_all(request):
    post= models.Post.objects.all()
    return render(request,'post_list.html',

    {
        'post':post,
     })
def blog_detail_view(request, id):
    post = get_object_or_404(models.Post, id=id )
    return render(request, 'post_list_detail.html', {'post_id':post})

def create_post_view(request):
    method = request.method
    form = forms.ShowForm()
    if method=="POST":
        form= forms.ShowForm(request.POST, request.FILES)
        form.save()
        return HttpResponse('Good')
    else:
        form=forms.ShowForm()


    return render(request,'add_show.html', {'form':form})