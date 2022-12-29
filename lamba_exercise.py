import re

prog_lang=[('Python',3.8),('Java',13),('JavaScript',2019),('Scala', 2.13)]

###Sort the list by each language's version in ascending order###
prog_lang.sort(key=lambda x:x[1] )
print(prog_lang)

###Sort the list by the length of the name of each language in descending order###
len_name =prog_lang
new_lst=sorted(len_name,key=lambda x:x[1],reverse =True)
print (new_lst)

###Filter the list so that it only contains languages with 'a' in it.###
#
fil=list(filter(lambda x:re.findall(r'[a]+',x[0]),prog_lang))
print(f"The languages with letter a are : {fil}")

###Filter the list so that it only contains languages whose version is in integer form.###

int_form=list(filter(lambda x: x if(type(x[1])==int) else 0 , prog_lang))
print(f" The languages with int values: {int_form}")

###Transform the list so that it contains the tuples in the form,
# ("language in all lower case", length of the language string)###
 
print(list(map(lambda x:(x[0].lower(),len(x[0])),prog_lang)))

###test regular functions###
# def check(lst):
#     example=[]
#     for i in (prog_lang): 
#         a,b= (str(i[0].lower()),len(i[0]))
#         example.append(((a,b)))
      #print (example)
    
 
###Generate a tuple in the form,("All languages separated by commas","All versions separated by commas")##
# ##
#('Python,Java,JavaScript,Scala', '3.8,13,2019,2.13')
 
diff_langs= list(map(lambda x: (x[0]),prog_lang))
lang_values=list(map(lambda x: (str(x[1])),prog_lang))
concat= (','.join(diff_langs),','.join(lang_values))

print (concat)