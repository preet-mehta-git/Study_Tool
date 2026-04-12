from django.shortcuts import render,redirect,get_object_or_404
from django.http import JsonResponse
from .models import Register
from io import BytesIO
from .models import Register,Comment,Question,Choice,Event
import random
from django.db.models import Max
from datetime import datetime
from calendar import HTMLCalendar
import re
from django.shortcuts import render, redirect
from .models import Register
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name'].strip()
        middle_name = request.POST['middle_name'].strip()
        last_name = request.POST['last_name'].strip()
        email = request.POST.get('email').strip()
        password = request.POST.get('password')
        mobile = request.POST.get('mobile_number').strip()
        birth_date = request.POST.get('birth_date')
        qualification = request.POST.get('qualification').strip()

        if not (first_name.isalpha() and middle_name.isalpha() and last_name.isalpha()):
            messages.error(request, "Names must contain only alphabets.")
            return redirect('register')

        if len(password) < 6:
            messages.error(request, "Password must be at least 6 characters long.")
            return redirect('register')
        
        if not re.search(r'[A-Za-z]', password):
            messages.error(request, "Password must contain at least one letter.")
            return redirect('register')
        
        if not re.search(r'[^A-Za-z0-9]', password):
            messages.error(request, "Password must contain at least one special character.")
            return redirect('register')
        
        if (int(mobile) <= 1000000000) or (int(mobile) >= 9999999999):
            messages.error(request,'Please add a valid phone number')
            return redirect('register')
        
        date = birth_date.split('-')
        
        if int(date[0]) > 2024:
            messages.error(request,'Please enter a valid date')
            return redirect('register')

        new_user = Register(
            first_name=first_name,
            middle_name=middle_name,
            last_name=last_name,
            email=email,
            password=password,
            mobile_number=mobile,
            birth_date=birth_date,
            qualification=qualification
        )
        new_user.save()
        return redirect('login')

    return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = Register.objects.get(email=email)
            if user.password == password:
                request.session['user_email'] = user.email
                return redirect('home')
            else:
                error_message = "Incorrect password."
                return render(request, 'login.html', {'error': error_message})

        except Register.DoesNotExist:
            error_message = "No account found with this email."
            return render(request, 'login.html', {'error': error_message})
    return render(request, 'login.html')

def home(request):
    return render(request,'home.html')

def profile(request):
    if 'user_email' in request.session:
        user_email = request.session['user_email']
        try:
            user_profile = Register.objects.get(email=user_email)
            return render(request, 'profile.html', {'user_profile': user_profile})
        except Register.DoesNotExist:
            del request.session['user_email']
            return redirect('login')
    else:
        return redirect('login')

def analysis(request):
    if 'user_email' not in request.session:
        return redirect('login')

    if request.method == 'POST':
        try:
            score1 = float(request.POST.get('score1'))
            score2 = float(request.POST.get('score2'))
            score3 = float(request.POST.get('score3'))
            score4 = float(request.POST.get('score4'))
            total_marks = float(request.POST.get('total_marks'))

            trend1 = score2 - score1
            trend2 = score3 - score2
            trend3 = score4 - score3
            average_trend = (trend1 + trend2 + trend3) / 3
            
            predicted_score = score4 + average_trend

            if predicted_score > total_marks:
                predicted_score = total_marks
            elif predicted_score < 0:
                predicted_score = 0
            
            context = {
                'prediction': round(predicted_score, 2),
                'total_marks': total_marks
            }
            return render(request, 'analysis.html', context)

        except (ValueError, TypeError):
            error_message = 'Please enter valid numbers for all fields.'
            return render(request, 'analysis.html', {'error': error_message})

    return render(request, 'analysis.html')

def chat(request):
    if 'user_email' not in request.session:
        return redirect('login')
    
    user = get_object_or_404(Register, email=request.session['user_email'])

    if request.method == 'POST':
        content = request.POST.get('content')
        parent_id = request.POST.get('parent_id')
        if parent_id:
            parent_comment = get_object_or_404(Comment, id=parent_id)
            Comment.objects.create(author=user, content=content, parent=parent_comment)
        else:
            Comment.objects.create(author=user, content=content)
        
        return redirect('chat')
    top_level_comments = Comment.objects.filter(parent__isnull=True).order_by('-timestamp')
    
    context = {
        'comments': top_level_comments,
        'current_user': user
    }
    return render(request, 'chat.html', context)


