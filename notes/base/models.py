from django.db import models

# Create your models here.
class Note(models.Model):
    
    CATEGORY = (('BUSINESS', 'Business'),
                ('PERSONAL', 'Personal'),
                ('IMPORTANT', 'Important'))
    
    title = models.CharField(max_length=100)
    body = models.TextField()
    slug = models.SlugField(unique=True)
    category = models.CharField(max_length=15, choices=CATEGORY, default="PERSONAL")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            #Generate the Initial Slug.
            slug_base = slugify(self.title)
            slug = slug_base
            #Check if the slug is Unique and modify it if necessary.
            if Note.objects.filter(slug=slug).exists():
                slug = f'{slug_base}-{get_random_string(5)}'
            self.slug = slug
        super(Note, self).save(*args, **kwargs)
