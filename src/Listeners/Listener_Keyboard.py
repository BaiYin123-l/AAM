from pynput import keyboard
from src.tool import Logger  # 导入 get_logger 函数以获取日志记录器


class Listener_Keyboard(keyboard.Listener):
    def __init__(self):
        super().__init__(on_press=self.on_press, on_release=self.on_release)
        self.logger = Logger(__name__)  # 获取当前模块的日志记录器
        self.logger.info("键盘监听器初始化完成")

    def on_press(self, key):
        self.logger.info(f"按键按下: {key}")  # 通过日志记录器记录信息
        return True

    def on_release(self, key):
        self.logger.info(f"按键释放: {key}")  # 通过日志记录器记录信息
        return True