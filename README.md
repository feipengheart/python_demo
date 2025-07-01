# Python FastAPI Demo

A demonstration API built with FastAPI showcasing best practices for API development.

## Features

- RESTful API endpoints
- Automatic OpenAPI/Swagger documentation
- Configuration management
- Versioned API routes
- Example service layer

## Running the Application

Start the development server:

```
python main.py
```

## API Documentation

- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

## Project Structure

```
.
├── app/                      # 主应用代码
│   ├── api/                  # API接口层
│   │   └── v1/               # API版本1
│   │       ├── __init__.py   # 包初始化文件
│   │       ├── endpoints/    # API端点实现
│   │       │   ├── demo.py   # 示例API端点
│   │       │   └── ping.py   # 健康检查端点
│   │       └── schemas/      # 请求/响应数据模型
│   │           └── default.py # 基础数据模型
│   ├── core/                 # 核心功能模块
│   │   ├── config.py         # 应用配置管理
│   │   └── utils/            # 工具类
│   │       ├── datetime_utils.py # 日期时间工具
│   │       └── logger.py     # 日志记录工具
│   └── services/             # 业务服务层
│       └── example_service.py # 示例服务实现
├── .gitignore                # Git忽略规则
├── main.py                   # 应用入口文件
└── start_docker.sh           # Docker启动脚本
```

### 目录详细说明

- **app/api/**
  - 包含所有API接口代码，按版本组织
  - `endpoints/`: 
    - `demo.py`: 示例API端点实现
    - `ping.py`: 健康检查端点
  - `schemas/`: 
    - `default.py`: 基础数据模型定义

- **app/core/**
  - 核心功能和基础配置
  - `config.py`: 应用配置管理
  - `utils/`: 
    - `datetime_utils.py`: 日期时间处理工具
    - `logger.py`: 日志记录工具

- **app/services/**
  - 业务服务层
  - `example_service.py`: 示例服务实现

- **logs/**
  - 应用日志存储目录，按日期自动组织

- **根目录文件**
  - `.gitignore`: Git版本控制忽略规则
  - `main.py`: FastAPI应用主入口
  - `start_docker.sh`: Docker容器启动脚本