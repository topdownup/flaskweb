from flask import Flask
app = Flask(__name__,instance_relative_config=True)
app.config.from_object('source.config.config') # 从source下面加载config
# app.config.from_pyfile('config.py') # 从instance文件夹中加载配置
# APP_CONFIG_FILE是个指定路径，一般是绝对路径，可以在启动参数中定义
# app.config.from_envvar('APP_CONFIG_FILE')
from source import main