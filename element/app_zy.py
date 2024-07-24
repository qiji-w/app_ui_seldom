from poium import Page, Element, Elements

class BBSPage(Page):
    num1 = Element(
        id_='cn.xiaochuankeji.tieba:id/close_tv',
        timeout=5,
        describe='',
    )
    num2 = Element(
        id_='cn.xiaochuankeji.tieba:id/wiv_male_bg',
        timeout=5,
        describe='',
    )
    next = Element(
        id_='cn.xiaochuankeji.tieba:id/btn_next',
        timeout=5,
        describe='',
    )
    #
    enter_home_image1 = Element(
        xpath='(//android.widget.ImageView[@resource-id="cn.xiaochuankeji.tieba:id/coverImage"])[1]',
        timeout=5,
        describe='',
    )
    enter_home_image2 = Element(
        xpath='(//android.widget.ImageView[@resource-id="cn.xiaochuankeji.tieba:id/coverImage"])[2]',
        # index=1,
        timeout=5,
        describe='',
    )
    enter_home_image3 = Element(
        xpath='(//android.widget.ImageView[@resource-id="cn.xiaochuankeji.tieba:id/coverImage"])[3]',
        # index=2,
        timeout=5,
        describe='',
    )
    enter_home_btn = Element(
        id_='cn.xiaochuankeji.tieba:id/btn',
        timeout=5,
        describe='',
    )
