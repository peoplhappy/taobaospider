#coding=utf-8
#python 从json中提取值，或从html中获取
import json
import sys
import re
import bs4


def findvalue(str1, index):
    findpattern = r"\((.*)\)"
    searchobj = re.match(findpattern, index)
    if searchobj:
        if isinstance(str1,str):
            str1=json.loads(str1)
        if isinstance(str1,list):
            lst=[]
            condition = searchobj.group(1)
            condpattern = r"(\S+)\.(\S+)\((\S+)\)"
            searchcond = re.findall(condpattern, condition)
            if searchcond:
                for i in range(len(str1)):
                    value=str1[i]
                    valuelist=[]
                    for j in range(len(searchcond)):
                        label=searchcond[j][0]
                        methodname=searchcond[j][1]
                        params=searchcond[j][2]
                        valuelist.append(domethod(value,label,methodname,params))
                    if combinecond(condition,valuelist):
                        lst.append(value)
            return lst
    else:
        return getvalue(index, str1)

def combinecond(str,valuelist):
    pattern = r"\s+(and|or)\s+"
    searchobj=re.findall(pattern,str)
    result = valuelist[0];
    if searchobj:

        for i in range(len(searchobj)):
            if searchobj[i]=="and":
                result=result and valuelist[i+1]
            elif searchobj[i] =="or":
                result = result or valuelist[i+1]
    return result

#调用方法
def domethod(value,label,methondname,params):
    if methondname=="contains":
        return params in value[label]
    elif methondname=="isgreater":
        return value[label]>params
    elif methondname=="islesser":
        return value[label]<params
    elif methondname=="equals":
        return str(value[label])==params
    elif methondname=="islesserEqual":
        return value[label]<=params
    elif methondname=="isgreaterEqual":
        return value[label]>=params
    else:
        pass
        #print("unkown method cant do")

def getvalue(index, str1):
    if isinstance(str1,str):
        str1=json.loads(str1)
    if str(index).isdigit():
        index = int(index)
    else:
        index = str(index)
    return str1[index]

def getjsonvalue(jsondata, valuepath):
    data = json.loads(jsondata)
    # print(data)
    path = str.split(valuepath, "/")
    if len(path) == 0 or valuepath.strip() == "" or valuepath == "/":
        return jsondata
    result = data
    for obj in range(len(path)):
        result=findvalue(result,path[obj])
    return result

def gethtmlvalue(htmldata,selectpath, index):
    soup=bs4.BeautifulSoup(htmldata,"lxml")
    print(soup.select(selectpath)[index].string)
def readFile(path):
    file=open(path,"r", encoding="utf-8")
    str=file.read();
    return str


