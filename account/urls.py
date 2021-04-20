from .views import login,sample_api,signup_student,list_student,change_student_password,student_state_change,\
delete_student,list_active_phrases, book_state_change,PasswordResetConfirmAccountView
from django.urls import path
from django.urls import reverse_lazy
from rest_framework.authtoken import views

# from django.conf.urls import url
from django.contrib.auth import views
from django.contrib.auth import views as auth_views
app_name = 'account'

urlpatterns = [
    path('api-login/', login,name="api-login"),
    # path('sampleapi/', sample_api),
    path('login/', views.LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('password-change/', views.PasswordChangeView.as_view(template_name="registration/password_change.html",
                                                              success_url=reverse_lazy('account:password_change_done')),
         name='password_change'),
    path('password-change/done/', views.PasswordChangeDoneView.as_view(template_name="registration/password_change_finish.html"),
         name='password_change_done'),
    # path('password-reset/', views.PasswordResetView.as_view(template_name="registration/password_reset.html",
    #                                                         success_url=reverse_lazy('account:password_reset_done')
    #                                                         ),
    #      name='password_reset'),
    # path('password-reset/done/', views.PasswordResetDoneView.as_view(template_name="registration/password_reset_sent.html"), name='password_reset_done'),
    # path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(template_name="registration/password_reset_email.html"), name='password_reset_confirm'),
    # path('reset/done/', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('signup_student/', signup_student, name='signup'),
    path('list_student/', list_student, name='list_student'),
    path('change_student_password/<id>/', change_student_password, name='change_student_password'),
    path('student_state_change/<userid>/', student_state_change, name='student_state_change'),
    path('book_state_change/<bookid>/', book_state_change, name='book_state_change'),
    path('delete_student/<userid>/', delete_student, name='delete_student'),
    path('list_active_phrases/', list_active_phrases, name='list_active_phrases'),
    path('', views.LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('reset_password/',
         auth_views.PasswordResetView.as_view(template_name="registration/password_reset.html",
                                                            success_url=reverse_lazy('account:password_reset_done')),
         name="password_reset"),

    path('reset_password_sent/',
         auth_views.PasswordResetDoneView.as_view(template_name="registration/password_reset_sent.html"),
         name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
         PasswordResetConfirmAccountView.as_view(template_name="registration/password_reset_confirm_made.html",
             success_url=reverse_lazy('account:password_reset_complete')),
         name="password_reset_confirm"),

    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name="registration/password_reset_done_made.html"),
         name="password_reset_complete"),
]
