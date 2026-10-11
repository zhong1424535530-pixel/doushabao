# 豆沙包

用于 Discord 的中文 AI 问答机器人，通过本机 AI 中转服务连接 xAI 的 Grok。

## 功能

- 在频道中 @豆沙包，可以提问。
- 回复豆沙包之前的消息，可以继续对话。
- 支持随提问上传图片，每次最多读取 3 张。
- 给 AI 提供网页和 X 搜索工具，实际可用情况取决于中转服务。
- 过长的回答会自动拆成多条 Discord 消息。

股票研究专用功能已移除。本版本尚未加入自动查询其他频道历史消息的能力。

## 运行前准备

需要 Python 3.10 或更新版本，并确保 Discord 机器人已加入你的服务器。

在 Discord 机器人设置中开启读取消息内容的开关，并给机器人查看频道、发送消息和读取历史消息的权限。

本机需要已有可用的 AI 中转服务，默认地址为 `http://127.0.0.1:8317/v1`，并支持 `grok-4.20-0309-non-reasoning` 及程序使用的工具和图片格式。中转程序的官方代码和服务器运行程序副本已保存在 `grok-proxy/` 中；真实登录资料不包含在本仓库中。

## 安装和启动

在项目目录执行：

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
cp 运行配置.example.sh 运行配置.sh
chmod 600 运行配置.sh
```

打开 `运行配置.sh`，填写 Discord 机器人口令，以及与本机中转服务配置一致的口令。然后执行：

```bash
source 运行配置.sh
python bot.py
```

如果使用服务器的自动启动功能，也需要给启动程序设置 `DISCORD_TOKEN` 和 `GROK_PROXY_API_KEY` 这两个值。

`config.example.yaml` 只是中转服务的配置示例，豆沙包不会直接读取这个文件。

## 文件说明

- `bot.py`：收取提问、调用 AI 和发送回答。
- `bot_logic.py`：保留对话、整理图片和拆分长消息。
- `requirements.txt`：运行所需的第三方工具。
- `运行配置.example.sh`：填写本机口令的示例。
- `config.example.yaml`：AI 中转服务的配置示例。

## 注意事项

对话只保留在运行中的程序里，重启后会丢失。每条对话保留最近 12 条消息，最多记录 300 个回答的对话。

真实口令、`.env`、`运行配置.sh`、`config.yaml`、AI 登录资料及运行日志都不要上传到仓库。

这是根据当前服务器项目整理出的上传版本；尚未运行模拟测试。

## Grok 登录和中转程序

需要分析 Grok 登录和调用方式时，请从 [中转程序说明](grok-proxy/README.md) 和 [给其他 AI 的分析说明](grok-proxy/给其他AI的分析说明.md) 开始。

其中包含 CLIProxyAPI 7.1.19 的完整官方代码，以及与官方发布一致的当前服务器运行程序。服务器上的实际配置、口令和登录资料未上传。