if __name__=="__main__":
    type=None
    #jsondata=readFile(sys.argv[2])
    #valuepath=sys.argv[3]
    #print(jsondata)
    #
    if(type=="json"):
      print(getjsonvalue(jsondata,valuepath))
    elif(type=="html"):
      print(gethtmlvalue(jsondata,valuepath))
    #jsondata=readFile("D:/projectautotest/temp.txt")
    #jsondata = jsondata.replace("\"{", "{").replace("}\"", "}").replace("\"[", "[").replace("]\"", "]").replace("\"\"",
    #print(jsondata)
    #print(getjsonvalue(jsondata, "responseValue/content/(name.equals(555))"))
    str="""<html data-ng-app="App" class="ng-scope"><head><style type="text/css">[uib-typeahead-popup].dropdown-menu{display:block;}</style><style type="text/css">.uib-time input{width:50px;}</style><style type="text/css">[uib-tooltip-popup].tooltip.top-left > .tooltip-arrow,[uib-tooltip-popup].tooltip.top-right > .tooltip-arrow,[uib-tooltip-popup].tooltip.bottom-left > .tooltip-arrow,[uib-tooltip-popup].tooltip.bottom-right > .tooltip-arrow,[uib-tooltip-popup].tooltip.left-top > .tooltip-arrow,[uib-tooltip-popup].tooltip.left-bottom > .tooltip-arrow,[uib-tooltip-popup].tooltip.right-top > .tooltip-arrow,[uib-tooltip-popup].tooltip.right-bottom > .tooltip-arrow,[uib-tooltip-html-popup].tooltip.top-left > .tooltip-arrow,[uib-tooltip-html-popup].tooltip.top-right > .tooltip-arrow,[uib-tooltip-html-popup].tooltip.bottom-left > .tooltip-arrow,[uib-tooltip-html-popup].tooltip.bottom-right > .tooltip-arrow,[uib-tooltip-html-popup].tooltip.left-top > .tooltip-arrow,[uib-tooltip-html-popup].tooltip.left-bottom > .tooltip-arrow,[uib-tooltip-html-popup].tooltip.right-top > .tooltip-arrow,[uib-tooltip-html-popup].tooltip.right-bottom > .tooltip-arrow,[uib-tooltip-template-popup].tooltip.top-left > .tooltip-arrow,[uib-tooltip-template-popup].tooltip.top-right > .tooltip-arrow,[uib-tooltip-template-popup].tooltip.bottom-left > .tooltip-arrow,[uib-tooltip-template-popup].tooltip.bottom-right > .tooltip-arrow,[uib-tooltip-template-popup].tooltip.left-top > .tooltip-arrow,[uib-tooltip-template-popup].tooltip.left-bottom > .tooltip-arrow,[uib-tooltip-template-popup].tooltip.right-top > .tooltip-arrow,[uib-tooltip-template-popup].tooltip.right-bottom > .tooltip-arrow,[uib-popover-popup].popover.top-left > .arrow,[uib-popover-popup].popover.top-right > .arrow,[uib-popover-popup].popover.bottom-left > .arrow,[uib-popover-popup].popover.bottom-right > .arrow,[uib-popover-popup].popover.left-top > .arrow,[uib-popover-popup].popover.left-bottom > .arrow,[uib-popover-popup].popover.right-top > .arrow,[uib-popover-popup].popover.right-bottom > .arrow,[uib-popover-html-popup].popover.top-left > .arrow,[uib-popover-html-popup].popover.top-right > .arrow,[uib-popover-html-popup].popover.bottom-left > .arrow,[uib-popover-html-popup].popover.bottom-right > .arrow,[uib-popover-html-popup].popover.left-top > .arrow,[uib-popover-html-popup].popover.left-bottom > .arrow,[uib-popover-html-popup].popover.right-top > .arrow,[uib-popover-html-popup].popover.right-bottom > .arrow,[uib-popover-template-popup].popover.top-left > .arrow,[uib-popover-template-popup].popover.top-right > .arrow,[uib-popover-template-popup].popover.bottom-left > .arrow,[uib-popover-template-popup].popover.bottom-right > .arrow,[uib-popover-template-popup].popover.left-top > .arrow,[uib-popover-template-popup].popover.left-bottom > .arrow,[uib-popover-template-popup].popover.right-top > .arrow,[uib-popover-template-popup].popover.right-bottom > .arrow{top:auto;bottom:auto;left:auto;right:auto;margin:0;}[uib-popover-popup].popover,[uib-popover-html-popup].popover,[uib-popover-template-popup].popover{display:block !important;}</style><style type="text/css">.uib-datepicker-popup.dropdown-menu{display:block;float:none;margin:0;}.uib-button-bar{padding:10px 9px 2px;}</style><style type="text/css">.uib-position-measure{display:block !important;visibility:hidden !important;position:absolute !important;top:-9999px !important;left:-9999px !important;}.uib-position-scrollbar-measure{position:absolute !important;top:-9999px !important;width:50px !important;height:50px !important;overflow:scroll !important;}.uib-position-body-scrollbar-measure{overflow:scroll !important;}</style><style type="text/css">.uib-datepicker .uib-title{width:100%;}.uib-day button,.uib-month button,.uib-year button{min-width:100%;}.uib-left,.uib-right{width:100%}</style><style type="text/css">.ng-animate.item:not(.left):not(.right){-webkit-transition:0s ease-in-out left;transition:0s ease-in-out left}</style><style type="text/css">@charset "UTF-8";[ng\:cloak],[ng-cloak],[data-ng-cloak],[x-ng-cloak],.ng-cloak,.x-ng-cloak,.ng-hide:not(.ng-hide-animate){display:none !important;}ng\:form{display:block;}.ng-animate-shim{visibility:hidden;}.ng-anchor{position:absolute;}</style> <meta charset="utf-8"> <title>考生端</title> <meta name="description" content=""> <meta name="viewport" content="width=device-width,initial-scale=1,maximum-scale=1,minimum-scale=1,user-scalable=0"> <link rel="stylesheet" href="styles/vendor.8888683c.css"> <link rel="stylesheet" href="styles/app.d35b4e43.css"> <link rel="stylesheet" href="styles/main.6574d436.css"> <script>// 重命名 Electron 提供的 require 详细请参考：https://www.w3cschool.cn/electronmanual/electronmanual-electron-faq.html
	    	if(typeof(require) != "undefined"){
	    		window.nodeRequire = require;
					delete window.require;
					delete window.exports;
					delete window.module;
	    	}</script> <link rel="stylesheet" href="https://ecs-dev.qmth.com.cn:8878/oe/scripts/theme/default/layer.css?v=3.1.1" id="layuicss-layer"></head> <body data-ng-controller="AppController" onpaste="return false" oncopy="return false" oncut="return false" class="ng-scope"> <!-- uiView:  --><div class="app ng-scope app-header-fixed app-aside-fixed" id="top" data-ui-view="" data-ng-class="{'app-header-fixed': app.settings.headerFixed, 'app-aside-fixed': app.settings.asideFixed, 'app-aside-folded': app.settings.asideFolded, 'app-aside-dock': app.settings.asideDock, 'container': app.settings.container}" style=""><!-- uiView:  --><div ui-view="" class="fade-in-right smooth ng-scope"><div class="container ng-scope"> <div class="login-bg-5"></div> <div class="panel panel-default login-panel-5 col-xs-12 col-md-4 col-md-offset-4"> <!--远程教育网络考试</p>--> <div class="panel-heading"> <h3 class="text-center ng-binding">远程教育网络考试</h3> </div> <div class="panel-body" style="padding-top: 0"> <form class="login-form form-validation ng-valid-maxlength ng-dirty ng-valid-parse ng-valid ng-valid-required" name="loginForm" novalidate="" data-ng-submit="login()" style=""> <div class="form-group"> <label class="i-checks"> <input type="radio" name="a" value="STUDENT_CODE" data-ng-model="user.accountType" class="ng-pristine ng-untouched ng-valid"> <i></i> 学号 </label> <label class="i-checks" style="margin-left: 20px"> <input type="radio" name="a" value="STUDENT_IDENTITY_NUMBER" data-ng-model="user.accountType" class="ng-valid ng-dirty ng-valid-parse ng-touched" style=""> <i></i> 身份证号 </label> </div> <div class="form-group"> <div class="input-group"> <span class="input-group-addon">&nbsp;<i class="fa fa-user"></i></span> <input type="text" name="loginName" placeholder="账号" class="form-control ng-valid-maxlength ng-dirty ng-valid-parse ng-valid ng-valid-required ng-touched" dirty-blur="" ng-model="user.accountValue" required="" maxlength="50" style=""> </div> <div ng-messages="loginForm.loginName.$error" ng-visible="(loginForm.loginName.$touched || loginForm.$submitted) &amp;&amp; loginForm.loginName.$invalid" class="ng-inactive" style="visibility: hidden;"> &nbsp; <!-- ngMessage: required --> </div> </div> <div class="form-group"> <div class="input-group"> <span class="input-group-addon"><i class="fa fa-key"></i></span> <input type="password" name="password" placeholder="密码" class="form-control ng-valid-maxlength ng-dirty ng-valid-parse ng-valid ng-valid-required ng-touched" dirty-blur="" ng-model="user.password" required="" maxlength="50" style=""> </div> <div ng-messages="loginForm.password.$error" ng-visible="(loginForm.password.$touched || loginForm.$submitted) &amp;&amp; loginForm.password.$invalid" class="ng-inactive" style="visibility: hidden;"> &nbsp; <!-- ngMessage: required --> </div> </div> <p class="text-error text-center ng-binding" ng-bind="loginErrMsg"></p> <div class="form-group"> <div class="hbox"> <div class="col" style="padding-right: 5px"> <button class="btn btn-block btn-danger submit ajax-post ng-binding" type="submit" ng-bind="btnText" ng-disabled="loginButtonDisabled">登录</button> </div> <div class="col" style="padding-left: 5px"> <button class="btn btn-block btn-default" ng-click="closeApp()">关闭</button> </div> </div> </div> </form> </div> </div> <div style="position: absolute"> <img ng-src="/api/ecs_core/org/logo?domain=undefined" class="logo" width="200" src="/api/ecs_core/org/logo?domain=undefined"> </div> </div></div></div> <div class="pager-loading text-white hide" data-pager-loading=""><i class="fa fa-spinner fa-spin fa-5x m-b"></i><p class="text-base">数据加载中...</p></div> <div id="toast-container" ng-class="[config.position, config.animation]" class="toast-top-right"><!-- ngRepeat: toaster in toasters --></div> <script src="scripts/vendor.6fb30232.js"></script> <script src="scripts/examcloud-student-app.min.5ed52923.js"></script>  </body></html>"""
    gethtmlvalue(str,"head title",0)
