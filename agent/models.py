from django.db import models

# Create your models here.
from django.db import models


class Mirror(models.Model):
    name = models.CharField(max_length=64)
    http_url = models.CharField(max_length=256, null=True, blank=True)
    https_url = models.CharField(max_length=256, null=True, blank=True)
    ftp_url = models.CharField(max_length=256, null=True, blank=True)
    rsync_url = models.CharField(max_length=256, null=True, blank=True)
    sponsor_url = models.CharField(max_length=64, blank=True)
    authorized_ipv4 = models.GenericIPAddressField(blank=True, null=True)
    authorized_ipv6 = models.GenericIPAddressField(blank=True, null=True)

    tier_level_choices = (
        ('0', 'Master'),
        ('1', 'Tier 1'),
        ('2', 'Tier 2'),
        ('3', 'Tier 3'),
        ('4', 'Tier ?'),
    )
    tier_level = models.CharField(max_length=1, choices=tier_level_choices, default='4')
    iso = models.BooleanField(default=True)
    repo = models.BooleanField(default=True)
    active = models.BooleanField(default=True)
    contact_name = models.CharField(max_length=64, blank=True)
    contact_mail = models.EmailField(blank=True)
    stats_url = models.CharField(max_length=256, blank=True)
    notice = models.TextField(max_length=4096, default='')

