from django.db import models

from users.models import User

NULLABLE = {"blank": True, "null": True}


class Tree(models.Model):
    """Tree model."""

    TYPE_OF_TREE_CHOICES = [
        ("pine", "Сосна"),
        ("birch", "Береза"),
        ("oak", "Дуб"),
    ]
    name = models.CharField(max_length=250,
                            verbose_name="Наименование",
                            help_text="Придумайте имя своему дереву",
                            **NULLABLE)
    type_of_tree = models.CharField(max_length=5,
                                    choices=TYPE_OF_TREE_CHOICES,
                                    verbose_name="Вид дерева",
                                    help_text="Выберите вид своего дерева",)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата и время посадки")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, **NULLABLE, related_name="trees")

    class Meta:
        verbose_name = "дерево"
        verbose_name_plural = "деревья"

    def __str__(self):
        return f"Дерево {self.name} вида {self.type_of_tree} посажено {self.owner} {self.created_at}"
