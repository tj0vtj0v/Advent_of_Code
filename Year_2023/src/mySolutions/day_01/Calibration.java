package mySolutions.day_01;

import mySolutions.generals.InputFile;

public class Calibration {
    private final String[] fileContent;

    public Calibration() {
        fileContent = new InputFile("01").readFile();
    }

    public int sum() {
        int calibrationSum = 0;

        for (String line : fileContent) {
            calibrationSum += calibrationValue(line);
        }

        return calibrationSum;
    }

    private int calibrationValue(String line) {
        return frontDigit(line) * 10 + backDigit(line);
    }


    private int frontDigit(String line) {
        for (int index = 0; index < line.length(); index++) {
            char charAtIndex = line.charAt(index);

            if (Character.isDigit(charAtIndex)) {
                return (charAtIndex - '0');
            }
        }

        return -1;
    }

    private int backDigit(String line) {
        for (int index = 1; index <= line.length(); index++) {
            char charAtIndex = line.charAt(line.length() - index);

            if (Character.isDigit(charAtIndex)) {
                return charAtIndex - '0';
            }
        }

        return -1;
    }

    public void textToDigits() {
        String[] digitText = new String[]{"zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
        System.out.println(fileContent.length);
        for (int line = 0; line < fileContent.length; line++) {
            for (int index = 0; index < fileContent[line].length(); index++) {
                for (int digit = 0; digit <= 9; digit++) {
                    if (fileContent[line].length() >= digitText[digit].length()) {
                        if (fileContent[line].startsWith(digitText[digit], index)) {
                            fileContent[line] = fileContent[line].substring(0, index) + digit + fileContent[line].substring(index + digitText[digit].length());
                        }
                    }
                }
            }
        }
    }
}
