import os
import logging
from logging.handlers import TimedRotatingFileHandler
from logging import Formatter, StreamHandler  # 新增 StreamHandler


class Logger(logging.Logger):
    def __init__(self, name=None, log_dir="logs"):
        """
        初始化日志记录器
        :param name: 日志记录器的名称，默认为调用者的模块名
        :param log_dir: 日志文件存储目录，默认为当前目录下的 "logs" 文件夹
        """
        # 如果未指定 name，则使用调用者的模块名
        if name is None:
            import inspect
            frame = inspect.stack()[1]
            module = inspect.getmodule(frame[0])
            name = module.__name__ if module else "unknown"

        super(Logger, self).__init__(name)

        # 配置文件日志处理器
        os.makedirs(log_dir, exist_ok=True)
        log_file_path = os.path.join(log_dir, "using.log")

        file_handler = TimedRotatingFileHandler(
            log_file_path, when="midnight", backupCount=7, encoding="utf-8"
        )
        log_formatter = Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        file_handler.setFormatter(log_formatter)
        self.addHandler(file_handler)

        # 配置控制台日志处理器
        console_handler = StreamHandler()  # 新增控制台处理器
        console_handler.setFormatter(log_formatter)  # 使用相同的格式化器
        self.addHandler(console_handler)  # 将控制台处理器添加到日志记录器


# 为了兼容使用 logging 模块的其他代码，可以添加以下代码
logging.setLoggerClass(Logger)