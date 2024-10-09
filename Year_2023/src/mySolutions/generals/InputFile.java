package mySolutions.generals;

import java.io.File;
import java.io.FileNotFoundException;
import java.nio.file.Path;
import java.util.Scanner;

public class InputFile {
    String filepath;

    public InputFile(String day) {
        filepath = System.getProperty("user.dir") + "\\Year_2023\\src\\mySolutions\\day_" + day + "\\input.txt";
    }

    public String[] readFile() {
        String[] content = new String[0];

        try {
            content = readContent();
        } catch (FileNotFoundException e) {
            fileNotFoundException();
        }

        return content;
    }

    private String[] readContent() throws FileNotFoundException {
        Scanner scanner = new Scanner(new File(filepath));
        String[] content = new String[fileLength()];

        int line = 0;

        while (scanner.hasNextLine()) {
            content[line] = scanner.nextLine().strip();
            line++;
        }

        return content;
    }

    private int fileLength() {
        int lines = 0;

        try {
            Scanner scanner = new Scanner(new File(filepath));

            while (scanner.hasNextLine()) {
                scanner.nextLine();
                lines++;
            }

        } catch (FileNotFoundException e) {
            fileNotFoundException();
        }

        return lines;
    }

    private void fileNotFoundException() {
        System.out.println("file '" + filepath + "' not found.");
        System.exit(1);
    }
}
