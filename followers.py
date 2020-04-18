import instaloader
import json
import copy
import js_create
import html_create
#Profile = instaloader.Profile()
def followers(L,inObj,PROFILE):
    followers = L.get_followers()
    dictObj1={"id":" ","name":" ","data":{"url":""},"children":[]}
    dictObj={"id":" ","name":" ","data":{"url":""},"children":[]}
    users = set()
    print(PROFILE)
    for account in followers:
        print(account.username)
        accountOwner=instaloader.Profile.from_username(inObj.context,account.username)
        tempDict=copy.deepcopy(dictObj1)
        tempDict["id"]=accountOwner.userid
        tempDict["name"]=account.username
        tempDict["data"]["url"]=accountOwner.profile_pic_url
        dictObj["children"].append(tempDict)
        print(tempDict)
 #  if not post.tagged_users in users:
       # L.download_post(post, '#osint')
    # print(post.owner_profile)
    # print(post.tagged_users)
   
    dictObj["name"]=L.username
    dictObj["data"]["url"]=L.profile_pic_url
    dictObj["id"]="1"
       #print(post.owner_id)
 #   else:
  #      print("{} from {} skipped.".format(post, post.owner_profile))
#h=json.loads(dictObj)
#File=open(L.username + ".json","w+")
#File.write(json.dumps(dictObj,indent=2))
    print(json.dumps(dictObj,indent=2))
    fileName=L.username+'_followers'
    js_create.jsCreate(dictObj,fileName+'.js')
    html_create.html_create(fileName)
