

# fis code update

通过fis 配置修改解决fis 在html-ejs 模板编译的问题。

``fis-parser-html-ejs``

```javascript
'use strict';

var ejs = require('ejs');
var cheerio = require("cheerio");
var path = require("path");

module.exports = function(content, file, conf){
    conf.filename = file.getId();
    conf.client = true;
    if(conf.compress){
        content = content.replace(/<!--[\s\S]*?-->/g, '');
        content = content.replace(/^\s+|\s+$|\n/gm, '');
    }
        ejs.open = '{{';
        ejs.close = '}}';
    var $ = cheerio.load(content,{decodeEntities:false});

    //拉取所有data-tmpl="ejs"的div
    var tmpls = $("[type='text/ejs']");
    for(var i=0;i<tmpls.length;i++){
    	var item = $(tmpls[i]);
    	var data = filetype(item.attr("data-json"))
    	var jsondata = JSON.parse(data);
    	item.replaceWith(ejs.render(item.html(), jsondata).toString());
    }

    return $.html();
};

function filetype(filename){    
    var root = fis.util.realpath();
    var config = fis.file(root ,filename);
        //读取对应的js配置文件
        if(/(**).js$/g.test(filename)){//js文件 需要转为json
            var b = '{'+fis.file.wrap(config).getContent().split(/\w+(?=\s*=\s*){/)[1];
            var data = /;$/g.test(b)? b.slice(-1):b;
        }else if(/(**).json$/g.test(filename)){//json文件
            var data= fis.file.wrap(config).getContent();
        }
    return data;
}

```javascript

