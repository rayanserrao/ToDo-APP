from django.urls import path
from mytodo.views import index,todo_add,todo_delete,todo_edit


urlpatterns=[
    path('index/',index,name='index'),
    path('todo_add/',todo_add,name='todoadd'),
    path('todo_delete/<int:del_id>',todo_delete,name='todo_delete'),
    path('todo_edit/<int:edit_id>',todo_edit,name='todo_edit'),
]