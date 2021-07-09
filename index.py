import gkeepapi

##### KEYS / AUTH
user1 = "someemail@gmail.com"
# 16 character App key you created with google. Make sure two factor auth is turned on.
p1 = "xxxxxxxxxxxxxxxx"
# A user login token you can re-use to minimize log-in instances
t1 = LOGIN_TOKEN_HERE


######## STUFF
keep = gkeepapi.Keep()
keep.resume(user2, t2)
# gnotes = keep.find(colors=[gkeepapi.node.ColorValue.Purple])
gnotes = keep.find(archived=True)
# gnotes = keep.all()
gnotes = keep.find(labels=[keep.findLabel('uncat')])

# label = keep.findLabel('uncat')
# label = keep.findLabel('uncat')
# keep.deleteLabel(label)
# label = keep.findLabel('Poetry')
# label2 = keepfindLabel('someLabEL')

for x in gnotes:
  # x.labels.add(label)
  # x.labels.add(label2)
  x.archived = True
  # print("hey!")
  # x.archived = True
  # x.collaborators.add("anotherEmail@example.com")
  # x.color = gkeepapi.node.ColorValue.Purple
  # x.delete()
  # print(x.timestamps)
  # x.labels.add(label)

keep.sync()

msg = "Operation Complete"
print(msg)






####### NOTES
# Using debugging tools with python
# https://code.visualstudio.com/docs/python/python-tutorial
# go to google accoutn here to mess with 2 factor auth and stuff: https://support.google.com/accounts/answer/3067630?hl=en

# possible fix for 'NeedsBrowser' login error:
# https://accounts.google.com/b/0/DisplayUnlockCaptcha

# success = keep.login('kennedy@bermanco.com', 'muxsmdmjtvoxnlgr')
# print("Master token is: ", keep.getMasterToken())