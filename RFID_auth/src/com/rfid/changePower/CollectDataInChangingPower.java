package com.rfid.changePower;

import com.impinj.octane.*;
import com.rfid.config.ChangePowerConfig;
import com.rfid.config.ChangePowerConfig;
import com.rfid.readerPrint.ReadPrintUtils;
import com.rfid.rfTool.TagReportListenerImplementation;

import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.text.SimpleDateFormat;
import java.util.*;

public class CollectDataInChangingPower extends Thread{

    private String count;
    private volatile boolean flag = false;

    @Override
    public void run() {
        String hostname = ChangePowerConfig.hostname;
        // 记录总信息
        ArrayList<String> TagInfoArray = new ArrayList<String>();
        try {
            if (hostname == null) {
                throw new Exception("Must specify the hostname property'");
            }

            // 创建阅读器对象
            ImpinjReader reader = new ImpinjReader();

            // 进行连接
            while (!reader.isConnected()) {
                try {
                    System.out.println("Connecting to " + hostname);
                    reader.connect(hostname);
                } catch (OctaneSdkException e1) {
                    System.out.println("******************************************************************" + e1.getMessage());
                } catch (Exception e2) {
                    System.out.println("******************************************************************" + e2.getMessage());
                    e2.printStackTrace(System.out);
                }
            }
            // 包含阅读器的功能和特性
            FeatureSet f = reader.queryFeatureSet();
            String readerModel = f.getReaderModel().toString();//SpeedwayR420 SpeedwayR220

            // 频率列表
            double[] freqList = ChangePowerConfig.getFreqList(920.625, 924.125);
            int freqIndex = 0;
            while (!flag){
                // 按顺序访问频率
                double freq = freqList[freqIndex];
                freqIndex++;
                if (freqIndex > 7) {
                    freqIndex = 0;
                }
                // 随机选择持续时间
                long stayTime = ChangePowerConfig.stayTime;

                // Setting类为阅读器的配置类，获取阅读器的默认设置，如readerMode，searchMode，filters
                Settings settings = reader.queryDefaultSettings();

                System.out.println(readerModel);

                // 可以对标签进行一系列的调整
                ReportConfig report = settings.getReport();
                report.setIncludeAntennaPortNumber(true);
                report.setIncludePeakRssi(true);
                report.setIncludePhaseAngle(true);
                report.setIncludeLastSeenTime(true);
                report.setIncludeChannel(true);
                report.setMode(ReportMode.Individual);// 每个标签单独作为一个report返回
                report.setMode(ReportMode.Individual);

                // 设置过滤标签设置
                TagFilter filter1 = new TagFilter();
                filter1.setMemoryBank(MemoryBank.Epc);
                filter1.setBitPointer(BitPointers.Epc);
                filter1.setBitCount(4L * ChangePowerConfig.targetMask1.length());
                filter1.setTagMask(ChangePowerConfig.targetMask1);
                filter1.setFilterOp(TagFilterOp.Match);

                TagFilter filter2 = new TagFilter();
                filter2.setMemoryBank(MemoryBank.Epc);
                filter2.setBitPointer(BitPointers.Epc);
                filter2.setBitCount(4L * ChangePowerConfig.targetMask2.length());
                filter2.setTagMask(ChangePowerConfig.targetMask2);
                filter2.setFilterOp(TagFilterOp.Match);

                FilterSettings filterSettings = new FilterSettings();
                filterSettings.setTagFilter1(filter1);
                filterSettings.setTagFilter2(filter2);
                filterSettings.setMode(TagFilterMode.Filter1OrFilter2);
                settings.setFilters(filterSettings);


                String mode = ReadPrintUtils.chooseMode(readerModel, ChangePowerConfig.mode);
                settings.setReaderMode(ReaderMode.valueOf(mode));

                // 可以对天线进行一系列的调整
                AntennaConfigGroup antennas = settings.getAntennas();
                antennas.disableAll();
                antennas.enableById(new short[]{1});
                antennas.getAntenna((short) 1).setIsMaxRxSensitivity(false);
                antennas.getAntenna((short) 1).setIsMaxTxPower(false);
                antennas.getAntenna((short) 1).setTxPowerinDbm(ChangePowerConfig.TxPowerinDbm);
                antennas.getAntenna((short) 1).setRxSensitivityinDbm(-70);

                /* 内置方法跳频
                    ArrayList<Double> freqList = new ArrayList<>(ChangePowerConfig.freqList);
                */

                // 外层循环跳频
                ArrayList<Double> freqs = new ArrayList<>();
                freqs.add(freq);
                settings.setTxFrequenciesInMhz(freqs);
                // freqList.clear();


                // 对标签返回信息做了规范
                reader.setTagReportListener(new TagReportListenerImplementation() {
                    @Override
                    public void onTagReported(ImpinjReader reader0, TagReport report0) {
                        // tags为得到的所有标签
                        List<Tag> tags = report0.getTags();
                        for (Tag t : tags) {
                            if (ChangePowerConfig.targetMask1.equals(t.getEpc().toString())
                                    || ChangePowerConfig.targetMask2.equals(t.getEpc().toString())) {
                                String temp = t.getEpc().toString() + "," + t.getChannelInMhz() + ","
                                        + t.getLastSeenTime().ToString() + "," + (2*Math.PI - t.getPhaseAngleInRadians())
                                        + "," + t.getPeakRssiInDbm() + ","  + freq;
                                System.out.println(temp);
                                TagInfoArray.add(temp);
                            }
                            // 如果标签阵列中有当前监听到的标签
                        }
                    }
                });

                // 直接更改不会生效，必须进行apply
                reader.applySettings(settings);

                /*
                // Scanner Mode 1 Start：手动开始和结束扫描
                //开始扫描
                System.out.println("在控制台敲击回车开始扫描.");
                System.out.println("再次敲击回车结束扫描.");
                Scanner s = new Scanner(System.in);
                s.nextLine();
                //System.out.println("Starting");
                reader.start();
                s = new Scanner(System.in);
                s.nextLine();
                reader.stop();
                reader.disconnect();
                // Scanner Mode 2 Finish


                 */

                // Scanner Mode 2 Start：自动开始，定时结束
                reader.start();
                // 定时自动结束
                // 单个频率持续的世界
                Thread.sleep(ChangePowerConfig.stayTime);
                reader.stop();
//                Thread.sleep(500);
            }


            reader.disconnect();
            // Scanner Mode 2 Finish
            myWriteFile("", TagInfoArray, count);

        } catch (OctaneSdkException ex) {
            System.out.println(ex.getMessage());
        } catch (Exception ex) {
            System.out.println(ex.getMessage());
            ex.printStackTrace(System.out);
        }
    }


