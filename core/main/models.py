from django.db import models

# Create your models here.
class HomeCarusel(models.Model):
    name1 = models.CharField('Carusel name', max_length=30)
    name2 = models.CharField('Carusel name', max_length=60)
    about = models.TextField('Carusel about')
    img1 = models.ImageField('Carusel image', upload_to='media')
    img2 = models.ImageField('Carusel image', upload_to='media')

    def __str__(self):
        return self.name1

    class Meta:
        verbose_name = 'HomeCarusel'
        verbose_name_plural = 'HomeCarusels'

class HomeCategory(models.Model):
    name = models.CharField('Category name', max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'HomeCategory'
        verbose_name_plural = 'HomeCategories'

class HomeSubCategory(models.Model):
    homecategory = models.ForeignKey(HomeCategory, on_delete=models.CASCADE, related_name='subcateg')
    name = models.CharField('SubCategory name', max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'HomeSubCategory'
        verbose_name_plural = 'HomeSubCategories'


class HomeBrand(models.Model):
    name = models.CharField('Brand name', max_length=30)
    count = models.IntegerField('Brand count', null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'HomeBrand'
        verbose_name_plural = 'HomeBrands'


class HomeFeatureItem(models.Model):
    price = models.CharField('Item price', max_length=20)
    about = models.TextField('Item about')
    img = models.ImageField('Item image', upload_to='media')

    def __str__(self):
        return self.price

    class Meta:
        verbose_name = 'HomeFeatureItem'
        verbose_name_plural = 'HomeFeatureItems'

class HomeRec(models.Model):
    price = models.CharField('Rec price', max_length=20)
    about = models.TextField('Rec about')
    img = models.ImageField('Rec image', upload_to='media')

    def __str__(self):
        return self.price

    class Meta:
        verbose_name = 'HomeRec'
        verbose_name_plural = 'HomeRecs'


class HomeShipping(models.Model):
    name = models.CharField('HomeShipping name', max_length=10, blank=True)
    img = models.ImageField('Shipping name', upload_to='media')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'HomeShipping'
        verbose_name_plural = 'HomeShippings'