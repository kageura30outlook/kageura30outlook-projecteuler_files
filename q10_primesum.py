using System; 
public class Hello{
    public static bool　core(int i){
        int divider = 2;
        bool checker = true;
        if(i == 1)
        {
            checker = false;
            return checker;
        }
        else if(i == 2)
        {
            checker = true;
            return checker;
        }
        else;
        {
            for(int r = 1; r <= Math.Sqrt(i); r++){
                if (i % divider == 0){
                    checker = false;
                    break;
                }
                else;
                {
                    divider = divider + 1;
                }
            
            
            }
        }

        return checker;
    }
    public static void Main(){
    int num = 0;

        for(int i = 1; i <= 10000; i++)
        {
            if(core(i) == true)
            {
                num = num + i;

            }
            
        }
        
        Console.WriteLine(num); 
    }
}