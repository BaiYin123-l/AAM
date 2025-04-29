from .Listener_Mouse import Listener_Mouse
from .Listener_Keyboard import Listener_Keyboard
from ..tool.logger import Logger # 导入 get_logger 函数以获取日志记录器


class Listeners:
    def __init__(self):
        self.listener_mouse = Listener_Mouse()
        self.listener_keyboard = Listener_Keyboard()
        self.logger = Logger(__name__)  # 获取当前模块的日志记录器
        self.logger.info("Listeners 初始化完成")

    def start(self):
        self.logger.info("开始监听")
        self.listener_mouse.start()
        self.listener_keyboard.start()

    def stop(self):
        self.logger.info("停止监听")
        self.listener_mouse.stop()
        self.listener_keyboard.stop()