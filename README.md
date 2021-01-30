# WEB CRAWLING 
## CRAWLING SCORE FROM NATIONAL EXAM

<br>
<p align="center">
    <img src="https://zok-blog.oss-cn-hangzhou.aliyuncs.com/pythonlg.jpg" 
        alt="python3 spider">
</p>
<br />
<p align="center">
    <a href="#"><img src="https://img.shields.io/badge/status-updating-brightgreen.svg"></a>
    <a href="https://www.python.org/downloads/"><img src="https://zok-blog.oss-cn-hangzhou.aliyuncs.com/ico/python-3.7-green.svg"></a>


</p>
<br />


This is source code crawl data college Test scores using Scrapy
## Introduction :
Author       | Email
------------ | -------------
Nguyen Tan Dat | dat.nguyen190401@vnuk.edu.vn
Vu Dang Long | long.vu190404@vnuk.edu.vn




## Installing: 
To use the project, first clone the repo on your device using the command below: 
```conda
git init
```
```cd
git clone https://github.com/shayongithub/DataChallenge
```
As we mentioned above, we use Pycharm as an IDE for this project, you can also you other IDE or run it directly from your terminal. If you want to download Pycharm, you can find it here: ```cd
https://www.jetbrains.com/pycharm/download/#section=windows
```
Scrapy works best with python 3.6 – 3.7, so we recommend you create an environment with this version inside, we have undergone some troubles with later version like 3.9. Anaconda supports very well in managing your environment, so you may want to install it here: ```cd
https://www.anaconda.com/products/individual
```
Then, you can create an environment with specific version with this command (run on your Anaconda terminal): 
```cd
conda create -n myenv python=3.6
```
Install libraries Scrapy and Selenium, as well as some supported library like Loguru and Json:
```cd
pip install scrapy
```
```cd
pip install selenium
```
```cd
pip install loguru
```
```cd
pip install json
```
We use FireFox as a web browser for this project, so you have to install Geckodriver to support for it: 
https://github.com/mozilla/geckodriver/releases .<br />
Note:  
The main problem can happen is that you don’t get the right path for your directory. So, pay attention to it, especially the path link to your Firefox browser and where you put Geckodriver.<br />
Besides, we use relative path to ensure the users can run it easily without changing all the path, so make sure you set your terminal path to some things like this:
F:\...\...\...\diemthi>


## Usage

Make sure you have Python installed 
Just run the following command at the root of your project and answer questions:
First, activate conda environment that install all library above:
```conda
 conda activate myenv 
```
Next is running command line directory to spider : 
```cd
 cd DataChallenge/diemthi/spiders/
```
And last one is running: 
```Scrapy
 Scrapy crawl crawldiemthi
```
When data crawled, it will be appear in a folder and Watchdog will automatically clean,merged and transfer it to a form(csv). Next, data will be pushed to mongoDB and SQLserver. 

![a](https://user-images.githubusercontent.com/65530922/106276039-7a6d3e80-6269-11eb-9437-5a0d0dc5cd05.png)
![b](https://user-images.githubusercontent.com/65530922/106276677-81488100-626a-11eb-9487-29c1c0986a98.jpg)
![c](https://user-images.githubusercontent.com/65530922/106276665-7ee62700-626a-11eb-9a5c-f35f2d800c65.jpg)
![d](https://user-images.githubusercontent.com/65530922/106276674-80175400-626a-11eb-89c7-3c3b7a64daa6.jpg)


Finally, we drew some graphs to visualize the data more understandable and get some insights from it.

![2](https://user-images.githubusercontent.com/74718176/106347176-168d5900-62ef-11eb-8f9d-e09dd34259a6.jpg)
![3](https://user-images.githubusercontent.com/74718176/106347177-17be8600-62ef-11eb-85af-0d3ba6e2eab4.jpg)
![4](https://user-images.githubusercontent.com/74718176/106347178-17be8600-62ef-11eb-9b82-68acafc8f3c5.jpg)
![1](https://user-images.githubusercontent.com/74718176/106347179-18571c80-62ef-11eb-9031-40d4bf4f6fe9.jpg)






Do not forget that you have to install SQl server and MongoDB on your computer first. Details can find here:
```Scrapy
https://www.microsoft.com/en-gb/sql-server/sql-server-downloads  
```

```Scrapy
https://www.mongodb.com/try/download/community
```


## License
[MIT](https://choosealicense.com/licenses/mit/)
## Author 
VU DANG LONG [@VU DANG LONG](long.vu190404@vnuk.edu.vn).<br />
NGUYEN TAN DAT [@NGUYEN TAN DAT](dat.nguyen190401@vnuk.edu.vn) .<br />


