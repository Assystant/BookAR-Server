from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views
from .views import login, signup_student, list_student, change_student_password, student_state_change, delete_student, list_active_phrases, book_state_change, PasswordResetConfirmAccountView

app_name = 'account'

urlpatterns = [
    path('api-login/', login, name="api-login"),
    path('login/', auth_views.LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('password-change/', auth_views.PasswordChangeView.as_view(template_name="registration/password_change.html",
                                                              success_url=reverse_lazy('account:password_change_done')),
         name='password_change'),
    path('password-change/done/', auth_views.PasswordChangeDoneView.as_view(template_name="registration/password_change_finish.html"),
         name='password_change_done'),
    path('signup_student/', signup_student, name='signup'),
    path('list_student/', list_student, name='list_student'),
    path('change_student_password/<id>/', change_student_password, name='change_student_password'),
    path('student_state_change/<user_id>/', student_state_change, name='student_state_change'),
    path('book_state_change/<book_id>/', book_state_change, name='book_state_change'),
    path('delete_student/<user_id>/', delete_student, name='delete_student'),
    path('list_active_phrases/', list_active_phrases, name='list_active_phrases'),
    path('', auth_views.LoginView.as_view(redirect_authenticated_user=True), name='login'),
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