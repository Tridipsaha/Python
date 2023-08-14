


import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.net.Socket;
import java.util.Scanner;

public class Client {

    DataInputStream disp;
    DataOutputStream out;

    File my1File = new File("C:\\Users\\tridi\\OneDrive\\Documents\\PU Documents\\2nd Semester\\LAB_EXAM(B)");
    File send1File = new File("C:\\Users\\tridi\\OneDrive\\Documents\\PU Documents\\2nd Semester\\LAB_EXAM(B)\\Unknown_file.txt");

    FileInputStream disp_f;
    FileOutputStream out_f;

    Client() {
        try {
            Socket socket = new Socket("localhost", 7777);
            disp = new DataInputStream(socket.getInputStream());
            out = new DataOutputStream(socket.getOutputStream());

            Sending();
            Receving();

        } catch (Exception e) {
            System.out.println("Error occur in Client!");
        }
    }

    public void Receving() {
        Runnable r3 = () -> {
            try {
                while (true) {

                    String msg = disp.readUTF();

                    if (msg.equals("send_file")) {

                        out_f = new FileOutputStream(send1File);

                        msg = disp.readUTF();
                        char ch[] = msg.toCharArray();

                        for (int i = 0; i < msg.length(); i++) {
                            out_f.write(ch[i]);
                        }
                        msg = "File Received check the folder......";
                    }

                    System.out.println("Client:" + msg);
                }
            } catch (Exception e) {
                System.out.println("Error occur in the receving!");
            }
        };
        new Thread(r3).start();
    }

    public void Sending() {

        Runnable r4 = () -> {
            String msg;
            Scanner sc = new Scanner(System.in);

            int i = 0;
            String text = "";

            try {
                while (true) {
                    System.out.print("You: ");
                    msg = sc.nextLine();

                    if (msg.equals("0"))
                        break;

                    if (msg.equals("send_file")) {

                        Scanner scan = new Scanner(System.in);
                        File file_list[] = my1File.listFiles();
                        System.out.print("Enter the search file: ");
                        String search = scan.nextLine();

                        for (File e : file_list) { // loop upto the "LastFile"
                            String existFile = e.getName(); // convert "File" to "String"

                            if (existFile.equals(search)) {
                                File myFile = new File(e.getPath());
                                disp_f = new FileInputStream(myFile);
                                while ((i = disp_f.read()) != -1) {
                                    text += (char) i;
                                }
                                out.writeUTF(msg);
                                out.flush();
                                System.out.println("File send successfuly please check the folder.........");
                            }else{
                                System.out.println("File not exit");
                            }
                            
                        }
                        msg = text;
                    }

                    out.writeUTF(msg);
                    out.flush();
                }
            } catch (Exception e) {
                System.out.print("Error occur in Sending.....");
            }

        };
        new Thread(r4).start();
    }

    public static void main(String[] args) {
        Client obj = new Client();
    }
}