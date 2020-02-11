   a=i
      my_cursor.execute(sql_genesequence,(a,))
      mydb.commit()
      p=parser(a)
      
      
      #print(p)

    else:
      #pass

      #print(i)
      my_cursor.execute(sql_genename,(i,))
      mydb.commit()

    
'''
    if (i[0]=='>'):
      #print(i)
      my_cursor.execute(sql_genename,(i,))
      mydb.commit()
'''