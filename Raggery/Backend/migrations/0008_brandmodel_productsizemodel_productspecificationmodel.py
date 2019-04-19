# Generated by Django 2.2 on 2019-04-19 19:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0007_auto_20190417_1554'),
    ]

    operations = [
        migrations.CreateModel(
            name='BrandModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=50)),
                ('phone', models.CharField(max_length=40)),
                ('founded_date', models.DateTimeField()),
                ('type_of_company', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=50)),
                ('icon', models.ImageField(default='brand_folder/None/no-img.jpg', upload_to='brand_folder/%Y/%m/%d/')),
                ('status', models.CharField(max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductSpecificationModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('status', models.CharField(max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='Backend.CategoryModel')),
                ('product_type', models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='Backend.ProductTypeModel')),
                ('subcategory', models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='Backend.SubcategoryModel')),
            ],
        ),
        migrations.CreateModel(
            name='ProductSizeModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('status', models.CharField(max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='Backend.CategoryModel')),
                ('product_type', models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='Backend.ProductTypeModel')),
                ('subcategory', models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='Backend.SubcategoryModel')),
            ],
        ),
    ]