import instaloader
import json
import copy
import js_create
import html_create


def tag_users(L,inObj,PROFILE):
    posts = L.get_posts()
    dictObj1={"id":" ","name":" ","data":{"url":""},"children":[]}
    dictObj={"id":" ","name":" ","data":{"url":""},"children":[]}
    users = set()
    print(PROFILE)
    for post in posts:
        postDict=copy.deepcopy(dictObj1)
        postDict["id"]=post.mediaid
        print(post.mediaid)
        postDict["name"]=post.mediaid
        postDict["data"]["url"]=post.url
 #  if not post.tagged_users in users:
       # L.download_post(post, '#osint')
    
    # print(post.owner_profile)
    # print(post.tagged_users)
        for user in post.tagged_users:
            if not user in users:
                users.add(user)
                Taggeduser = instaloader.Profile.from_username(inObj.context, user)
                print(user)
                tempDict=copy.deepcopy(dictObj1)
                tempDict["id"]=Taggeduser.userid
                tempDict["name"]=user
                tempDict["data"]["url"]=Taggeduser.profile_pic_url
                postDict["children"].append(tempDict)
                print(tempDict)
        dictObj["children"].append(postDict)
    dictObj["name"]=L.username
    dictObj["data"]["url"]=L.profile_pic_url
    dictObj["id"]="1"
    print(dictObj)
       #print(post.owner_id)
 #   else:
  #      print("{} from {} skipped.".format(post, post.owner_profile))i
    k=L.username+'_posts_and_tagged_users'
    js_create.jsCreate(dictObj,k+'.js')
    html_create.html_create(k)
#File=open("highlightmap.json","w+")
#File.write(json.dumps(dictObj,indent=2))

