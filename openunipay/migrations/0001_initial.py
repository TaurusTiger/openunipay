# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-17 13:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AliPayOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('out_trade_no', models.CharField(db_index=True, editable=False, max_length=32, verbose_name='商户订单号')),
                ('subject', models.CharField(editable=False, max_length=128, verbose_name='商品名称')),
                ('body', models.CharField(editable=False, max_length=512, verbose_name='商品详情')),
                ('total_fee', models.DecimalField(decimal_places=2, editable=False, max_digits=6, verbose_name='总金额(单位:元)')),
                ('it_b_pay', models.CharField(editable=False, max_length=19, verbose_name='交易有效期')),
                ('interface_data', models.TextField(editable=False, max_length=500, verbose_name='接口数据')),
                ('date_create', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name_plural': '支付宝订单',
                'verbose_name': '支付宝订单',
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('orderno', models.CharField(editable=False, max_length=50, primary_key=True, serialize=False, verbose_name='订单号')),
                ('user', models.CharField(blank=True, max_length=50, null=True, verbose_name='用户标识')),
                ('product_desc', models.CharField(max_length=128, verbose_name='商品描述')),
                ('product_detail', models.TextField(max_length=1000, verbose_name='商品详情')),
                ('fee', models.DecimalField(decimal_places=0, max_digits=6, verbose_name='金额(单位:分)')),
                ('attach', models.CharField(blank=True, max_length=127, null=True, verbose_name='附加数据')),
                ('dt_start', models.DateTimeField(editable=False, verbose_name='交易开始时间')),
                ('dt_end', models.DateTimeField(editable=False, verbose_name='交易失效时间')),
                ('dt_pay', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='付款时间')),
                ('paied', models.BooleanField(default=False, editable=False, verbose_name='已收款')),
                ('lapsed', models.BooleanField(default=False, editable=False, verbose_name='已失效')),
                ('payway', models.CharField(choices=[('WEIXIN', '微信支付'), ('ALI', '支付宝支付')], default='WEIXIN', max_length=10, verbose_name='支付方式')),
                ('date_create', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('date_update', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
            ],
            options={
                'verbose_name_plural': '付款单',
                'verbose_name': '付款单',
            },
        ),
        migrations.CreateModel(
            name='WeiXinOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appid', models.CharField(editable=False, max_length=32, verbose_name='公众账号ID')),
                ('mch_id', models.CharField(editable=False, max_length=32, verbose_name='商户号')),
                ('body', models.CharField(editable=False, max_length=128, verbose_name='商品描述')),
                ('attach', models.CharField(blank=True, editable=False, max_length=127, null=True, verbose_name='附加数据')),
                ('out_trade_no', models.CharField(db_index=True, editable=False, max_length=32, verbose_name='商户订单号')),
                ('fee_type', models.CharField(editable=False, max_length=16, verbose_name='货币类型')),
                ('total_fee', models.SmallIntegerField(editable=False, verbose_name='总金额')),
                ('spbill_create_ip', models.CharField(editable=False, max_length=16, verbose_name='终端IP')),
                ('time_start', models.CharField(editable=False, max_length=14, verbose_name='交易起始时间')),
                ('time_expire', models.CharField(editable=False, max_length=14, verbose_name='交易结束时间')),
                ('notify_url', models.CharField(editable=False, max_length=256, verbose_name='通知地址')),
                ('trade_type', models.CharField(editable=False, max_length=16, verbose_name='交易类型')),
            ],
            options={
                'verbose_name_plural': '微信统一订单',
                'verbose_name': '微信统一订单',
            },
        ),
        migrations.CreateModel(
            name='AliPayResult',
            fields=[
                ('order', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='pay_result', serialize=False, to='openunipay.AliPayOrder')),
                ('notify_time', models.CharField(blank=True, editable=False, max_length=19, null=True, verbose_name='通知时间')),
                ('notify_type', models.CharField(blank=True, editable=False, max_length=50, null=True, verbose_name='通知类型')),
                ('notify_id', models.CharField(blank=True, editable=False, max_length=50, null=True, verbose_name='通知校验ID')),
                ('out_trade_no', models.CharField(blank=True, editable=False, max_length=32, null=True, verbose_name='商户订单号')),
                ('subject', models.CharField(blank=True, editable=False, max_length=128, null=True, verbose_name='商品名称')),
                ('trade_no', models.CharField(blank=True, editable=False, max_length=64, null=True, verbose_name='支付宝交易号')),
                ('trade_status', models.CharField(blank=True, editable=False, max_length=16, null=True, verbose_name='交易状态')),
                ('seller_id', models.CharField(blank=True, editable=False, max_length=30, null=True, verbose_name='卖家支付宝用户号')),
                ('seller_email', models.CharField(blank=True, editable=False, max_length=100, null=True, verbose_name='卖家支付宝账号')),
                ('buyer_id', models.CharField(blank=True, editable=False, max_length=30, null=True, verbose_name='买家支付宝用户号')),
                ('buyer_email', models.CharField(blank=True, editable=False, max_length=100, null=True, verbose_name='买家支付宝账号  ')),
                ('total_fee', models.DecimalField(blank=True, decimal_places=2, editable=False, max_digits=6, null=True, verbose_name='总金额(单位:元)')),
            ],
        ),
        migrations.CreateModel(
            name='WeiXinPayResult',
            fields=[
                ('order', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='pay_result', serialize=False, to='openunipay.WeiXinOrder')),
                ('prepayid', models.CharField(blank=True, db_index=True, editable=False, max_length=64, null=True, verbose_name='预支付交易会话标识')),
                ('openid', models.CharField(blank=True, editable=False, max_length=128, null=True, verbose_name='用户标识(openId)')),
                ('bank_type', models.CharField(blank=True, editable=False, max_length=16, null=True, verbose_name='付款银行')),
                ('total_fee', models.SmallIntegerField(blank=True, editable=False, null=True, verbose_name='总金额')),
                ('attach', models.CharField(blank=True, editable=False, max_length=128, null=True, verbose_name='商户附加数据')),
                ('tradestate', models.CharField(blank=True, editable=False, max_length=32, null=True, verbose_name='交易状态')),
                ('tradestatedesc', models.CharField(blank=True, editable=False, max_length=256, null=True, verbose_name='交易状态描述')),
            ],
        ),
    ]
