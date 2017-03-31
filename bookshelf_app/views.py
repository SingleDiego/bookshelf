from django.shortcuts import render, redirect
from django import forms

from bookshelf_app.models import Book, BookID
from bookshelf_app.forms import BookForm, BookFormReadOnly

# 添加图书的页面
def add_book(request):
    context = {}

    lately_book_id_obj = BookID.objects.filter(is_lately_book=True) # 最近添加图书id对象
    lately_books_count = lately_book_id_obj.count() # 近添加图书id计数
    context['lately_books_count'] = lately_books_count

    lately_books = BookID.objects.all().order_by('-book_id')[0:lately_books_count] # 最近添加的图书列表
    context['lately_books'] = lately_books

    book_form = BookForm # 添加书目的表单
    context['book_form'] = book_form

    return render(request, 'add_book.html', context)

# 保存添加的图书
def save_book(request):
    context = {}

    if request.method == 'POST':
        book_form = BookForm(request.POST)

        # 表单通过验证
        if book_form.is_valid():
            amount = book_form.cleaned_data['amount'] # 图书册数
            book_obj = book_form.save() # 保存图书对象

            # 根据册数生成对应的图书id,is_lately_book 默认为True
            for i in range(amount):
                book_id_obj = BookID.objects.create(belong_to = book_obj)
            
            return redirect(to='add_book') # 保存后跳转回 add_book 页面

        # 表单未通过验证
        else:
            lately_book_id_obj = BookID.objects.filter(is_lately_book=True) # 最近添加图书id对象
            lately_books_count = lately_book_id_obj.count() # 近添加图书id计数
            context['lately_books_count'] = lately_books_count

            lately_books = BookID.objects.all().order_by('-book_id')[0:lately_books_count] # 最近添加的书目
            context['lately_books'] = lately_books

            context['book_form'] = book_form
            return render(request, 'add_book.html', context)
            

# 图书列表
def book_list(request):
    context = {}
    book_list = Book.objects.all()
    context['book_list'] = book_list
    return render(request, 'book_list.html', context)


# 最近录入书目计数清零
def clean_books_count(request):
    lately_book_id_obj = BookID.objects.filter(is_lately_book=True) # 最近添加图书id对象
    lately_book_id_obj.update(is_lately_book=False)
    return redirect(to='add_book') 


# 图书详细页面
def book_detail(request, id):
    context = {}
    book_detail = Book.objects.get(id=id)

    book_form = BookFormReadOnly(
        # 设置表单默认值
        initial={
        'title': book_detail.title,
        'author': book_detail.author, 
        'publisher': book_detail.publisher,
        'ISBN': book_detail.ISBN,
        'CLC': book_detail.CLC,
        'pub_date': book_detail.pub_date,
        'amount': book_detail.bookid_set.count()
        }, 
        )
    context['book_form'] = book_form
    
    return render(request, 'book_detail.html', context)