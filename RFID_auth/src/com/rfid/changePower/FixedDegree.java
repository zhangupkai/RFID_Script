package com.rfid.changePower;

import com.impinj.octane.*;
import com.rfid.config.FixedDegreeConfig;
import com.rfid.readerPrint.ReadPrintUtils;
import com.rfid.rfTool.TagReportListenerImplementation;

import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Date;
import java.util.List;
import java.util.Scanner;

public class FixedDegree {
    /**
     * 普通采集相位的程序
     *
     * @param
     * @return
     * @author Zhang QiHang.
     * @date 2021/11/5 16:28
     */
//    public static void collectNormalPhase(String count) {
//        String hostname = FixedDegreeConfig.hostname;
//        // 记录总信息
//        ArrayList<String> TagInfoArray = new ArrayList<String>();
//        try {
//            if (hostname == null) {
//                throw new Exception("Must specify the hostname property'");
//            }
//
//            // 创建阅读器对象
//            ImpinjReader reader = new ImpinjReader();
//
//            // 进行连接
//            while (!reader.isConnected()) {
//                try {
//                    System.out.println("Connecting to " + hostname);
//                    reader.connect(hostname);
//                } catch (OctaneSdkException e1) {
//                    System.out.println("******************************************************************" + e1.getMessage());
//                } catch (Exception e2) {
//                    System.out.println("******************************************************************" + e2.getMessage());
//                    e2.printStackTrace(System.out);
//                }
//            }
//            // 包含阅读器的功能和特性
//            FeatureSet f = reader.queryFeatureSet();
//            String readerModel = f.getReaderModel().toString();//SpeedwayR420 SpeedwayR220
//
//
//            // Setting类为阅读器的配置类，获取阅读器的默认设置，如readerMode，searchMode，filters
//            Settings settings = reader.queryDefaultSettings();
//
//            System.out.println(readerModel);
//
//            // 可以对标签进行一系列的调整
//            ReportConfig report = settings.getReport();
//            report.setIncludeAntennaPortNumber(true);
//            report.setIncludePeakRssi(true);
//            report.setIncludePhaseAngle(true);
//            report.setIncludeLastSeenTime(true);
//            report.setIncludeChannel(true);
//            report.setMode(ReportMode.Individual);// 每个标签单独作为一个report返回
//            report.setMode(ReportMode.Individual);
//
//            // 设置过滤标签设置
//            TagFilter filter1 = new TagFilter();
//            filter1.setMemoryBank(MemoryBank.Epc);
//            filter1.setBitPointer(BitPointers.Epc);
//            filter1.setBitCount(4L * FixedDegreeConfig.targetMask.length());
//            filter1.setTagMask(FixedDegreeConfig.targetMask);
//            filter1.setFilterOp(TagFilterOp.Match);
//            FilterSettings filterSettings = new FilterSettings();
//            filterSettings.setTagFilter1(filter1);
//            filterSettings.setMode(TagFilterMode.OnlyFilter1);
//            settings.setFilters(filterSettings);
//
//            String mode = ReadPrintUtils.chooseMode(readerModel, FixedDegreeConfig.mode);
//            settings.setReaderMode(ReaderMode.valueOf(mode));
//
//            // 可以对天线进行一系列的调整
//            AntennaConfigGroup antennas = settings.getAntennas();
//            antennas.disableAll();
//            antennas.enableById(new short[]{1});
//            antennas.getAntenna((short) 1).setIsMaxRxSensitivity(false);
//            antennas.getAntenna((short) 1).setIsMaxTxPower(false);
//            antennas.getAntenna((short) 1).setTxPowerinDbm(FixedDegreeConfig.TxPowerinDbm);
//            antennas.getAntenna((short) 1).setRxSensitivityinDbm(-70);
//
//            // 对标签返回信息做了规范
//            reader.setTagReportListener(new TagReportListenerImplementation() {
//                @Override
//                public void onTagReported(ImpinjReader reader0, TagReport report0) {
//                    // tags为得到的所有标签
//                    List<Tag> tags = report0.getTags();
//                    for (Tag t : tags) {
//                        if (FixedDegreeConfig.targetMask.equals(t.getEpc().toString())) {
//                            String temp = t.getEpc().toString() + "," + t.getChannelInMhz() + ","
//                                    + t.getLastSeenTime().ToString() + "," + t.getPhaseAngleInRadians()
//                                    + "," + t.getPeakRssiInDbm();
//                            System.out.println(temp);
//                            TagInfoArray.add(temp);
//                        }
//                        // 如果标签阵列中有当前监听到的标签
//                    }
//                }
//            });
//
//            // 直接更改不会生效，必须进行apply
//            reader.applySettings(settings);
//
//            //开始扫描
//            System.out.println("在控制台敲击回车开始扫描.");
//            System.out.println("再次敲击回车结束扫描.");
//            Scanner s = new Scanner(System.in);
//            s.nextLine();
//            //System.out.println("Starting");
//            reader.start();
//            s = new Scanner(System.in);
//            s.nextLine();
//            reader.stop();
//            reader.disconnect();
//
//            myWriteFile("normal", TagInfoArray, count);
//        } catch (OctaneSdkException ex) {
//            System.out.println(ex.getMessage());
//        } catch (Exception ex) {
//            System.out.println(ex.getMessage());
//            ex.printStackTrace(System.out);
//        }
//    }


