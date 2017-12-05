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
m4 = 'Mon.4'
m5 = 'Mon.5'
m6 = 'Mon.6'
m7 = 'Mon.7'
m8 = 'Mon.8'
m9 = 'Mon.9'
m10 = 'Mon.10'
m11 = 'Mon.11'
t6 = 'Tues.6'
t7 = 'Tues.7'
t8 = 'Tues.8'
t9 = 'Tues.9'
t10 = 'Tues.10'
t11 = 'Tues.11'
w5 = 'Wed.5'
w6 = 'Wed.6'
w7 = 'Wed.7'
w8 = 'Wed.8'
w9 = 'Wed.9'
w10 = 'Wed.10'
w11 = 'Wed.11'

domain = [m4, m5, m8, m9, m10, m11, t6, t7, t8, t9, t10, t11]

monica = Dancer('Monica', [m4, m5, m6, m7, m8, m9, m10, m11, t6, t7, t8, t9, t10, t11, w5, w6, w7, w8, w9, w10],'dancer')
emma = Dancer('Emma', [s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11,m4, m5, m6, m7, m8, m9, m10, m11, t6, t7, t8, t9, 
	t10, t11, w5, w6, w7, w8, w9, w10], 'choreographer')
anna_a = Dancer('Anna A', [m4, m10, m11, t6, t7, t8, t9, t10, t11, w10], 'choreographer')
miriam = Dancer('Miriam', [m7, m8, m9, m10, m11, t6, t7, t8, t9, t10, t11, w5, w6, w7, w8, w9, w10, w11], 'choreographer')
hazel = Dancer('Hazel', [s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, m5, m6, m7, m8, m9, m10, m11, t6, t7, t8, t9, 
	t10, t11, w5, w6, w7, w8, w9, w10, w11], 'choreographer')
phoebe = Dancer('Phoebe', [s4, s5, s6, s7, s8, s9, s10, s11,m4, m5, m6, m7, m8, m9, m10, t6, t7, t8, t9, t10, w9, w10, w11], 'choreographer')
arlesia = Dancer('Arlesia', [s5, s6, s7, s8, s9, s10, s11,m4, m5, m11, t8, t9, t10, t11,  w8, w9, w11], 'choreographer')
laura = Dancer('Laura', [m6, m7, m8, m9, m10, m11, t6, t7, t8, t9, 
	t10, t11, w5, w6, w7, w8, w9, w10, w11], 'choreographer')
sarah = Dancer('Sarah', [m5, m6, m7, m8, m9, m10,t6, t7, t8, t9, t10, w5, w6, w7, w8, w9, w10], 'choreographer')
neta = Dancer('Neta', [s1, s2, s3, s4, s5, s6, s7, m5, m6, m7, m8, m9, t6, t7, t8, t9, 
	t10, w5, w6, w7, w8, w9, w10],'choreographer')
michelle = Dancer('Michelle', domain, 'choreographer')
maryelizabeth = Dancer('MaryElizabeth', [s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11,t6, t7, t8, t9, 
	t10, t11,w9, w10, w11], 'nonharvard')
talia = Dancer('Talia', [s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11,m8, m9, m10, m11, t6, t7, t8, t9, 
	t10, t11, w6, w7, w8, w9, w10, w11],'nonharvard')
florence = Dancer('Florence', [m4, m5, m6, m7, m8, m9, m10, m11, t8, t9, t10, t11, w5, w6, w7, w8, w9, w10, w11],'nonharvard')
violet = Dancer('Violet', [s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11,m4, m5, m6, m7, m8, m9, m10, m11, t9, 
	t10, t11, w5, w6, w7, w8, w9, w10, w11], 'nonharvard')
lilly = Dancer('Lilly', [s3, s4, s5, s6, s7, s8, s9, s10, s11, m5, m6, m7, m8, m9, m10, t6, t7, t8, t9, 
	t10, t11, w5, w6, w7], 'nonharvard')
nicole = Dancer('Nicole', [s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, m5, m6, m8, m9, m10, m11, t6, t7, t8, t9, 
	t10, t11, w5, w6, w7, w8, w9, w10, w11], 'nonharvard')
emily = Dancer('Emily', [s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11,m4, m5, m8, m9, m10, m11, t6, t7, t8, t9, 
	t10, t11, w5, w8, w9, w10, w11],'nonharvard')

Emma = Rehearsal(emma, [emily], domain)
Anna_A = Rehearsal(anna_a, [laura], domain)
Miriam = Rehearsal(miriam, [neta, maryelizabeth, phoebe, talia], domain)
Hazel = Rehearsal(hazel, [florence, talia, emily], domain)
Phoebe = Rehearsal(phoebe, [maryelizabeth, emily, violet, lilly, nicole], domain)
Arlesia = Rehearsal(arlesia, [monica, lilly, nicole], domain)
Laura = Rehearsal(laura, [sarah, lilly, emma, florence], domain)
Sarah = Rehearsal(sarah, [neta, violet], domain)
Neta = Rehearsal(neta, [sarah], domain)
Michelle = Rehearsal(michelle, [neta], domain)

dancers = [monica, emma, anna_a, miriam, hazel, phoebe, arlesia, laura, sarah, neta, michelle, maryelizabeth, talia, florence, violet, lilly, nicole, emily]
pieces = [Emma, Anna_A, Miriam, Hazel, Phoebe, Arlesia, Laura, Sarah, Neta, Michelle]








