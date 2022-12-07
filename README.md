# RFID_Script
> 一些采集RFID数据的脚本

- RFID_auth/src/com/rfid/changePower：主要数据采集代码
  - CollectHopFreq.java：采集跳频情况下的射频信号数据
- RFID_auth/src/com/rfid/config：相关配置文件
  - ChangePowerConfig.java：对应`CollectHopFreq` 采集程序的配置文件
- data：采集的原始射频信号数据
- DataProcess：数据处理相关代码及数据
  - auto_rotation：处理旋转收集的射频信号数据
    - phase_orientation_time_tag_pair：从原始数据中提取相位时间序列
    - single_freq_build_phase_mat：根据相位时间序列进行角度定位并构建特征矩阵
    - phase_time_sequence：相位时间序列数据
    - phase_mat_data：特征矩阵数据
    - locate_degree：角度定位相关代码
    - test_phase_cut_sequence：测试天线朝向相关代码（含滑动窗口截取有效时间序列）
  - utils：各类工具方法



PS：

论文扩展思路及验证实验结果（草稿）：https://www.yuque.com/docs/share/f0cddbc4-2ebe-4c62-b697-bc050bed99e7?# 《论文扩展实验》