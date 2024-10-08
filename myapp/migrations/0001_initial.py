# Generated by Django 4.1.7 on 2024-08-17 17:58

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('is_active', models.BooleanField(default=True)),
                ('cat_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('url', models.CharField(max_length=100, unique=True)),
                ('image', models.ImageField(upload_to='category/')),
                ('add_date', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='categoryQuiz',
            fields=[
                ('typeCate', models.CharField(choices=[('TEST ONL', 'TEST ONL'), ('CONTEST', 'CONTEST')], default='TEST ONL', max_length=10)),
                ('is_active', models.BooleanField(default=True)),
                ('image', models.ImageField(upload_to='category/')),
                ('cat_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('url', models.CharField(max_length=100, unique=True)),
                ('add_date', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('order', models.PositiveIntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('url', models.SlugField(blank=True, max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Community',
            fields=[
                ('is_active', models.BooleanField(default=True)),
                ('author', models.CharField(max_length=30)),
                ('community_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('url', models.CharField(max_length=100, unique=True)),
                ('cat', models.CharField(choices=[('Khác', 'Khác'), ('Góp Ý', 'Góp Ý'), ('Chia Sẽ', 'Chia Sẽ'), ('Kiến Thức', 'Kiến Thức')], max_length=100)),
                ('image', models.ImageField(upload_to='post/')),
                ('add_date', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('details', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Header',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('title', models.CharField(max_length=100)),
                ('url', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('bio', models.TextField()),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='instructors/')),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True)),
                ('website', models.URLField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('typeP', models.CharField(choices=[('Card', 'Card'), ('App', 'App'), ('Web', 'Web')], max_length=4)),
                ('title', models.CharField(max_length=100)),
                ('url', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('url', models.SlugField(blank=True, max_length=100, unique=True)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('is_active', models.BooleanField(default=True)),
                ('seller', models.CharField(max_length=30)),
                ('store_id', models.AutoField(primary_key=True, serialize=False)),
                ('nameStore', models.CharField(max_length=200)),
                ('numberStore', models.DecimalField(decimal_places=0, default=0, max_digits=10)),
                ('content', models.TextField()),
                ('preview_content', models.CharField(max_length=1000)),
                ('numberPhone_seller', models.DecimalField(decimal_places=0, default=0, max_digits=10)),
                ('link_conection_seller', models.CharField(max_length=100)),
                ('price_000vnd', models.DecimalField(decimal_places=2, max_digits=10)),
                ('url', models.CharField(max_length=100, unique=True)),
                ('add_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.category')),
            ],
        ),
        migrations.CreateModel(
            name='Science',
            fields=[
                ('is_active', models.BooleanField(default=True)),
                ('author', models.CharField(max_length=30)),
                ('science_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('preview_content', models.CharField(max_length=1000)),
                ('url', models.CharField(max_length=100, unique=True)),
                ('image', models.ImageField(upload_to='post/')),
                ('add_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.category')),
            ],
        ),
        migrations.CreateModel(
            name='quizQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('question_text', models.CharField(max_length=200)),
                ('choice1', models.CharField(max_length=200)),
                ('choice2', models.CharField(max_length=200)),
                ('choice3', models.CharField(max_length=200)),
                ('choice4', models.CharField(max_length=200)),
                ('correct_choice', models.IntegerField(choices=[(1, 'Choice 1'), (2, 'Choice 2'), (3, 'Choice 3'), (4, 'Choice 4')])),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.categoryquiz')),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='store/')),
                ('preview_content', models.CharField(default='None', max_length=1000)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.store')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('is_active', models.BooleanField(default=True)),
                ('author', models.CharField(max_length=30)),
                ('post_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('preview_content', models.CharField(max_length=1000)),
                ('url', models.CharField(max_length=100, unique=True)),
                ('image', models.ImageField(upload_to='post/')),
                ('add_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.category')),
            ],
        ),
        migrations.CreateModel(
            name='LessonVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('youtube_link', models.URLField()),
                ('duration', models.DurationField(blank=True, null=True)),
                ('order', models.PositiveIntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('url', models.SlugField(blank=True, max_length=100, unique=True)),
                ('chapter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='myapp.chapter')),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('url', models.SlugField(blank=True, max_length=100, unique=True)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('language', models.CharField(default='Vietnamese', max_length=50)),
                ('duration', models.CharField(max_length=50)),
                ('level', models.CharField(choices=[('beginner', 'Beginner'), ('intermediate', 'Intermediate'), ('advanced', 'Advanced')], max_length=50)),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='course_thumbnails/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('instructors', models.ManyToManyField(related_name='courses', to='myapp.instructor')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='myapp.subject')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('body', models.TextField()),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('object_id', models.PositiveIntegerField(default=None, null=True)),
                ('content_type', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
            ],
        ),
        migrations.AddField(
            model_name='chapter',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chapters', to='myapp.course'),
        ),
        migrations.CreateModel(
            name='AccRoblox5k',
            fields=[
                ('username', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=True)),
                ('store_id', models.AutoField(primary_key=True, serialize=False)),
                ('nameStore', models.CharField(default='MÃ SỐ: A5K-', max_length=200)),
                ('content', models.TextField(default='Đây là Tài Khoản Roblox Bloxfruit 5k')),
                ('preview_content', models.CharField(default='MỤC: RANDOM5K', max_length=1000)),
                ('price_000vnd', models.DecimalField(decimal_places=2, default='5.00', max_digits=10)),
                ('url', models.CharField(max_length=100, unique=True)),
                ('image', models.ImageField(blank=True, default='store/background-playlist_lxw56b', upload_to='store/')),
                ('add_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('cat', models.ForeignKey(default='Acc Roblox 5k', on_delete=django.db.models.deletion.CASCADE, to='myapp.category')),
            ],
        ),
    ]
