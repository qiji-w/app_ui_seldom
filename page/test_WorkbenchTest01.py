import seldom
from seldom.appium_lab import AppiumLab

from element.app_zy import BBSPage


# @seldom.skip()
class WorkbenchTest01(seldom.TestCase):
    def start_class(self):
        # 启动app
        # self.launch_app()

        self.sleep(5)

    def test_01_elements_children(self):
        # 导入 AppiumLab
        appium_lab = AppiumLab(self.driver)
        bbs_page = BBSPage(self.driver)

        bbs_page.num1.click()
        self.sleep(5)
        bbs_page.num2.click()

        appium_lab.find_text_view("00年").click()
        self.sleep(2)
        bbs_page.next.click()
        bbs_page.enter_home_image1.click()
        bbs_page.enter_home_image2.click()
        bbs_page.enter_home_image3.click()
        self.sleep(5)

        # elems = self.get_elements(id_="com.meizu.flyme.flymebbs:id/a29")
        # for title in elems:
        #     print(title.text)
        #     self.assertIn("lyme", title.text)
