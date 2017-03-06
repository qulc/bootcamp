import markdown
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseBadRequest, HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from bootcamp.decorators import ajax_required
from bootcamp.articles.forms import ArticleForm
from bootcamp.articles.models import Article, Tag, ArticleComment


def _articles(request, articles):
    paginator = Paginator(articles, 10)
    page = request.GET.get('page')
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)
    popular_tags = Tag.get_popular_tags()
    return render(request, 'articles/articles.html',
                  {'articles': articles, 'popular_tags': popular_tags})


def articles(request):
    all_articles = Article.get_published()
    return _articles(request, all_articles)


def article(request, slug):
    article = get_object_or_404(Article, slug=slug, status=Article.PUBLISHED)
    return render(request, 'articles/article.html', {'article': article})


def tag(request, tag_name):
    tags = Tag.objects.filter(tag=tag_name)
    articles = []
    for tag in tags:
        if tag.article.status == Article.PUBLISHED:
            articles.append(tag.article)
    return _articles(request, articles)


@login_required
def write(request):
    if request.method == 'GET':
        form = ArticleForm()
        return render(request, 'articles/write.html', {'form': form})

    form = ArticleForm(request.POST)

    if form.is_valid():
        article = Article()
        article.create_user = request.user
        article.title = form.cleaned_data.get('title')
        article.content = form.cleaned_data.get('content')
        status = form.cleaned_data.get('status')

        if status in [Article.PUBLISHED, Article.DRAFT]:
            article.status = form.cleaned_data.get('status')

        article.save()

        tags = form.cleaned_data.get('tags')
        article.create_tags(tags)
        return redirect('/articles/')

    return render(request, 'articles/write.html', {'form': form})


@login_required
def drafts(request):
    drafts = Article.objects.filter(
        create_user=request.user, status=Article.DRAFT)
    return render(request, 'articles/drafts.html', {'drafts': drafts})


@login_required
def edit(request, article_id):
    tags = ''
    if not article_id:
        article = get_object_or_404(Article, pk=article_id)

        for tag in article.get_tags():
            tags = f'{tags} {tag.tag}'
        tags = tags.strip()
    else:
        article = Article(create_user=request.user)

    if request.POST:
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('/articles/')
    else:
        form = ArticleForm(instance=article, initial={'tags': tags})

    return render(request, 'articles/edit.html', {'form': form})


@login_required
@ajax_required
def preview(request):
    if request.method != 'POST':
        return HttpResponseBadRequest

    content = request.POST.get('content')
    html = _('Nothing to display :(')

    if len(content.strip()) > 0:
        html = markdown.markdown(content, safe_mode='escape')

    return HttpResponse(html)


@login_required
@ajax_required
def comment(request):
    if request.method != 'POST':
        return HttpResponseBadRequest()

    article_id = request.POST.get('article')
    comment = request.POST.get('comment').strip()

    article = Article.objects.get(pk=article_id)

    if len(comment) > 0:
        ArticleComment.objects.create(
            user=request.user,
            article=article,
            comment=comment
        )

    html = ''
    for comment in article.get_comments():
        template = render_to_string('articles/partial_article_comment.html',
                                    {'comment': comment})
        html = f'{html}{template}'

    return HttpResponse(html)
