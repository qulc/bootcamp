## Bootcamp是一个[Python Django][0]构建的社区论坛类网站.

[![Build Status](https://travis-ci.org/qulc/bootcamp.svg?branch=master)](https://travis-ci.org/qulc/bootcamp)

## 示例
Demo: [http://bootcamp.lichun.me/][1]
![](http://i.imgur.com/pGS1kRd.png)

### V1.0.1:
    Django版本升级到最新的1.9.x
    切换到DaoCloud来部署该Demo程序
    新增了Dockerfile构建脚本，支持Docker容器构建
    切换原因是SAE的共享数据库缺陷问题，不支持Django新版本的migrate
    吐槽详情见：http://v2ex.com/t/270558

### V1.0.0:
    中文国际化支持、允许游客身份访问、
    Feeds超级用户删除权限, 还有一些微小的改动.
    支持SAE容器部署 (只能使用Django 1.7版本）

## 序言
这个项目是我刚学Python的时候关注的, 以当时战五渣的水平去修改这个程序了. 在Fork原项目的基础上添加了自己的功能

介于当时没有掌握正确的开发姿势，(写出了屎一样的code & git commit message), 导致现在Pull requests的Comparing changes已经面目全非了，只有作者眼瞎才有可能merge的提交了

接下来就当做自己练手的项目吧，准备修改支持Python3和最新新版本的Django, 现在用上了travis ci做持续集成, 再补上单元测试, 按正常的开发流程来，用pull requests，不再直接往master提交


## 部署方式

### Docker构建
```bash
$ git clone https://github.com/qulc/bootcamp.git

$ cd bootcamp/

$ docker build -t bootcamp .

$ docker run -p 80:80 bootcamp
```

[0]: https://www.djangoproject.com/
[1]: http://bootcamp.lichun.me/
[2]: http://www.sinacloud.com/doc/sae/docker/python-getting-started.html
