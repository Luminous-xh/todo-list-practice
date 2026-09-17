# 安装uv工具
```bash
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

# 安装依赖
```bash
uv sync
```

# 运行程序
```bash
uv run api-server
```