from django.db import migrations

def add_categories(apps, schema_editor):
    Category = apps.get_model('api', 'Category')
    Category.objects.create(name='Categoria 1', description='Descrição da Categoria 1')
    Category.objects.create(name='Categoria 2', description='Descrição da Categoria 2')

class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_categories),
    ]
