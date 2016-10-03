import tweepy
from Tkinter import *

def newTweet():
	#print("Message to tweet: \n")
	print("First tweet: %s\nSecond tweet: %s" % (e1.get(),e2.get()))
	
master = Tk()
Label(master,text="Tweet to").grid(row=0)
Label(master,text="First Tweet").grid(row=1)
Label(master,text="Last Tweet").grid(row=2)

e0=Entry(master)
e1=Entry(master)
e2=Entry(master)

e0.grid(row=0,column=1)
e1.grid(row=1,column=1)
e2.grid(row=2,column=1)

Button(master,text='Cancel',command=master.quit).grid(row=3,column=0,sticky=W,pady=4)
Button(master,text='Tweet it!',command=newTweet).grid(row=3,column=1,sticky=W,pady=4)
#mainloop()
	
def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)

def main():
  # Fill in the values noted in previous step here
  
  cfg = { 
    "consumer_key"        : "n6H3XbvOZZYKTr98zewsjgRBM",
    "consumer_secret"     : "uYhhGCnY4UzEIjD2E8uVh7mcvh12Pu7PlEruQjXLhRkPbF9fQl",
    "access_token"        : "768155398306078720-1aEtTzq5MblfBSDqgMrFTeBQ2amTZL7",
    "access_token_secret" : "R86hPq9Q18xeanX8XAN1iodYXN9DVgQbwrRMgaIJT0uFj" 
    }

  mainloop()
  api = get_api(cfg)
  username=e0.get()
  tweet1=e1.get()
  tweet2=e2.get()
  twt = api.search(q="charu201")
  t=['charu201','@charu201']
  for s in twt:
	for i in t:
		if i==s.text:
			sn=s.user.screen_name
			m="@%s Hey!" % (sn)
			s= api.update_status(m,s.id)
  #tweet = "Happy birthday"+" @priya_bansal_19"+" I'm sending this tweet via Python, my first hand at tweepy!!!"
  #status = api.update_status(status=tweet) 
  #status = api.update_status(status='@'+username+" "+tweet1+" "+tweet2)
  #status = api.update_status(status=tweet2)
  '''user=api.me()
  print('Name: '+user.name)
  print('Location: '+user.location)
  print('Friends: '+str(user.friends_count))'''
  # Yes, tweet is called 'status' rather confusing

if __name__ == "__main__":
  main()
