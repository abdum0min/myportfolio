from django.shortcuts import redirect
from  .models import Post
from django.views.generic import ListView,DetailView
from .forms import CommentForm
from django.views.generic.edit import FormMixin
# Create your views here.

class PostListView(ListView):
    model = Post
    template_name = 'main/blog.html'
    context_object_name = 'posts'
    paginate_by = 4
    
class PostDetailView(DetailView, FormMixin):
    model = Post
    template_name = 'main/blog_detail.html'
    context_object_name = 'post'
    form_class = CommentForm
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.all()
        # context['form'] = self.get_form()
        return context
    
    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        
        self.object = self.get_object()
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog = self.object
            comment.user = request.user
            comment.save()
            return redirect('blog_detail',pk=self.object.pk)
        
        return self.render_to_response(self.get_context_data(form=form))