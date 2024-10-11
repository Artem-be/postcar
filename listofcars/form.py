from django import forms
from .models import Comment
from .models import Car

class CarForm(forms.ModelForm):
    """
    Форма для создания и редактирования записей в модели Car.
    """
    class Meta:
        """
        Метакласс, определяющий настройки формы.
        """
        model = Car  # Модель, для которой создается форма
        fields = ['make', 'model', 'year', 'description']  # Поля, которые будут отображаться в форме

class CommentsForm(forms.ModelForm):
    """
    Форма для создания и редактирования записей в модели Comment.
    """
    class Meta:
        """
        Метакласс, определяющий настройки формы.
        """
        model = Comment  # Модель, для которой создается форма
        fields = ('content',)  # Поля, которые будут отображаться в форме