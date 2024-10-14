# from django.db import models
#
#
# class PortfolioTag(models.Model):
#     tag = models.CharField(max_length=128)
#     name = models.CharField(max_length=128)
#
#     def __str__(self):
#         return self.name
#
#
# class PortfolioItem(models.Model):
#     archive_img = models.ImageField
#     title = models.CharField(max_length=250)
#     tag = models.ForeignKey(PortfolioTag, on_delete=models.CASCADE)
#
#
#     def __str__(self):
#         return self.title