from django.db import models

# Create your models here.

class apicase(models.Model):

    item = models.CharField(max_length=128)
    release = models.CharField(max_length=128)
    modules = models.CharField(max_length=128)
    casename = models.CharField(max_length=128)
    casenumber = models.CharField(max_length=128)
    caseurl = models.CharField(max_length=300)
    caserequest = models.CharField(max_length=30)
    caseheaders = models.CharField(max_length=300)
    casebody = models.CharField(max_length=1000)
    caseexpected = models.CharField(max_length=1000)
    casedeliver = models.CharField(max_length=300)
    casekey = models.CharField(max_length=300)
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.item

    class Meta:
        ordering = ["-c_time"]
        verbose_name = "接口用例"
        verbose_name_plural = "接口用例"

class apilist(models.Model):

    item = models.CharField(max_length=128)
    release = models.CharField(max_length=128)
    modules = models.CharField(max_length=128)
    casename = models.CharField(max_length=500)
    caselists =  models.CharField(max_length=1000)
    case_id = models.AutoField(primary_key=True)
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.item

    class Meta:
        ordering = ["-c_time"]
        verbose_name = "接口用例"
        verbose_name_plural = "接口用例"

class reportlist(models.Model):

    reportname = models.CharField(max_length=128)
    reportclass = models.CharField(max_length=128,default="")
    report = models.CharField(max_length=5000)
    report_id = models.AutoField(primary_key=True)
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.reportname

    class Meta:
        ordering = ["-c_time"]
        verbose_name = "测试报告"
        verbose_name_plural = "测试报告"