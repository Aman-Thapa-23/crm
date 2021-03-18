from CRM1.accounts.models import *

# Return all customer from customer table
customers = Customer.objects.all()

#Return first customer in table
firstcustomer = Customer.objects.first()

#Return last customer in table
lastcustomer = Customer.objects.last()

#Return single customer by name
customerByName = Customer.objects.get(name='Yogesh Bhattarai')

#Return single customer by id
customerById = Customer.objects.get(id=3)

#Return all orders related to customer (first customer variablel set above)
firstcustomer.order_set.all()

#Return order custome name: (Query parent model values)
order = order.objects.first()
parentName = order.customer.name

#Return products from product table with the value "out door" in Category attribute
products = Products.objects.filter(category="Out Door")

#Order/sort Objects by id
leastToGreatest = Products.objects.all().Order_by('id')
greatestToLeast = Products.objects.all().order_by('-id')

#Return all products with tag of "sports": (Query Many to Many fields)
productsFiltered = Products.objects.filter(tags_name="Sports")

'''
(11) bonus
Qns: If the customer has more than 1 ball, how would you reflect it in the database?
Ans: Because there are many different products and this value changes constantly you 
would most likely not want to store the value in the database but rather just make this
 a function we can run each time we load the customers profile.
'''

#Return the total count for number of time a "Ball" was ordered by the first customor
ballOrders = firstcustomer.order_set.filter(product_name="Ball").count()

#Return total count for each product ordered
allOrders = {}

for order in firstcustomer.order_set.all():
    if order.product.name in allOrders:
        allOrders[order.product.name] +=1
    else:
        allOrders[order.product.name] = 1

#Returns: allOrders: {'Ball': 2, 'BBQ Grill': 1}


#RELATED SET EXAMPLE
class ParentModel(models.Model):
    name = models.CharField(max_length= 200, null=True)

class ChildModel(models.Model):
    parent= models.ForeignKey(ParentModel)
    name = models.CharField(max_length=200, null=True)

parent = ParentModel.objects.first()
#Return all child models related to parent
parent.childmodel_set.all()