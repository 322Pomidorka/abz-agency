from datetime import datetime
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Employees(MPTTModel):
    first_name = models.CharField(max_length=50,
                                  verbose_name='Имя')
    last_name = models.CharField(max_length=50,
                                 verbose_name='Фамилия')
    employment_position = models.CharField(max_length=100,
                                           default=None,
                                           verbose_name='Должность')
    employment_start_date = models.DateTimeField(auto_now_add=False,
                                                 null=True,
                                                 blank=True)
    salary = models.IntegerField(null=True,
                                 blank=True)
    date_added = models.DateTimeField(default=datetime.now,
                                      blank=True)
    employment_photo = models.ImageField(blank=True,
                                         upload_to='images/%Y/%m/%d',
                                         help_text='150x150px',
                                         verbose_name='employment_photo')
    parent = TreeForeignKey('self',
                            on_delete=models.CASCADE,
                            null=True,
                            blank=True,
                            related_name='children',
                            db_index=True,
                            verbose_name='parent')

    class MPTTMeta:
        order_insertion_by = ['first_name', 'last_name']

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    def __str__(self):
        return f'Name {self.first_name}'
