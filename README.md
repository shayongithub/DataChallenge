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
Before you start writing code, it’s important to ensure you have Python installed as well as the proper modules.
- Step One: Go to https://www.python.org, navigate to the downloads section and download the latest version of
python.
- Step Two: Go through the setup wizard and make sure to install pip as well as add python to the path (screenshot
credit: Data to Fish) [Data to Fish](https://datatofish.com/add-python-to-windows-path/)
![](Desktop/New folder (2)/ 1.png)
- Step Three: Go to https://www.jetbrains.com/pycharm/download/#section=windows, under Community, choose
the free download option. Go through the setup wizard using default options.
- Step Four: Open PyCharm once downloaded and select Create New Project (screenshot credit: BeginnersBook) [BeginnersBook](https://datatofish.com/add-python-to-windows-path/)
Once package has been successfully installed, we can move onto the next module to install.
For this project, install all of the following modules (name is exactly the name of the
package)
- Anaconda : Go to https://www.anaconda.com/products/individual download and install it
- Then create an environment by run Anaconda terminal and run : conda create -n myenv python=3.6
- Install libraries Scrapy and Selenium, as well as some supported library like Loguru and Json:
            pip install scrapy,
            pip install selenium,
            pip install loguru,
            pip install json.
- We use FireFox as a web browser for this project, so you have to install Geckodriver to support for it: https://github.com/mozilla/geckodriver/releases





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
## License
[MIT](https://choosealicense.com/licenses/mit/)
## Author 
VU DANG LONG [@VU DANG LONG](long.vu190404@vnuk.edu.vn).<br />
NGUYEN TAN DAT [@NGUYEN TAN DAT](dat.nguyen190401@vnuk.edu.vn) .<br />


