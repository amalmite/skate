from django.http import HttpRequest
from django.shortcuts import render, HttpResponse
from rest_framework.views import APIView
from rest_framework import generics

from rest_framework.response import Response
from rest_framework import status, permissions
from .serializers import *
from .models import *
from .forms import *
from django.core.mail import send_mail
from rest_framework.serializers import ValidationError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from random import randint
from rest_framework_simplejwt.tokens import RefreshToken
from icerink.settings import ALLOWED_HOSTS
from django.contrib import messages

from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate, login, logout

from django.shortcuts import redirect

from django.views.generic import TemplateView
from web_project import TemplateLayout
from datetime import date
from django.shortcuts import redirect
from django.contrib import messages
from django.views.generic import TemplateView
from web_project import TemplateLayout
from web_project.template_helpers.theme import TemplateHelper

from django.shortcuts import render, redirect, get_object_or_404


class AdminLoginView(TemplateView):
    def get_context_data(self, **kwargs):
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))

        context.update(
            {
                "layout_path": TemplateHelper.set_layout("layout_blank.html", context),
            }
        )

        return context

    def post(self, request):
        username = request.POST.get("email-username")
        password = request.POST.get("password")
        if not (username and password):
            messages.error(request, "Please enter your username and password.")
            return redirect("admin_login")

        user = self.get_user(username)
        if user is None:
            messages.error(request, "Invalid username or password.")
            return redirect("admin_login")
        authenticated_user = authenticate(request, email=user.email, password=password)
        if authenticated_user is not None:
            login(request, authenticated_user)
            return redirect("admin_home")
        else:
            messages.error(request, "Invalid username or password")
            return redirect("admin_login")

    def get_user(self, username):
        if "@" in username:
            user = User.objects.filter(email=username).first()
        else:
            user = User.objects.filter(username=username).first()
        return user


def admin_logout(request):
    logout(request)
    messages.success(request, "Logout Successfully")
    return redirect("admin_login")


class SessionCreateView(TemplateView):

    def get_context_data(self, **kwargs):
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        session_form = SessionForm()
        hourly_session_form = HourlySessionForm()
        membership_session_form = MembershipSessionForm()
        context["session_form"] = session_form
        context["hourly_session_form"] = hourly_session_form
        context["membership_session_form"] = membership_session_form
        return context

    def post(self, request, *args, **kwargs):
        session_form = SessionForm(request.POST, request.FILES)
        hourly_session_form = HourlySessionForm(request.POST)
        membership_session_form = MembershipSessionForm(request.POST)

        if session_form.is_valid():
            session = session_form.save(commit=False)
            session_type = session_form.cleaned_data["session_type"]
            session.save()

            if session_type == "hour":
                if hourly_session_form.is_valid():
                    hour_session = hourly_session_form.save(commit=False)
                    hour_session.session = session
                    hour_session.save()
                    messages.success(request, "Hourly session added successfully.")
                    return redirect("session_list")
            elif session_type == "month":
                if membership_session_form.is_valid():
                    membership_session = membership_session_form.save(commit=False)
                    membership_session.session = session
                    membership_session.save()
                    messages.success(request, "Membsership session added successfully.")
                    return redirect("session_list")
            else:
                messages.error(request, "Session creation failed.Enter valid data")
                return redirect("session_create")
        else:
            messages.error(request, "Session creation failed.Enter valid data")
            return redirect("session_create")


class SessionListView(TemplateView):

    def get_context_data(self, **kwargs):
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        sessions = self.get_total_sessions()
        context.update(
            {
                "sessions": sessions,
                "session_count": sessions.count(),
                "membership_session_count": self.get_total_membership_sessions(),
                "hour_session_count": self.get_total_hourly_sessions(),
                "canceled_session_count": self.get_total_canceled(),
            }
        )
        print("status", sessions.values_list("status"))
        return context

    def get_total_sessions(self):
        return Session.objects.all().order_by("id")

    def get_total_hourly_sessions(self):
        return Session.objects.filter(session_type="hour").count()

    def get_total_membership_sessions(self):
        return Session.objects.filter(session_type="month").count()

    def get_total_canceled(self):
        return Session.objects.filter(status=False).count()


