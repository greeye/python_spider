# python_spider
项目名称：北京二手房信息爬虫
项目介绍：链家网(https://bj.lianjia.com/ershoufang)爬取上北京二手房的相关信息字段：包括如下字段：name，style，area，orientation，decoration，elevator，floor，build_year，sign_time，unit_price，total_price一共11个与二手房信息相关的字段。并将爬取到的数据导入到mysql中。
项目工作情况：
该项目过程遇到一个问题，在爬取一个包含style、area、orientation、decoration、elevator五个字段信息的过程中，用xpath只能将五一起爬再分类，但是网页数据可能缺失了elevator数据，导致分类出现异常。解决办法：先将 <div>的houseinfo整段爬取，然后在用etree遍历爬取里面的各个列表元素信息，在里面进行分类，并将空值也添加成一个空字段，便于后面导入数据库。
 项目结果：可以实现爬取1000条数据，并且能正常导入数据库中。






