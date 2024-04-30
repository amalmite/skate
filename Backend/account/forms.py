from django import forms
from .models import *


class SessionUpdateForm(forms.ModelForm):
    class Meta:
        model = Session
        fields = [
            "name",
            "status",
            "price",
            "vat",
            "description",
            "session_type",
            "image1",
            "image2",
        ]
        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "session name"}
            ),
            "status": forms.Select(
                choices=((True, "Active"), (False, "Inactive")),
                attrs={"class": "form-control"},
            ),
            "price": forms.NumberInput(
                attrs={"class": "form-control", "placeholder": "price"}
            ),
            "vat": forms.NumberInput(
                attrs={"class": "form-control", "placeholder": "vat"}
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control h-px-100",
                    "rows": 3,
                    "placeholder": "Description",
                    "maxlength": 255,
                }
            ),
            "session_type": forms.RadioSelect(),
        }


class SessionForm(forms.ModelForm):
    class Meta:
        model = Session
        fields = [
            "name",
            "price",
            "vat",
            "description",
            "session_type",
            "image1",
            "image2",
        ]
        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "session name"}
            ),
            "price": forms.NumberInput(
                attrs={"class": "form-control", "placeholder": "price"}
            ),
            "vat": forms.NumberInput(
                attrs={"class": "form-control", "placeholder": "vat"}
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control h-px-100",
                    "rows": 3,
                    "placeholder": "Description",
                    "maxlength": 255,
                }
            ),
            "session_type": forms.RadioSelect(),
        }


class HourlySessionForm(forms.ModelForm):
    class Meta:
        model = HourlySession
        fields = ["hour", "minute"]
        widgets = {
            "hour": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "session name",
                    "id": "hour_hour",
                }
            ),
            "minute": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "price",
                    "id": "hour_minute",
                }
            ),
        }


class MembershipSessionForm(forms.ModelForm):
    class Meta:
        model = MembershipSession
        fields = ["month", "day", "total_sessions"]
        widgets = {
            "month": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Month",
                    "id": "member_month",
                }
            ),
            "day": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Day",
                    "id": "member_day",
                }
            ),
            "total_sessions": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Total Session",
                    "id": "member_total",
                }
            ),
        }


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "code", "price", "description", "image", "vat", "stock"]
        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "session name"}
            ),
            "code": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "code"}
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control h-px-100",
                    "rows": 3,
                    "placeholder": "Description",
                    "maxlength": 255,
                }
            ),
            "price": forms.NumberInput(
                attrs={"class": "form-control", "placeholder": "price"}
            ),
            "vat": forms.NumberInput(
                attrs={"class": "form-control", "placeholder": "vat"}
            ),
            "stock": forms.NumberInput(
                attrs={"class": "form-control", "placeholder": "stock"}
            ),
        }


class ProductUpdateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            "name",
            "code",
            "price",
            "description",
            "image",
            "vat",
            "stock",
            "status",
        ]
        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Product name"}
            ),
            "code": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "code"}
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control h-px-100",
                    "rows": 3,
                    "placeholder": "Description",
                    "maxlength": 255,
                }
            ),
            "price": forms.NumberInput(
                attrs={"class": "form-control", "placeholder": "price"}
            ),
            "vat": forms.NumberInput(
                attrs={"class": "form-control", "placeholder": "vat"}
            ),
            "stock": forms.NumberInput(
                attrs={"class": "form-control", "placeholder": "stock"}
            ),
            "status": forms.Select(
                choices=((True, "Active"), (False, "Inactive")),
                attrs={"class": "form-control"},
            ),
            
        }



class AdminProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["email", "first_name", "last_name", "username", "phone_number"]
        widgets = {
            "first_name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "First Name"}
            ),
            "last_name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Last Name"}
            ),
            "username": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Username"}
            ),
            "email": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Email"}
            ),
            "phone_number": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Phone"}
            ),
        }


class CompanyGroupForm(forms.ModelForm):
    class Meta:
        model = CompanyGroup
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Name"}
            ),
            "email": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Email"}
            ),
            "mobile_number": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Mobile Number"}
            ),
            "address": forms.Textarea(
                attrs={
                    "class": "form-control h-px-100",
                    "rows": "3",
                    "placeholder": "Address",
                }
            ),
        }


