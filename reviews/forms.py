from django import forms
from .models import Review

RATING_CHOICES = [
    (5, "5"),
    (4, "4"),
    (3, "3"),
    (2, "2"),
    (1, "1"),
]


class ReviewForm(forms.ModelForm):
    review = forms.CharField(
        max_length=200,
        strip=True,
        widget=forms.Textarea(attrs={"placeholder": "WRITE YOUR REVIEW HERE"}),
        error_messages={"required": "The review section is required."},
    )
    rating = forms.IntegerField(
        widget=forms.RadioSelect(
            choices=RATING_CHOICES, attrs={"class": "radio_input"}
        ),
        error_messages={"required": "Please choose a rating."},
    )

    class Meta:
        model = Review
        fields = ["review", "rating"]
