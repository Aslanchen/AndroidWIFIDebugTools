# 说明
Android支持WIFI调试，但开启的流程不是很方便，所以就诞生了这个工具，一键开启。
- 一键开启
- 支持同时开启多台手机
- 支持多个平台（windows，linux，mac）

# 前提准备
- 电脑支持python3.7。
- 设置adb系统环境变量。
- 手机和电脑先用数据线usb连接。
- 打开手机的开发者调试模式（系统设置-开发者工具-打开debug模式-打开usb调试）。
- 确保手机和pc是在同一个WIFI下面。

# 开始
- 前提准备之后，运行connect devices.py即可。
- 查看已经连接设备，运行devices.py即可。

# License
```
Copyright 2020 Aslan(ChenHengFei)

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```