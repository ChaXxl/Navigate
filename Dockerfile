# 拉取python3.9的官方镜像
FROM python:3.9

# 工作目录
WORKDIR /app

# 将项目复制到app目录
COPY . /app

# 安装依赖
RUN pip install -r BackEnd/requirements.txt

# 通过uwsgi运行Django项目
CMD ["uwsgi","--ini","BackEnd/wsgi.ini"] 
