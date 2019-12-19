from django.conf import settings
from django.db import models
from django.utils import timezone


class Version(models.Model):
	v_number  = models.IntegerField(verbose_name='バージョン番号', default=None)
	v_title = models.CharField(verbose_name='バージョン名', default=None, max_length=200)

	def __str__(self):
		return "IIDX{}/{}".format(self.v_number, self.v_title)


class Music(models.Model):
	whohas = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # 誰所有？
	n = models.IntegerField(verbose_name='Normal', default=None)
	h = models.IntegerField(verbose_name='Hyper', default=None)
	a = models.IntegerField(verbose_name='Another', default=None)
	title = models.CharField(max_length=200)
	version = models.ForeignKey(Version, on_delete=models.CASCADE, null=True)
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)

	# def publish(self):
	#     self.published_date = timezone.now()
	#     self.save()

	def __str__(self):
		return "{}".format(self.title)
