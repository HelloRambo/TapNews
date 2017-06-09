var express = require('express');
var router = express.Router();

/* GET news listing. */
router.get('/', function(req, res, next) {
  news = [
      {
          'url':'http://slide.news.sina.com.cn/c/slide_1_2841_156226.html#p=1',
          'title':'985公交成高考家长休息站 寓全上985',
          'description':'gaokao',
          'source':'sina',
          'urlToImage':'http://n.sinaimg.cn/news/1_img/upload/857ccb57/20170608/RYEM-fyfzhac0352286.jpg',
          'digest':'ssldjflsjdfls==\n',
          'reason':'Hot'
      },
      {
          'url':'http://news.sina.com.cn/pl/2017-06-08/doc-ifyfzhac0422570.shtml',
          'title':'高考作文即使得满分也只是庸常得出类拔萃',
          'description':'zuowen',
          'source':'sina',
          'urlToImage':'http://n.sinaimg.cn/public_column/crawl/20170608/dIBR-fyfzhap4204581.jpg',
          'digest':'asdfsweroiusdf==\n',
          'reason':'Hot'
      }
  ]

  res.json(news);
});

module.exports = router;
