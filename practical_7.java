import java.math.BigInteger;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.Scanner;

class practical_7{
	public static String encryptThisString(String sample){
		try{
			MessageDigest md = MessageDigest.getInstance("SHA-1");
			byte[] messageDigest = md.digest(sample.getBytes());
	
			BigInteger no = new BigInteger(1, messageDigest);

			String hashtext = no.toString(16);

			while(hashtext.length() < 32){
				hashtext = "0" + hashtext;
			}

			return hashtext;
		}
		catch (NoSuchAlgorithmException e){
			throw new RuntimeException(e);
		}
	}
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.print("Enter message : ");
		String inp = sc.next();
		System.out.println("SHA-1 encryption of " + inp + " is : " + encryptThisString(inp));
	}
}