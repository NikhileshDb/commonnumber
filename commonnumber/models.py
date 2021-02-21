from django.db import models





class TeerResult(models.Model):
    firstresult = models.IntegerField(verbose_name='FR', null=True, blank=True)
    secondresult = models.IntegerField(verbose_name='SR', null=True, blank=True)
    date = models.DateField(auto_now=False, null=True, blank=True)
    commonnumber = models.CharField(max_length=20, null=True, blank=True)
    def __str__(self):
        return (str(self.date) +' | '+'FR-'+ str(self.firstresult)+' / '+'SR-' + str(self.secondresult))



