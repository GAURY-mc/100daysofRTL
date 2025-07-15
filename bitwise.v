module xyz (input a,b,c,output reg flag);
   always @ (*)
     if (a==1) f=b&c;
endmodule