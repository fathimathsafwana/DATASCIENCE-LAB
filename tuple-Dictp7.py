pairs_list=[]
print("Enter key-value pairs(Type 'done' when you are finished):\n")
while True:
    user_input=input("enter pair(Format:key:value):")
    if user_input.lower()=='done':
        break
    if ":" in user_input:
        key,value=user_input.split(":",1)
        pairs_list.append((key.strip(),value.strip()))
    else:
        print("invalid format.please use 'key:value'(eg:age:21)")
nested_tuple=tuple(pairs_list)
print(f"\nGenerated Tuple:{nested_tuple}")
result_dict=dict(nested_tuple)
print(f"Resulting Dictionary:{result_dict}")
