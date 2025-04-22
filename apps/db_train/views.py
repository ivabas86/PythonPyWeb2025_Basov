from django.shortcuts import render
from django.views import View
from .models import Author, AuthorProfile, Entry, Tag
from django.db.models import Q, Max, Min, Avg, Count

class TrainView(View):
    def get(self, request):
        # Создайте здесь запросы к БД
        self.answer1 = None  # TODO Какие авторы имеют самую высокую уровень самооценки(self_esteem)?
        max_self_esteem = Author.objects.aggregate(max_self_esteem=Max('self_esteem'))
        self.answer1 = Author.objects.filter(self_esteem=max_self_esteem['max_self_esteem'])
        self.answer2 = None  # TODO Какой автор имеет наибольшее количество опубликованных статей?
        self.answer2 = Author.objects.annotate(num_entries= Count('entries')).order_by('-num_entries').first()
        self.answer3 = None  # TODO Какие статьи содержат тег 'Кино' или 'Музыка' ?
        self.answer3 = Entry.objects.filter(tags__name__in = ['Кино','Музыка']).distinct()
        self.answer4 = None  # TODO Сколько авторов женского пола зарегистрировано в системе?
        self.answer4 = Author.objects.filter(gender = 'ж').count()
        self.answer5 = None  # TODO Какой процент авторов согласился с правилами при регистрации?
        author_all = Author.objects.count()
        author_rule = Author.objects.filter(status_rule=True).count()

        self.answer5 = round(author_rule*100/author_all,2)
        self.answer6 = None  # TODO Какие авторы имеют стаж от 1 до 5 лет?
        self.answer6 = Author.objects.filter(authorprofile__stage__range = (1,5))
        self.answer7 = None  # TODO Какой автор имеет наибольший возраст?
        max_age = Author.objects.aggregate(max_age =Max('age'))
        self.answer7 = Author.objects.filter(age = max_age['max_age'])
        self.answer8 = None  # TODO Сколько авторов указали свой номер телефона?
        self.answer8 = Author.objects.filter(phone_number__isnull= False).count()
        self.answer9 = None  # TODO Какие авторы имеют возраст младше 25 лет?
        self.answer9 = Author.objects.filter(age__lt = '25')
        self.answer10 = None  # TODO Сколько статей написано каждым автором?
        self.answer10 = Author.objects.annotate(count= Count('entries'))

        context = {f'answer{index}': self.__dict__[f'answer{index}'] for index in range(1, 11)}

        return render(request, 'train_db/training_db.html', context=context)


