from classes import Dancer, Rehearsal
domain = ['a.4', 'a.5', 'a.6', 'a.7', 'a.8', 'a.9', 'a.10', 'a.11']

anna = Dancer('Anna', ['a.6','a.7','a.8','a.9'],'choreographer')
mara = Dancer('Mara', ['a.5', 'a.6', 'a.7', 'a.8', 'a.9', 'a.10', 'a.11'],'choreographer')
ali = Dancer('Ali', ['a.5', 'a.6', 'a.7', 'a.8', 'a.9', 'a.10'],'choreographer')
deedee = Dancer('Deedee', ['a.4', 'a.5', 'a.6', 'a.7', 'a.8', 'a.9', 'a.10', 'a.11'],'dancer')
jen = Dancer('Jen',['a.4', 'a.5', 'a.6', 'a.7', 'a.8', 'a.9'],'dancer')
isabel = Dancer('Isabel', ['a.6', 'a.7', 'a.8', 'a.9', 'a.10', 'a.11'],'dancer')
sarah = Dancer('Sarah', ['a.4', 'a.5', 'a.6', 'a.7', 'a.8', 'a.9'], 'nonharvard')
arlesia = Dancer('Arlesia', ['a.4', 'a.5', 'a.6', 'a.7', 'a.8'], 'dancer')
emily = Dancer('Emily', ['a.4', 'a.5', 'a.6', 'a.7', 'a.8', 'a.9'], 'nonharvard')
annabel = Dancer('Annabel',['a.5', 'a.6', 'a.7', 'a.8', 'a.9', 'a.10', 'a.11'], 'dancer')
angela = Dancer('Angela',['a.5', 'a.6', 'a.7', 'a.8'], 'dancer')


Anna = Rehearsal(anna, [deedee, isabel, jen, sarah, mara, angela], domain)
Mara = Rehearsal(mara, [jen, arlesia, emily], domain)
Ali = Rehearsal(ali, [sarah, emily, anna, annabel], domain)

dancers = [anna, mara, ali, deedee, jen, isabel, sarah, arlesia, emily, annabel, angela]
pieces = [Anna, Mara, Ali]

