from django.db import models

# Create your models here.


class AcceptedProject(models.Model):
    user_id = models.ForeignKey('user.User', on_delete=models.CASCADE)
    freelancer_id = models.ForeignKey('user.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField('project.Tag',related_name='projects')
    category = models.ForeignKey('project.Category', on_delete=models.CASCADE)
    price = models.IntegerField()
    deadline = models.DateTimeField()
    file = models.FileField(upload_to='files/', blank=True)
    latitude = models.DecimalField(max_digits=10, decimal_places=7, blank=True, default=None, null=True)
    longitude = models.DecimalField(max_digits=10, decimal_places=7, blank=True, default=None, null=True)
    accepted_bid = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return str(self.id)



class AcceptedMilestone(models.Model):
    user_id = models.ForeignKey('user.User', on_delete=models.CASCADE)
    acceptedproject_id = models.ForeignKey('AcceptedProject', on_delete=models.CASCADE)
    description = models.TextField()
    amount = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deadline = models.DateTimeField(default=None)

    def __str__(self):
        return (self.id)