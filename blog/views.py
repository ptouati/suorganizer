from django.shortcuts import (get_object_or_404, render, redirect)

from django.views.generic import View
from django.views.decorators.http import \
    require_http_methods
from .models import Post
from .forms import PostForm


class PostCreate(View):
    form_class = PostForm
    template_name = 'blog/post_form.html'

    def get(self, request):
        return render(
            request, self.template_name, {'form': self.form_class()}
        )

    def post(self, request):
        bound_form = self.form_class(request.POST)
        if bound_form.is_valid():
            new_post = bound_form.save()
            return redirect(new_post)
        else:
            return render(
                request, self.template_name, {'form': bound_form}
            )


@require_http_methods(['HEAD', 'GET'])
def post_detail(request, year, month, slug, parent_template=None):
    post = get_object_or_404(
        Post,
        pub_date__year=year,
        pub_date__month=month,
        slug=slug
    )
    return render(request, 'blog/post_detail.html', {'post': post, 'parent_template': parent_template})


class PostList(View):
    template_name = 'blog/post_list.html'

    def get(self, request):
        return render(request,
                      self.template_name,
                      {'post_list': Post.objects.all()})
