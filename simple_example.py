from classes import Dancer, Rehearsal

anna = Dancer('Anna', [6,7,8,9],'choreographer')
mara = Dancer('Mara', [5,6,7,8,9,10,11],'choreographer')
ali = Dancer('Ali', [5,6,7,8,9,10],'choreographer')
deedee = Dancer('Deedee', [4,5,6,7,8,9,10,11],'dancer')
jen = Dancer('Jen',[4,5,6,7,8,9],'dancer')
isabel = Dancer('Isabel', [6,7,8,9,10,11],'dancer')
sarah = Dancer('Sarah', [4,5,6,7,8,9], 'nonharvard')
arlesia = Dancer('Arlesia', [4,5,6,7,8], 'dancer')
emily = Dancer('Emily', [4,5,6,7,8,9], 'nonharvard')
annabel = Dancer('Annabel',[5,6,7,8,9,10,11], 'dancer')
angela = Dancer('Angela',[5,6,7,8], 'dancer')


Anna = Rehearsal(anna, [deedee, isabel, jen, sarah, mara, angela])
Mara = Rehearsal(mara, [jen, arlesia, emily])
Ali = Rehearsal(ali, [sarah, emily, anna, annabel])

dancers = [anna, mara, ali, deedee, jen, isabel, sarah, arlesia, emily, annabel, angela]
pieces = [Anna, Mara, Ali]

domains = [4,5,6,7,8,9,10,11]