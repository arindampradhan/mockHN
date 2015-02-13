from django import template
import random
register = template.Library()


@register.filter(name="random_img")
def randomimage():
    num = random.randint(0, 39)
    addr_num = "/static/img/face{}".format(num)
    return num
