# AGENTS

本文件定义本项目的标准开发与发布流程。除非有明确说明，所有命令都在仓库根目录执行。

## 1. 环境准备

前置要求：
- Python `3.12+`（与 `pyproject.toml` 中 `requires-python = ">=3.12"` 一致）

使用 `uv`（推荐）：

```bash
# 同步开发环境（含 dev 依赖）
uv sync --extra dev

# CI/发布前：严格按 uv.lock 同步
uv sync --frozen --extra dev

# 仅运行时依赖（不含 dev）
uv sync --no-dev
```

使用 `pip`：

```bash
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

说明：
- `uv sync --extra dev` 与 `pip install -e ".[dev]"` 的目标一致：安装开发依赖。

## 2. 打包（Wheel / sdist）

```bash
# 使用 uv 管理环境时（推荐）
uv run python -m build

# 或直接使用当前 Python 环境
python -m build
```

产物目录：
- `dist/*.whl`
- `dist/*.tar.gz`

发布前建议校验包元数据：

```bash
uv run python -m twine check dist/*
# 或
python -m twine check dist/*
```

## 3. 安装验证

使用本地构建的 wheel 验证安装：

```bash
uv run python -m pip install --force-reinstall dist/*.whl
# 或
python -m pip install --force-reinstall dist/*.whl
```

## 4. 测试

```bash
uv run pytest
# 或
pytest
```

## 5. 代码风格检查

只检查（CI 推荐）：

```bash
uv run ruff format --check .
uv run ruff check .
# 或
ruff format --check .
ruff check .
```

自动修复（本地开发可用）：

```bash
uv run ruff format .
uv run ruff check --fix .
# 或
ruff format .
ruff check --fix .
```

## 6. 建议的发布前顺序

```bash
uv sync --frozen --extra dev
uv run python -m build
uv run python -m twine check dist/*
uv run pytest
uv run ruff format --check .
uv run ruff check .

# 或（非 uv）
python -m build
python -m twine check dist/*
pytest
ruff format --check .
ruff check .
```
