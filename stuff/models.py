from django.db import models
import uuid
from users.models import Profile
# Create your models here.


class Books(models.Model):
    author = models.CharField(max_length= 100, default = None)
    title = models.CharField(max_length=50)
    description = models.TextField(null=True,blank=True)
    price = models.DecimalField(max_digits=5, decimal_places  = 2, default = None)
    vote_total = models.IntegerField(default=0, null=True, blank=True)
    vote_ratio = models.IntegerField(default=0, null=True, blank=True)
    tags = models.ManyToManyField('Tag',blank=True)
    image = models.ImageField(null= True, blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, 
                          primary_key=True, editable=False)
    
    
    def __str__(self):
        return self.title
    
    
    class Meta:
        verbose_name_plural = 'Books'


    @property
    def imageURL(self):
        try:
            url = self.image.url            
        except:
            url = ''
   
        return url
    
    @property
    def getVoteCount(self):
        reviews = self.review_set.all()
        upVotes = reviews.filter(value='up').count()
        totalVotes = reviews.count()

        ratio = (upVotes / totalVotes) * 100
        self.vote_total = totalVotes
        self.vote_ratio = ratio

        self.save()
    
    
    @property
    def reviewers(self):
        queryset = self.review_set.all().values_list('owner__id', flat=True)
        return queryset
    
    
    

class Review(models.Model):
    VOTE_TYPE = (
        ('up','Up Vote'),
        ('down', 'Down Vote')
    )
    
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    book = models.ForeignKey(Books, on_delete=models.CASCADE) 
    body = models.TextField(null=True,blank=True)
    value = models.CharField(max_length=200, choices=VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, 
                          primary_key=True, editable=False)
    
    class Meta:
        unique_together = [['owner', 'book']]
    
    def __str__(self):
        return f'{self.value} {self.owner} {self.book}'



class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, 
                          primary_key=True, editable=False)
    
    
    def __str__(self):
        return self.name
    
    

class Order(models.Model):
    customer = models.ForeignKey(Profile, on_delete = models.SET_NULL, null = True, blank = True)
    order_date = models.DateTimeField(auto_now_add = True)
    complete = models.BooleanField(default= False)
    transaction_id = models.CharField(max_length=100, null=True)
    
    def __str__(self):
        return str(self.id)
    
    @property
    def shipping(self):
        shipping = True
        return shipping
    
    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total
    
    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total
    
class OrderItem(models.Model):
    book = models.ForeignKey(Books, on_delete = models.SET_NULL, null = True)
    order = models.ForeignKey(Order, on_delete = models.SET_NULL, null = True)
    quantity = models.IntegerField(default = 0, null = True, blank = True)
    date_added = models.DateTimeField(auto_now_add = True)
    
    @property
    def get_total(self):
        total = self.book.price * self.quantity
        return total

class ShippingAddress(models.Model):
    customer = models.ForeignKey(Profile, on_delete = models.SET_NULL, null = True, blank = True)
    order = models.ForeignKey(Order, on_delete = models.SET_NULL, null = True)
    address = models.CharField(max_length=200, null = True)
    city = models.CharField(max_length=200, null = True)
    state = models.CharField(max_length=200, null = True)
    zipcode = models.CharField(max_length=200, null = True)
    date_added = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.address