    public static void collectHoppingPhase(String count) {
        String hostname = FixedDegreeConfig.hostname;
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
            filter1.setBitCount(4L * FixedDegreeConfig.targetMask1.length());
            filter1.setTagMask(FixedDegreeConfig.targetMask1);
            filter1.setFilterOp(TagFilterOp.Match);

            TagFilter filter2 = new TagFilter();
            filter2.setMemoryBank(MemoryBank.Epc);
            filter2.setBitPointer(BitPointers.Epc);
            filter2.setBitCount(4L * FixedDegreeConfig.targetMask2.length());
            filter2.setTagMask(FixedDegreeConfig.targetMask2);
            filter2.setFilterOp(TagFilterOp.Match);

            FilterSettings filterSettings = new FilterSettings();
            filterSettings.setTagFilter1(filter1);
            filterSettings.setTagFilter2(filter2);
            filterSettings.setMode(TagFilterMode.Filter1OrFilter2);
            settings.setFilters(filterSettings);


            String mode = ReadPrintUtils.chooseMode(readerModel, FixedDegreeConfig.mode);
            settings.setReaderMode(ReaderMode.valueOf(mode));

            // 可以对天线进行一系列的调整
            AntennaConfigGroup antennas = settings.getAntennas();
            antennas.disableAll();
            antennas.enableById(new short[]{1});
            antennas.getAntenna((short) 1).setIsMaxRxSensitivity(false);
            antennas.getAntenna((short) 1).setIsMaxTxPower(false);
            antennas.getAntenna((short) 1).setTxPowerinDbm(FixedDegreeConfig.TxPowerinDbm);
            antennas.getAntenna((short) 1).setRxSensitivityinDbm(-70);

//            调频处理
//            if (!f.isHoppingRegion()) {
//                Collections.shuffle(FixedDegreeConfig.freqList);
//                ArrayList<Double> freqList = new ArrayList<>(FixedDegreeConfig.freqList);
//                settings.setTxFrequenciesInMhz(freqList);
//            }

            // 不跳频
//            ArrayList<Double> freqList = new ArrayList<>();
//            freqList.add(FixedDegreeConfig.freq);
            // ----

            // 跳频
            ArrayList<Double> freqList = new ArrayList<>(FixedDegreeConfig.freqList);
            // ----

            settings.setTxFrequenciesInMhz(freqList);
//            freqList.clear();
            // 直接更改不会生效，必须进行apply
            reader.applySettings(settings);

            // 对标签返回信息做了规范
            reader.setTagReportListener(new TagReportListenerImplementation() {
                @Override
                public void onTagReported(ImpinjReader reader0, TagReport report0) {
                    // tags为得到的所有标签
                    List<Tag> tags = report0.getTags();
                    for (Tag t : tags) {
                        if (FixedDegreeConfig.targetMask1.equals(t.getEpc().toString())
                                || FixedDegreeConfig.targetMask2.equals(t.getEpc().toString())) {
                            String temp = t.getEpc().toString() + "," + t.getChannelInMhz() + ","
                                    + t.getLastSeenTime().ToString() + "," + (2*Math.PI - t.getPhaseAngleInRadians())
                                    + "," + t.getPeakRssiInDbm();
                            System.out.println(temp);
                            TagInfoArray.add(temp);
                        }
                        // 如果标签阵列中有当前监听到的标签
                    }
                }
            });



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
            Thread.sleep(FixedDegreeConfig.duration);
            reader.stop();
            Thread.sleep(500);
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

//        File file = new File(FixedDegreeConfig.filePath + timeFlag + filename + ".csv");
        File file = new File(FixedDegreeConfig.filePath + filename
                + FixedDegreeConfig.targetMask1
                + "_" + FixedDegreeConfig.targetMask2
                + count
                + "_" + FixedDegreeConfig.TxPowerinDbm
//                + "_" + FixedDegreeConfig.freq
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
    public static void main(String[] args) {
//        collectHoppingPhase();
//        String[] tags = new String[]{"A991", "A992", "A993", "A994", "A995"};
        String[] tags = new String[]{"E002", "C001"};
//        String[] tags = new String[]{"B023"};
//        String baseDir = "D:\\Coding\\RFID\\RFID_Script\\data\\tagPair\\auto_rotation\\B034_B029\\";
        String baseDir = "D:\\Coding\\RFID\\RFID_Script\\data\\tagPair\\fixed_degree\\E002_C001\\degree_360\\";

//        int count = 2;
        for (int count = 46; count <= 46 ; ++count) {
           FixedDegreeConfig.targetMask1 = tags[0];
           FixedDegreeConfig.targetMask2 = tags[1];
           FixedDegreeConfig.filePath = baseDir;
           collectHoppingPhase("(" + count + ")");
        }


        // 920.625 ~ +0.5 ~ 924.375
//        double[] freqList = FixedDegreeConfig.getFreqList(920.625, 924.375);
//        // 24 ~ +1 ~ 31
//        // 24
//        double[] powerList = FixedDegreeConfig.getPowerList(24.0, 24.0);
//        for (String tag : tags) {
//            FixedDegreeConfig.targetMask = tag;
//            FixedDegreeConfig.filePath = baseDir;
//            for (double power : powerList) {
//                FixedDegreeConfig.TxPowerinDbm = power;
//                for (double freq : freqList) {
//                    FixedDegreeConfig.freq = freq;
//                    collectHoppingPhase();
//                }
//            }
//        }
    }
}

