# 使用官方 Python 镜像作为基础镜像
FROM python:3.10-slim

# 设置工作目录
WORKDIR /app

# 复制当前目录下的所有文件到工作目录中
COPY . .

# 安装项目的依赖
RUN pip install --no-cache-dir -r requirements.txt

# 暴露端口号
EXPOSE 4000

# 启动 Flask 应用
CMD ["python", "index.py"]