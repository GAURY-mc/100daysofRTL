module compare(A)1,A0,B1,B0,it,gt,eq);
 input A1,A0,B1,B0;
 output reg lt,gt,eq;
 always @ (A1,A0,B1,B0)
   begin
     lt=({A1,A0}<{B1,B0});
     gt=({A1,A0}>{B1,B0});
     eq=({A1,A0}=={B1,B0});
     end
endmodule