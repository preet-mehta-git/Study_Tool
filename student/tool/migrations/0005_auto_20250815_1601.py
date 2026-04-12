from django.db import migrations

def create_quiz_questions(apps, schema_editor):
    Question = apps.get_model('tool', 'Question')
    Choice = apps.get_model('tool', 'Choice')

    # --- Question Set 1 ---
    q1 = Question.objects.create(set_number=1, text="What does MVC stand for in the context of Django?")
    Choice.objects.create(question=q1, text="Model-View-Controller", is_correct=True)
    Choice.objects.create(question=q1, text="Media-View-Context")
    Choice.objects.create(question=q1, text="Model-View-Component")

    q2 = Question.objects.create(set_number=1, text="Which command is used to create a new Django project?")
    Choice.objects.create(question=q2, text="django-admin startapp myapp")
    Choice.objects.create(question=q2, text="django-admin startproject myproject", is_correct=True)
    Choice.objects.create(question=q2, text="python manage.py createproject myproject")

    q3 = Question.objects.create(set_number=1, text="What is the purpose of models.py in a Django app?")
    Choice.objects.create(question=q3, text="To handle URL routing")
    Choice.objects.create(question=q3, text="To define the database schema", is_correct=True)
    Choice.objects.create(question=q3, text="To write the business logic")
    
    q4 = Question.objects.create(set_number=1, text="Which template tag is used to load static files?")
    Choice.objects.create(question=q4, text="{% import static %}")
    Choice.objects.create(question=q4, text="{% static_files %}")
    Choice.objects.create(question=q4, text="{% load static %}", is_correct=True)

    q5 = Question.objects.create(set_number=1, text="What does ORM stand for?")
    Choice.objects.create(question=q5, text="Object-Relational Mapping", is_correct=True)
    Choice.objects.create(question=q5, text="Object-Resource Management")
    Choice.objects.create(question=q5, text="Operational-Record Machine")

    # --- Question Set 2 ---
    q6 = Question.objects.create(set_number=2, text="How do you access URL parameters in a view function?")
    Choice.objects.create(question=q6, text="Through request.GET")
    Choice.objects.create(question=q6, text="As keyword arguments to the view function", is_correct=True)
    Choice.objects.create(question=q6, text="Through request.PARAMS")
    
    q7 = Question.objects.create(set_number=2, text="What is the purpose of a ForeignKey field in a model?")
    Choice.objects.create(question=q7, text="To create a many-to-many relationship")
    Choice.objects.create(question=q7, text="To store a unique identifier")
    Choice.objects.create(question=q7, text="To create a many-to-one relationship", is_correct=True)

    q8 = Question.objects.create(set_number=2, text="Which command applies database migrations?")
    Choice.objects.create(question=q8, text="python manage.py makemigrations")
    Choice.objects.create(question=q8, text="python manage.py migrate", is_correct=True)
    Choice.objects.create(question=q8, text="python manage.py runmigrations")
    
    q9 = Question.objects.create(set_number=2, text="What is the function of `{% csrf_token %}` in a form?")
    Choice.objects.create(question=q9, text="To prevent Cross-Site Request Forgery attacks", is_correct=True)
    Choice.objects.create(question=q9, text="To validate form fields")
    Choice.objects.create(question=q9, text="To style the form with CSS")

    q10 = Question.objects.create(set_number=2, text="In which file do you register models to appear in the admin site?")
    Choice.objects.create(question=q10, text="views.py")
    Choice.objects.create(question=q10, text="models.py")
    Choice.objects.create(question=q10, text="admin.py", is_correct=True)
    
    # --- Question Set 3 ---
    q11 = Question.objects.create(set_number=3, text="What does `render()` function do in a view?")
    Choice.objects.create(question=q11, text="Redirects to another URL")
    Choice.objects.create(question=q11, text="Combines a template with a context and returns an HttpResponse", is_correct=True)
    Choice.objects.create(question=q11, text="Executes a database query")

    q12 = Question.objects.create(set_number=3, text="A `ManyToManyField` is used to define what kind of relationship?")
    Choice.objects.create(question=q12, text="One-to-One")
    Choice.objects.create(question=q12, text="Many-to-One")
    Choice.objects.create(question=q12, text="Many-to-Many", is_correct=True)

    q13 = Question.objects.create(set_number=3, text="How do you get data from a POST request in a view?")
    Choice.objects.create(question=q13, text="request.POST.get('field_name')", is_correct=True)
    Choice.objects.create(question=q13, text="request.data['field_name']")
    Choice.objects.create(question=q13, text="request.GET.post('field_name')")

    q14 = Question.objects.create(set_number=3, text="What is the purpose of `urls.py`?")
    Choice.objects.create(question=q14, text="To define the application's URL patterns and map them to views", is_correct=True)
    Choice.objects.create(question=q14, text="To store user session information")
    Choice.objects.create(question=q14, text="To manage static files")

    q15 = Question.objects.create(set_number=3, text="Which decorator protects a view from access by non-logged-in users?")
    Choice.objects.create(question=q15, text="@login_required", is_correct=True)
    Choice.objects.create(question=q15, text="@staff_member_required")
    Choice.objects.create(question=q15, text="@permission_required")

    # --- Question Set 4 ---
    q16 = Question.objects.create(set_number=4, text="What is the base template in Django often called?")
    Choice.objects.create(question=q16, text="index.html")
    Choice.objects.create(question=q16, text="main.html")
    Choice.objects.create(question=q16, text="base.html", is_correct=True)

    q17 = Question.objects.create(set_number=4, text="Which template tag is used for conditional logic?")
    Choice.objects.create(question=q17, text="{% for ... %}")
    Choice.objects.create(question=q17, text="{% if ... %}", is_correct=True)
    Choice.objects.create(question=q17, text="{% block ... %}")

    q18 = Question.objects.create(set_number=4, text="How can you retrieve a single object from a model by its primary key?")
    Choice.objects.create(question=q18, text="MyModel.objects.filter(pk=1)")
    Choice.objects.create(question=q18, text="MyModel.objects.get(pk=1)", is_correct=True)
    Choice.objects.create(question=q18, text="MyModel.objects.select(pk=1)")

    q19 = Question.objects.create(set_number=4, text="Where do you configure the database connection in a Django project?")
    Choice.objects.create(question=q19, text="In the DATABASES setting in settings.py", is_correct=True)
    Choice.objects.create(question=q19, text="In db.py")
    Choice.objects.create(question=q19, text="In manage.py")

    q20 = Question.objects.create(set_number=4, text="What does the `on_delete=models.CASCADE` argument do?")
    Choice.objects.create(question=q20, text="It prevents the object from being deleted")
    Choice.objects.create(question=q20, text="When the referenced object is deleted, also delete the objects that have a reference to it", is_correct=True)
    Choice.objects.create(question=q20, text="It sets the foreign key to NULL when the referenced object is deleted")

class Migration(migrations.Migration):
    dependencies = [
        ('tool', '0004_question_choice'),  # Change this to your previous migration file name
    ]
    operations = [
        migrations.RunPython(create_quiz_questions),
    ]