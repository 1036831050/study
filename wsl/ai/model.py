import os
import logging
from datetime import datetime


def setup_logger():
    """设置日志记录器，仅记录到文件中"""
    # 获取脚本所在目录的绝对路径
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # 构建日志文件的完整路径
    log_file = os.path.join(script_dir, "dialogue_log_" + datetime.now().strftime('%Y-%m-%d') + ".txt")
    
    # 创建一个logger
    logger = logging.getLogger('DialogueSystem')
    logger.setLevel(logging.DEBUG)  # 设置日志级别为DEBUG以记录更多细节
    
    # 创建一个handler，用于写入日志文件
    file_handler = logging.FileHandler(log_file, encoding='utf-8')
    file_handler.setLevel(logging.DEBUG)  # 设置文件handler的日志级别为DEBUG
    
    # 定义handler的输出格式
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    
    # 给logger添加handler（仅添加文件handler）
    logger.addHandler(file_handler)
    
    return logger