class SessionUpdateView(TemplateView):
    def get_context_data(self, id, **kwargs):
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        session = get_object_or_404(Session, pk=id)
        session_form = SessionUpdateForm(instance=session)
        if session.session_type == "hour":
            hourly_session_form = HourlySessionForm(
                instance=session.hourlysession or None
            )
            membership_session_form = MembershipSessionForm()
        elif session.session_type == "month":
            hourly_session_form = HourlySessionForm()
            membership_session_form = MembershipSessionForm(
                instance=session.membershipsession or None
            )
        context["session_form"] = session_form
        context["hourly_session_form"] = hourly_session_form
        context["membership_session_form"] = membership_session_form
        return context

    def post(self, request, id, *args, **kwargs):
        session = get_object_or_404(Session, pk=id)
        session_form = SessionUpdateForm(request.POST, request.FILES, instance=session)
        if session.session_type == "hour":
            hourly_session_form = HourlySessionForm(
                request.POST, instance=session.hourlysession or None
            )
            membership_session_form = MembershipSessionForm()
        elif session.session_type == "month":
            hourly_session_form = HourlySessionForm()
            membership_session_form = MembershipSessionForm(
                request.POST, instance=session.membershipsession or None
            )

        if session_form.is_valid():
            session = session_form.save(commit=False)
            session.save()
            if session.session_type == "hour":
                if hourly_session_form.is_valid():
                    hourly_session = hourly_session_form.save(commit=False)
                    hourly_session.save()
            elif session.session_type == "month":
                if membership_session_form.is_valid():
                    membership_session = membership_session_form.save(commit=False)
                    membership_session.save()
            messages.success(request, "Session updated successfully.")
            return redirect("session_list")
        else:
            messages.error(request, "Session updated failed . Enter valid data")
            return redirect("session_update", id=id)


class ProductCreateView(TemplateView):

    def get_context_data(self, **kwargs):
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        product_form = ProductForm()
        context["product_form"] = product_form
        return context

    def post(self, request, *args, **kwargs):
        product_form = ProductForm(request.POST, request.FILES)
        if product_form.is_valid():
            product_form.save()
            messages.success(request, "Product added successfully.")

            return redirect("product_list")
        else:
            messages.error(request, "Failed to add product. Please enter valid data.")
            return redirect("product_create")


class ProductListView(TemplateView):

    def get_context_data(self, **kwargs):
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        products = self.get_total_products()
        context.update(
            {
                "products": products,
                "product_count": products.count(),
                "available_products": self.get_total_available_products(),
                "canceled_products": self.get_total_canceled(),
                "rental_products": self.get_total_rent(),
            }
        )
        return context

    def get_total_products(self):
        return Product.objects.all().order_by("id")

    def get_total_available_products(self):
        return Product.objects.filter(status=True).count()

    def get_total_canceled(self):
        return Product.objects.filter(status=False).count()

    def get_total_rent(self):
        return Product.objects.filter(is_rent=True).count()


class ProductUpdateView(TemplateView):

    def get_context_data(self, id, **kwargs):
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        product = get_object_or_404(Product, id=id)
        product_form = ProductUpdateForm(instance=product)
        context["product_form"] = product_form
        return context

    def post(self, request, id, *args, **kwargs):
        product = get_object_or_404(Product, id=id)

        product_form = ProductUpdateForm(request.POST, request.FILES, instance=product)
        if product_form.is_valid():
            product_form.save()
            messages.success(request, "Product updated successfully.")

            return redirect("product_list")
        else:
            messages.error(
                request, "Failed to update product. Please enter valid data."
            )
            return redirect("product_update", id=id)


class AdminDashboard(TemplateView):
    def get_context_data(self, **kwargs):
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        return context

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect("admin_login")
        return super().dispatch(request, *args, **kwargs)


class AdminProfileView(TemplateView):
    def get_context_data(self, **kwargs):
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        context.update(
            {
                "get_profile": self.get_profile_data(),
                "get_company": self.get_company(),
            }
        )
        return context

    def get_profile_data(self):
        return User.objects.filter(id=self.request.user.id).first()

    def get_company(self):
        return CompanyGroup.objects.all()


class AdminProfileUpdateView(TemplateView):
    def get_context_data(self, **kwargs):
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        user = get_object_or_404(User, pk=self.request.user.id)
        admin_form = AdminProfileForm(instance=user)
        context["admin_form"] = admin_form
        return context

    def post(self, request, *args, **kwargs):
        user = get_object_or_404(User, pk=self.request.user.id)
        admin_form = AdminProfileForm(request.POST, instance=user)
        if admin_form.is_valid():
            user = admin_form.save(commit=False)
            user.save()
            messages.success(request, "Profile updated successfully.")
            return redirect("admin_profile")
        else:
            for field, errors in admin_form.errors.items():
                for error in errors:
                    messages.error(request, f"Error in {field}: {error}")
            return redirect("admin_update")


class CompanyGroupCreationView(TemplateView):
    def get_context_data(self, **kwargs):
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        company_form = CompanyGroupForm()
        context["company_form"] = company_form
        return context

    def post(self, request, *args, **kwargs):
        company_form = CompanyGroupForm(request.POST, request.FILES)
        if company_form.is_valid():
            company = company_form.save()
            messages.success(request, "Company added successfully.")
            return redirect("company_detail", id=company.id)
        else:
            messages.error(request, "Failed to add product. Please enter valid data.")
            return redirect("company_create")


class CompanyGroupUpdateView(TemplateView):
    def get_context_data(self, id, **kwargs):
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        company = get_object_or_404(CompanyGroup, pk=id)
        company_form = CompanyGroupForm(instance=company)
        context["company_form"] = company_form
        return context

    def post(self, request, id, *args, **kwargs):
        company = get_object_or_404(CompanyGroup, id=id)

        company_form = CompanyGroupForm(request.POST, request.FILES, instance=company)
        if company_form.is_valid():
            company = company_form.save()
            messages.success(request, "Company updated successfully.")
            return redirect("company_detail", id=company.id)
        else:
            messages.error(
                request, "Failed to update product. Please enter valid data."
            )
            return redirect("company_update", id=id)


