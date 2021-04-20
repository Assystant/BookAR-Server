from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from django.http import JsonResponse

from rest_framework.permissions import IsAuthenticated,IsAdminUser
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from rest_framework.response import Response
from .forms import SignUpForm,PwdChangeForm
from django.contrib.auth.models import Group,User
from book_api.models import AuthorModel, PublisherModel, BookModel,PhrasesModel
from book_api.serializers import UserAuthenticationSerializer
from django.contrib.auth.forms import (
    AuthenticationForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm,
)
import ast

from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response



@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    """
        username -- A first parameter
        password -- A second parameter
        Your docs
        ---

        type:
          username:
            required: true
            type: string
          password:
            required: false
            type: string
        parameters:
            - name: username
              description: Username of user
              required: true
              type: string
            - name: password
              description: User Password
              required: true
              type: string

        responseMessages:
            - code: 401
              message: Not authenticated
            - code: 200
              message: Token
            - code: 201
              message: Token
    ---
    """
    serialized = UserAuthenticationSerializer(data=request.data)
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},
                    status=HTTP_200_OK)


@csrf_exempt
@api_view(["GET","POST"])
@permission_classes([IsAuthenticated])
def sample_api(request):
    data = {'sample_data': 123}
    return Response(data, status=HTTP_200_OK)

@csrf_exempt
@api_view(['GET','POST'])
@permission_classes([IsAdminUser])
def signup_student(request):
    """
    :param request:
    Used to create the student by admin
    """
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            # username = form.cleaned_data.get('username')
            # raw_password = form.cleaned_data.get('password1')
            # user = authenticate(username=username, password=raw_password)
            group = Group.objects.get(name='user')
            user.groups.add(group)
            return redirect('account:list_student')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


@csrf_exempt
@api_view(['GET'])
@permission_classes([IsAdminUser])
def list_student(request):
    """
    :param request:
    Used to list all students
    """
    if request.method == 'GET':
        students = Group.objects.get(name="user").user_set.all()
        print("users_in_group",students)
    return render(request, 'students/index.html', {'students': students})

@csrf_exempt
@api_view(['GET','POST'])
@permission_classes([IsAdminUser])
def  change_student_password(request,id):
    """

    :param request:
    :param id:
    using this view admin can change the password of any user
    """
    print("id",id)
    user = User.objects.get(pk=id)
    print("USER",user)
    if request.method == 'POST':
        form = PwdChangeForm(request.POST)
        if form.is_valid():
            print("USer ID ", id)
            user = User.objects.get(pk=id)
            user.set_password(request.POST.get("password1"))
            user.save()
            print("User",user)
            return redirect('account:list_student')
    elif request.method == 'GET':
        form = PwdChangeForm()
        print("GET USER", user)
        return render(request, 'registration/student_password_change.html', {'form': form,"User":user})

@csrf_exempt
@api_view(['GET'])
@permission_classes([IsAdminUser])
def student_state_change(request,userid):
    """

    :param request:
    :param userid:
    Using this view admin can change the state of User
    """
    user =  User.objects.get(pk = userid)
    print(vars(user))
    if user.is_active:
        user.is_active = False
    else:
        user.is_active = True
    user.save()
    # students = Group.objects.get(name="user").user_set.all()
    return redirect('account:list_student')
    # return render(request, 'students/index.html', {'students': students})
    # return Response({user.email:user.is_active})

@csrf_exempt
# @api_view(['DELETE'])
@permission_classes([IsAdminUser])
def delete_student(request,userid):
    """

    :param request:
    :param userid:
    Using this View Admin can delete the Student using userid
    """
    user =  User.objects.get(pk = userid)
    user.delete()
    # return Response({user.email:user.is_active})
    return JsonResponse({"status":True,"message":"Student Successfully Deleted"})


@csrf_exempt
@api_view(['GET'])
@permission_classes([IsAdminUser])
def list_active_phrases(request):
    """
    :param request:
    Used to list all the active phrases
    """
    if request.method == 'GET':
        active_phrases = PhrasesModel.objects.filter(status="active")
        print("active_phrases",active_phrases)
    return render(request, 'students/index.html', {'active_phrases': active_phrases})#here page need to change


