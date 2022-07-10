import random
from django.utils.text import slugify


def slugify_instance_customer(instance, save=False, new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.customer)
    klass = instance.__class__
    qs = klass.objects.filter(slug=slug).exclude(id=instance.id)
    if qs.exists():
        rand_int1 = random.randint(1, 900_000)
        rand_int2 = random.randint(1, 900_000)
        slug = f"{slug}-{rand_int1}-{rand_int2}"
        return slugify_instance_customer(instance, save=save, new_slug=slug)
    instance.slug = slug
    if save:
        instance.save()
    return instance
