import re

threshold = 3

def ip_test(ip_dict, threshold): # a function for getting the flagged IPs (one with >= 3 failures)
        flagged = []
        for address, number in ip_dict.items():
            if number >= threshold:
                flagged.append(address)
        return flagged

try:
    file = open("auth.log" , "r") 
    print("Opening the file")
    count = 0
    failed_count = 0
    ip_dict = {}  # a dictionary to store ip addresses and their failures
    accepted_ips = set()  # set to store accepted IP addresses

    for line  in file :
        count += 1
        if "Failed" in line:
            failed_count += 1

            """
            print(line.strip())
            print (line.split())
            
            split_line = line.split() splits line into indexes  such that you print a certain index
            print(split_line[10])
            """

            ip = re.search(r"\d+\.\d+\.\d+\.\d+", line)# getting ip addresses in the line that has a failed statement
            if ip:
                failed_ips = ip.group() # putting all failed ip addresses in one variable
                print(failed_ips)# prints all failed ip addresses
                print()

                ip_dict[failed_ips] = ip_dict.get(failed_ips , 0) +1 #putting ip addresses and their repetition count in the dictionary   

           # handles lines with accepted statement
        elif "Accepted" in line:
            match =  re.search(r"\d+\.\d+\.\d+\.\d+", line)
            if match:
                accepted_ips.add(match.group()) # adds the IP to the set (accepted_ips)
            
    file.close()
    print(f"There are {count} lines in the log file")    
    print(f"There are {failed_count} failed words in the log file") 

    # gives the table for ips and their number of failures      
    print(f" {'ip_address':<17}{'failures':>10}")       
    for ip, number in ip_dict.items():  
        print(f"{ip:<17}:{number:>6}")   
        print() 

      # gives ips with >= 3 failures 
    flagged_ips = ip_test(ip_dict, threshold)    
    print(f"\nfor ip addresses with {threshold} or more failures are to be flagged")
    if flagged_ips:
        for addresses in flagged_ips:
            print(addresses)
    else:
        print("No address was flagged")

# to get if a flagged ip later logged in succesfully
    breached = []   #list of breached ips
    for addresses in flagged_ips:
        if addresses in accepted_ips:
            breached.append(addresses)

    if breached:
        print("\nPresence of a breach: A flagged IP later loged in succesfully")        
        for addresses in breached:
            print(addresses)
    else:
        print("There are no signes of a presence of a breach")        


except FileNotFoundError:
    print("The file doesnt exist!! try another file")   


