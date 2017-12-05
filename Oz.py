from classes import Dancer, Rehearsal

s1 = 'Sun.1'
s2 = 'Sun.2'
s3 = 'Sun.3' 
s4 = 'Sun.4' 
s5 = 'Sun.5' 
s6 = 'Sun.6' 
s7 = 'Sun.7' 
s8 = 'Sun.8' 
s9 = 'Sun.9' 
s10 = 'Sun.10' 
s11 = 'Sun.11' 
m3 = 'Mon.3'
m4 = 'Mon.4'
m5 = 'Mon.5'
m6 = 'Mon.6'
m7 = 'Mon.7'
m8 = 'Mon.8'
m9 = 'Mon.9'
m10 = 'Mon.10'
m11 = 'Mon.11'
t3 = 'Tues.3'
t4 = 'Tues.4'
t5 = 'Tues.5'
t6 = 'Tues.6'
t7 = 'Tues.7'
t8 = 'Tues.8'
t9 = 'Tues.9'
t10 = 'Tues.10'
t11 = 'Tues.11'
w3 = 'Wed.3'
w4 = 'Wed.4'
w5 = 'Wed.5'
w6 = 'Wed.6'
w7 = 'Wed.7'
w8 = 'Wed.8'
w9 = 'Wed.9'
w10 = 'Wed.10'
w11 = 'Wed.11'

domain1 = [s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, m3, m4, m5]
domain2 = [m6, m7, m8, m9, m10, m11, t4, t5, t6, t7, t8, t9, t10, t11, w5]

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

Alex = Rehearsal(alex, [sarah], domain2)
Margot = Rehearsal(margot, [monica, julia, lilly, anna_a], domain2)
Ali = Rehearsal(ali, [anna_a], domain2)
Anna_A = Rehearsal(anna_a, [sarah, alex, jonah], domain2)
Nina = Rehearsal(nina, [phoebe, anna_a], domain2)
Anna_RS = Rehearsal(anna_rs, [neta, alex], domain2)
Margaret = Rehearsal(margaret, [ali, neta], domain2)

dancers = [monica, alex, margot, ali, anna_a, nina, anna_rs, margaret, jonah, lilly, julia, phoebe, sarah, neta]
pieces = [Alex, Margot, Ali,Anna_A,  Nina,  Anna_RS, Margaret]

