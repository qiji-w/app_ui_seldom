import os
import sys
import click
import seldom
from appium.options.android import UiAutomator2Options

from config import privatization_config
from util.tools import email

root_dir = os.path.dirname(__file__)
sys.path.append(root_dir)

capabilities = {
    "platformName": "Android",
    "automationName": "UiAutomator2",
    "deviceName": "d499fbfa",
    "platformVersion": "13",
    "appPackage": "cn.xiaochuankeji.tieba",
    "appActivity": ".ui.base.SplashActivity",
    "ignoreHiddenApiPolicyError": True,
    "noReset": True
}
options = UiAutomator2Options().load_capabilities(capabilities)
seldom.main(
    app_server="http://127.0.0.1:4723/wd/hub",
    app_info=options,
    path="page/test_WorkbenchTest01.py",
    title="APP-私有化测试报告",
    report="report.html",
    tester="如果奇迹有颜色",
    description="APP-自动化测试用例",
    debug=True
)
