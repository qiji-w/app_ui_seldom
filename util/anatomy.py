import time
import asyncio
import threading
from loguru import logger
from mitmproxy import addons
import mitmproxy.http
from mitmproxy.options import Options


class MyAddon1(object):
    def __init__(self):
        self.logger = logger
        self.logger.info('初始化 MyAddon1 成功')

    def request(self, flow: mitmproxy.http.HTTPFlow):
        self.logger.info(f'request ---> {flow.request.url}')
        self.logger.info(f'request ---> {flow.request.json()}')


class MyAddon2(object):
    def __init__(self):
        self.logger = logger
        self.logger.info('初始化 MyAddon2 成功')

    def response(self, flow: mitmproxy.http.HTTPFlow):
        self.logger.info(f'response ---> status_code:{flow.response.status_code}')


def main_1():
    # DumpMaster 是继承 mitmproxy.master.Master
    from mitmproxy.tools.dump import DumpMaster

    async def func_temp():
        opts = Options(listen_host='0.0.0.0', listen_port=8888)
        dm = DumpMaster(opts, with_termlog=False, with_dumper=False)
        # dm.addons.add(MyAddon1())
        dm.addons.add(*[MyAddon1(), MyAddon2()])
        try:
            await dm.run()
        except BaseException as be:
            dm.shutdown()

    asyncio.run(func_temp())


def main_2():
    from mitmproxy.master import Master

    async def func_temp():
        opts = Options(listen_host='0.0.0.0', listen_port=8888)
        m = Master(opts, with_termlog=False)
        addon_list = [
            # default_addons 这个好像必须加上，不加上拦截不住
            *addons.default_addons(),
            MyAddon1(), MyAddon2()
        ]
        m.addons.add(*addon_list)
        try:
            await m.run()
        except BaseException as be:
            m.shutdown()

    asyncio.run(func_temp())


def main_3():
    # 创建一个事件循环thread_loop
    thread_loop = asyncio.new_event_loop()

    def func_new_thread(new_loop: asyncio.AbstractEventLoop = None):
        from mitmproxy.master import Master
        # 为子线程设置自己的事件循环
        asyncio.set_event_loop(new_loop)
        opts = Options(listen_host='127.0.0.1', listen_port=8888)
        m = Master(opts, new_loop)
        addon_list = [
            *addons.default_addons(),
            MyAddon1(), MyAddon2()
        ]
        m.addons.add(*addon_list)
        new_loop.run_until_complete(m.run())

    thd = threading.Thread(target=func_new_thread, args=(thread_loop,))
    thd.daemon = True
    thd.start()
    thd.join()


def main_4():
    from mitmproxy.master import Master
    from mitmproxy.addons import dumper, errorcheck, keepserving, readfile, termlog

    # 创建一个事件循环thread_loop
    new_loop = asyncio.new_event_loop()

    async def func_temp():
        opts = Options(listen_host='0.0.0.0', listen_port=8888)
        m = Master(opts, new_loop)
        addon_list = [
            *addons.default_addons(),
            MyAddon1(), MyAddon2()
        ]
        m.addons.add(*addon_list)
        await m.run()

    coro = func_temp()
    future = asyncio.run_coroutine_threadsafe(coro, new_loop)

    ####################################################################
    # 在一个线程中专门运行时间循环。
    def start_event_loop(loop):
        asyncio.set_event_loop(loop)
        loop.run_forever()

    t = threading.Thread(target=start_event_loop, args=(new_loop,))
    t.start()
    ####################################################################
    future.add_done_callback(lambda f: new_loop.call_soon_threadsafe(new_loop.stop))
    future.result()
    t.join()


if __name__ == "__main__":
    main_1()
    # main_2()
    # main_3()
    # main_4()
    pass