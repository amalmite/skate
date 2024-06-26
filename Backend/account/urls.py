from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()
# router.register(r'products', SkatingProductViewSet)


urlpatterns = [
    # path("session/", SessionTestView.as_view(template_name = "Session/session.html"), name="session"),
    path("session/", create_outer_repeater, name="session"),
    path("test/", SessionView.as_view(template_name="Session/test.html"), name="test"),
    path("", AdminDashboard.as_view(template_name="test.html"), name="admin_home"),
    path(
        "admin_login/",
        AdminLoginView.as_view(template_name="Auth/admin_login.html"),
        name="admin_login",
    ),
    path(
        "admin_profile/",
        AdminProfileView.as_view(template_name="Admin/admin_profile.html"),
        name="admin_profile",
    ),
    path(
        "admin_update/",
        AdminProfileUpdateView.as_view(template_name="Admin/edit_modal.html"),
        name="admin_update",
    ),
    path("logout/", admin_logout, name="logout"),
    path(
        "company_create/",
        CompanyGroupCreationView.as_view(template_name="Company/create_company.html"),
        name="company_create",
    ),
    path(
        "company_update/<int:id>/",
        CompanyGroupUpdateView.as_view(template_name="Company/update_company.html"),
        name="company_update",
    ),
    path(
        "company_detail/<int:id>/",
        CompanyDetailView.as_view(template_name="Company/list_company.html"),
        name="company_detail",
    ),
    path(
        "tax_create/",
        TaxCreateView.as_view(template_name="Company/create_tax.html"),
        name="tax_create",
    ),
    path(
        "tax_update/<int:id>/",
        TaxUpdateView.as_view(template_name="Company/update_tax.html"),
        name="tax_update",
    ),
    path(
        "tax_list/",
        TaxListView.as_view(template_name="Company/list_tax.html"),
        name="tax_list",
    ),
    path(
        "location_create/",
        LocationcreateView.as_view(template_name="Company/create_location.html"),
        name="location_create",
    ),
    path(
        "location_list/",
        LocationListView.as_view(template_name="Company/list_location.html"),
        name="location_list",
    ),
    path(
        "location_update/<int:id>/",
        LocationUpdateView.as_view(template_name="Company/update_location.html"),
        name="location_update",
    ),
    path(
        "mall_create/",
        MallcreateView.as_view(template_name="Company/create_mall.html"),
        name="mall_create",
    ),
    path(
        "mall_list/",
        MallListView.as_view(template_name="Company/list_mall.html"),
        name="mall_list",
    ),
    path(
        "mall_update/<int:id>/",
        MallUpdateView.as_view(template_name="Company/update_mall.html"),
        name="mall_update",
    ),
    path(
        "business_profile_create/",
        BusinessProfileCreateView.as_view(template_name="Company/create_business.html"),
        name="business_profile_create",
    ),
    path(
        "business_profile_list/",
        BusinessProfileListView.as_view(template_name="Company/list_business.html"),
        name="business_profile_list",
    ),
    path(
        "business_profile_update/<int:id>/",
        BusinessProfileUpdateView.as_view(template_name="Company/update_business.html"),
        name="business_profile_update",
    ),
    path(
        "session_create/",
        SessionCreateView.as_view(template_name="Session/create_session.html"),
        name="session_create",
    ),
    path(
        "session_list/",
        SessionListView.as_view(template_name="Session/list_session.html"),
        name="session_list",
    ),
    path(
        "session_update/<int:id>/",
        SessionUpdateView.as_view(template_name="Session/update_session.html"),
        name="session_update",
    ),
    path(
        "sessio_schedule/",
        SessionScheduleView.as_view(template_name="Session/session_schedule.html"),
        name="session_schedule",
    ),
    path(
        "product_create/",
        ProductCreateView.as_view(template_name="Product/create_product.html"),
        name="product_create",
    ),
    path(
        "product_list/",
        ProductListView.as_view(template_name="Product/list_product.html"),
        name="product_list",
    ),
    path(
        "product_update/<int:id>/",
        ProductUpdateView.as_view(template_name="Product/update_product.html"),
        name="product_update",
    ),
    path(
        "module_create/",
        ModuleCreateListView.as_view(template_name="Company/create_module.html"),
        name="module_create",
    ),
    path(
        "module_list/",
        ModuleCreateListView.as_view(template_name="Company/list_module.html"),
        name="module_list",
    ),
    path(
        "module_update/<int:id>/",
        ModuleUpdateView.as_view(template_name="Company/update_module.html"),
        name="module_update",
    ),
    path("module_delete/<int:id>/", module_delete, name="module_delete"),
    path(
        "role_create/",
        RoleCreateListView.as_view(template_name="Company/create_role.html"),
        name="role_create",
    ),
    path(
        "role_list/",
        RoleCreateListView.as_view(template_name="Company/list_role.html"),
        name="role_list",
    ),
    path(
        "role_update/<int:id>/",
        RoleUpdateView.as_view(template_name="Company/update_role.html"),
        name="role_update",
    ),
    path("role_delete/<int:id>/", role_delete, name="role_delete"),
    path(
        "header-form/",
        HeaderForm.as_view(template_name="header_form.html"),
        name="header-form",
    ),
    path("inedx/", index, name="index"),
    path("dashboard/", dashboard_crm, name="dashboard-crm"),
    path("api/product", include(router.urls)),
    path("api/user/register/", UserRegisterView.as_view(), name="user_register"),
    path("api/activation/", AccountActivationView.as_view(), name="account_activation"),
    path("api/login/", Login.as_view(), name="login"),
    path("api/user/profile/", UserDetailAPIView.as_view(), name="profile"),
    path("api/change-password/", ChangePasswordView.as_view(), name="change_password"),
    path("api/forgot-password/", ForgotPasswordView.as_view(), name="forgot_password"),
    path(
        "api/reset-password/<str:uidb64>/<str:token>/",
        ResetPasswordView.as_view(),
        name="reset_password",
    ),
    path("api/change-email/", ChangeEmailView.as_view(), name="change_email"),
    path(
        "api/change-email/verify/",
        ChangeEmailVerifyView.as_view(),
        name="change_email_verify",
    ),
    path(
        "api/employee/register/",
        EmployeeRegistrationAPIView.as_view(),
        name="employee_register",
    ),
    path(
        "api/employee/profile/",
        EmployeeProfileAPiView.as_view(),
        name="employee_profile",
    ),
    path(
        "api/employee/login/",
        EmployeeLoginApiView.as_view(),
        name="employee_login",
    ),
    path(
        "api/employee/login/",
        EmployeeLoginApiView.as_view(),
        name="employee_login",
    ),
    path("api/employee/list/", EmployeeListView.as_view(), name="employee_list"),
    # path("api/session/", CreateSessionAPIView.as_view(), name="employee_list"),
    path("api/", getRoutes),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# def create_outer_repeater(request):
#     if request.method == 'POST':
#         outer_form = SessionDateForm(request.POST)
#         inner_formset = SessionScheduleFormset(request.POST)

#         if outer_form.is_valid() and inner_formset.is_valid():
#             start_date = outer_form.cleaned_data['start_date']
#             end_date = outer_form.cleaned_data['end_date']

#             session_date_instance = outer_form.save()
#             current_date = start_date
#             while current_date <= end_date:
#                 for form in inner_formset:
#                     start_time = form.cleaned_data['start_time']
#                     end_time = form.cleaned_data['end_time']
#                     session =SessionSchedule.objects.create(session_date = session_date_instance,start_time=start_time,end_time=end_time)
#                     session.save()
#                 current_date += timedelta(days=1)
#             return HttpResponse('Data saved successfully.')
#     else:
#         outer_form = SessionDateForm()
#         inner_formset = SessionScheduleFormset()
#     return render(request, 'Session/session.html', {'outer_form': outer_form, 'inner_formset': inner_formset})