class CompanyDetailView(TemplateView):
    def get_context_data(self, id, **kwargs):
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        company = get_object_or_404(CompanyGroup, id=id)
        context["company"] = company
        return context


class TaxCreateView(TemplateView):
    def get_context_data(self, **kwargs):
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        tax_form = TaxForm()
        context["tax_form"] = tax_form
        return context

    def post(self, request, *args, **kwargs):
        tax_form = TaxForm(request.POST)
        if tax_form.is_valid():
            tax_form.save()
            messages.success(request, "Tax added successfully.")
            return redirect("tax_list")
        else:
            for field, errors in tax_form.errors.items():
                for error in errors:
                    messages.error(request, f"Error in {field}: {error}")
            return redirect("tax_create")


class TaxListView(TemplateView):
    def get_context_data(self, **kwargs):
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        tax = self.get_total_tax()
        context.update({"tax": tax})
        return context

    def get_total_tax(self):
        return Tax.objects.all().order_by("id")


class TaxUpdateView(TemplateView):
    def get_context_data(self, id, **kwargs):
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        tax = get_object_or_404(Tax, pk=id)
        tax_form = TaxForm(instance=tax)
        context["tax_form"] = tax_form
        return context

    def post(self, request, id, *args, **kwargs):
        tax = get_object_or_404(Tax, pk=id)
        tax_form = TaxForm(request.POST, instance=tax)
        if tax_form.is_valid():
            tax = tax_form.save(commit=False)
            tax.save()
            messages.success(request, "Profile updated successfully.")
            return redirect("tax_list")
        else:
            for field, errors in tax_form.errors.items():
                for error in errors:
                    messages.error(request, f"Error in {field}: {error}")
            return redirect("tax_update")


class LocationcreateView(TemplateView):
    def get_context_data(self, **kwargs):
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        location_form = LocationForm()
        context["location_form"] = location_form
        return context

    def post(self, request, *args, **kwargs):
        location_form = LocationForm(request.POST)
        if location_form.is_valid():
            location_form.save()
            messages.success(request, "Mall added successfully.")
            return redirect("location_list")
        else:
            for field, errors in location_form.errors.items():
                for error in errors:
                    messages.error(request, f"Error in {field}: {error}")
            return redirect("mall_create")


class LocationListView(TemplateView):
    def get_context_data(self, **kwargs):
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        location = self.get_location()
        context.update({"locations": location})
        return context

    def get_location(self):
        return Location.objects.all().order_by("id")


class LocationUpdateView(TemplateView):
    def get_context_data(self, id, **kwargs):
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        location = get_object_or_404(Location, pk=id)
        location_form = LocationForm(instance=location)
        context["location_form"] = location_form
        return context

    def post(self, request, id, *args, **kwargs):
        location = get_object_or_404(Location, pk=id)
        location_form = LocationForm(request.POST, instance=location)
        if location_form.is_valid():
            location = location_form.save(commit=False)
            location.save()
            messages.success(request, "Location updated successfully.")
            return redirect("location_list")
        else:
            for field, errors in location_form.errors.items():
                for error in errors:
                    messages.error(request, f"Error in {field}: {error}")
            return redirect("location_update", id=id)


class MallcreateView(TemplateView):
    def get_context_data(self, **kwargs):
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        mall_form = MallForm()
        context["mall_form"] = mall_form
        return context

    def post(self, request, *args, **kwargs):
        mall_form = MallForm(request.POST, request.FILES)
        if mall_form.is_valid():
            mall_form.save()
            messages.success(request, "Mall added successfully.")
            return redirect("mall_list")
        else:
            for field, errors in mall_form.errors.items():
                for error in errors:
                    messages.error(request, f"Error in {field}: {error}")
            return redirect("mall_create")


class MallListView(TemplateView):
    def get_context_data(self, **kwargs):
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        context.update(
            {
                "malls": self.get_mall(),
            }
        )
        return context

    def get_mall(self):
        return Mall.objects.all()


class MallUpdateView(TemplateView):
    def get_context_data(self, id, **kwargs):
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        mall = get_object_or_404(Mall, pk=id)
        mall_form = MallForm(instance=mall)
        context["mall_form"] = mall_form
        return context

    def post(self, request, id, *args, **kwargs):
        mall = get_object_or_404(Mall, pk=id)
        mall_form = MallForm(request.POST, request.FILES, instance=mall)
        if mall_form.is_valid():
            location = mall_form.save(commit=False)
            location.save()
            messages.success(request, "Mall updated successfully.")
            return redirect("mall_list")
        else:
            for field, errors in mall_form.errors.items():
                for error in errors:
                    messages.error(request, f"Error in {field}: {error}")
            return redirect("mall_update", id=id)