    public static <T> void myWriteFile(String filename, ArrayList<T> content, String count) {
        String timeFlag = new SimpleDateFormat("yyyyMMddhhmmss").format(new Date());

        File file = new File(ChangePowerConfig.filePath + filename
                + ChangePowerConfig.targetMask1
                + "_" + ChangePowerConfig.targetMask2
                + count
                + "_" + ChangePowerConfig.TxPowerinDbm
                + ".csv");
        BufferedWriter bw = null;
        try {
            bw = new BufferedWriter(new FileWriter(file));
            for (int i = 0; i < content.size(); i++) {
                String temp = (String) content.get(i);
                bw.write(temp); // 写入所有的EPC,RSSI,Phase,Hz,time,天线号
                //	bw.write("," + (i + 1));// ,id
                bw.newLine();
            }
            bw.flush();
            bw.close();
        } catch (IOException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }
    }
    public static void main(String[] args) throws InterruptedException {
        String[] tags = new String[]{"E002", "C001"};
//        String[] tags = new String[]{"B023"};
        String baseDir = "D:\\Coding\\RFID\\RFID_Script\\data\\tagPair\\auto_rotation_v2\\E002_C001\\";
//        String baseDir = "D:\\Coding\\RFID\\RFID_Script\\data\\tagPair\\fixed_degree\\B034_B029\\";

        int countN = 5;
//        for (int countN = 21; countN <= 50 ; ++countN) {
            System.out.println("现在是 Count " + countN);

            Scanner sc = new Scanner(System.in);
            System.out.println("按任意键开始收集，按任意键结束收集");
            sc.nextLine();

            ChangePowerConfig.targetMask1 = tags[0];
            ChangePowerConfig.targetMask2 = tags[1];
            ChangePowerConfig.filePath = baseDir;
//           collectHoppingPhase("(" + count + ")");
            CollectDataInChangingPower cp = new CollectDataInChangingPower();
            cp.flag = false;
            cp.count = "(" + countN + ")";
            cp.start();

            // 一轮数据采集持续的时长
//            Thread.sleep(ChangePowerConfig.duration);

            Scanner scanner = new Scanner(System.in);
            scanner.nextLine();

            cp.flag = true;
//        }


        // 920.625 ~ +0.5 ~ 924.375
//        double[] freqList = ChangePowerConfig.getFreqList(920.625, 924.375);
//        // 24 ~ +1 ~ 31
//        // 24
//        double[] powerList = ChangePowerConfig.getPowerList(24.0, 24.0);
//        for (String tag : tags) {
//            ChangePowerConfig.targetMask = tag;
//            ChangePowerConfig.filePath = baseDir;
//            for (double power : powerList) {
//                ChangePowerConfig.TxPowerinDbm = power;
//                for (double freq : freqList) {
//                    ChangePowerConfig.freq = freq;
//                    collectHoppingPhase();
//                }
//            }
//        }
    }
}

