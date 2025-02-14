import json

file_path = "C:/Users/Lenovo/Desktop/PP2_labs/sample-data.json"
with open(file_path, "r", encoding="utf-8") as file:
    data = json.load(file)


print(data)
# ================================================================================
# DN                                                 Description           Speed    MTU  
# -------------------------------------------------- --------------------  ------  ------""")


# for i in data["imdata"]:
#     dn_key=i["l1PhysIf"]["attributes"]["dn"]
#     descr_key=i["l1PhysIf"]["attributes"].get("descr", "N/A")
#     speed_key=i["l1PhysIf"]["attributes"].get("speed", "N/A")
#     mtu_key=i["l1PhysIf"]["attributes"]["mtu"].get("mtu", "N/A")
    
#     print(dn_key, descr_key, speed_key, mtu_key)
    