class TaxForm(forms.ModelForm):
    class Meta:
        model = Tax
        fields = [
            "full_name",
            "short_name",
            "tax_percentage",
            "fixed_price_tax_amount",
            "status",
        ]
        widgets = {
            "full_name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Full Name"}
            ),
            "short_name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Short Name"}
            ),
            "tax_percentage": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Tax Percentage"}
            ),
            "fixed_price_tax_amount": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Fixed price tax"}
            ),
            "status": forms.Select(
                choices=((True, "Active"), (False, "Inactive")),
                attrs={"class": "form-control"},
            ),
        }


class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ["name", "emirates", "country", "google_map"]
        widgets = {
            "google_map": forms.TextInput(
                attrs={"class": "location_field" "form-control", "placeholder": "Map"}
            ),
            "name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Name"}
            ),
            "emirates": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Emirates"}
            ),
            "country": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Country"}
            ),
        }


class MallForm(forms.ModelForm):
    class Meta:
        model = Mall
        fields = ["name", "location", "image"]
        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Name"}
            ),
            "location": forms.Select(
                attrs={"class": "form-control", "placeholder": "Location"}
            ),
        }


class BusinessProfileForm(forms.ModelForm):
    class Meta:
        model = BusinessProfile
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Name"}
            ),
            "mall": forms.Select(attrs={"class": "form-control"}),
            "select_tax": forms.SelectMultiple(attrs={"class": "form-control h-100"}),
            "company_group": forms.Select(attrs={"class": "form-control"}),
            "phone_number": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Phone Number"}
            ),
            "email": forms.EmailInput(
                attrs={"class": "form-control", "placeholder": "Email"}
            ),
            "currency": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Currency"}
            ),
            "trn_no": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "TRN No"}
            ),
            "tax_reporting_dates": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Tax Reporting Dates",
                    "type": "date",
                }
            ),
            "license_no": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "License No"}
            ),
            "expiry": forms.DateInput(
                attrs={"class": "form-control", "placeholder": "Expiry", "type": "date"}
            ),
            "operational_hours_start": forms.TimeInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Operational Hours Start",
                    "type": "time",
                }
            ),
            "operational_hours_end": forms.TimeInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Operational Hours End",
                    "type": "time",
                }
            ),
            "report_generation_start_time": forms.TimeInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Report Generation Start Time",
                    "type": "time",
                }
            ),
            "report_generation_end_time": forms.TimeInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Report Generation End Time",
                    "type": "time",
                }
            ),
            "invoice_heading": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Invoice Heading"}
            ),
            "address": forms.Textarea(
                attrs={
                    "class": "form-control h-px-100",
                    "rows": 3,
                    "placeholder": "Address",
                }
            ),
            "logo": forms.FileInput(attrs={"class": "form-control-file"}),
            "status": forms.Select(
                attrs={"class": "form-control"},
                choices=((True, "Active"), (False, "Inactive")),
            ),
        }


class ModuleForm(forms.ModelForm):
    class Meta:
        model = Module
        fields = '__all__'
        widgets = {
            "name": forms.Select(
                attrs={"class": "form-control", "placeholder": "Page Name"}
            ),
            "url": forms.Select(
                attrs={"class": "form-control", "placeholder": "Page URL"}
            ),
        }

class RoleForm(forms.ModelForm):
    class Meta:
        model = Role
        fields = '__all__'
        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Role Name"}
            ),
            "role_type": forms.Select(
                attrs={"class": "form-control"}
            ),
            "business_profile": forms.Select(
                attrs={"class": "form-control"}
            ),
            "modules": forms.SelectMultiple(attrs={"class": "form-control h-100"})

        }

class SessionScheduleForm(forms.ModelForm):
    class Meta:
        model = SessionSchedule
        fields = ['start_time','end_time']


class SessionDateForm(forms.ModelForm):

    class Meta:
        model = SessionDate
        fields = ['session', 'start_date', 'end_date']
        
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }
