#coding:utf-8
import requests
import json
if __name__=="__main__":
      examId="1"
      upload_url="http://192.168.10.159:8080/api/scan/student/"+examId
      username="nikang"
      password="nikang"
      header = {   # 登录抓包获取的头部
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36   ",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Accept-Encoding": "gzip, deflate",
        "Content-Type": "application/json;charset=UTF-8",
        "auth-info": "loginname=" + username + ";password=" + password,
        "X-Requested-With": "XMLHttpRequest",
        "Connection": "keep-alive"
      }

      postdata={"examNumber": "15120204258","sliceCount": "2",
                "sheetCount": "2",
                "absent": "0",
                "answers": "A,D,D,A,B,C,B,C,C,A,#,#,#,#,#,#,#,#,#,#,#,#,#,#,#,#,#,#,#,#,AC,ABCD,BC,BCD,ABD,#,#,#,#,#,#,#,#,#,#,A,B,B,A,B,A,B,B,B,B,#,#,#,#,#"
      }
      print(json.dumps(postdata))
      session = requests.session()
      result = requests.post(upload_url, headers=header,data=postdata)
      print(result)
      print(result.json())
      print(len(result.json()))

