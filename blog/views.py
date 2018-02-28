from django.shortcuts import (get_object_or_404, render)

from django.views.generic import View
from django.views.decorators.http import \
    require_http_methods
from .models import Post


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
