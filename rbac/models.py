from django.db import models


class Menu(models.Model):
    title = models.CharField(verbose_name='菜单', max_length=32)
    icon = models.CharField(verbose_name='图标', max_length=32)

    def __str__(self):
        return self.title

class Permission(models.Model):
    """
    权限表
    """
    title = models.CharField(verbose_name='标题', max_length=32)
    url = models.CharField(verbose_name='含正则的URL', max_length=128)

    pid = models.ForeignKey(verbose_name='关联的权限',to='Permission',blank=True,null=True,help_text='用户选择二级菜单',
                               related_name='parents',on_delete=models.CASCADE)

    name = models.CharField(verbose_name='URL',unique=True,max_length=32)

    # is_menu = models.BooleanField(verbose_name='make a list',default=False)
    # icon = models.CharField(verbose_name='icon',max_length=32,null=True,blank=True) #表示可以为空

    menu = models.ForeignKey(verbose_name='菜单',to='Menu',blank=True,null=True,help_text='null表示非菜单',on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Role(models.Model):
    """
    角色
    """
    title = models.CharField(verbose_name='角色名称', max_length=32)
    permission = models.ManyToManyField(verbose_name='拥有的所有权限', to='Permission', blank=True)

    def __str__(self):
        return self.title


class UserInfo(models.Model):
    """
    用户表
    """
    name = models.CharField(verbose_name='用户名', max_length=32)
    password = models.CharField(verbose_name='密码', max_length=64)
    email = models.CharField(verbose_name='邮箱', max_length=32)
    role = models.ManyToManyField(verbose_name='拥有的所有角色', to='Role', blank=True)

    def __str__(self):
        return self.name
