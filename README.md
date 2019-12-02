# Piracy_detection
Software_piracy_detection

Extracted opcode sequence from Elmedia video player 

Considered it as  base software


Considered the top 30 most frequent opcodes to train the models

Generated multiple morphed copies of the software with varying percentage of dead-code insertion

Generated multiple copies of the base software by inserting conditional jumps in the base opcode sequence


Trained HMM model on the base sequence

Used that model to score the morphed copies and copies with conditional jumps


Created Opcode similarity graph from the base sequence


Computed the distance of OGS matrix generated from various morphed copies and OGS matrix from the base sequence


These HMM and OGS scores are used as features to a SVM model to determine if there is linear separation



