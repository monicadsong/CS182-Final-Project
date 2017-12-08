from classes import Dancer, Rehearsal
from timeslot_vars import *

domain1 = [s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, m3, m4, m5]
domain2 = [m6, m7, m8, m9, m10, m11, t4, t5, t6, t7, t8, t9, t10, t11, w5]
domain3 = [s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, m3, m4, m5,m6, m7, m8, m9, m10, m11, t4, t5, t6, t7, t8, t9, t10, t11, w5]

monica = Dancer('Monica', [s1, s5, s6, s7, s8, s9, s10, s11, m3, m4, m5, m6, m7, m8, m9, m10, m11, t4, t5, t6, t7, t8, t9, t10, t11, w4, w5, w6, w11], 'Dancer')
alex = Dancer('Alex', [s1, s2, s3, s4, m6, m7, m8, m9, t6, t7, t8, t9, t10, t11, w3, w4, w5, w6, w7], 'choreographer')
margot = Dancer('Margot', [s1, s5, m5, m6, m7, t6, t7, w4, w5, w6, w7],'choreographer')
ali = Dancer('Ali', [s1, s2, s3, s4, m3, m6, m7, t5, t6, t7, t8, t9, t10, t11, w3, w4, w5, w6, w7, w8, w9, w10, w11 ], 'choreographer')
anna_a = Dancer('Anna A', [s1,s6, s9, s10, s11, m4, m5, m6,  m9, m10, m11, t3, t4, t5, t6, t7, t8, t9, t10, t11, w5, w6, w7, w8, w9, w10, w11 ], 'choreographer')
nina = Dancer('Nina', [s1, s2, s3, s4, m9, m10, t9, t10, t11, w8, w9, w10],'choreographer')
anna_rs = Dancer('Anna RS', [s1, s2, s3, s4, s5,s6, s7, s8, s9, s10, s11, m5, m6, m7, m8, m9, m10, m11, t5, t6, t7, t8, t9, t10, t11, w5, w6, w7, w8, w9, w10, w11], 'choreographer')
margaret = Dancer('Margaret', [ m3, m4, m5, m6, m7, m8, m9, m10, m11, t3, t4, t5, t6, t7, t8, t9, t10, t11, w7, w8, w9, w10, w11], 'choreographer')

jonah = Dancer('Jonah', [s10, s11,m9, m10, m11, w8, w9, w10, w11], 'nonharvard')
lilly = Dancer('Lilly', [s1, s5,s6, s7, m6, m7, m8, m9, m10, m11, t5, t6, t7, t8, t9, t10, t11],'nonharvard')
julia = Dancer('Julia', [s1, s2, s3, s4, s5,s6, s7, s8, s9, m6, m7, m8, m9, m10, m11, t5, t6, t7, t8, t9, t10, t11, w4, w5, w6, w7, w8, w9, w10, w11], 'nonharvard')
phoebe = Dancer('Phoebe', [m6, m7, m8, m9, m10, t5, t6, t7, t8, t9, t10, w3, w4,  w8, w9, w10, w11],'nonharvard')
sarah = Dancer('Sarah', [s1, s2, s3, s4, s5,s6, m5, m6, m7, m8, m9, m10,t3, t4, t5, t6, t7, t8, t9, w5, w6, w7, w8, w9, w10, w11], 'nonharvard')
neta = Dancer('Neta', [s1, s2, s3, s4, m3, m4, m10, m11, t6, t7, t8, t9, t10, t11, w4, w5, w6, w7, w8, w9], 'nonharvard')

Alex = Rehearsal(alex, [sarah], domain3)
Margot = Rehearsal(margot, [monica, julia, lilly, anna_a], domain3)
Ali = Rehearsal(ali, [anna_a], domain3)
Anna_A = Rehearsal(anna_a, [sarah, alex, jonah], domain3)
Nina = Rehearsal(nina, [phoebe, anna_a], domain3)
Anna_RS = Rehearsal(anna_rs, [neta, alex], domain3)
Margaret = Rehearsal(margaret, [ali, neta], domain3)
Alex2 = Rehearsal(alex, [sarah], domain3)
Margot2 = Rehearsal(margot, [monica, julia, lilly, anna_a], domain3)
Ali2 = Rehearsal(ali, [anna_a], domain3)
Anna_A2 = Rehearsal(anna_a, [sarah, alex, jonah], domain3)
Nina2 = Rehearsal(nina, [phoebe, anna_a], domain3)
Anna_RS2 = Rehearsal(anna_rs, [neta, alex], domain3)
Margaret2 = Rehearsal(margaret, [ali, neta], domain3)


pieces = [Alex, Margot, Ali,Anna_A,  Nina,  Anna_RS, Margaret, Alex2, Margot2, Ali2,Anna_A2,  Nina2,  Anna_RS2, Margaret2]
dancers = [monica, alex, margot, ali, anna_a, nina, anna_rs, margaret, jonah, lilly, julia, phoebe, sarah, neta]
actual = {Alex: t7,
Margot: s2, 
Ali: m7,
Anna_A: m9,
Nina: s9,  
Anna_RS: s8, 
Margaret: t9, 
Alex2: t6, 
Margot2: m6, 
Ali2: m8,
Anna_A2: m10, 
Nina2: s10,  
Anna_RS2: s8, 
Margaret2: t10}


