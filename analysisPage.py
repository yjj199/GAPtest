# coding=utf-8
from farmework.base_page import BasePage
from farmework.logger import Logger
import time
logger = Logger(logger="analysisPage").getlog()
class AnalysisPage(BasePage):
    #工具栏
    #保存图片
    save_photo = "xpath=>/html/body/div[1]/div[2]/div/div/div[1]/div/div/ul/li/div[1]"
    #选择
    choice = 'xpath=>/html/body/div[1]/div[2]/div/div/div[1]/div/div/ul/li/div[2]'
    #框选
    kuang_xuan = 'xpath=>/html/body/div[1]/div[2]/div/div/div[1]/div/div/ul/li/div[3]'
    #删除
    delete = 'xpath=>/html/body/div[1]/div[2]/div/div/div[1]/div/div/ul/li/div[4]'
    #切割
    qie_ge = 'xpath=>/html/body/div[1]/div[2]/div/div/div[1]/div/div/ul/li/div[5]'
    #撤销
    rework = 'xpath=>/html/body/div[1]/div[2]/div/div/div[1]/div/div/ul/li/div[6]'

    #过滤
    filter = 'xpath=>/html/body/div[1]/div[2]/div/div/div[1]/div/div/ul/li/button'
    #化学品
    entity_1= 'xpath=>/html/body/div[2]/div[1]/div/label[1]/span'
    #法律法规
    entity_2='xpath=>/html/body/div[2]/div[1]/div/label[2]/span'
    #化学反应
    entity_3='xpath=>/html/body/div[2]/div[1]/div/label[3]/span'
    #化工企业
    entity_4='xpath=>/html/body/div[2]/div[1]/div/label[4]/span'
    #重大危险源
    entity_5='xpath=>/html/body/div[2]/div[1]/div/label[5]/span'
    #事故信息
    entity_6='xpath=>/html/body/div[2]/div[1]/div/label[6]/span'
    #关系类别
    #f反应物
    relation_1='xpath=>/html/body/div[2]/div[3]/div/label[1]/span'
    #生成物
    relation_2='xpath=>/html/body/div[2]/div[3]/div/label[2]/span'
    #属于
    relation_3='xpath=>/html/body/div[2]/div[3]/div/label[3]/span'
    #事故企业
    relation_4='xpath=>/html/body/div[2]/div[3]/div/label[4]/span'

    #添加实体
    add_shiti='xpath=>/html/body/div[1]/div[2]/div/div/div[1]/div/div/ul/li/div[8]'
    #添加实体输入框
    addshiti_input='xpath=>/html/body/div[1]/div[2]/div/div/div[2]/div[4]/div/div[2]/div/div[1]/input'#添加实体输入框
    addshiti_search='xpath=>/html/body/div[1]/div[2]/div/div/div[2]/div[4]/div/div[2]/div/div[1]/span/i'#添加实体搜索按钮
    dangye='xpath=>/html/body/div[1]/div[2]/div/div/div[2]/div[4]/div/div[2]/div/div[2]/div/label[1]/span/span'#添加实体选择当页
    add_analysis='xpath=>/html/body/div[1]/div[2]/div/div/div[2]/div[4]/div/div[2]/div/div[2]/div/button'#添加到当前分析
    #添加实体界面 关闭按钮“X”
    addshiti_close='xpath=>/html/body/div[1]/div[2]/div/div/div[2]/div[4]/div/div[1]/button'
    #选框1
    # marquee_1='xpath=>/html/body/div[1]/div[2]/div/div/div[2]/div[4]/div/div[2]/div/div[4]/div[1]/div/div[1]/label/span[1]/span'
    marquee_1='xpath=>/html/body/div[1]/div[2]/div/div/div[2]/div[4]/div/div[2]/div/div[4]/div[1]/div/div[1]/label/span[1]'
    #选框2
    marquee_2='xpath=>/html/body/div[1]/div[2]/div/div/div[2]/div[4]/div/div[2]/div/div[4]/div[2]/div/div[1]/label/span[1]/span'
    #选框3
    marquee_3='xpath=>/html/body/div[1]/div[2]/div/div/div[2]/div[4]/div/div[2]/div/div[4]/div[3]/div/div[1]/label/span[1]/span'
    #选框4
    marquee_4='xpath=>/html/body/div[1]/div[2]/div/div/div[2]/div[4]/div/div[2]/div/div[4]/div[4]/div/div[1]/label/span[1]/span'
    #点击下一页 按钮
    nextpage='xpath=>/html/body/div[1]/div[2]/div/div/div[2]/div[4]/div/div[2]/div/div[5]/div/button[2]'
    #点击上一页 按钮
    onpage='xpath=>/html/body/div[1]/div[2]/div/div/div[2]/div[4]/div/div[2]/div/div[5]/div/button[1]'
    #输入页数
    inputpage1='xpath=>/html/body/div[1]/div[2]/div/div/div[2]/div[4]/div/div[2]/div/div[5]/div/span[2]/div/input'

    #点击还原
    path_any = 'xpath=>/html/body/div[1]/div[2]/div/div/div[1]/div/div/ul/li/div[7]'
    #路径分析
    path_analysis= 'xpath=>/html/body/div[1]/div[2]/div/div/div[1]/div/div/ul/li/div[9]'
    #最短路径
    shortest='xpath=>/html/body/div[1]/div[2]/div/div/div[2]/div[1]/div/div[2]/div[1]/label[1]/span[1]/span'
    #所有路径
    allpath='xpath=>/html/body/div[1]/div[2]/div/div/div[2]/div[1]/div/div[2]/div[1]/label[2]/span[1]/span'
    #路径输入框
    inputpath='xpath=>/html/body/div[1]/div[2]/div/div/div[2]/div[1]/div/div[2]/div[2]/input'
    #确认按钮
    confirm='xpath=>/html/body/div[1]/div[2]/div/div/div[2]/div[1]/div/div[3]/div/div/div[1]/button'
    #取消按钮
    cancel='xpath=>/html/body/div[1]/div[2]/div/div/div[2]/div[1]/div/div[3]/div/div/div[2]/button'
    #反应链分析
    reaction ='xpath=>/html/body/div[1]/div[2]/div/div/div[1]/div/div/ul/li/div[10]/span'
    #搜索框
    search_place='xpath=>/html/body/div[1]/div[2]/div/div/div[1]/div/div/ul/li/div[11]/div/input'
    search_button='xpath=>/html/body/div[1]/div[2]/div/div/div[1]/div/div/ul/li/div[11]/div/span/i'
    #属性
    back = 'xpath=>/html/body/div/div[3]/div/div/div[2]/div[1]/i[1]'
    back_1='xpath=>/html/body/div/div[3]/div/div/div[2]/div[1]/i[2]'
    #全屏
    #fullscreen = 'xpath=/html/body/div/div[3]/div/div/div[1]/div[1]/div[1]'
    fullscreen='xpath=>/html/body/div/div[3]/div/div/div[1]/div[1]/div[1]'
    #居中
    center = 'xpath=>/html/body/div/div[3]/div/div/div[1]/div[1]/div[2]'
    #退出
    logout = 'xpath=>/html/body/div/div[1]/div/div/div[3]/span[2]'



    #环形菜单化工企业
    ring_huagong=''
    huagong_xianshi=''
    #环形菜单事故信息
    # huanxing_shigu='css_selector=>html body div#app.container-fluid div.row.my-body div#my-body.text-center div.row.flex div#my-graph.pull-left div#svgContainer.analysisSvg svg#mainSVG.mainSVG g.mainG g#firstPie.pieContainer g path.piePath'
    #环形菜单 重大危险源hazards
    ring_hazards=''
    hazards_shaixuan=''
    hazards_xianshi=''



    #节点
    node='id=>nodeCircle_12'#甲醛
    node1='id=>nodeCircle_10'
    node2='id=>nodeCircle_33406'#空气
    node3='id=>nodeCircle_11'#甲醇
    node4='id=>nodeCircle_6720'#水

    def acclick_node4(self):
        self.acclick(self.node4)
        logger.info("点击水")
    def acclick_node3(self):
        self.acclick(self.node3)
        logger.info("点击甲醇")


    def ac(self):
        self.yidong(self.node)
        logger.info("移动到化工企业")

    def acclick_node1(self):
        self.acclick(self.node1)
        logger.info("点击天然气")
    def acclick_node(self):
        self.acclick(self.node)
        logger.info("点击甲醛")

    def acclick_node2(self):
        self.acclick(self.node2)
        logger.info("点击空气")


    # 敲击所在文本框enter
    inputpage2 = 'css_selector=>div.task-container:nth-child(4) > div:nth-child(3) > div:nth-child(1) > span:nth-child(5) > div:nth-child(1) > input:nth-child(1)'


    #环形菜单
    # chemical化工
    # chemical_screening='xpath=>'
    # chemical_show='xpath=>'
    # 化工企业筛选省下拉列表
    province='xpath=>//*[@id="my-body"]/div/div[5]/div[1]/div/div[1]/div[1]/div[1]/input'
    province_1='xpath=>/html/body/div[2]/div[1]/div[1]/ul/li[1]'#北京
    province_2='xpath=>/html/body/div[2]/div[1]/div[1]/ul/li[2]'#天津
    province_3='xpath=>/html/body/div[2]/div[1]/div[1]/ul/li[17]'#湖北
    province_4='xpath=>/html/body/div[2]/div[1]/div[1]/ul/li[24]'#贵州
    province_5= 'xpath=>/html/body/div[3]/div[1]/div[1]/ul/li[32]'#台湾

    #筛选关闭按钮
    shaixuan_close='xpath=>//*[@id="my-body"]/div/div[5]/i'
    def click_shaixuan_close(self):
        self.click(self.shaixuan_close)
        logger.info("筛选关闭 X")
    #城市列表
    city='xpath=>//*[@id="my-body"]/div/div[5]/div[1]/div/div[1]/div[2]/div[1]/input'
    #市区根本省的改变而变化，北京和天津均为默认
    city_3='xpath=>/html/body/div[3]/div[1]/div[1]/ul/li[7]'#荆门
    city_4='xpath=>/html/body/div[3]/div[1]/div[1]/ul/li[3]'#遵义
    city_5='xpath=>/html/body/div[3]/div[1]/div[1]/ul/li[6]'#高雄
    #企业规模
    size='xpath=>//*[@id="my-body"]/div/div[5]/div[1]/div/div[2]/div/div[1]/input'
    size_1='xpath=>/html/body/div[3]/div[1]/div[1]/ul/li[1]'#其他
    size_2='xpath=>/html/body/div[3]/div[1]/div[1]/ul/li[2]'
    size_3='xpath=>/html/body/div[3]/div[1]/div[1]/ul/li[3]'
    size_4='xpath=>/html/body/div[3]/div[1]/div[1]/ul/li[4]'
    size_5='xpath=>/html/body/div[3]/div[1]/div[1]/ul/li[5]'
    #化工企业筛选 关系
    sx_relation='xpath=>//*[@id="my-body"]/div/div[5]/div[1]/div/div[3]/div/div[1]/span/span/i'
    sx_relation_1='xpath=>/html/body/div[2]/div[1]/div[1]/ul/li[1]'#原料
    sx_relation_2='xpath=>/html/body/div[2]/div[1]/div[1]/ul/li[2]'#进口
    sx_relation_3='xpath=>/html/body/div[2]/div[1]/div[1]/ul/li[3]'#中间产品
    sx_relation_4='xpath=>/html/body/div[2]/div[1]/div[1]/ul/li[4]'#产品
    chemical_sxbutton='xpath=//*[@id="my-body"]/div/div[5]/div[2]/button[1]'#点击筛选按钮
    chemical_qxbutton='xpath=>//*[@id="my-body"]/div/div[5]/div[2]/button[2]'#点击取消按钮

    #重大危险源筛选
    dangerous='xpath=>//*[@id="my-body"]/div/div[5]/div[1]/div/div/div[1]/span/span/i'
    dangerous_1='xpath=>/html/body/div[3]/div[1]/div[1]/ul/li[1]'
    dangerous_2='xpath=>/html/body/div[3]/div[1]/div[1]/ul/li[2]'
    dangerous_3='xpath=>/html/body/div[3]/div[1]/div[1]/ul/li[3]'
    dangerous_4='xpath=>/html/body/div[3]/div[1]/div[1]/ul/li[4]'
    # dangerous_sxbutton='xpath=>'
    # dangerous_qxbutton='xpath=>'

    #事故信息筛选
    accident='xpath=>//*[@id="my-body"]/div/div[5]/div[1]/div/div/div[1]/span/span/i'
    accident_1='xpath=>/html/body/div[3]/div[1]/div[1]/ul/li[1]'#火灾
    accident_2 = 'xpath=>/html/body/div[3]/div[1]/div[1]/ul/li[2]'  # 泄露
    accident_3='xpath=>/html/body/div[3]/div[1]/div[1]/ul/li[3]'#爆炸
    accident_4='xpath=>/html/body/div[3]/div[1]/div[1]/ul/li[4]'#其他
    accident_5='xpath=>/html/body/div[3]/div[1]/div[1]/ul/li[5]'#中毒
    ring_accident=''#移动到事故信息
    # accident_shaixuan=''
    # accident_xianshi=''

    #属性框展示
    #查看详情
    details='xpath=>//*[@id="attributePanel"]/div/button'#查看详情
    directory='xpath=>//*[@id="my-body"]/div/div[2]/div[2]/div[2]/ul/li[2]'#所属目录
    standard='xpath=>//*[@id="my-body"]/div/div[2]/div[2]/div[2]/ul/li[3]/a'#法规标准
    fallback='xpath=>/html/body/div[1]/div[3]/div/div[1]/div[1]' #回退按钮

    #更换主题
    theme='xpath=>/html/body/div/div[1]/div/div/div[3]/div/span'
    theme_1='xpath=>/html/body/ul/li[1]'
    theme_2='xpath=>/html/body/ul/li[2]'
    theme_3='xpath=>/html/body/ul/li[3]'


    def click_theme(self):
        self.click(self.theme)
        logger.info("点击更换主题")
    def click_theme_1(self):
        self.click(self.theme_1)
        logger.info("点击高雅紫")
    def click_theme_2(self):
        self.click(self.theme_2)
        logger.info("点击科技蓝")
    def click_theme_3(self):
        self.click(self.theme_3)
        logger.info("点击明亮黄")

    #属性框
    def click_details(self):
        self.click(self.details)
        logger.info("点击查看详情")
    def click_directory(self):
        self.click(self.directory)
        logger.info("点击 所属目录")
    def click_standard(self):
        self.click(self.standard)
        logger.info("点击法规标准")
    def click_fallback(self):
        self.click(self.fallback)
        logger.info("点击回退 <-")
    #事故信息筛选
    def click_accident(self):
        self.click(self.accident)
        logger.info("点击事故类型下拉列表")

    def click_accident_1(self):
        self.click(self.accident_1)
        logger.info("点击火灾")
    def click_accident_2(self):
        self.click(self.accident_2)
        logger.info("点击泄露")
    def click_accident_3(self):
        self.click(self.accident_3)
        logger.info("点击爆炸")
    def click_accident_4(self):
        self.click(self.accident_1)
        logger.info("点击其他")
    def click_accident_5(self):
        self.click(self.accident_5)
        logger.info("点击中毒")

    #重大危险源筛选
    def click_dangerous(self):
        self.click(self.dangerous)
        logger.info("点击下拉列表")
    def click_dangerous_1(self):
        self.click(self.dangerous_1)
        logger.info("点击1级")
    def click_dangerous_2(self):
        self.click(self.dangerous_2)
        logger.info("点击2级")
    def click_dangerous_3(self):
        self.click(self.dangerous_3)
        logger.info("点击3级")
    def click_dangerous_4(self):
        self.click(self.dangerous_4)
        logger.info("点击4级")

    #化工企业筛选省下拉列表
    def click_province(self):
        self.click(self.province)
        logger.info("点击 下拉列表")

    def click_province_1(self):
        self.click(self.province_1)
        logger.info("列表1 北京")

    def click_province_2(self):
        self.click(self.province_2)
        logger.info("列表2天津")

    def click_province_3(self):
        self.click(self.province_3)
        logger.info("列表3湖北")

    def click_province_4(self):
        self.click(self.province_4)
        logger.info("列表4贵州")

    def click_province_5(self):
        self.click(self.province_5)
        logger.info("列表最后澳门特别行政区")
    #市区下拉列表
    def click_city(self):
        self.click(self.city)
        logger.info("点击市区下拉列表")
    def click_city_3(self):
        self.click(self.city_3)
        logger.info("勾选 荆门")
    def click_city_4(self):
        self.click(self.city_4)
        logger.info("勾选 遵义")
    def click_city_5(self):
        self.click(self.city_5)
        logger.info("勾选 高雄")

    def click_size(self):
        self.click(self.size)
        logger.info("点击企业规模下拉列表")
    def click_size_1(self):
        self.click(self.size_1)
        logger.info("勾选其他")
    def click_size_2(self):
        self.click(self.size_2)
        logger.info("勾选微型企业")
    def click_size_3(self):
        self.click(self.size_3)
        logger.info("勾选小型企业")
    def click_size_4(self):
        self.click(self.size_4)
        logger.info("勾选中型企业")
    def click_size_5(self):
        self.click(self.size_5)
        logger.info("勾选大型企业")

    def click_sx_relation(self):
        self.click(self.sx_relation)
        logger.info("点击关系下拉列表")
    def click_sx_relation_1(self):
        self.click(self.sx_relation_1)
        logger.info("原料")

    def click_sx_relation_2(self):
        self.click(self.sx_relation_2)
        logger.info("进口")
    def click_sx_relation_3(self):
        self.click(self.sx_relation_3)
        logger.info("中间产品")
    def click_sx_relation_4(self):
        self.click(self.sx_relation_4)
        logger.info("产品")
    def click_chemical_sxbutton(self):
        self.click(self.chemical_sxbutton)
        logger.info("点击筛选按钮")
    def click_chemical_qxbutton(self):
        self.click(self.chemical_qxbutton)
        logger.info("点击取消按钮")


    def click_save_photo(self):
        self.click(self.save_photo)
        logger.info('点击保存图片')
    def click_choice(self):
        self.click(self.choice)
        logger.info('点击选择')
    def click_kuang_xuan(self):
        self.click(self.kuang_xuan)
        logger.info('点击框选')
    def click_delete(self):
        self.click(self.delete)
        logger.info('点击删除')
    def click_qie_ge(self):
        self.click(self.qie_ge)
        logger.info('点击切割')
    def click_rework(self):
        self.click(self.rework)
        logger.info('点击撤销')

    def click_filter(self):
        self.click(self.filter)
        logger.info('点击过滤')
    def click_entity_1(self):
        self.click(self.entity_1)
        logger.info("点击化学品")

    def click_entity_2(self):
        self.click(self.entity_2)
        logger.info("点击法律法规")

    def click_entity_3(self):
        self.click(self.entity_3)
        logger.info("点击化学反应")

    def click_entity_4(self):
        self.click(self.entity_4)
        logger.info("点击化工企业")
    def click_entity_5(self):
        self.click(self.entity_5)
        logger.info("点击重大危险源")
    def click_entity_6(self):
        self.click(self.entity_6)
        logger.info("点击事故信息")

    def click_relation_1(self):
        self.click(self.relation_1)
        logger.info("反应物")
    def click_relation_2(self):
        self.click(self.relation_2)
        logger.info("生成物")
    def click_relation_3(self):
        self.click(self.relation_3)
        logger.info("属于")
    def click_relation_4(self):
        self.click(self.relation_4)
        logger.info("事故企业")

    def click_add_shiti(self):
        self.click(self.add_shiti)
        logger.info('添加实体')
    def type_addshiti_input(self,text):
        self.type(self.addshiti_input,text)
        logger.info("添加实体输入框")
    def click_addshiti_search(self):
        self.click(self.addshiti_search)
        logger.info("添加实体搜索按钮")
    def click_dangye(self):
        self.click(self.dangye)
        logger.info("选择当页")
    def click_add_analysis(self):
        self.click(self.add_analysis)
        logger.info("添加到当前分析")
    def click_addshiti_close(self):
        self.click(self.addshiti_close)
        logger.info("添加实体 关闭按钮")
    def click_marquee_1(self):
        self.click(self.marquee_1)
        logger.info("勾选选框1")
    def click_marquee_2(self):
        self.click(self.marquee_2)
        logger.info("勾选选框2")
    def click_marquee_3(self):
        self.click(self.marquee_3)
        logger.info("勾选选框3")
    def click_marquee_4(self):
        self.click(self.marquee_4)
        logger.info("勾选选框4")
    def click_nextpage(self):
        self.click(self.nextpage)
        logger.info("点击下一页")
    def click_onpage(self):
        self.click(self.onpage)
        logger.info("点击上一页")

    def type_inputpage1(self,text):
        self.type(self.inputpage1,text)
        logger.info("输入页数")


    def click_path_any(self):
        self.click(self.path_any)
        logger.info('点击还原')
    def click_reaction(self):
        self.click(self.reaction)
        logger.info('反应链分析')

    def click_path_analysis(self):
        self.click(self.path_analysis)
        logger.info(("路径分析"))
    def click_shortest(self):
        self.click(self.shortest)
        logger.info("最短路径")
    def click_allpath(self):
        self.click(self.allpath)
        logger.info("所有路径")
    def type_inputpath(self,text):
        self.type(self.inputpath,text)
        logger.info("输入路径")
    def click_confirm(self):
        self.click(self.confirm)
        logger.info("点击确认")
    def click_cancel(self):
        self.click(self.cancel)
        logger.info("点击取消")

    def type_search_place(self,text):
        self.type(self.search_place,text)
        logger.info('搜索框输入')
    def click_search_button(self):
        self.click(self.search_button)
        logger.info('点击搜索按钮')
    def click_back(self):
        self.click(self.back)
        logger.info('收回属性框')
    def click_back_1(self):
        self.click(self.back_1)
        logger.info("展开属性框")
    def click_fullscreen(self):
        self.click(self.fullscreen)
        logger.info('点击全屏')
    def click_center(self):
        self.click(self.center)
        logger.info('点击居中')

        #点击节点
    def right_click_node(self):
        self.right_click(self.node)
        logger.info("右击节点甲醛")#甲醛节点

    def move_el_ring_huagong(self):
        self.move_el(self.ring_huagong)
        logger.info("移动到化工企业")

    def move_el_shigu(self):
        self.move_el(self.move_el_shigu)
        logger.info("移动到事故信息")
    #
    # def click_huagong_shaixuan(self):
    #     self.click(self.huagong_shaixuan)
    #     logger.info("点击化工企业筛选")#点击环形菜单化工企业筛选

    def click_shaixuan2(self):
        self.click(self.shaixuan2)
        logger.info("点击事故筛选")


    def enter_confirm(self):
        self.enter(self.inputpage1)
        time.sleep(1)
        logger.info("敲击enter")









