#coding:utf-8

from xadmin.plugins.actions import BaseActionView
from django.http import HttpResponse

class MyAction(BaseActionView):

    action_name = "my_action"  #: 相当于这个 Action 的唯一标示, 尽量用比较针对性的名字
    description = (u'停止运行Job') #: 描述, 出现在 Action 菜单中, 可以使用 ``%(verbose_name_plural)s`` 代替 Model 的名字.

    model_perm = "change" # 该Action 所需权限

    # 而后实现 do_action 方法
    def do_action(self, queryset):
        # queryset 是包含了已经选择的数据的 queryset
        for obj in queryset:
            # obj 的操作
            print obj
        # 返回 HttpResponse
        return HttpResponse("success")