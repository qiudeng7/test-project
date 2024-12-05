from django.db import models

class BaseModel(models.Model):
    # 所有模型共有的基础字段
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    version = models.IntegerField(default=1, verbose_name="版本号")
    is_deleted = models.BooleanField(default=False, verbose_name="是否已删除")
    # submitter = models.ForeignKey('Employee', on_delete=models.CASCADE, related_name='%(class)s_submitted', verbose_name="提交人")

    class Meta:
        abstract = True

class Approval(BaseModel):
    # 审批表
    approval_content = models.TextField(verbose_name="审批内容")
    submitter = models.ForeignKey('Employee', on_delete=models.CASCADE, related_name='approvals_submitted', verbose_name="提交人")
    approver = models.ForeignKey('Employee', on_delete=models.CASCADE, related_name='approvals_approved', verbose_name="审批人")

class Customer(BaseModel):
    # 客户表
    name = models.CharField(max_length=255, verbose_name="名称")
    customer_group = models.CharField(max_length=255, verbose_name="客户群")
    contact_person = models.CharField(max_length=255, verbose_name="联系人")
    contact_method = models.CharField(max_length=255, verbose_name="联系方式")  # 微信或电话
    media_person = models.ForeignKey('Employee', on_delete=models.CASCADE, related_name='customers_media', verbose_name="媒介")
    business_person = models.ForeignKey('Employee', on_delete=models.CASCADE, related_name='customers_business', verbose_name="商务")
    advance_limit = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="垫款额度")
    temporary_advance_limit = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="临时垫款额度")
    repayment_cycle = models.IntegerField(verbose_name="回款周期")
    petty_cash = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="备用金")

class Agent(BaseModel):
    # 代理商表
    name = models.CharField(max_length=255, verbose_name="名称")
    agent_group = models.CharField(max_length=255, verbose_name="代理商群")
    placement_type = models.CharField(max_length=255, verbose_name="投放类型")  # 投放类型
    payment_method = models.CharField(max_length=255, verbose_name="支付方式")  # 支付方式

class Account(BaseModel):
    # 账户表：平台账户
    account_id = models.CharField(max_length=255, db_index=True, verbose_name="账户ID")
    account_name = models.CharField(max_length=255, verbose_name="账户名称")
    customer_group = models.CharField(max_length=255, verbose_name="客户群")
    media_person = models.ForeignKey('Employee', on_delete=models.CASCADE, related_name='accounts_media', verbose_name="媒介",null=True)
    agent = models.ForeignKey('Agent', on_delete=models.CASCADE, related_name='accounts_agent', verbose_name="代理商",null=True)

class Employee(BaseModel):
    # 员工表
    position = models.CharField(max_length=255, verbose_name="职位")
    base_salary = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="底薪")
    commission = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="提成")

class Contract(BaseModel):
    # 合同表
    contract_number = models.CharField(max_length=255, verbose_name="合同编号")
    file_content = models.TextField(verbose_name="文件内容")
    signed_date = models.DateTimeField(verbose_name="签订时间")
    expiration_date = models.DateTimeField(verbose_name="截止时间")
    business_person = models.ForeignKey('Employee', on_delete=models.CASCADE, related_name='contracts_business', verbose_name="商务")
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE, related_name='contracts_customer', verbose_name="客户")

class PlatformAccountRecharge(BaseModel):
    # 平台账户充值表
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='recharges', verbose_name="账户")
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="金额")
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE, related_name='recharges_agent', verbose_name="代理商")