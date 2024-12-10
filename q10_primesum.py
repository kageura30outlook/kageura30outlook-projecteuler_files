using System; 
public class Hello{
    public static bool　buri(int i){
        int warizan = 2;
        bool hanntei = true;
        if(i == 1)
        {
            hanntei = false;
            return hanntei;
        }
        else if(i == 2)
        {
            hanntei = true;
            return hanntei;
        }
        else;
        {
            for(int r = 1; r <= Math.Sqrt(i); r++){
                if (i % warizan == 0){
                    hanntei = false;
                    break;
                }
                else;
                {
                    warizan = warizan + 1;
                }
            
            
            }
        }

        return hanntei;
    }
    public static void Main(){
    int listener = 0;

        for(int i = 1; i <= 10000; i++)
        {
            if(buri(i) == true)
            {
                listener = listener + i;

            }
            
        }
        
        Console.WriteLine(listener); 
    }
}
