from django.db import models


class Contact(models.Model):

    """
    Using a tuple to propose a multiple choice
    first element of each tuple is the value
    that will be stored in the database
    second element is the human-readable labe
    """

    REASON_CHOICES = (
        ("1", "Registration Issue"),
        ("2", "Login Issue"),
        ("3", "Payment Issue"),
        ("4", "General Enquiry"),
        ("5", "Product Query"),
        ("6", "Report a Review"),
    )

    reason = models.CharField(
        max_length=2, choices=REASON_CHOICES, default="4"
        )

    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    message = models.TextField(max_length=2000)
    written_on = models.DateTimeField(auto_now=True)

    class Meta:
        """
         to specify human-readable names for the model
         used for instance in Django admin site
        """
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'

    def __str__(self):
        """
         to return contact name and date as a string
         used for instance in Django admin site
        """
        return f'Message from {self.name} on {self.written_on}'
