from django.conf import settings
from django.db import models
from django.utils import timezone

#models.ModelはPostがDjangoモデルであり、Djangoがこれをデータベースに保存するべきだとわかるようにしてます・
class Post(models.Model):
   
   author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # 他のモデルへのリンク
   title = models.CharField(max_length=200)  # 制限あり文字フィールド
   text = models.TextField() # 制限なしテキストフィールド
   created_date = models.DateTimeField(default=timezone.now)  # 日付、時間のフィールド
   published_date = models.DateTimeField(blank=True, null=True)

   def publish(self):
      self.published_date = timezone.now()
      self.save()

   def __str__(self):
      return self.title