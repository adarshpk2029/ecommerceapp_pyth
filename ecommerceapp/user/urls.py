from django.urls import path
from .views import *


urlpatterns=[
    path("uhome",UserHomeView.as_view(),name="uhome"),
    path("prolist/<str:cat>",ProductsView.as_view(),name="pro"),
    path('det/<int:pid>',DetailsView.as_view(),name='det'),
    path('acart/<int:pid>',addtocart,name="addcart"),
    path('clist',CartListView.as_view(),name="cart"),
    # path('delt/<int:cid>',DeleteView.as_view(),name='delt')
    path('deletecart/<cid>',CartItemDeleteView.as_view(),name='cdelt'),
    path('addrev/<pid>',addreview,name="arev"),
    path('porder/<int:cid>',PlaceorderView.as_view(),name="pldr"),
    path('order',OrderListView.as_view(),name="order"),
    path('corder/<int:oid>',cancelorder,name="corder")
]