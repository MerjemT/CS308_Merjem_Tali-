from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True
operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=25)),
                ('name', models.CharField(max_length=25)),
            ],
        ),
        
migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25)),
                ('publisher', models.CharField(max_length=25)),
                ('publication_date', models.DateTimeField(verbose_name='publication date')),
                ('number_of_pages', models.IntegerField()),
                ('authors', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.author')),
            ],
        ),
    ]
