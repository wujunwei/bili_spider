dbconfig = {
    'host': '115.159.222.116',
    'port': 3306,
    'user': 'adam',
    'passwd': '123654',
    'db': 'bili_spider'
}

user_config = {
    'name': "//span[@id='h-name']/text()",
    'gender': "//span[@id='h-gender']/@class",
    'level': "//a[@class='h-level m-level']/@lvl",
    'register_time': "//div[@class='item regtime']/span[@class='text']/text()"
}

extend_config = {
    'head_img': "//div[@class='h-avatar']/img/@src",
    'sign': "//div[@class='h-sign']/text()",
    'birthday': "//div[@class='item birthday']/span[@class='text guest']/text()",
    'follow_num': "//a[@class='item data-gz']/span[@class='quantity']/text()",
    'fans_num': "//a[@class='item data-fs']/span[@class='quantity space-fans']/text()"
}
