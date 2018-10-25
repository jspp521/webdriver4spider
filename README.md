# webdriver4spider
基于谷歌浏览器的浏览器模式爬取网站数据，所见即所得的策略

### 步骤1
 准备centos服务器的版本要求是7，版本6很麻烦，我没安装成功过

### 步骤2
选择下载python3版本，按默认提示安装
 ```shell
wget https://repo.anaconda.com/archive/Anaconda3-5.3.0-Linux-x86_64.sh
chmod u+x Anaconda3-5.3.0-Linux-x86_64.sh
./Anaconda3-5.3.0-Linux-x86_64.sh
```

### 步骤3
先退出shell界面，然后重新登录一次再执行下面
```shell
conda install selenium
```

### 步骤4
需要安装一个谷歌浏览器
```shell
cd /etc/yum.repos.d/
vim google-chrome.repo
[google-chrome]
name=google-chrome
baseurl=http://dl.google.com/linux/chrome/rpm/stable/$basearch
enabled=1
gpgcheck=1
gpgkey=https://dl-ssl.google.com/linux/linux_signing_key.pub
yum -y install google-chrome-stable --nogpgcheck
```
### 步骤6
爬虫的重点代码块
```python
chrome_opt = webdriver.ChromeOptions() 
chrome_opt.add_argument('headless') #无可视化界面运行
chrome_opt.add_argument('no-sandbox')
```

### 步骤7
网页元素定位文档参考
https://www.seleniumhq.org/docs/03_webdriver.jsp
