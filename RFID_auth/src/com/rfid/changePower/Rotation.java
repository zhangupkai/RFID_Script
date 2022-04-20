package com.rfid.changePower;

/**
 * @Description
 * @Author Kai
 * @Date 2022/4/13 11:10
 */
public enum Rotation {
    LEVEL1("level1", (60 * 4 + 30) * 1000),
    LEVEL2("level2", (60 * 2 + 30) * 1000),
    LEVEL3("level3", (60 + 30) * 1000),
    LEVEL4("level4", 60 * 1000);
    private String key;
    private long value;

    Rotation(String key, long value) {
        this.key = key;
        this.value = value;
    }

    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }

    public long getValue() {
        return value;
    }

    public void setValue(long value) {
        this.value = value;
    }
}