class BusinessProfileCreateView(TemplateView):
    def get_context_data(self, **kwargs):
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        form = BusinessProfileForm()
        context["form"] = form
        return context

    def post(self, request, *args, **kwargs):
        form = BusinessProfileForm(request.POST, request.FILES)
        if form.is_valid():
            business = form.save(commit=False)
            business.save()
            messages.success(request, "Business added successfully.")
            return redirect("business_profile_list")
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"Error in {field}: {error}")
            return redirect("business_profile_create")


class BusinessProfileListView(TemplateView):
    def get_context_data(self, **kwargs):
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        context.update(
            {
                "business_profiles": self.get_business_profiles(),
            }
        )
        return context

    def get_business_profiles(self):
        return BusinessProfile.objects.all()


class BusinessProfileUpdateView(TemplateView):
    def get_context_data(self, id, **kwargs):
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        business = get_object_or_404(BusinessProfile, id=id)
        form = BusinessProfileForm(instance=business)
        context["form"] = form
        return context

    def post(self, request, id, *args, **kwargs):
        business = get_object_or_404(BusinessProfile, id=id)
        form = BusinessProfileForm(request.POST, request.FILES, instance=business)
        if form.is_valid():
            form.save()
            messages.success(request, "Business updates successfully.")
            return redirect("business_profile_list")
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"Error in {field}: {error}")
            return redirect("business_profile_update", id=id)



class ModuleCreateListView(TemplateView):
    def get_context_data(self, **kwargs):
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        form = ModuleForm()
        context['form'] = form
        context.update(
                    {
                "modules": self.get_module(),
            }
        )
        return context
    
    def post(self, request, *args, **kwargs):
        form = ModuleForm(request.POST)
        if form.is_valid():
            module = form.save(commit=False)
            module.save()
            messages.success(request, "Module added successfully.")
            return redirect("module_list")
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"Error in {field}: {error}")
            return redirect("module_create")
    

    def get_module(self):
        return Module.objects.all()
    
class ModuleUpdateView(TemplateView):
    def get_context_data(self,id, **kwargs):
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        module = get_object_or_404(Module,id = id)
        form = ModuleForm(instance=module)
        context['form'] = form
        context['module'] = module

        return context
    
    def post(self, request, id, *args, **kwargs):
        module = get_object_or_404(Module,id = id)
        form = ModuleForm(request.POST,instance=module)
        if form.is_valid():
            form.save()
            messages.success(request, "Module updated successfully.")
            return redirect("module_list")
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"Error in {field}: {error}")
            return redirect("module_update",id=id)
        
        
def module_delete(request, id, *args, **kwargs):
    module = get_object_or_404(Module, id=id)
    module.delete()
    messages.success(request, "Module deleted successfully.")
    return redirect("module_list")

class RoleCreateListView(TemplateView):
    def get_context_data(self, **kwargs):
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        form = RoleForm()
        context['form'] = form
        context.update(
                    {
                "roles": self.get_role(),
            }
        )
        return context
    
    def post(self, request, *args, **kwargs):
        form = RoleForm(request.POST)
        if form.is_valid():
            role = form.save(commit=False)
            role.save()
            modules = form.cleaned_data.get("modules")
            for module_name in modules:
                try:
                    module = Module.objects.filter(name=module_name).first()
                    role.modules.add(module)
                except Module.DoesNotExist:
                    messages.error(request, f"No module with name '{module_name}' exists.")
                except Module.MultipleObjectsReturned:
                    messages.warning(request, f"Multiple modules found with name '{module_name}'. Please select the desired one.")
            messages.success(request, "Role added successfully.")
            return redirect("role_list")
        else:
            return redirect("role_create")


    def get_role(self):
        return Role.objects.all()

class RoleUpdateView(TemplateView):
    def get_context_data(self,id, **kwargs):
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        role = get_object_or_404(Role ,id =id)
        form = RoleForm(instance=role)
        context['form'] = form
        context['role'] = role
        return context
    
    def post(self, request, id ,*args, **kwargs):
        role = get_object_or_404(Role ,id =id)
        form = RoleForm(request.POST,instance=role)
        if form.is_valid():
            role = form.save(commit=False)
            role.save()
            modules = form.cleaned_data.get("modules")
                
            for module_name in modules:
                try:
                    module = Module.objects.filter(name=module_name).first()
                    if module not in role.modules.all():
                        role.modules.add(module)
                    else:
                        messages.warning(request, f"Module '{module_name}' is already associated with the role.")
                except Module.DoesNotExist:
                    messages.error(request, f"No module with name '{module_name}' exists.")
                except Module.MultipleObjectsReturned:
                    messages.warning(request, f"Multiple modules found with name '{module_name}'. Please select the desired one.")
            role.save()
            messages.success(request, "Role updated successfully.")
            return redirect("role_list")
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"Error in {field}: {error}")
            return redirect("role_update",id=id)

