import psycopg2

def create_connection():
    try:
        conn=psycopg2.connect(host="localhost",database="postgres",user="postgres",password="220507",port="5432")
        return conn
    except psycopg2.Error as e:
        print("Error connecting to the database:", e)
        return None
        

def create_pattern():
    query="""SELECT * FROM PhoneBook WHERE"""
    print("Do you want to search by surname(0)/name(1)/number(2)/enter the number:")
    mode=int(input())
    if mode == 0:
        query+=" surname"
        print("Enter string")
        substr=input()
        print("""Select option:
              1-surname equal to string
              2-surname starts with string 
              3-surname ends with string
              4-surname contains the string""")
        
        mode1=int(input())
        if mode1==1:
            query+="='{}'".format(substr)
        elif mode1==2:
            query+=" iLIKE '{}%'".format(substr)
        elif mode1==3:
            query+=" iLIKE '%{}'".format(substr)
        else:
            query+=" iLIKE '%{}%'".format(substr)
    elif mode==1:
        query+="name"
        print("Enter string")
        substr=input()
        print("""Select option:
              1-name equal to string 
              2-name starts with string
              3-name ends with string 
              4-name contains the string""")
        mode1=int(input())
        if mode1==1:
            query+="='{}'".format(substr)
        elif mode1==2:
            query+="iLIKE '{}%'".format(substr)
        elif mode1==3:
            query+="iLIKE '%{}'".format(substr)
        else:
            query+="iLIKE '%{}%'".format(substr)
    elif mode==2:
        query+=" CAST(number AS TEXT)"
        print("Enter string")
        substr=input()
        print("""Select option:
              1-number equal to string 
              2-number starts with string
              3-number ends with string 
              4-number contains the string""")
        mode1=int(input())
        if mode1==1:
            query+="='{}'".format(substr)
        elif mode1==2:
            query+="iLIKE '{}%'".format(substr)
        elif mode1==3:
            query+="iLIKE '%{}'".format(substr)
        else:
            query+="iLIKE '%{}%'".format(substr)
            
    else:
        return "error"
    return query

def insert(surname,name,phone):
    conn=create_connection()
    if conn:
        try:
            cursor=conn.cursor()
            cursor.execute("SELECT count(*) FROM PhoneBook WHERE surname=%s AND name=%s", (surname,name))
            if cursor.fetchone()[0]==0:
                cursor.execute("INSERT INTO PhoneBook (surname,name,number) VALUES (%s,%s,%s)",(surname,name,phone))
            else:
                cursor.execute("UPDATE PhoneBook SET number=%s WHERE surname=%s AND name=%s",(phone, surname, name))
            conn.commit()
        except psycopg2.Error as e:
            print("Error executing insert/update query:", e)
        finally:
            if cursor:
                cursor.close()
            conn.close()
def loop_insert():
    banned=[]
    while True:
        print("Want to enter a person's data? yes/no")
        mode = input()
        if mode.lower()== "no":
            break 
        person=input().strip().split()
        if len(person)!=3:
            banned.append(person)
            continue
        if not (person[2].isdigit() and 11 <= len(person[2]) <= 12):
            banned.append(person)
            continue
        insert(*person)
    if banned:
        print("This data were not added due to incorrect format:")
        for i in banned:
             print(i)
def pagination():
    query = create_pattern()
    if query == "error":
        return "error"
    print("Need offset? yes/no:")
    mode = input()
    if mode.lower() == "yes":
         print("Enter offset:")
         offset = int(input())
         query += " OFFSET {}".format(offset)
    print("Need limit? yes/no:")
    mode = input()
    if mode.lower() == "yes":
         print("Enter limit:")
         limit = int(input())
         query += " LIMIT {}".format(limit)
    query += ";"
    return query

def delete():
    conn = create_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * from PhoneBook")
            print("=== Full phonebook before delete ===")
            print(cursor.fetchall())
            print("Do you wanna delete by surname(0)/name(1)/number(2), enter the number:")
            mode = int(input())
            if mode == 0:
                print("Enter surname to delete:")
                value = input()
                query = "DELETE FROM PhoneBook WHERE surname = %s"
            elif mode == 1:
                print("Enter name to delete:")
                value = input()
                query = "DELETE FROM PhoneBook WHERE name = %s"
            else:
                print("Enter number to delete:")
                value = input()
                query = "DELETE FROM PhoneBook WHERE number = %s"
            cursor.execute(query, (value,))
            conn.commit()
            cursor.execute("SELECT * from PhoneBook")
            print(cursor.fetchall())
            
        except psycopg2.Error as e:
            print("Error executing delete query:", e)
        finally:
            if cursor:
                cursor.close()
            conn.close()

            
if __name__ == "__main__":
    loop_insert()
    a=pagination()
    if a !="error":
        conn=create_connection()
    if conn:
        try:
            cursor=conn.cursor()
            cursor.execute(a)
            print(cursor.fetchall())
        except psycopg2.Error as e:
                 print("Error executing pagination query:", e)
        finally:
                 if cursor:
                     cursor.close()
                 conn.close()
    delete()
        
            
                
            
            
        
          
    
          
