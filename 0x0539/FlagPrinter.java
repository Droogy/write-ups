/*    */ public class FlagPrinter {
/* 14 */   public static String flag = "FLAG{d0nt_y0u_just_l0v3_byt3_c0d3}";
/*    */   
/*    */   public static void main(String[] paramArrayOfString) {
/* 19 */     if (paramArrayOfString.length < 1) {
/* 21 */       System.out.print("You must provide the magic number as the first argument.");
/*    */       return;
/*    */     } 
/* 25 */     if (!paramArrayOfString[0].equals("42")) {
/* 27 */       System.out.println("The magic number you provided is wrong. We don't give the key to non-wizards, sorry.");
/*    */       return;
/*    */     } 
/* 31 */     System.out.print(flag);
/*    */   }
/*    */ }


/* Location:              /home/alex/write-ups/0x0539/!/FlagPrinter.class
 * Java compiler version: 8 (52.0)
 * JD-Core Version:       1.1.3
 */