@csrf_exempt
@api_view(['GET'])
@permission_classes([IsAdminUser])
def book_state_change(request,bookid):
    """

    :param request:
    :param bookid:
    Using this admin can change the state of the book ("active","inactive")
    """
    book =  BookModel.objects.get(pk = bookid)
    if book.status=='Active':
        book.status = 'Inactive'
    else:
        book.status = 'Active'
    book.save()
    books = BookModel.objects.all()
    return render(request, "books/index.html", {"books": books})
    # redirect('book-ui:ui-book-list')
    # return Response({book.name:book.status})
def error_404_view(request,exception):
    return render(request,"404.html")



# Avoid shadowing the login() and logout() views below.
from django.contrib.auth import (
    REDIRECT_FIELD_NAME, get_user_model, login as auth_login,
    logout as auth_logout, update_session_auth_hash,
)

from django.contrib.auth.forms import (
    SetPasswordForm,
)
from django.contrib.auth.tokens import default_token_generator
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.utils.translation import gettext_lazy as _
from django.views.decorators.cache import never_cache
from django.views.decorators.debug import sensitive_post_parameters
from django.views.generic.edit import FormView
UserModel = get_user_model()
class PasswordContextMixin:
    extra_context = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'title': self.title,
            **(self.extra_context or {})
        })
        return context

INTERNAL_RESET_SESSION_TOKEN = '_password_reset_token'
from django.utils.http import ( urlsafe_base64_decode,
)
class PasswordResetConfirmAccountView(PasswordContextMixin, FormView):
    form_class = SetPasswordForm
    post_reset_login = False
    post_reset_login_backend = None
    reset_url_token = 'set-password'
    success_url = reverse_lazy('password_reset_complete')
    template_name = 'appserver/account/registration/password_reset_confirm.html'
    title = _('Enter new password')
    token_generator = default_token_generator

    @method_decorator(sensitive_post_parameters())
    @method_decorator(never_cache)
    def dispatch(self, *args, **kwargs):
        assert 'uidb64' in kwargs and 'token' in kwargs

        self.validlink = False
        self.user = self.get_user(kwargs['uidb64'])

        if self.user is not None:
            token = kwargs['token']
            if token == self.reset_url_token:
                session_token = self.request.session.get(INTERNAL_RESET_SESSION_TOKEN)
                if self.token_generator.check_token(self.user, session_token):
                    # If the token is valid, display the password reset form.
                    print("Everything Worked")
                    self.validlink = True

                    return super().dispatch(*args, **kwargs)
            else:
                if self.token_generator.check_token(self.user, token):
                    # Store the token in the session and redirect to the
                    # password reset form at a URL without the token. That
                    # avoids the possibility of leaking the token in the
                    # HTTP Referer header.
                    self.request.session[INTERNAL_RESET_SESSION_TOKEN] = token
                    redirect_url = self.request.path.replace(token, self.reset_url_token)
                    return HttpResponseRedirect(redirect_url)

        # Display the "Password reset unsuccessful" page.
        return self.render_to_response(self.get_context_data())

    def get_user(self, uidb64):
        try:
            # urlsafe_base64_decode() decodes to bytestring
            uid = urlsafe_base64_decode(uidb64).decode()
            user = UserModel._default_manager.get(pk=uid)
        except (TypeError, ValueError, OverflowError, UserModel.DoesNotExist, ValidationError):
            user = None
        return user

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.user
        return kwargs

    def form_valid(self, form):
        user = form.save()
        del self.request.session[INTERNAL_RESET_SESSION_TOKEN]
        if self.post_reset_login:
            auth_login(self.request, user, self.post_reset_login_backend)
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.validlink:
            context['validlink'] = True
        else:
            context.update({
                'form': None,
                'title': _('Password reset unsuccessful'),
                'validlink': False,
            })
        return context
