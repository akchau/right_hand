from django.db import models

from contacts.models import Company


UNIT_OF_MEASUREMENT = {
    ('шт', 'шт'),
    ('кг', 'кг'),
    ('м', 'м'),
}


class Product(models.Model):
    """Модель товара."""
    name = models.CharField(
        "Название товара.",
        max_length=200,
        help_text="Укажите название товара.",
    )
    maker = models.ForeignKey(
        Company,
        related_name="products",
        verbose_name="Производитель",
        on_delete=models.SET_NULL,
        null=True,
        help_text="Укажите произоводителя"
    )
    reference = models.CharField(
        "Артикул производителя.",
        max_length=50,
        help_text="Укажите заводской артикул"
    )
    unit = models.CharField(
        "Еденица измерения",
        choices=UNIT_OF_MEASUREMENT,
        max_length=10
    )
    price = models.PositiveIntegerField(
        "Стоимость в прайсе производтеля.",
    )

    def __str__(self):
        return self.name


class Collection(models.Model):
    """Сборка из комплектующих."""
    name = models.CharField(
        "Название сборки",
        max_length=200,
        help_text="Укажите название сборки.",
    )
    description = models.TextField(
        "Описание сборки",
        help_text="Добавьте описание сборки",
        null=True
    )

    @property
    def numbers_of_position_in(self):
        positions = ProductsCollection.objects.filter(collection=self).count()
        return positions

    @property
    def total_of_position_in(self):
        positions = ProductsCollection.objects.filter(collection=self)
        sum_of_collection = sum([item.total_of_position for item in positions])
        return sum_of_collection

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Сборка'
        verbose_name_plural = 'Сборки'


class ProductsCollection(models.Model):
    """Пара товар сборка."""
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="collections",
        verbose_name="Продукт",
    )
    collection = models.ForeignKey(
        Collection,
        on_delete=models.CASCADE,
        related_name="products",
        verbose_name="Сборка",
        help_text="Укажите названине сборки."
    )
    numbers = models.PositiveIntegerField(
        "Количество элементов в сборке",
        help_text="Укажите количество.",
    )

    @property
    def price_of_position(self):
        return self.product.price

    @property
    def total_of_position(self):
        return self.product.price * self.numbers

    def __srt__(self):
        return f'{self.product} - {self.collection} - {self.numbers} шт.'
