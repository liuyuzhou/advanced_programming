def name_email_phone_split(record):
    name, email, *phone_numbers = record
    return name, email, phone_numbers


if __name__ == "__main__":
    i_record = ('xiao ming', 'abc@abc.com', '0755-23451233', '0755-20009999')
    o_name, o_email, o_phone_numbers = name_email_phone_split(i_record)
    print(f'name is:{o_name}, email is:{o_email}, phone numbers is:{o_phone_numbers}')
