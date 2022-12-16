names_file = open("project\\names.txt","r") 
values_file = open('project\\values.txt')
#symbols that needs to be removed
symbol_list = ['-' , "'" ] 
#making dictionary
abv_dict = score_dict = temp_dict =abr_dict_score= dict()
#making list
file_list = abv_list = temp_list=final_list=templist= list()

#to calculate abrevation score
def abv_score(txt , name_list):
    dns = 0
    txt_list = list(txt)  #['A' , 'L' , 'D']
   
    for i in range(0 , len(txt_list)):
        if name_list.index(txt_list[i]) < 3:
            dns += name_list.index(txt_list[i]) + int(score_dict[txt_list[i]] )
        else:
            dns += 3 + int( score_dict[txt_list[i]] )
    temp_list = dns

    return txt,temp_list
  
#making abrevation for single word
def sgl_abv(name_list , file_data):  
    
    abv_temp=list()
    abv = name_list[0]  #abv = A 
    for i in range(1 , len(name_list)):      #['A' , 'L' , 'D' , 'E' ,'R']
        for j in range(i+1 , len(name_list)):    #['A' , 'L' , 'D' , 'E' ,'R']
            abv += name_list[i] + name_list[j]   #abv = ALD
            abv_temp.append(abv_score(abv,name_list))
            abv = name_list[0] 

    return abv_temp

#making abrevation for two words
def dbl_abv(name_list , file_data):
    dbl_name = file_data.split()
    abv = name_list[0]  #abv = A 
    for i in range(1 , len(name_list)):      #['A' , 'L' , 'D' , 'E' ,'R']
        for j in range(i+1 , len(name_list)):    #['A' , 'L' , 'D' , 'E' ,'R']
            if name_list[i] != ' ' and name_list[j] !=  ' ':
                abv += name_list[i] + name_list[j]   #abv = ALD
                # abv_score(abv , name_list) 
                abv_list.append(abv)
                abv = name_list[0] 
    return abv_list


#making abrevation for three words
def tpl_abv(name_list , file_data):
    # print( name_list , file_data )
    dbl_name = file_data.split()
    abv = name_list[0]  #abv = A 
    for i in range(1 , len(name_list)):      #['A' , 'L' , 'D' , 'E' ,'R']
        for j in range(i+1 , len(name_list)):    #['A' , 'L' , 'D' , 'E' ,'R']
            if name_list[i] != ' ' and name_list[j] !=  ' ':
                abv += name_list[i] + name_list[j]   #abv = ALD
                abv_list.append(abv)
                abv = name_list[0] 
    return abv_list

#defining main function
def main():
# stripping the main file   
    for item in names_file:
        file_list.append(item.strip())

#splitting the values
    for item in values_file:
        k , v = item.split()
        score_dict[k] = v



    for data in file_list:      
        file_data = data.upper() #ALDER
        name_list = list(file_data)  #['A' , 'L' , 'D' , 'E' , 'R'] 

#removing symbols
        for smbl in symbol_list:
            try:
                check1 = name_list.index(smbl)
            except:
                continue
            for name in name_list:
                if name == name_list[check1]:
                    if name == '-' :
                        name_list[check1] = ' '
                    elif name == "'":
                        name_list.remove(name_list[check1])

# counting number of words in the name                       
        scount = name_list.count(' ')
        if scount == 0:    # Single Word

            templist=sgl_abv(name_list , file_data)
           
            def arrtostr(item):
                strr=''
                for b in item:
                    strr+=str(b)+'   '
                return strr

# write to your file
            with open('surana_trees_abbrevs.txt','w+') as doc:
                for item in templist:
                    doc.write(arrtostr(item)+'\n')
                doc.close()
            
        #two words
        elif scount == 1:
            dbltemplist=sgl_abv(name_list , file_data)
            print(dbltemplist)
                
        #three words
        else:
            if scount == 2:
                tpltemplist=sgl_abv(name_list , file_data)
                print(tpltemplist)


if __name__=="__main__":main()