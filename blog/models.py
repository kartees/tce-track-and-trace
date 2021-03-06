from django.db import models


# Create your models here.
class Equipment(models.Model):
    section = models.IntegerField(null=True)
    condition = models.CharField(null=True, max_length=50)
    condition_code = models.CharField(null=True, max_length=50)
    from_date = models.DateTimeField(null=True, auto_now=False, auto_now_add=False)
    to_date = models.DateTimeField(null=True, auto_now=False, auto_now_add=False)
    duration = models.TimeField(auto_now=False, auto_now_add=False)
    # OPERATNG = 'OPERATNG'
    # UNAVAILABLE = 'UNAVAILABLE'
    # IDLE = 'IDLE'
    # CONDITION = (
    #     (OPERATNG, 'Operating'),
    #     (UNAVAILABLE, 'Unavailable'),
    #     (IDLE, 'Idle'),
    # )
    # condition = models.CharField(max_length=2,
    #                                   choices=CONDITION,
    #                                   default=OPERATNG)


class Parameter(models.Model):
    from_date = models.DateTimeField(null=True, auto_now=False, auto_now_add=False)
    to_date = models.DateTimeField(null=True, auto_now=False, auto_now_add=False)
    Signal_Energy_avg = models.FloatField(null=True)
    Signal_Energy_max = models.FloatField(null=True)
    Signal_Energy_min = models.FloatField(null=True)
    Velocity_X_avg = models.FloatField(null=True)
    Velocity_X_max = models.FloatField(null=True)
    Velocity_X_min = models.FloatField(null=True)
    Velocity_Y_min = models.FloatField(null=True)
    Velocity_Y_max = models.FloatField(null=True)
    Velocity_Y_avg = models.FloatField(null=True)
    Velocity_Z_min = models.FloatField(null=True)
    Velocity_Z_max = models.FloatField(null=True)
    Velocity_Z_avg = models.FloatField(null=True)
    Temperature_min = models.FloatField(null=True)
    Temperature_avg = models.FloatField(null=True)
    Temperature_max = models.FloatField(null=True)
    Noise_min = models.FloatField(null=True)
    Noise_avg = models.FloatField(null=True)
    Noise_max = models.FloatField(null=True)


class Var(models.Model):
    name = models.CharField(null=True, max_length=50)
    description = models.CharField(null=True, max_length=50)
    serverName = models.CharField(null=True, max_length=50)
    topicName = models.CharField(null=True, max_length=50)
    address = models.CharField(null=True, max_length=50)
    coef = models.FloatField(null=True)
    offset = models.FloatField(null=True)
    logEnabled = models.BooleanField(null=True)
    alEnabled = models.BooleanField(null=True)
    alBool = models.BooleanField(null=True)
    memTag = models.BooleanField(null=True)
    mbsTcpEnabled = models.BooleanField(null=True)
    mbsTcpFloat = models.BooleanField(null=True)
    snmpEnabled = models.BooleanField(null=True)
    rTLogEnabled = models.BooleanField(null=True)
    alAutoAck = models.BooleanField(null=True)
    forceRO = models.BooleanField(null=True)
    snmpOID = models.BooleanField(null=True)
    autoType = models.BooleanField(null=True)
    alHint = models.CharField(null=True, max_length=50)
    alHigh = models.FloatField(null=True)
    alLow = models.FloatField(null=True)
    alTimeDB = models.BooleanField(null=True)
    alLevelDB = models.FloatField(null=True)
    IVGroupA = models.BooleanField(null=True)
    IVGroupB = models.BooleanField(null=True)
    IVGroupC = models.BooleanField(null=True)
    IVGroupD = models.BooleanField(null=True)
    pageId = models.IntegerField(null=True)
    RTLogWindow = models.IntegerField(null=True)
    RTLogTimer = models.IntegerField(null=True)
    logDB = models.FloatField(null=True)
    LogTimer = models.BooleanField(null=True)
    AlLoLo = models.CharField(null=True, max_length=50)
    AlHiHi = models.CharField(null=True, max_length=50)
    MbsTcpRegister = models.BooleanField(null=True)
    mbsTcpCoef = models.FloatField(null=True)
    mbsTcpOffset = models.FloatField(null=True)
    EEN = models.CharField(null=True, max_length=50)
    ETO = models.CharField(null=True, max_length=50)
    ECC = models.CharField(null=True, max_length=50)
    ESU = models.CharField(null=True, max_length=50)
    EAT = models.CharField(null=True, max_length=50)
    ESH = models.CharField(null=True, max_length=50)
    SEN = models.CharField(null=True, max_length=50)
    STO = models.CharField(null=True, max_length=50)
    SSU = models.CharField(null=True, max_length=50)
    TEN = models.CharField(null=True, max_length=50)
    TSU = models.CharField(null=True, max_length=50)
    FEN = models.CharField(null=True, max_length=50)
    FFN = models.CharField(null=True, max_length=50)
    FCO = models.CharField(null=True, max_length=50)
    KPI = models.BooleanField(null=True)
    UseCustomUnit = models.BooleanField(null=True)
    Type = models.IntegerField(null=True)
    Unit = models.CharField(null=True, max_length=50)
    AlStat = models.BooleanField(null=True)
    ChangeTime = models.CharField(null=True, max_length=50)
    tagValue = models.IntegerField(null=True)
    tagQuality = models.IntegerField(null=True)
    AlType = models.BooleanField(null=True)
