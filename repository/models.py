from django.db import models

# Create your models here.
'''
˵��ForeignKey��one-to-many�ģ�������һ���������ӣ�
�����������һ���ǳ��ֱ���һ�����������������һ��car�ֶΣ���ʾ�������Ӧ�ĳ���
���ڳ�����˵�������Ӧһ��car�����������������car�ֶ�Ӧ����ForeignKey����ʾ��
����������˵��һ������ֻ���ܶ�Ӧһ��car�����Ա�����OneToOneField��
OneToOneField(someModel) �������Ϊ ForeignKey(SomeModel, unique=True)��
����
�������ߵķ����ѯ���в��ģ�
����ForeignKey�����ѯ���ص���һ���б�һ�����ж�����ӣ���
����OneToOneField�����ѯ���ص���һ��ģ��ʾ������Ϊһ��һ��ϵ����
'''


class UserInfo(models.Model):
    '''
    �û���
    '''
    nid = models.BigAutoField(primary_key=True)
    username = models.CharField(verbose_name='�û���', max_length=32, unique=True)
    password = models.CharField(verbose_name='����', max_length=64)
    nickname = models.CharField(verbose_name='�ǳ�', max_length=32)
    email = models.EmailField(verbose_name='����', unique=True)
    avatar = models.ImageField(verbose_name='ͷ��')

    create_time = models.DateTimeField(verbose_name='����ʱ��', auto_now_add=True)


class Blog(models.Model):
    '''������Ϣ'''
    nid = models.BigIntegerField(primary_key=True)
    title = models.CharField(verbose_name='���˲��ͱ���', max_length=64)
    site = models.CharField(verbose_name='���˲���ǰ׺', max_length=32, unique=True)
    theme = models.CharField(verbose_name='��������', max_length=32)

    ##  һ��һ�� һ�����Ͷ�Ӧһ���û�
    user = models.OneToOneField(to='UserInfo', to_field='nid')


class UserFans(models.Model):
    '''
    ���۹�ϵ��
    '''
    user = models.ForeignKey(verbose_name='����', to='UserInfo', to_field='nid', related_name='users')
    follower = models.ForeignKey(verbose_name='��˿', to='UserInfo', to_field='nid', related_name='followers')

    class Meta:
        unique_together = [  ## ����Ψһ
            ('user', 'follower')
        ]


class CateGory(models.Model):
    '''
    �����������·���
    '''
    nid = models.AutoField(primary_key=True)
    title = models.CharField(verbose_name='�������', max_length=32)

    blog = models.ForeignKey(verbose_name='��������', to='Blog', to_field='nid')


class ArticleDetail(models.Model):
    '''
     ����������ϸ��
     content:����
     artice: ��������id --һ������ֻ��һ����Ҫ����
    '''
    content = models.TextField(verbose_name='��������')
    artice = models.OneToOneField(verbose_name='��������', to='Article', to_field='nid')


class UpDown(models.Model):
    '''
    ���²Ȼ����Ƕ�
    article ���Ȼ��޵�����--- ��Ӧһƪ����
    user�� ˭�ȵġ�����վ---- ��Ӧһ���û�
    up���޻����ǲ�
    '''

    article = models.ForeignKey(verbose_name='����', to='Article', to_field='nid')
    user = models.ForeignKey(verbose_name='�޻��߲ȵ��û�', to='UserInfo', to_field='nid')
    up = models.BooleanField(verbose_name='�Ȼ�����')




