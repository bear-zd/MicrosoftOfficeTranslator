# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 21:29:41 2020

@author: a8275
"""


import win32com.client
import BaiduTranslatorAPI

def PPtTranslator(filepath):
    ppt=win32com.client.Dispatch('PowerPoint.Application')
    ppt.Visible=1
    ppt_open=ppt.Presentations.Open(filepath)
    slide_count=ppt_open.Slides.Count #ppt的页数
    for i in range(1,slide_count+1):
        shapes_count=ppt_open.Slides(i).Shapes.Count
        print(f"—————————————————————读取第{i}页—————————————————————")
        for j in range(1,shapes_count+1):
            if ppt_open.Slides(i).Shapes(j).HasTextFrame:
                Textframe=ppt_open.Slides(i).Shapes(j)
                text=Textframe.TextFrame.TextRange.Text
                TranslatedText=BaiduTranslatorAPI.BaiduTranslator(text)
                if TranslatedText==-1:
                    continue
                try:
                    Textframe.TextFrame.TextRange.Text=TranslatedText
                except com_error :
                    print("There is something wrong!")
                else:
                    print(f"—————————————第{i}页第{j}元素翻译完成—————————————")
    path,after=filepath.split('.')
    ppt_open.saveas(path+'-副本.'+after)   
            
#def WordTranslator(filepath):
#    word=win32com.client.Dispatch('Word.Application')
#    word.Visible=0
PPtTranslator(r'C:\Users\a8275\Desktop\git仓库\ppt翻译\TestPPt.ppt')