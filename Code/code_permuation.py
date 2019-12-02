#conditional jumps 
import random
def metamorphic_gen(seq_list,blocks):
    modules=[[] for k in range(blocks)]
    block_length=int(len(seq_list)/blocks)
    
    first_itr=0
    module_indices=[i for i in range(blocks)]
    morphed_seq=[]
    prev=-1
    
    #frames built
    for i in range(blocks):
        modules[i]=seq_list[first_itr:first_itr+block_length]
        first_itr+=block_length
     
    #randomly permutating frames with jmp instruction
    for i in range(blocks):
        index=random.choice(module_indices)
        #print(index)
        module_indices.remove(index)
        morphed_seq+=modules[index]
        if index==blocks-1:#no jump after last block 
            print('test')
            prev=index
            pass
        else:
            morphed_seq.append('JMP')
            prev=index
        
    return morphed_seq
        
        


import pandas as pd
opcode1=pd.read_csv('opcode-1.csv')
opcode1['Opcode']=opcode1['Opcode'].str.strip()
series1 = pd.Series(opcode1['Opcode'], index=opcode1.index)
data_final1=series1.tolist()
morphed_seq=metamorphic_gen(data_final1,20)    
morphed_seq_DF=pd.DataFrame(morphed_seq)
#morphed_seq_DF.to_csv(r'/Users/shreya90/Desktop/Morphed/Morphed_20.csv', sep=',', encoding='utf-8')
