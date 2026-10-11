# 豆沙包使用的 Grok 中转程序

这个目录保存了豆沙包依赖的 CLIProxyAPI 原版代码，以及服务器当前使用的运行程序，方便其他 AI 分析和改进。

## 从哪里开始看

- `source/internal/cmd/xai_login.go`：Grok 登录入口。
- `source/sdk/auth/xai.go`：打开登录页面、接收登录结果和保存登录资料。
- `source/internal/auth/xai/xai.go`：登录验证、交换登录凭据和续期。
- `source/internal/auth/xai/token.go`：登录资料的保存格式。
- `source/internal/runtime/executor/xai_executor.go`：向 Grok 提交问题、图片和工具请求，并处理返回结果。
- `source/internal/api/`：接收豆沙包发来的请求。
- `source/internal/translator/`：转换不同 AI 服务的消息格式。
- 仓库根目录的 `bot.py`：Discord 问答机器人如何调用这个中转程序。

## 版本来源

- 官方项目：https://github.com/router-for-me/CLIProxyAPI
- 服务器运行版本：`7.1.19`。
- 对应代码版本：`21fad9dbb447a2ab70d51d0ac3e3d032525a6054`。
- 官方发布：https://github.com/router-for-me/CLIProxyAPI/releases/tag/v7.1.19
- `source/` 保存上述固定版本的完整官方代码，保留原有许可证和文件。
- `runtime/cli-proxy-api-linux-amd64.gz` 是服务器当前运行程序的压缩副本。它与官方发布包中的程序逐字节一致。
- `版本来源.json` 保存了版本、来源和文件指纹，方便核对。

程序内置的构建记录有 `vcs.modified=true` 标记，但服务器程序与官方发布程序完全相同。这个标记本身不能当作“服务器另外改过代码”的证据。

## 当前连接关系

Discord 用户 → 根目录的 `bot.py` → 本机 `http://127.0.0.1:8317/v1` → CLIProxyAPI → xAI Grok → 返回回答。

豆沙包当前使用 `grok-4.20-0309-non-reasoning`，会提交文字、最多 3 张图片，以及网页搜索和 X 搜索工具。

`config.example.yaml` 是去掉实际口令后的中转配置示例。服务器实际使用的配置和登录资料没有放进仓库。

## 给其他 AI 的说明

请先阅读旁边的 `给其他AI的分析说明.md`，然后重点查看 Grok 登录和请求处理文件。

本次只是整理并上传文件，没有修改服务器上的运行程序，没有重启服务，也没有进行模拟测试。

## 许可证

官方代码按原有 MIT 许可证保留，见 `source/LICENSE`。这里的官方代码和官方运行程序也遵循该许可证。
