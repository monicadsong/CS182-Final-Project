from classes import Dancer, Rehearsal
from timeslot_vars import *

domain = [Sun1, Sun2, Sun3, Sun4, Sun5, Sun6, Sun7, Sun8, Sun9, Sun10, Mon4, Mon5, Mon6, Mon7, Mon8, Mon9, Mon10, Tues4, Tues5, Tues6, 
Tues7, Tues8, Tues9, Tues10]


phoebe = Dancer('Phoebe', [Sat3, Sat4, Sat5, Sat6, Sat7, Sat8, Sat9, Sat10, Sun6, Sun7, Sun8, Mon4, Mon5, 
	Tues4, Tues5, Tues6, Tues7, Tues8],'choreographer')

lia = Dancer('Lia',[Sat9, Sun6, Sun7, Sun8, Sun9, Mon6, Mon7, Tues6, Tues7, Tues8, Tues9, Wed6],'choreographer')

sarah = Dancer('Sarah', [Sat3, Sat4, Sat5, Sat6, Sat7, Sat8, Tues4, Tues5, Tues6, Tues7, Tues8, Wed6], 'choreographer')

arlesia = Dancer('Arlesia',[Sat7, Sat8, Sat9, Sat10, Sun1, Sun2, Sun3, Sun4, Mon9, Mon10],'choreographer')

anna_a = Dancer('Anna A', [Sun1, Sun2, Sun3,Sun9, Sun10, Mon8, Mon9, Mon10, Tues5, Tues6, Tues7, Tues10],'choreographer')

anna_rs = Dancer('Anna RS', [Sat1, Sat2, Sat3, Sat4, Sat5, Sat6, Sat7, Sat8, Sat9, Sat10], 'choreographer')

julia_s = Dancer('Julia S', [Sat1, Sat2, Sat3, Sat4, Sat5, Sat6, Sat7, Sat8, Sat9, Sat10, Sun3, Sun4, Sun5, Sun6, Sun7, Sun8, Sun9, Sun10, Mon6, Mon7, Mon8, Tues4, Tues5, Tues6, Tues7, Tues8, Tues9, Wed5, Wed6], 'nonharvard')
lilly_s = Dancer('Lilly S',[Mon6, Mon7, Mon8, Mon9, Mon10, Tues4, Tues5, Tues6, Tues7, Tues8, Tues9, Wed4, Wed5, Wed6], 'nonharvard')

emily = Dancer('Emily', [Sat4, Sat5, Sat6, Sat7, Sat8, Sat9, Sat10, Sun9, Sun10, Tues4, Tues5, Tues6, Tues7,Tues8, Tues9, Tues10], 'nonharvard')

violet = Dancer('Violet', [Mon4, Mon5, Mon6, Tues4, Tues5, Tues6, Tues7, Tues8, Tues9, Tues10, Wed4, Wed5, Wed6],'nonharvard')
maryelizabeth = Dancer('MaryElizabeth',[Sat1, Sat2, Sat3, Sat4, Sat5, Sun1, Sun2, Sun3, Sun4, Sun5, Sun6, Sun7, Sun10, Mon9, Mon10, Tues7, Tues8, Tues9, Tues10, Wed4, Wed6, Wed6],'nonharvard')
nicole = Dancer('Nicole',[Sat1, Sat2, Sat3, Sat4, Sun1, Sun2, Sun3, Sun4, Sun5, Sun8, Sun9, Sun10, Mon4, Mon5, Mon6, Mon7, Mon8, Mon9, Mon10, Tues4, Tues5, Tues6, Tues7, Tues8, Tues9, Tues10, Wed4, Wed5, Wed6],'nonharvard')

melanie = Dancer('Melanie',[Sun6, Sun7, Sun8, Sun9, Sun10, Mon8, Mon9, Mon10, Tues7, Tues8, Tues9],'nonharvard')

maya = Dancer('Maya', [Mon4, Mon5, Mon6, Tues6, Tues7, Tues8, Tues9, Tues10, Wed4, Wed5, Wed6],'nonharvard')

theresa = Dancer('Theresa',[Sat1, Sat2, Sat3, Sat4, Sat5, Sat6, Sat7, Sat8, Sat9, Sat10, Sun1, Sun2, Sun3, Sun4, 
	Sun5, Sun6, Sun7, Sun8, Sun9, Mon4, Mon5, Mon6, Mon7, Mon8, Mon9, Mon10, Tues5, Tues6, Tues7, Tues8, Tues9, Tues10],'nonharvard')

allenda = Dancer('Allenda',[Sat9, Sat10, Sun6, Sun7, Sun8, Sun9, Sun10, Mon10, Tues7, Tues8, Tues9, Tues10, Wed6],'nonharvard')


jesse = Dancer('Jesse',domain, 'choreographer')

#Pieces
Jesse = Rehearsal(jesse, [julia_s, allenda, lilly_s], domain)
Phoebe = Rehearsal(phoebe, [lilly_s], domain)
Lia = Rehearsal(lia, [melanie], domain)
Sarah = Rehearsal(sarah, [anna_a, emily, maryelizabeth, nicole], domain)
Arlesia = Rehearsal(arlesia, [theresa, melanie, maya], domain)
Anna_A = Rehearsal(anna_a, [phoebe, allenda, violet], domain)
Anna_RS = Rehearsal(anna_rs, [], domain)

dancers2 = [phoebe, lia, sarah, arlesia, anna_a, anna_rs, julia_s, lilly_s, emily, violet, maryelizabeth, nicole,  melanie, maya, theresa, allenda, jesse]
pieces2 = [Jesse, Phoebe, Lia, Sarah, Arlesia, Anna_A, Anna_RS]