def role_delete(request, id, *args, **kwargs):
    module = get_object_or_404(Role, id=id)
    module.delete()
    messages.success(request, "Role deleted successfully.")
    return redirect("role_list")




class tryview(TemplateView):
    def get_context_data(self, **kwargs):
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        return context


class HeaderForm(TemplateView):
    def get_context_data(self, **kwargs):
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        return context


class SessionScheduleView(TemplateView):
    def get_context_data(self, **kwargs):
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        return context

from datetime import timedelta

def create_outer_repeater(request):
    if request.method == 'POST':
        outer_form = SessionDateForm(request.POST)

        if outer_form.is_valid():
            start_date = outer_form.cleaned_data['start_date']
            end_date = outer_form.cleaned_data['end_date']

            session_date_instance = outer_form.save()
            current_date = start_date
            while current_date <= end_date:
                for form in outer_form:
                    start_time = form.cleaned_data.get('start_time')
                    end_time = form.cleaned_data.get('end_time')
                    print(start_date,end_time)
                    session =SessionSchedule.objects.create(session_date = session_date_instance,start_time=start_time,end_time=end_time)
                    session.save()
                current_date += timedelta(days=1)
            return HttpResponse('Data saved successfully.')
    else:
        outer_form = SessionDateForm()
    return render(request, 'Session/session.html', {'outer_form': outer_form})



# def create_session(request):
#     if request.method == 'POST':

#         session_date_form = SessionDateForm(request.POST)
#         session_schedule_form = SessionScheduleForm(request.POST)

#         if form.is_valid():
#             start_time = form.cleaned_data['start_time']

#             end_time = form.cleaned_data['end_time']
#             session_date = form.save()
#             current_date = session_date.start_date
#             while current_date <= session_date.end_date:
#                 SessionSchedule.objects.create(session_date=session_date,start_time=start_time,end_time=end_time)
#                 current_date += timedelta(days=1)
#             return redirect('list_page')
#     else:
#         form = SessionDateForm()
#     return render(request, 'Session/session.html', {'form': form})
# def create_outer_repeater(request):
#     if request.method == 'POST':
#         outer_form = OuterRepeaterForm(request.POST)
#         inner_formset = InnerRepeaterFormset(request.POST)

#         if outer_form.is_valid() and inner_formset.is_valid():
#             outer_instance = outer_form.save()
#             for form in inner_formset:
#                 if form.is_valid():
#                     data = form.cleaned_data.get('inner_text_input') 
#                     print('data',data)
#                     inner_instance = form.save(commit=False)
#                     inner_instance.outer_repeater = outer_instance  
#                     inner_instance.save()
#             return HttpResponse('Data saved successfully.')
#     else:
#         outer_form = OuterRepeaterForm()
#         inner_formset = InnerRepeaterFormset()

#     return render(request, 'Session/session.html', {'outer_form': outer_form, 'inner_formset': inner_formset})


# def create_outer_repeater(request):
#     if request.method == 'POST':
#         outer_form = OuterRepeaterForm(request.POST)
#         inner_formset = InnerRepeaterFormset(request.POST)

#         if outer_form.is_valid() and inner_formset.is_valid():
#             outer_instance = outer_form.save()
#             for form in inner_formset:
#                 if form.is_valid():
#                     data = form.cleaned_data.get('inner_text_input') 
#                     print('data',data)
#                     inner_instance = form.save(commit=False)
#                     inner_instance.outer_repeater = outer_instance  
#                     inner_instance.save()
#             return HttpResponse('Data saved successfully.')
#     else:
#         outer_form = OuterRepeaterForm()
#         inner_formset = InnerRepeaterFormset()

#     return render(request, 'Session/session.html', {'outer_form': outer_form, 'inner_formset': inner_formset})

def index(request):
    return HttpResponse("hello")


def dashboard_crm(request):
    return HttpResponse("hello")

from datetime import datetime


def parse_query_dict(data):
    parsed_dict = {}
    for key, value in data.items():
        if key not in ['csrfmiddlewaretoken', 'submitButton']:
            current_dict = parsed_dict
            keys = key.split('[')
            for i, k in enumerate(keys):
                if k.endswith(']'):
                    k = k[:-1]
                if k not in current_dict:
                    current_dict[k] = {}
                if i < len(keys) - 1:
                    current_dict = current_dict[k]
                else:
                    current_dict[k] = value[0] if isinstance(value, list) else value
    return parsed_dict

