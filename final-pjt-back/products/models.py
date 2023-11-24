from django.db import models

# Create your models here.
class DepositProducts(models.Model):
    fin_co_no = models.CharField(max_length=10)
    kor_co_nm = models.TextField()
    fin_prdt_cd = models.TextField(unique=True)
    fin_prdt_nm = models.TextField()
    dcls_month = models.IntegerField()
    join_member = models.TextField()
    join_deny = models.IntegerField()
    join_way = models.TextField()
    mtrt_int = models.TextField()
    spcl_cnd = models.TextField()
    etc_note = models.TextField()


class DepositOptions(models.Model):
    product = models.ForeignKey(DepositProducts, on_delete=models.CASCADE)
    fin_co_no = models.CharField(max_length=15)
    fin_prdt_cd = models.TextField()
    save_trm = models.IntegerField()
    intr_rate_type_nm = models.CharField(max_length=100)
    intr_rate = models.FloatField(null=True)
    intr_rate2 = models.FloatField(null=True)


class SavingProducts(models.Model):
    fin_co_no = models.CharField(max_length=10)
    kor_co_nm = models.TextField()
    fin_prdt_cd = models.TextField(unique=True)
    fin_prdt_nm = models.TextField()
    dcls_month = models.IntegerField()
    join_member = models.TextField()
    join_deny = models.IntegerField()
    join_way = models.TextField()
    mtrt_int = models.TextField()
    spcl_cnd = models.TextField()
    etc_note = models.TextField()
    max_limit = models.IntegerField(null=True)


class SavingOptions(models.Model):
    product = models.ForeignKey(SavingProducts, on_delete=models.CASCADE)
    fin_co_no = models.CharField(max_length=15)
    fin_prdt_cd = models.TextField()
    save_trm = models.IntegerField()
    intr_rate_type_nm = models.CharField(max_length=100)
    rsrv_type = models.CharField(max_length=10)
    rsrv_type_nm = models.CharField(max_length=10)
    intr_rate = models.FloatField(null=True)
    intr_rate2 = models.FloatField(null=True)