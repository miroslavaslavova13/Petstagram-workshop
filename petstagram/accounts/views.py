from django.contrib.auth import get_user_model, login
from django.contrib.auth.views import LoginView, LogoutView
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from petstagram.accounts.forms import UserCreateForm
from petstagram.photos.models import Photo

UserModel = get_user_model()


class LogInView(LoginView):
    template_name = 'accounts/login-page.html'


class RegisterView(CreateView):
    template_name = 'accounts/register-page.html'
    form_class = UserCreateForm
    success_url = reverse_lazy('index')

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)

        login(request, self.object)

        return response


class LogOutView(LogoutView):
    next_page = reverse_lazy('index')


class UserDeleteView(DeleteView):
    template_name = 'accounts/profile-delete-page.html'
    model = UserModel
    success_url = reverse_lazy('index')


class UserDetailsView(DetailView):
    template_name = 'accounts/profile-details-page.html'
    model = UserModel

    photos_paginate_by = 2

    def get_photos_page(self):
        return self.request.GET.get('page', 1)

    def get_paginated_photos(self):
        page = self.get_photos_page()
        photos = self.object.photo_set.order_by('-publication_date')

        paginator = Paginator(photos, self.photos_paginate_by)

        return paginator.get_page(page)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # self.request.user is the logged user, self.object is the selected user
        context['is_owner'] = self.request.user == self.object
        context['pets_count'] = self.object.pet_set.count()

        photos = self.object.photo_set.prefetch_related('photolike_set')

        context['photos_count'] = photos.count()
        context['likes_count'] = sum(x.photolike_set.count() for x in photos)

        context['photos'] = self.get_paginated_photos()

        return context


class EditUserView(UpdateView):
    template_name = 'accounts/profile-edit-page.html'
    model = UserModel
    fields = ('first_name', 'last_name', 'email', 'gender')

    def get_success_url(self):
        return reverse_lazy('details user', kwargs={'pk': self.request.user.pk})
