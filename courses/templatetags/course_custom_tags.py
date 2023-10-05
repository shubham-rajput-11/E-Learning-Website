from django import template
import math 
from courses.models import UserCourse, Course

# this is a kind of helper function which can calculate prices discount and provide answer which is then render in html
register = template.Library()



@register.simple_tag
def calc_sellprice(price,discount):
    if discount is None or discount == 0:
        return price
    sellprice = price
    sellprice = price - ( price * discount * 0.01)
    return math.floor(sellprice)


@register.filter
def rupee(price):
    return f'₹{price}'

@register.simple_tag
def is_enrolled(request, course):
    user = None
    if not request.user.is_authenticated:
        return False
    # if you are enrooled in this course you can watch every video
    user = request.user
    try:
        user_course = UserCourse.objects.get(user = user  , course = course)
        return True
    except:
        return False