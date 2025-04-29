from pynput import mouse
from ..tool.logger import Logger  # 导入 get_logger 函数以获取日志记录器


class Listener_Mouse(mouse.Listener):
    def __init__(self):
        super().__init__(on_click=self.on_click, on_scroll=self.on_scroll, on_move=self.on_move)
        self.logger = Logger(__name__)  # 获取当前模块的日志记录器
        self.logger.info("鼠标监听器初始化完成")

    def on_click(self, x, y, button, pressed):
        self.logger.info(f"鼠标点击: x={x}, y={y}, button={button}, pressed={pressed}")
        return True

    def on_move(self, x, y):
        self.logger.info(f"鼠标移动: x={x}, y={y}")
        return True

    def on_scroll(self, x, y, dx, dy):
        self.logger.info(f"鼠标滚动: x={x}, y={y}, dx={dx}, dy={dy}")
        return True