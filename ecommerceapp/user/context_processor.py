from account.models import Cart

def hi(request):
    return{"hi":"hello"}


def cart_count(request):
    if request.user.is_authenticated:
       count=Cart.objects.filter(user=request.user,status="added").count()
       return {"count":count}
    else:
        return {"count":0}