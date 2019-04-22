# Generated by Django 2.2 on 2019-04-20 19:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0009_auto_20190419_1931'),
    ]

    operations = [
        migrations.CreateModel(
            name='TemplateParentModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=60)),
                ('product_code', models.CharField(max_length=60)),
                ('purchase_price', models.CharField(max_length=50)),
                ('sale_price', models.CharField(max_length=50)),
                ('off_price', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterField(
            model_name='brandmodel',
            name='icon',
            field=models.ImageField(default='brand_image/Blank-avatar.png', upload_to='brand_image/'),
        ),
        migrations.CreateModel(
            name='TemplateSpecificationChild',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('specification_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='Backend.ProductSpecificationModel')),
                ('template', models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='Backend.TemplateParentModel')),
            ],
        ),
        migrations.CreateModel(
            name='TemplateSizeChildModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('size_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='Backend.ProductSizeModel')),
                ('template', models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='Backend.TemplateParentModel')),
            ],
        ),
        migrations.AddField(
            model_name='templateparentmodel',
            name='brand',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='Backend.BrandModel'),
        ),
        migrations.AddField(
            model_name='templateparentmodel',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='Backend.CategoryModel'),
        ),
        migrations.AddField(
            model_name='templateparentmodel',
            name='product_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='Backend.ProductTypeModel'),
        ),
        migrations.AddField(
            model_name='templateparentmodel',
            name='subcategory',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='Backend.SubcategoryModel'),
        ),
        migrations.CreateModel(
            name='TemplateMetarialChildModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('metarial_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='Backend.ProductMetarial')),
                ('template', models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='Backend.TemplateParentModel')),
            ],
        ),
    ]
