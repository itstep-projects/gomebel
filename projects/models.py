from django.db import models


def user_directory_path(instance, filename):
    return f'project_{instance.id}/{filename}'


class Category(models.Model):
    name = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=100, null=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    about = models.CharField(max_length=100, null=False)
    text = models.TextField(max_length=500, null=False)
    image_1 = models.FileField(null=True, upload_to=user_directory_path)
    image_2 = models.FileField(null=True, upload_to=user_directory_path)
    image_3 = models.FileField(null=True, upload_to=user_directory_path)
    image_4 = models.FileField(null=True, upload_to=user_directory_path)
    image_5 = models.FileField(null=True, upload_to=user_directory_path)

    # Переопределение метода save для класса для формирования правильного пути сохраниения
    # def save(self, *args, **kwargs):
    #     if self.pk is None:
    #         saved_image = self.image
    #         self.image = None
    #         super(Project, self).save(*args, **kwargs)
    #         self.image = saved_image
    #         kwargs.pop('force_insert')
    #
    #     super(Project, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


