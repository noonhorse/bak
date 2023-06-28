# 全局变量设置

## 1、问题
常见于 xx 命令未找到 如：`bash: lighthouse: command not found...`

## 2、原因
    主要是环境变量配置错误，对应的全局变量的命令字，导致命令字查找不到。

## 3、解决方法

### 1、linux 中解决方案
查找路径 `npm list -g` 查找对应的包安装路径

如查询出来路径为：`/home/work/node-v14.15.0-linux-x64/bin`


  **3.1.1 添加环境变量**

1、临时方案

在shell中运行下列命令，`$PATH:` 后跟想要加入环境变量的目录

```
export PATH=$PATH:/home/work/node-v14.15.0-linux-x64/bin
```

2、当前登录用户方案
修改用户目录下的 `.bashrc` 文件 `vi ~/.bashrc` 在文件最后添加该语句

```
PATH=$PATH:/home/work/node-v14.15.0-linux-x64/bin
```
重新登录即生效

3 所有账户均有效
修改 `/etc/profile` 文件 `sudo vi /etc/profile` 在末尾添加以下内容

```
export PATH="$PATH:/home/work/node-v14.15.0-linux-x64/bin"
```

退出当前shell再重新登录即可生效或执行source /etc/profile该命令


## windows 下解决方法

我的电脑 -> 右键属性  -> 高级系统设置  -> 环境变量  -> 新建或选着Path 修改，添加新安装工具目录。