class SessionView(TemplateView):
    def get_context_data(self, **kwargs):
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        time_form = SessionScheduleForm()
        date_form = SessionDateForm()
        context['time_form']=time_form
        context['date_form'] = date_form
        return context
    
    def post(self, request):
        data = request.POST
        parsed_dict = parse_query_dict(data)
        for outer_key, outer_value in parsed_dict.items():
            for inner_key, inner_value in outer_value.items():
                print(inner_value,'ppp')
                start_date = inner_value['start_date']
                end_date = inner_value['end_date']
                end_date = inner_value.get('end_date', None)
                monday = inner_value.get('monday', None)
                tuesday = inner_value.get('tuesday', None)
                wednesday = inner_value.get('wednesday', None)
                thursday = inner_value.get('thursday', None)
                friday = inner_value.get('friday', None) 
                saturday = inner_value.get('saturday', None)
                sunday = inner_value.get('sunday', None)
                session_id = inner_value.get('session', None)

                session_instance = get_object_or_404(Session, id=session_id)
                session_date_instance = SessionDate.objects.create(start_date=start_date, end_date=end_date, session=session_instance,
                                                        monday=bool(monday), tuesday=bool(tuesday), wednesday=bool(wednesday), thursday=bool(thursday), friday=bool(friday), saturday=bool(saturday), sunday=bool(sunday)
                )       
                allowed_days = []
                for day in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
                    if getattr(session_date_instance, day):
                        allowed_days.append(day.lower())

                inner_list = inner_value['inner-list']
                current_date = datetime.strptime(session_date_instance.start_date, '%Y-%m-%d')
                end_date = datetime.strptime(session_date_instance.end_date, '%Y-%m-%d')

                while current_date <= end_date:
                    if current_date.strftime('%A').lower() in allowed_days:
                        for inner_list_key, inner_list_value in inner_list.items():
                            start_time = inner_list_value['start_time']
                            end_time = inner_list_value['end_time']
                            price = inner_list_value['price']
                            SessionSchedule.objects.create(
                                        session_date=session_date_instance, start_time=start_time, end_time=end_time,current_date=current_date
                                )
                    current_date += timedelta(days=1)

            return redirect('index')
        return redirect('test')



        # outer_list_keys = [key for key in data.keys() if key.startswith('outer-list')]
        # outer_lists = {key: data[key] for key in outer_list_keys}    

        # for i, (key, value) in enumerate(outer_lists.items()):
        #     session_id =outer_lists.get(f"outer-list[{i}][session]")
        #     start_date = outer_lists.get(f"outer-list[{i}][start_date]")
        #     end_date = outer_lists.get(f"outer-list[{i}][end_date]")    
        #     monday =outer_lists.get(f"outer-list[{i}][monday][]")
        #     tuesday =outer_lists.get(f"outer-list[{i}][tuesday][]")    
        #     wednesday =outer_lists.get(f"outer-list[{i}][wednesday][]")    
        #     thursday =outer_lists.get(f"outer-list[{i}][thursday][]")    
        #     friday =outer_lists.get(f"outer-list[{i}][friday][]")    
        #     saturday =outer_lists.get(f"outer-list[{i}][saturday][]")    
        #     sunday =outer_lists.get(f"outer-list[{i}][sunday][]") 
        #     try: 
        #         session_instance = Session.objects.get(id=session_id)
        #     except Session.DoesNotExist:
        #         print('errorrrrrrrrrrrr')


        #     if start_date and end_date:
        #         session_date = SessionDate.objects.create(session=session_instance,start_date=start_date, end_date=end_date,
        #                                                   monday=bool(monday),tuesday=bool(tuesday),wednesday=bool(wednesday),thursday=bool(thursday),friday=bool(friday),saturday=bool(saturday),sunday=bool(sunday))
        #         allowed_days = []
        #         for day in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
        #             if getattr(session_date, day):
        #                 allowed_days.append(day.lower())
            
                
        #         inner_list_keys = [inner_key for inner_key in data.keys() if f"outer-list[{i}][inner-list]" in inner_key]
        #         inner_lists = {inner_key: data[inner_key] for inner_key in inner_list_keys}
                
        #         current_date = datetime.strptime(session_date.start_date, '%Y-%m-%d')
        #         end_date = datetime.strptime(session_date.end_date, '%Y-%m-%d')


        #         while current_date <= end_date:
        #             if current_date.strftime('%A').lower() in allowed_days:

        #                 for j, (inner_key, inner_value) in enumerate(inner_lists.items()):
        #                     start_time = inner_lists.get(f"outer-list[{i}][inner-list][{j}][start_time]")
        #                     end_time = inner_lists.get(f"outer-list[{i}][inner-list][{j}][end_time]")
        #                     price = inner_lists.get(f"outer-list[{i}][inner-list][{j}][price]")
        #                     total_admissions = inner_lists.get(f"outer-list[{i}][inner-list][{j}][total_admissions]")

                            
        #                     if start_time and end_time:
        #                         SessionSchedule.objects.create(
        #                             start_time=start_time,
        #                             end_time=end_time,
        #                             session_date=session_date,price=price,total_admissions=total_admissions
        #                         )
        #             current_date += timedelta(days=1)
                    
        # return redirect('test')


        

    # def post(self, request):
    #     outer_form = OuterRepeaterForm(request.POST)
        
    #     inner_form = InnerRepeater(request.POST)
    #     print(request.POST)
    #     # if outer_form.is_valid() and inner_form.is_valid():

    #     # for key, value in request.POST.items():
    #     #     if key.startswith('outer-list'):
    #     #         if 'main-input' in key:
    #     #             outer_repeater = OuterRepeater.objects.create(text_input=value)
    #     #             inner_list_prefix = key.replace('maininput-', 'inner-list')
    #     #             inner_list_keys = [k for k in request.POST.keys() if k.startswith(inner_list_prefix)]
    #     #             for inner_key in inner_list_keys:
    #     #                 InnerRepeater.objects.create(outer_repeater=outer_repeater, inner_text_input=request.POST[inner_key])

    #     return redirect('test')



