import math;

def convert_base_letter(ch: chr):
    result  = None;
    if(ch =='A' or ch =='a'):
        result = chr(ord('0') + 10);
    elif(ch =='B' or ch =='b'):
        result = chr(ord('0') + 11);
    elif(ch =='c' or ch =='C'):
        result = chr(ord('0') + 12);
    elif(ch =='D' or ch =='c'):
        result = chr(ord('0') + 13);
    elif(ch =='E' or ch =='e'):
        result = chr(ord('0') + 14);
    elif(ch =='F' or ch =='f'):
        result = chr(ord('0') + 15);
    else:
        result  =  ch;
    return   result;

def convert_number_base_letter(value:int):
    result  =  None; 
    if(value ==10):
        result  ='A';
    elif(value == 11):
        result  = 'B'
    elif(value == 12):
        result  ='C';
    elif(value ==13):
        result  = 'D'
    elif(value ==14):
        result  =  'E'
    elif(value == 15):
        result  = 'F'
    else:
        result  =  chr(ord('0') + value);
    return result;
    
def validatorbase(value , base):
    highest_base  =  base - 1;
    status  =  True;
    for ch in value:
        if(base >= 10):
            ch  =  convert_base_letter(ch);
        n  =  ord(ch);
        base_ch  =  chr(ord('0') + highest_base);
        if(n < ord('0')) or (n  > ord(base_ch)):
            status  = False;
            break;
    return status;

"""
 convert any base to base 10 is a very important thing for
 example programmer
 
"""
def tobase(value:str, **kwargs):
    value  =  str(value);
    validator    =  kwargs['validator'] if('validator' in kwargs) else validatorbase;
    input_base   =  kwargs['input_base'] if('input_base' in kwargs)   else 10;
    isvalid  =  True;
    error    = "";
    if(validator != None) and (callable(validator)):
        isvalid =  validator(value, input_base);
        
    if(isvalid is not True):
        raise ValueError("invalid input = {0} for base {1}".format(value, input_base));
    
    length  =  len(value);
    result = 0;
    power = 0;
    
    for i in range(1, length + 1):
        index  =  i * -1;
        ch  = convert_base_letter(value[index]);
        num  =  ord(ch) - ord('0');
        result = result + (num * (input_base **power))
        power += 1;

    return result;


def tobase_any(value: str, **kwargs):
    """
    @param input
    """
    input_base   =  kwargs['input_base'] if('input_base' in kwargs)   else 10;
    output_base   =  kwargs['output_base'] if('output_base' in kwargs) else 10;
   
    decimal  =  tobase(value, **kwargs);
    
    if (output_base != 10):       
        result  =  "";
        remainder  =  decimal  % output_base;
        dividend   =  decimal // output_base;
        ch     = convert_number_base_letter(remainder);
        result += ch;
        
        while(dividend != 0):
            remainder  =  dividend  % output_base;
            dividend   =  dividend // output_base;
            result += convert_number_base_letter(remainder);
        decimal = result[len(result)::-1]; #reverse the string
    return decimal;
   

        

if(__name__ == "__main__"):
    numbers  =  [61,62,52,45,66,32,56,21,56,24,67,21,67,21,56,21, 26, 91, 82, 15*15];
    counter  =  0;
    with open('text.bin', mode='w+') as file:
        for num in numbers:
            if((counter % 4) == 0):
               file.write('\n');
            file.write(tobase_any(num, input_base = 10, output_base = 16));
            file.write(' ');
            counter = counter + 1;

        
        
    
        
