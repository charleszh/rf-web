from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import TemplateView
from . import logger
from .forms import CommentForm


class CommentView(TemplateView):
    logger.info("in comment view")
    http_method_names = ['post']
    template_name = 'comment/result.html'
    logger.info('in comment view')
    
    def post(self, request, *args, **kwargs):
        logger.info('in post')
        comment_form = CommentForm(request.POST)
        target = request.POST.get('target')
        logger.info('in post for comment view')
        logger.info(comment_form.is_valid())
        logger.info('test')

        if comment_form.is_valid():
            logger.info("in is valid")
            instance = comment_form.save(commit=False)
            instance.target = target
            instance.save()
            succeed = True
            logger.info(instance)
            logger.info("the instance")
            logger.info(target)
            return redirect(target)
        else:
            succeed = False

        context = {
                'succeed': succeed,
                'form': comment_form,
                'target': target,
        }
        logger.info(context)
        return self.render_to_response(context)
