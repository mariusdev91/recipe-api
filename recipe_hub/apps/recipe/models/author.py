from django.db import models


class Author(models.Model):
    first_name = models.CharField(help_text='Please enter your first name',
                                  max_length=50)
    last_name = models.CharField(help_text='Please enter your last name',
                                 max_length=50)
    email = models.EmailField(help_text='Enter a valid email address')
    social_media_account = models.URLField(
        help_text="Enter the link to your "
                  "social media account if you have one.",
        blank=True)
    recipe_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.last_name} {self.first_name}"