# Employee & Use API


class UserRegisterView(APIView):

    serializer_class = UserRegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.is_user = True
            user.save()
            email_code = AccountActivation(user=user)
            activation_code = email_code.create_confirmation()
            print(activation_code, "code")
            try:
                subject = "Registration OTP"
                message = f"Your OTP for registration is: {activation_code}"
                to_email = user.email
                send_mail(subject, message, None, [to_email])
                return Response({"message": "OTP sent"}, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response(
                    {"message": f"Failed to send OTP: {str(e)}"},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AccountActivationView(APIView):

    serializer_class = AccountActivationSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            activation_code = serializer.validated_data.get("code")
            try:
                email_confirmation = AccountActivation.objects.get(
                    activation_code=activation_code
                )

                if email_confirmation.verify_confirmation(activation_code):

                    return Response(
                        {"message": "Account Activated. Proceed To Log in"},
                        status=status.HTTP_200_OK,
                    )
                else:
                    return Response(
                        {"error": "Invalid confirmation code."},
                        status=status.HTTP_400_BAD_REQUEST,
                    )
            except AccountActivation.DoesNotExist:
                return Response(
                    {"error": "Invalid confirmation code."},
                    status=status.HTTP_400_BAD_REQUEST,
                )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Login(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        serializer = UserDataSerializer(user)
        token = RefreshToken.for_user(user)
        data = serializer.data
        data["tokens"] = {"refresh": str(token), "access": str(token.access_token)}
        return Response(data, status=status.HTTP_200_OK)


class UserDetailAPIView(APIView):

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        try:
            user = self.request.user
            serializer = self.serializer_class(user)
            return Response(serializer.data)
        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def put(self, request, *args, **kwargs):
        try:
            user = self.request.user
            serializer = self.serializer_class(user, data=request.data, partial=True)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            raise ValidationError(serializer.errors)

        except ValidationError as validation_error:
            return Response(
                {"error": "Validation error", "detail": validation_error.detail},
                status=status.HTTP_400_BAD_REQUEST,
            )

        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class ChangePasswordView(APIView):

    serializer_class = ChangePasswordSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        if serializer.is_valid():
            user = request.user
            user.set_password(serializer.validated_data["password"])
            user.save()
            return Response(
                {"message": "Password changed successfully."}, status=status.HTTP_200_OK
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ForgotPasswordView(APIView):
    serializer_class = ForgotPasswordSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data["email"]
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                return Response(
                    {"error": "User with this email does not exist"},
                    status=status.HTTP_404_NOT_FOUND,
                )

            uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
            token = default_token_generator.make_token(user)

            reset_link = f"http://localhost:3000/reset-password/{uidb64}/{token}/"
            subject = "Forgot Password"
            message = f"Click the link to reset your password: {reset_link}"
            to_email = user.email
            try:
                send_mail(subject, message, None, [to_email])
            except Exception as e:
                return Response(
                    {"error": "Failed to send password reset email"},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )
            return Response(
                {"detail": "Password reset email sent successfully"},
                status=status.HTTP_200_OK,
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )


class ResetPasswordView(APIView):
    serializer_class = PasswordResetSerializer

    def post(self, request, uidb64, token, *args, **kwargs):
        try:
            uid = urlsafe_base64_decode(uidb64).decode()
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, User.DoesNotExist):
            user = None
        if user and default_token_generator.check_token(user, token):
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                new_password = serializer.validated_data.get("new_password")
                user.set_password(new_password)
                user.save()
                return Response(
                    {"detail": "Password reset successfully"}, status=status.HTTP_200_OK
                )
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(
                {"detail": "Invalid reset link"}, status=status.HTTP_400_BAD_REQUEST
            )


class ChangeEmailView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ChangeEmailSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            user = request.user
            new_email = serializer.validated_data["email"]

            if new_email != user.email:
                raise ValidationError(
                    "Provided email doesn't match the logged-in user's email."
                )

            code = str(randint(100000, 999999))
            user.email_verification_code = code
            user.save()
            subject = "Confirm Email Change"
            message = f"Your email verification code is: {code}"
            from_email = "Your Email"
            to_email = user.email
            send_mail(subject, message, from_email, [to_email], fail_silently=True)
            return Response(
                {"message": "Email change request sent successfully."},
                status=status.HTTP_200_OK,
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ChangeEmailVerifyView(APIView):

    serializer_class = ChangeEmailVerifySerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            user = request.user
            code = serializer.validated_data["code"]
            new_email = serializer.validated_data["new_email"]

            if user.email_verification_code == code:
                user.email = new_email
                user.email_verification_code = None
                user.save()
                return Response(
                    {"success": "Email changed successfully."},
                    status=status.HTTP_200_OK,
                )
            else:
                return Response(
                    {"error": "Invalid or expired verification code."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Employee registeration
class EmployeeRegistrationAPIView(APIView):

    serializer_class = EmployeeRegistrationSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Registeration Sucessfull"}, status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Employee Profile
class EmployeeProfileAPiView(APIView):

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = EmployeeSerializer

    def get(self, request, *args, **kwargs):
        try:
            employee = Employee.objects.get(user=request.user)
            serializer = self.serializer_class(employee)
            return Response(serializer.data)
        except Employee.DoesNotExist:
            return Response(
                {"error": "Employee does not exist"}, status=status.HTTP_404_NOT_FOUND
            )

    def put(self, request, *args, **kwargs):
        try:
            employee = Employee.objects.get(user=request.user)
        except Employee.DoesNotExist:
            return Response(
                {"error": "Employee does not exist"}, status=status.HTTP_404_NOT_FOUND
            )
        serializer = self.serializer_class(employee, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmployeeLoginApiView(APIView):

    serializer_class = EmployeeLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        serializer = UserDataSerializer(user)
        token = RefreshToken.for_user(user)
        data = serializer.data
        data["tokens"] = {"refresh": str(token), "access": str(token.access_token)}
        return Response(data, status=status.HTTP_200_OK)


class EmployeeListView(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


# class SkatingProductViewSet(viewsets.ModelViewSet):
#     queryset = Product.objects.all()
#     serializer_class = SkatingProductSerializer


from rest_framework.decorators import api_view


@api_view(["GET"])
def getRoutes(request):
    routes = {
        "login": request.build_absolute_uri("/api/login/"),
        "register": request.build_absolute_uri("/api/user/register/"),
        "profile": request.build_absolute_uri("/api/user/profile/"),
    }
    return Response(routes)


# from .serializers import *

# class UserLoginAPIVew(APIView):
#     def post(self, request, *args, **kwargs):
#         serializer = UserLoginSerializer(data=request.data)
#         if serializer.is_valid():
#             email = serializer.validated_data.get("email", None)
#             username = serializer.validated_data.get("username", None)
#             password = serializer.validated_data["password"]

#             custom_token_serializer = MyTokenObtainPairSerializer()

#             if email is not None:
#                 user = authenticate(request, email=email, password=password)
#                 if user is not None:
#                     token = custom_token_serializer.get_token(user)
#                     return Response(
#                         {
#                             "mes": "User Log in Successfully",
#                             "jwt_token": {
#                                 "access": str(token.access_token),
#                                 "refresh": str(token),
#                             },
#                             # "data": UserSerializer(user).data,
#                         },
#                         status=status.HTTP_200_OK,
#                     )
#                 return Response(
#                     {"msg": "User Not Found"}, status=status.HTTP_404_NOT_FOUND
#                 )

#             if username is not None:
#                 user = authenticate(request, username=username, password=password)
#                 if user is not None:
#                     token = custom_token_serializer.get_token(user)

#                     return Response(
#                         {
#                             "mes": "User Log in Successfully",
#                             "jwt_token": {
#                                 "access": str(token.access_token),
#                                 "refresh": str(token),
#                             },
#                             # "data": UserSerializer(user).data,
#                         },
#                         status=status.HTTP_200_OK,
#                     )
#                 # raise AuthenticationFailed("There is no User")
#             return Response(
#                 {"msg": "There is n   o valid Credentials"},
#                 status=status.HTTP_400_BAD_REQUEST,
#             )
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# from datetime import timedelta,datetime

# class CreateSessionAPIView(APIView):
#     def get(self,request):
#         data =SessionScheduling.objects.all()
#         serializers=SessionSchedulingSerializer(data,many=True)
#         return Response(serializers.data)

#     def post(self, request):
#         serializer = SessionSchedulingSerializer(data=request.data)
#         if serializer.is_valid():
#             from_date = serializer.validated_data['from_date']
#             to_date = serializer.validated_data['to_date']
#             start_time = serializer.validated_data['start_time']
#             end_time = serializer.validated_data['end_time']
#             no_of_slot = serializer.validated_data['no_of_slot']
#             delta = timedelta(days=1)
#             current_date = from_date
#             start_datetime = datetime.combine(datetime.today(), start_time)
#             while current_date <= to_date:
#                 for i in range(no_of_slot):
#                     session_start_time = start_datetime + timedelta(hours=i)
#                     session_end_time = session_start_time + timedelta(hours=1)
#                     session = SessionScheduling.objects.create(
#                         from_date=current_date,
#                         to_date=current_date,
#                         start_time=session_start_time.time(),
#                         end_time=session_end_time.time(),
#                     )
#                     session.save()
#                 current_date += delta
#             return Response(status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request):
#         SessionScheduling.objects.all().delete()
#         return Response({"message": "deleted"}, status=status.HTTP_204_NO_CONTENT)
