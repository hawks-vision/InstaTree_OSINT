import instaloader
import json
import copy
import js_create
import html_create


def tag_highlight(L,inObj,PROFILE):
    posts = L.get_posts()
    dictObj1={"id":" ","name":" ","data":{"name":"Profile_url","Profile_url":"","name":"Post_url","Post_url":""},"children":[]}
    dictObj={"id":" ","name":" ","data":{"url":""},"children":[]}
    users = set()
    print(PROFILE)
    for post in posts:
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
                for highlight in inObj.get_highlights(Taggeduser):
                    childtemp=tempDict["children"]
                    highlightDict=copy.deepcopy(dictObj1)
                    highlightDict["id"]=highlight.unique_id
                    highlightDict["name"]=highlight.title#highlight.owner_profile
                    highlightDict["data"]["Post_url"]=highlight.cover_url
                    childtemp.append(highlightDict)
                tempDict["data"]["Profile_url"]=Taggeduser.profile_pic_url
                tempDict["data"]["Post_url"]=post.url
                dictObj["children"].append(tempDict)
                print(tempDict)
    dictObj["name"]=L.username
    dictObj["data"]["url"]=L.profile_pic_url
    dictObj["id"]="1"
    print(dictObj)
       #print(post.owner_id)
 #   else:
  #      print("{} from {} skipped.".format(post, post.owner_profile))i
    k=L.username+'_tagged_users_highlight'
    js_create.jsCreate(dictObj,k+'.js')
    html_create.html_create(k)
#File=open("highlightmap.json","w+")
#File.write(json.dumps(dictObj,indent=2))

