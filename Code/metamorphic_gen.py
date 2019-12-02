#Dead code generation code


import pandas as pd
import random
dead_code=pd.read_csv('/Users/shreya90/Desktop/Dead.csv')
dead_code_series = pd.Series(dead_code['Opcode'], index=dead_code.index)

dead_code_final=dead_code_series.tolist()

def dead_code_insert(seq_list,morph_percentage,dead_code):
    opcodes_required_length=morph_percentage*len(seq_list)
    print(opcodes_required_length)
    times=0
    extra=0
    if(opcodes_required_length>=len(dead_code)):
        times=int(opcodes_required_length/len(dead_code))
        print(times)
        extra=int(opcodes_required_length%len(dead_code))
        #print(extra)
    elif(opcodes_required_length<len(dead_code)):
        times=0
        extra=int(opcodes_required_length%len(dead_code))
        #print(extra)
        
    return helper_dead_code_insert(seq_list,times,extra,dead_code)
    
        
def helper_dead_code_insert(seq_list,times,extra,dead_code):
    index_list=[i for i in range(len(seq_list))]
    morphed_code=[]
    while(times>=0):
        index=random.choice(index_list)
        if(times>0):
            seq_list[index:index]=dead_code
            #print(len(seq_list))
            times-=1
        else:
            seq_list[index:index]=dead_code[:extra+1]
            times-=1
            pass
    return seq_list
            
        
import pandas as pd
opcode1=pd.read_csv('opcode-1.csv')
opcode1['Opcode']=opcode1['Opcode'].str.strip()
series1 = pd.Series(opcode1['Opcode'], index=opcode1.index)
data_final1=series1.tolist()

x=dead_code_insert(data_final1,1,dead_code_final)        
    
dead_code_inserted_seq_DF=pd.DataFrame(x)
#dead_code_inserted_seq_DF.to_csv(r'/Users/shreya90/Desktop/dead_code_inserted_seq_dF_300.csv', sep=',', encoding='utf-8')   
    
    