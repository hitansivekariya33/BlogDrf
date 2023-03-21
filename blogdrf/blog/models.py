from django.db import models
# Create your models here.
class BaseModel(models.Model):
    create_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-create_at']

class Author(models.Model):
    name = models.CharField(max_length=100,null=False)
    about_author = models.TextField()

    def __str__ (self):
        return self.name


class Blog(BaseModel):
    author = models.ForeignKey(Author, on_delete=models.CASCADE,related_name='blogs')
    title = models.CharField(max_length=100)
    blog_content = models.TextField()


    def __str__ (self):
        return self.title
