# SonarQube Rules Exporter

## 项目概述

SonarQube Rules Exporter 是一个 Python 脚本，用于从 SonarQube 的不同编程语言规则页面抓取静态代码分析规则，并将其导出为 Excel 文件。此脚本支持多种编程语言，方便用户快速获取和分析 SonarQube 规则。

## 功能

- 支持多种编程语言的 SonarQube 规则导出。
- 将规则导出为结构化的 Excel 文件。
- 自动编号导出的规则，便于参考和分析。

## 如何使用

1. 确保您的环境中已安装 Python 以及以下依赖库：
   - `requests`
   - `beautifulsoup4` (或 `bs4`)
   - `pandas`
   - `openpyxl`

2. 运行脚本前，根据需要修改或确认脚本中的 URL。

3. 使用以下命令运行脚本：

   ```bash
   python sonar_rules_exporter.py
