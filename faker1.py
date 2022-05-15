import faker

fake = faker.Faker(locale='zh_CN')
print('name',fake.name())
print('address:',fake.address())
print('text:',fake.text())
# import faker
#
# fake = faker.Faker(locale='zh_CN')
#
# identity_id = fake.ssn()
# print(identity_id)
#
# # 结果：
# # 511623199003268061
#
# identity_ids = [fake.ssn() for i in range(5)]  # 生成多个
# print(identity_ids)

# 结果：
# ['140108198905080513', '532325199712279418', '370601193711292094', '610526199905267515', '652101194803155106']
