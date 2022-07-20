from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from taggit.managers import TaggableManager

# Create your models here.


# The get_queryset()method of a manager returns the QuerySet that will be executed.
# To override this method to include out custom filter in the final QuerySet
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset()\
                    .filter(status='published')

class Post(models.Model):
    status_choices = (
        ('draft','Draft'),
        ('published','Published')
    )
    # This is the field for the post title. this field is charField,
    # which translates into a varchar column in the SQL database
    title = models.CharField(max_length=250)
    # This is a field intended to be used in URLs. A slug is a short lable
    # that contains only letters, numbers, underscores or hyphens.
    # unique_for_date parameter added to this field to build URLs for posts 
    # using  their publish date and slug.
    # Django will prevent multiple posts from having the same slug for a given date.
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    # This field defines a many to one relationship, meaning that each post is written by a user,
    # and a user can write any number of posts. For this field.
    # For this field django will create primary key of the related module.
    # In this case, relying on the User model of the Django authentication system.
    # The on_delete parameter specifies the behavior to adopt when the refernced object is deleted.
    # Using CASCADE, specify that when the referenced user is deleted, the database will also delete all related blog posts.
    # Specify the name of the reverse relationship, from User to Post, with the related_name attribute. This will
    # allow to access related objects easily.
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    # This is the body of the post. This field is a text field that translates into a TEXT column in the SQL database.
    body = models.TextField()
    # This datetime indicates when the post was published.
    # Used Django's timezone now method as the default value.
    publish = models.DateTimeField(default=timezone.now)
    # This dateTimeField indicates when the post was created.
    # Using auto_now_add here, the date will be saved automatically when creating an object.
    create = models.DateTimeField(auto_now_add=True)
    # This datetime indicates the last time the post was updated.
    # Using auto_now here, the date will be updated automatically when saving an object.
    update = models.DateTimeField(auto_now=True)
    # This field show the status of the post.
    # Using a choices parameter, so the value of the field can only be set to one of the given choices.
    status = models.CharField(max_length=10, choices=status_choices, default='draft')

    # The default manager
    objects = models.Manager()
    # The custom manager
    published = PublishedManager()

    # The Meta class inside the model contains metadata.
    # Telling Django to sorts results by the publish field in decending order by default when querying the database.
    # Specify the desecending order using the negative prefix. By doing this , posts published recently will appear first 
    class Meta():
        ordering = ('-publish',)

    # The __str__() method is the default human-readable representation of the object.
    # Djanogo will use it in many places, such as the administration site.
    def __str__(self):
        return self.title
    
    # We will use the get_absolute_url() method in the templates to link the specific posts
    def get_absolute_url(self):
        return reverse("blog:post_details", args=[self.publish.year,
                                                    self.publish.month,
                                                    self.publish.day,
                                                    self.slug])
    
    # The tags manager will allow to add, retvieve and remove tags from Post objects.
    tags = TaggableManager()
    
class Comments(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return f'Comment by {self.name} on {self.post}'

