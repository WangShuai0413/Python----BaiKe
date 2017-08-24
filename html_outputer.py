#coding:utf8
'''
Created on 2017年8月22日

@author: wshuai
'''
class HtmlOutputer(object):
    
    def __init__(self):
        self.datas = []
        
    
    def output_html(self):
        html = open('output.html','a')
        
        html.write("<html>")
        html.write('<header><meta http-equiv="Content-Type" content="text/html; charset=utf-8" /></header>')
        html.write("<body>")
        html.write("<table border='1'>")
        html.write("<tr><th>名称</th><th>解释</th></tr>")
        for data in self.datas:
            html.write("<tr>")
#             html.write("<td>%s</td>" %data['url'])
            html.write("<td>%s</td>" %data['title'].encode('utf-8'))
            html.write("<td>%s</td>" %data['summary'].encode('utf-8'))
            html.write("</tr>")
        
        
        html.write("</table>")
        html.write("</body>")
        html.write("</html>")
        
        html.close()
        

    
    def collect_data(self, data):
        if data is None:
            return
        
        self.datas.append(data) 
    
    
    
    