def like_comment(request, comment_id):
    if 'user_email' not in request.session:
        return redirect('login')
    
    comment = get_object_or_404(Comment, id=comment_id)
    user = get_object_or_404(Register, email=request.session['user_email'])

    if user in comment.likes.all():
        comment.likes.remove(user)
    else:
        comment.likes.add(user)
    
    return redirect('chat')

def quiz(request):
    if 'user_email' not in request.session:
        return redirect('login')
    
    if request.method == 'POST':
        score = 0
        total_questions = 0
        set_number = request.session.get('quiz_set_number')
        if not set_number:
            return redirect('quiz')

        questions = Question.objects.filter(set_number=set_number)
        total_questions = questions.count()

        for question in questions:
            selected_choice_id = request.POST.get(f'question_{question.id}')
            if selected_choice_id:
                selected_choice = Choice.objects.get(id=selected_choice_id)
                if selected_choice.is_correct:
                    score += 1
        
        del request.session['quiz_set_number']

        context = {
            'score': score,
            'total_questions': total_questions
        }
        return render(request, 'quiz.html', context)
    else:
        max_set = Question.objects.aggregate(Max('set_number'))['set_number__max']
        if not max_set:
            return render(request, 'quiz.html', {'error': 'No quiz questions found.'})
        random_set_number = random.randint(1, max_set)
        request.session['quiz_set_number'] = random_set_number
        questions = Question.objects.filter(set_number=random_set_number)
        
        context = {
            'questions': questions
        }
        return render(request, 'quiz.html', context)

class ScheduleCalendar(HTMLCalendar):
    def __init__(self, events=None):
        super().__init__()
        self.events = events

    # This method formats each day's table cell
    def formatday(self, day, weekday):
        if day == 0:
            return '<td class="noday">&nbsp;</td>'  # day outside month
        
        day_events_html = "<ul>"
        day_events = self.events.filter(start__day=day)
        
        for event in day_events:
            day_events_html += f"<li class='event-{event.event_type}'>{event.title}</li>"
        
        day_events_html += "</ul>"

        return f'<td class="{self.cssclasses[weekday]}"><span class="day-number">{day}</span>{day_events_html}</td>'


def schedule(request):
    if 'user_email' not in request.session:
        return redirect('login')

    user = get_object_or_404(Register, email=request.session['user_email'])

    # Handle form submission for new events
    if request.method == 'POST':
        title = request.POST.get('title')
        start = request.POST.get('start')
        event_type = request.POST.get('event_type')
        Event.objects.create(user=user, title=title, start=start, event_type=event_type)
        return redirect('schedule')

    # Handle displaying the calendar for GET requests
    # Get current month and year from URL, or use today's date
    try:
        year = int(request.GET.get('year', datetime.now().year))
        month = int(request.GET.get('month', datetime.now().month))
    except ValueError:
        year = datetime.now().year
        month = datetime.now().month

    # Calculate next and previous month/year for navigation
    last_month = month - 1 if month > 1 else 12
    last_year = year if month > 1 else year - 1
    next_month = month + 1 if month < 12 else 1
    next_year = year if month < 12 else year + 1

    # Fetch events for the logged-in user for the given month and year
    events = Event.objects.filter(user=user, start__year=year, start__month=month)

    # Create an instance of our custom calendar
    cal = ScheduleCalendar(events)
    html_cal = cal.formatmonth(year, month)
    
    context = {
        'calendar': html_cal,
        'current_month': datetime(year, month, 1).strftime('%B'),
        'current_year': year,
        'prev_month': last_month,
        'prev_year': last_year,
        'next_month': next_month,
        'next_year': next_year,
    }

    return render(request, 'schedule.html', context)

def faq(request):
    return render(request, 'faq.html')

def privacy_policy(request):
    return render(request, 'privacy_policy.html')

def tos(request):
    return render(request,'tos.html')

def contact_us(request):
    team_members = [
        {
            'name': 'Preet Mehta',
            'email': 'preet@studytool.com',
            'phone': '9876543210'
        },
        {
            'name': 'Rushiraj Raijada',
            'email': 'rushiraj@studytool.com',
            'phone': '9876543211'
        },
        {
            'name': 'Mrudang Dave',
            'email': 'mrudang@studytool.com',
            'phone': '9876543212'
        },
        {
            'name': 'Krish Radadiya',
            'email': 'krish@studytool.com',
            'phone': '9876543213'
        }
    ]
    
    context = {
        'members': team_members
    }
    return render(request, 'contact_us.html', context)