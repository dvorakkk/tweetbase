from main import TwitterBot

#buat pancing dyno

if __name__ == '__main__':
  session = TwitterBot()
  a = session.checkdm()
  session.post_all(a)
  session