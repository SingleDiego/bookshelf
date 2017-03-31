from django.db import models
from django.core.exceptions import ValidationError 
import re

# 出版日期验证器
def validate_pub_date(value):
    if value > 9999 or value < 1:
        raise ValidationError('出版年份应为0-9999年' ) 

# 分类号验证器
def validate_CLC(value):
    if re.match('^[ABCDEFGHIJKNOPQRSTUVXZ]', value) != None: 
        if len(value) == 1:               
            pass
        else:
            if re.match('^[ABCDEFGHIJKNOPQRSTUVXZ]\d+$', value) != None:
                pass
            else:
                raise ValidationError('请输入正确分类号' ) 
    else:
        raise ValidationError('请输入正确分类号' ) 

        
class Book(models.Model):
    # 书名，唯一的，不可为空
    title = models.CharField(
        unique=True, 
        max_length=200, 
        verbose_name='书名',
        error_messages={'unique':"该书名已存在，请重新检查"}
        )

    # 出版社
    publisher = models.CharField(
        null=True, 
        blank=True, 
        max_length=200,
        verbose_name='出版社',
        )

    # 作者
    author = models.CharField(
        null=True, 
        blank=True, 
        max_length=200,
        verbose_name='作者',
        )

    # ISBN
    ISBN = models.CharField(
        null=True, 
        blank=True,
        max_length=200,
        verbose_name='ISBN',
        )

    # 中图法分类号
    CLC = models.CharField(
        null=True, 
        blank=True, 
        max_length=200,
        validators=[validate_CLC], # 分类号验证器
        verbose_name='分类号',)

    # 出版日期
    pub_date = models.IntegerField(
        null=True, 
        blank=True,
        validators=[validate_pub_date], # 出版日期验证器
        verbose_name='出版日期',
        )

    def __str__(self):
        return self.title


class BookID(models.Model):
    belong_to = models.ForeignKey(Book)
    book_id = models.AutoField(primary_key=True)
    is_lately_book = models.BooleanField(default=True)



