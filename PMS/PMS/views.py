from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import generic


class HomeView(generic.TemplateView):

    """The Homepage Of LNNCHS-PMS"""

    template_name = "homepage.html"

    def get(self, request, *args, **kwargs):
        context = {
            'user': request.user,
            'page_title': 'Payment Monitoring System!',
        }
        if request.user and not request.user.is_anonymous():
            context = {
                'page_title': 'Welcome ' +
                str(request.user.get_full_name() or request.user.username),
            }
            if not request.user.profile.is_Profile_Set():
                return HttpResponseRedirect(
                    reverse('account:home', args=(request.user.id,))
                )
        return render(request, self.template_name, context)
