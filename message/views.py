from django.shortcuts import render
from django.urls import *
from django.views.generic import *
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
# 留言列表
class MessageList(LoginRequiredMixin,ListView):
    model = Message
    ordering = ['-id']  # 依 id 欄位由大至小排序
    # 未指定 template_name 屬性，預設使用 message/message_list.html

# 檢視留言
class MessageDetail(LoginRequiredMixin,DetailView):
    model = Message
    # 未指定 template_name 屬性，預設使用 message/message_detail.html

# 新增留言
class MessageCreate(LoginRequiredMixin,CreateView):
    model = Message
    fields = '__all__'          # 顯示 *所有* 欄位
    #success_url = '/message/'   # 新增成功後，導向留言列表頁面
    # 未指定 template_name 屬性，預設使用 message/message_form.html
    def get_success_url(self):
        return reverse('msg_list')
class MessageDelete(LoginRequiredMixin,DeleteView):
    model = Message

    def get_success_url(self):
        return reverse('msg_list')
