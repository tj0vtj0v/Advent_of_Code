package mySolutions.generals;

import mySolutions.day_01.Calibration;

public class Solver {
    public static void main(String[] args) {
        Calibration day1 = new Calibration();
        System.out.println(day1.sum());
        day1.textToDigits();
        System.out.println(day1.sum());
        // 54970 l
        // 55040 h

    }
}
