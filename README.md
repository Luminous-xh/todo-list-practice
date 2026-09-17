# api-server

Python 3.13 项目。环境与依赖使用 [Miniforge](https://conda-forge.org/miniforge/) + [conda-lock](https://github.com/conda/conda-lock) 管理：
`environment.yml` 是唯一手工维护的依赖清单，`conda-lock.yml` 是跨平台锁文件（自动生成，**不要手改**）。

## 支持平台

锁文件覆盖以下平台，`conda-lock install` 只会为当前系统安装：

| 平台 | 架构 |
| --- | --- |
| `linux-64` | x86_64 Linux |
| `osx-64` | Intel macOS |
| `osx-arm64` | Apple Silicon macOS |
| `win-64` | Windows x64 |

其它平台（如 `linux-aarch64`）需要先加入 `environment.yml` 的 `platforms` 并重新生成锁文件，否则 `conda-lock install` 会因默认的 `--validate-platform` 校验直接报错。

## 首次安装

```bash
cd api-server
```

### 1. 安装 Miniforge

<https://conda-forge.org/miniforge/>

### 2. 初始化 conda

```bash
conda init
```

执行后需**重开终端**（或重新加载对应 shell 的 profile）才会生效。

### 3. 安装 conda-lock（如果没有安装）

```bash
conda install -n base conda-lock -y
```

conda-lock 是锁定/安装工具，只需存在于 `base` 环境，**不要**把它写进 `environment.yml`——否则它连同 gitpython、dulwich、keyring、virtualenv 等一整套构建工具链都会被锁进运行时环境。

### 4. 创建项目环境

```bash
conda-lock install --name api-server conda-lock.yml
```

环境名由 `--name` 决定（这里覆盖 `environment.yml` 里的 `name`），请与后续 `activate` 的名称保持一致。

### 5. 激活环境

```bash
conda activate api-server
```

### 6. 运行

```bash
python -m src.main
```

当前入口只打印 `Hello World`。

## 日常维护

### 修改依赖

编辑 `environment.yml` 的 `dependencies`，然后重新求解锁文件：

```bash
conda-lock lock -f environment.yml --lockfile conda-lock.yml
```

`environment.yml` 与 `conda-lock.yml` 的改动需要一起提交，否则别人拿到的锁文件会和依赖清单不一致。

### 只升级某个包

```bash
conda-lock lock -f environment.yml --lockfile conda-lock.yml --update numpy
```

省略 `--update` 及其参数则重新求解整个环境。

### 按锁文件重建环境

```bash
# 环境未激活
conda-lock install --name api-server conda-lock.yml
# 环境已激活
conda env update -f environment.yml
```

## 目录结构

```
.
├── environment.yml    # 依赖声明（手工维护）
├── conda-lock.yml     # 跨平台锁文件（conda-lock 生成，勿手改）
├── src/
│   └── main.py        # 程序入口
└── tests/             # 测试目录（暂无用例）
```