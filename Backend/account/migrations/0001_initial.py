# Generated by Django 5.0.3 on 2024-04-23 09:55

import django.contrib.auth.models
import django.db.models.deletion
import django.utils.timezone
import location_field.models.plain
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('mobile_number', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.TextField()),
                ('logo', models.FileField(upload_to='logo/')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('emirates', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=100)),
                ('google_map', location_field.models.plain.PlainLocationField(max_length=63)),
            ],
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(choices=[('/product/product/', 'product')], max_length=150, null=True, verbose_name='Page Name')),
                ('name', models.CharField(choices=[('product Report', '/product/product-report/')], max_length=50, null=True, verbose_name='Page URL')),
                ('created_on', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PaymentMode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('wallet_id', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('Active', 'Active'), ('Disabled', 'Disabled')], default='Active', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('stock', models.IntegerField()),
                ('image', models.ImageField(upload_to='products/')),
                ('vat', models.DecimalField(decimal_places=2, max_digits=5)),
                ('description', models.TextField()),
                ('is_sale', models.BooleanField(default=False)),
                ('is_rent', models.BooleanField(default=True)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('vat', models.DecimalField(decimal_places=2, max_digits=5)),
                ('description', models.TextField()),
                ('image1', models.FileField(upload_to='session/')),
                ('image2', models.FileField(blank=True, null=True, upload_to='session/')),
                ('session_type', models.CharField(choices=[('hour', 'Hourly'), ('month', 'Monthly')], max_length=10)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Session',
                'verbose_name_plural': 'Sessions',
            },
        ),
        migrations.CreateModel(
            name='Tax',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('short_name', models.CharField(max_length=255)),
                ('tax_percentage_checkbox', models.BooleanField(default=False)),
                ('tax_percentage', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('fixed_price_tax_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.CharField(max_length=150)),
                ('transaction_date', models.DateField()),
                ('due_date', models.DateField()),
                ('total', models.DecimalField(decimal_places=2, max_digits=20)),
                ('status', models.CharField(choices=[('Paid', 'Paid'), ('Due', 'Due'), ('Canceled', 'Canceled')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('username', models.CharField(max_length=50, unique=True)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=15)),
                ('email_activation', models.BooleanField(default=False)),
                ('email_verification_code', models.CharField(blank=True, max_length=6, null=True)),
                ('is_user', models.BooleanField(default=False)),
                ('is_employee', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='AccountActivation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activation_code', models.CharField(blank=True, max_length=6, null=True, verbose_name='Activation Code')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Mall',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('picture', models.FileField(upload_to='mall/')),
                ('location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='account.location', verbose_name='Mall Location')),
            ],
        ),
        migrations.CreateModel(
            name='BusinessProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=64, null=True)),
                ('phone_number', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=254)),
                ('currency', models.CharField(max_length=25)),
                ('trn_no', models.CharField(max_length=20)),
                ('tax_reporting_dates', models.CharField(max_length=100)),
                ('license_no', models.CharField(max_length=50)),
                ('expiry', models.DateField()),
                ('operational_hours_start', models.TimeField()),
                ('operational_hours_end', models.TimeField()),
                ('report_generation_start_time', models.TimeField(default='07:00')),
                ('report_generation_end_time', models.TimeField(default='06:59')),
                ('invoice_heading', models.CharField(max_length=255)),
                ('address', models.TextField()),
                ('logo', models.ImageField(upload_to='logo/')),
                ('mall', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.mall')),
                ('select_tax', models.ManyToManyField(default=None, to='account.tax')),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('role_type', models.CharField(choices=[('Employee', 'Employee'), ('Business', 'Business'), ('Group', 'Group'), ('Django Admin', 'Django Admin')], max_length=20)),
                ('business_profile', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.businessprofile')),
                ('modules', models.ManyToManyField(default=None, to='account.module')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_id', models.CharField(max_length=100, unique=True)),
                ('nationality', models.CharField(choices=[('UAE', 'United Arab Emirates'), ('US', 'United States'), ('UK', 'United Kingdom'), ('CA', 'Canada'), ('IN', 'India')], max_length=100)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=10)),
                ('passport_no', models.CharField(max_length=20, unique=True)),
                ('passport_expiration_date', models.DateField()),
                ('emirates_id', models.CharField(max_length=20, unique=True)),
                ('id_expiration_date', models.DateField()),
                ('basic_pay', models.DecimalField(decimal_places=2, max_digits=10)),
                ('house_allowance', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('transportation_allowance', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('commission_percentage', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('joining_date', models.DateField()),
                ('business_profile', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.businessprofile')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('job_role', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.role')),
            ],
        ),
        migrations.CreateModel(
            name='MembershipSession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('day', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('total_sessions', models.PositiveIntegerField(blank=True, null=True)),
                ('session', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='account.session')),
            ],
        ),
        migrations.CreateModel(
            name='HourlySession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hour', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('minute', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('session', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='account.session')),
            ],
        ),
        migrations.CreateModel(
            name='HomeAdvertisement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banner_name', models.CharField(max_length=255)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('is_session', models.BooleanField(default=False)),
                ('is_url', models.BooleanField(default=False)),
                ('url', models.URLField(blank=True, null=True)),
                ('button_name', models.CharField(max_length=200)),
                ('image', models.FileField(blank=True, null=True, upload_to='banner/')),
                ('banner_text1', models.CharField(max_length=200)),
                ('banner_text2', models.CharField(max_length=200)),
                ('banner_text3', models.CharField(max_length=200)),
                ('session', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.session')),
            ],
        ),
        migrations.CreateModel(
            name='SessionDate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('monday', models.BooleanField(default=False)),
                ('tuesday', models.BooleanField(default=False)),
                ('sunday', models.BooleanField(default=False)),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.session')),
            ],
        ),
        migrations.CreateModel(
            name='SessionSchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total_admissions', models.PositiveBigIntegerField()),
                ('session_date', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.sessiondate')),
            ],
        ),
    ]
