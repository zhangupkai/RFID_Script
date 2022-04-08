package com.rfid.config;

import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class ChangePowerConfig {
    // 阅读器地址：192.168.1.221
    public static String hostname = "192.168.1.221";
    // 天线端口选择  R220:{1,2}  R420:{1,2,3,4}
    public static short[] port = new short[]{1};
    // 传输功率设定(10 ~ 32.5, 间隔0.25，共91个可选功率)
    public static double TxPowerinDbm = 25;

    public static double freq = 920.625;

    // 接收灵敏度设定
    public double RxSensitivityinDbm = -70.0;
    // 阅读器模式
    public static String mode = "MaxThroughput";
    // 标签过滤设定
    public static String targetMask1 = "";
    public static String targetMask2 = "";

    // 采集的数据存放的位置
    public static String filePath = "D:\\Coding\\RFID\\RFID_Script\\data\\tagPair\\degree_180\\";

    // 读取时间 Level 1 => 6min, Level 2 => 3min, Level 4 => 1min
    public static long duration = 60 * 1000 * 3;
    // 手动设置跳频，一个频率的持续时间
    public static long stayTime = 500;

    // 频率列表
    public static List<Double> freqList = Arrays.stream(getFreqList(920.625, 924.375)).boxed().collect(Collectors.toList());
//    public static List<Double> freqList = Arrays.stream(getFreqList(920.625, 920.625)).boxed().collect(Collectors.toList());

//    public static double[] freqList = getFreqList(920.625, 924.375);

    // 功率列表
    public static double[] powerList = getPowerList(20.0, 21.0);

    public static double[] getFreqList(Double startFreq, Double endFreq) {

        // (根据最小间隔0.25Mhz从920.625 MHz to 924.375生成频率列表 共16个)
        // 根据最小间隔0.5Mhz从920.625 MHz to 924.375生成频率列表 共8个
        double[] freqList = new double[(int) ((endFreq - startFreq) / 0.5 + 1)];
        for (int i = 0; i < freqList.length; i++) {
            freqList[i] = startFreq + i * 0.5;
        }
        return freqList;
    }

    public static double[] getPowerList(Double startPower, Double endPower) {
        // 根据最小间隔1db从10db到31db生成功率列表 共85个功率
        double[] powerList = new double[(int) ((endPower - startPower) / 1.0 + 1)];
        for (int i = 0; i < powerList.length; i++) {
            powerList[i] = startPower + i * 1.0;
        }
        return powerList;
    }

}
