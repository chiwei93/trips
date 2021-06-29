from django.views.generic import TemplateView


# Create your views here.


class HomeView(TemplateView):
    template_name = "information/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["current_page"] = "home"
        return context


class AboutUsView(TemplateView):
    template_name = "information/about_us.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["current_page"] = "about_us"
        return context


class ContactsView(TemplateView):
    template_name = "information/contacts.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["current_page"] = "contacts"
        return context


class PrivacyView(TemplateView):
    template_name = "information/privacy.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["current_page"] = "privacy"
        return context


class TermsView(TemplateView):
    template_name = "information/terms.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["current_page"] = "terms"
        return context
