RankedList（排名列表）
====
排名列表是一个对样本中的数据进行定位、区间统计的Python库。给定一组样本数据，将该数据进行升序、降序排序，得到一个有序列表。对于该有序列表，RankedList提供了两种定位的方式：绝对位置和相对位置。
* 绝对位置：从1开始计，要找的值排第几位。例如15表示排第15位的数据，-1表示排倒数第1位的数据。
* 相对位置：取值在0~1之间，表示要找的值在百分之多少的位置，可以以小数或百分比形式给出，例如0.34和'34%'均可表示排在第34%处的数据。

基于这两种定位方式，可以通过绝对/相对位置找出一个值或一组值；也可以反过来，找出一个值或一组值对应的绝对/相对位置。

另外，还可以通过区间统计获得落在某个区间内的值的数量，包括单个区间的统计和一系列区间的统计。

如何安装或更新
----
1.通过pip安装：
* `pip install rankedlist`

2.通过pip更新版本：
* `pip install rankedlist --upgrade`
<br>如果更新失败，可以尝试先卸载旧版本，再安装新版本：
* `pip uninstall rankedlist`
* `pip install rankedlist`

3.在pypi上下载analyticlab源代码并安装：
* 打开网址https://pypi.python.org/pypi/rankedlist
* 通过download下载tar.gz文件，解压到本地，通过cd指令切换到解压的文件夹内
* 通过`python setup.py install`实现安装

使用教程
----
### 1.导入RankedList类：
通过以下指令实现RankedList类的导入：
`from rankedlist import RankedList`
### 2.创建一个排名列表：
要创建一个排名列表，需要给定要排名的数据，以及排列顺序（升序、降序还是维持原有顺序不变）。数据可以以两种方式给出：直接在程序中列出数据，或者从txt文件中读取数据。下面依次介绍两种创建排名列表的方式：
#### 2.1 直接列数据创建：
直接列数据，即通过RankedList类的构造方法创建排名列表。RankedList类的构造方法如下：
<br>`RankedList(values, order=1)`
<br>其中values是排名列表中的数据，可以以list给出，比如`[1.66,1.76,1.82,1.71,1.75]`；也可以字符串形式给出，此时数据之间要以空格隔开，比如`'1.66 1.76 1.82 1.71 1.75'`；如果已有现成的RankedList，那么直接将现成的RankedList作为values即可。
<br>order为数据的排序方式。order=1时为升序，-1时为降序，0时为维持现有顺序不变。默认使用的是升序排列。
<br>下面举例说明：
* `r1 = RankedList([1.61, 3.20, 2.49, 2.61, 2.91])`
* `r2 = RankedList('1.61 3.20 2.49 2.61 2.91')`
* `r3 = RankedList(r2, order=-1)`

#### 2.2 通过txt文件读取数据创建：

运行环境
----
RankedList只能在Python 3.x环境下运行，不支持Python 2.x环境。要求系统已安装veryprettytable库，这个库用于在命令行状态下展示表格。在Jupyter Notebook环境下，会使用HTML展示表格。
