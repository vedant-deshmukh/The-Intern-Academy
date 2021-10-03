from tkinter import *
from PIL import ImageTk
from tkinter.messagebox import showerror
from bot import InstaAutoBot

# Instagram Automation Bot Creation
mybot = InstaAutoBot()

# Enhancing the Tkinter Package
class myTK(Tk):
	
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
        
	# Editing the Exception Display Method
	def report_callback_exception(self, exc, val, tb):
		exc1 = str("<class 'selenium.common.exceptions.NoSuchElementException'>")
		if str(exc) == exc1:
			mybot.driver.quit()
			showerror("Error", message='Bad Network Connection or Invalid Username/Password. \n\n\t    Try Restarting the Bot!')
			
		
		exc2 = str("<class 'selenium.common.exceptions.ElementClickInterceptedException'>")
		if str(exc) == exc2:
			mybot.driver.quit()
			showerror("Error", message='Your Password is too short. \n Please Try Again!')


# Creating the Front-End for Instagram Automation Bot
class UI:

	# Constructor for UI
	def __init__(self, root):

		# Initializing the Tkinter Window Properties
		self.root = root
		self.root.title("Instagram Automation Tool")
		self.root.geometry("800x600+540+50")
		self.root.resizable(False, False)

		# Setting the Icon of the Window
		photo = PhotoImage(file = "icon.png")
		self.root.iconphoto(False, photo)
		
		# Setting the Background of the Window
		self.bg = ImageTk.PhotoImage(file = "background.png")
		self.bg_image  =  Label(self.root, image = self.bg).place(x = 0 ,y =  0, relwidth  =  1, relheight =  1 )
		
		# Setting the Title Image on the Window
		self.title= ImageTk.PhotoImage(file = "title.png")
		self.title_image  =  Label(self.root, image = self.title).place(x = 0 ,y =  0)
		
		# Displays Login Frame
		self.login_frame()
		

	# Function to Create the Login Frame on the Window
	def login_frame(self):

		# Creating the Login Frame
		self.Frame_Login =  Frame(self.root , bg =  'white')
		self.Frame_Login.place(x =  145, y = 150, width =  500, height = 400)
		Label(self.Frame_Login, text = "Enter Your Details", font  =('Impact',35,"bold"), fg = "#E70A6A", bg = "white" ).pack()
		Label(self.Frame_Login, text =  "User Login", font  =('Goudy old style',24,"bold"), fg = "black", bg = "white" ).pack()
		
		# Creating Labels and Entry for Username 
		self.user_var = StringVar()
		Label(self.Frame_Login, text =  "Instagram Username", font  =('Goudy old style',15,"bold"), fg = "grey", bg = "white" ).place(x= 90,  y = 120)
		Label(self.Frame_Login, text =  "NOTE: Enter without @ and in  Lowercase.", font  =('Times new roman',9), fg = "#b0b0ae", bg = "white" ).place(x= 90,  y = 145)
		user_entry =  Entry (self.Frame_Login, text = "Enter Id in small letters without @", textvariable =  self.user_var, font = ('Goudy old style', 15), bg = "#E7E6E6")
		user_entry.place(x = 90,y  = 175, width = 320, height= 30)

		# Creating Labels and Entry for Password
		self.passw_var = StringVar()
		Label(self.Frame_Login, text =  "Instagram Password", font  =('Goudy old style',15,"bold"), fg = "grey", bg = "white" ).place(x= 90,  y = 215)
		self.passw_entry =  Entry (self.Frame_Login, font = ('Goudy old style', 15), textvariable = self.passw_var, show='*', bg = "#E7E6E6")
		self.passw_entry.place(x = 90,y  = 250, width = 320, height= 30)
		
		# Creating Login Button
		Button(self.Frame_Login, text =  "Login", font  =('Goudy old style',13,"bold"), command = self.login, fg = "white", bg = "grey", height = 2, width = 7).place(x= 220,  y = 320)

		# Creating Exit Button
		self.Exit = Button(self.root, text = 'Exit', font =('Goudy old style',15,"bold"), command = self.root.destroy, fg = "black", bg = "white", height = 1, width = 5)
		self.Exit.place(x = 725, y=550)
	

	# Command Function for Login Button of Login Frame
	# To Login to the Instagram 
	def login(self):
		username = self.user_var.get()
		password = self.passw_var.get()
		mybot.login(username, password)
		self.Frame_Login.place_forget()
		self.Exit.place_forget()
		self.show_funcs()


	# Function to Create Func_Frame on the Window
	def show_funcs(self):

		# Creating Buttons for All the functions
		self.Frame_Func =  Frame(self.root , bg =  'white')
		self.Frame_Func.place(x =  145, y = 150, width =  500, height = 400)
		Label(self.Frame_Func, text = "Functions To Perform", font  =('Impact',35,"bold"), fg = "#E70A6A", bg = "white" ).pack()
		Button(self.Frame_Func, text =  "Like By Hashtag", font  =('Times new roman',12,"bold"), command = self.like_by_hashtag_frame,fg = "white", bg = "grey", height = 1, width = 25).place(x= 140,  y = 80)
		Button(self.Frame_Func, text =  "Like & Comment By Hashtag", font  =('Times new roman',12,"bold"), command = self.comment_by_hashtag_frame, fg = "white", bg = "grey", height = 1, width = 25).place(x= 140,  y = 130)
		Button(self.Frame_Func, text =  "Like By Username", font  =('Times new roman',12,"bold"), command = self.like_by_username_frame, fg = "white", bg = "grey", height = 1, width = 25).place(x= 140,  y = 180)
		Button(self.Frame_Func, text =  "Like & Comment By Username", font  =('Times new roman',12,"bold"), command = self.comment_by_username_frame, fg = "white", bg = "grey", height = 1, width = 25).place(x= 140,  y = 230)
		Button(self.Frame_Func, text =  "Follow People", font  =('Times new roman',12,"bold"), command = self.follow_frame, fg = "white", bg = "grey", height = 1, width = 25).place(x= 140,  y = 280)
		Button(self.Frame_Func, text =  "Share Post", font  =('Times new roman',12,"bold"), command = self.share_frame, fg = "white", bg = "grey", height = 1, width = 25).place(x= 140,  y = 330)

		# Creating the Logout button
		self.Logout = Button(self.root, text = 'Logout', font =('Goudy old style',13,"bold"), command = self.logout, fg = "black", bg = "white", height = 1, width = 5)
		self.Logout.place(x = 725, y=550)


	# Function to Create Like By Hashtag Frame on the Window
	def like_by_hashtag_frame(self):

		# Create Like By Hashtag frame
		self.Frame_Func.place_forget()
		self.Frame_lbh =  Frame(self.root , bg =  'white')
		self.Frame_lbh.place(x =  145, y = 150, width =  500, height = 400)
		Label(self.Frame_lbh, text = "Like By Hashtag", font  =('Impact',35,"bold"), fg = "#E70A6A", bg = "white" ).pack()
		
		# Creating Label and Entry for Hashtag 
		self.hash_var = StringVar()
		Label(self.Frame_lbh, text =  "Enter Hashtag", font  =('Goudy old style',15,"bold"), fg = "grey", bg = "white" ).place(x= 90,  y = 120)
		Label(self.Frame_lbh, text =  "NOTE: Enter without #", font  =('Times new roman',9), fg = "#b0b0ae", bg = "white" ).place(x= 90,  y = 145)
		hash_entry =  Entry (self.Frame_lbh, text = "Enter Id in small letters without @", textvariable =  self.hash_var, font = ('Goudy old style', 15), bg = "#E7E6E6")
		hash_entry.place(x = 90,y  = 175, width = 320, height= 30)

		# Creating Label and Entry for Number of Likes
		self.like_var = StringVar()
		Label(self.Frame_lbh, text =  "Number of Likes", font  =('Goudy old style',15,"bold"), fg = "grey", bg = "white" ).place(x= 90,  y = 215)
		like_entry =  Entry (self.Frame_lbh, font = ('Goudy old style', 15), textvariable = self.like_var, bg = "#E7E6E6")
		like_entry.place(x = 90,y  = 250, width = 320, height= 30)

		# Creating the Like Button
		Button(self.Frame_lbh, text =  "Like", font  =('Goudy old style',12,"bold"), command = self.like_by_hashtag, fg = "white", bg = "grey", height = 2, width = 7).place(x= 220,  y = 320)
		
		# Creating the Back Button
		self.Back = Button(self.root, text = 'Back', font =('Goudy old style',13,"bold"), command = self.back, fg = "black", bg = "white", height = 1, width = 5)
		self.Back.place(x = 725, y = 510)


	# Command Function for Like By Hashtag Button of Function frame
	# To Like posts based on the Hashtag 
	def like_by_hashtag(self):
		hashtag = self.hash_var.get()
		num_likes = int(self.like_var.get())
		mybot.like_by_hashtags(hashtag, num_likes)
		self.Back.place_forget()
		self.Frame_lbh.place_forget()
		self.show_funcs()


	# Function to Create Like & Comment By Hashtag Frame on the Window
	def comment_by_hashtag_frame(self):

		# Create Like & Comment By Hashtag frame
		self.Frame_Func.place_forget()
		self.Frame_lcbh =  Frame(self.root , bg =  'white')
		self.Frame_lcbh.place(x =  145, y = 150, width =  500, height = 400)
		Label(self.Frame_lcbh, text = "Like & Comment By Hashtag", font  =('Impact',30,"bold"), fg = "#E70A6A", bg = "white" ).pack()
		
		# Creating Label and Entry for Hashtag
		self.hash_var = StringVar()
		Label(self.Frame_lcbh, text =  "Enter Hashtag", font  =('Goudy old style',15,"bold"), fg = "grey", bg = "white" ).place(x= 90,  y = 120)
		Label(self.Frame_lcbh, text =  "NOTE: Enter without #", font  =('Times new roman',9), fg = "#b0b0ae", bg = "white" ).place(x= 90,  y = 145)
		hash_entry =  Entry (self.Frame_lcbh, text = "Enter Id in small letters without @", textvariable =  self.hash_var, font = ('Goudy old style', 15), bg = "#E7E6E6")
		hash_entry.place(x = 90,y  = 175, width = 320, height= 30)

		# Creating Label and Entry for Number of Likes
		self.like_var = StringVar()
		Label(self.Frame_lcbh, text =  "Number of Likes", font  =('Goudy old style',15,"bold"), fg = "grey", bg = "white" ).place(x= 90,  y = 215)
		like_entry =  Entry (self.Frame_lcbh, font = ('Goudy old style', 15), textvariable = self.like_var, bg = "#E7E6E6")
		like_entry.place(x = 90,y  = 250, width = 320, height= 30)

		# Creating the Like & Comment Button
		Button(self.Frame_lcbh, text =  "Like & Comment", font  =('Goudy old style',12,"bold"), command = self.comment_by_hashtag, fg = "white", bg = "grey", height = 2, width = 15).place(x= 200,  y = 320)
		
		# Creating the Back Button
		self.Back = Button(self.root, text = 'Back', font =('Goudy old style',13,"bold"), command = self.back, fg = "black", bg = "white", height = 1, width = 5)
		self.Back.place(x = 725, y = 510)


	# Command Function for Like & Comment By Hashtag Button of Function frame
	# To Like & Comment on posts based on the Hashtag
	def comment_by_hashtag(self):
		hashtag = self.hash_var.get()
		num_likes = int(self.like_var.get())
		mybot.comment_by_hashtags(hashtag, num_likes)
		self.Back.place_forget()
		self.Frame_lcbh.place_forget()
		self.show_funcs()


	# Function to Create Like By Username Frame on the Window
	def like_by_username_frame(self):

		# Create Like By Username frame
		self.Frame_Func.place_forget()
		self.Frame_lbu =  Frame(self.root , bg =  'white')
		self.Frame_lbu.place(x =  145, y = 150, width =  500, height = 400)
		Label(self.Frame_lbu, text = "Like By Username", font  =('Impact',35,"bold"), fg = "#E70A6A", bg = "white" ).pack()
		
		# Creating Label and Entry for Username
		self.name_var = StringVar()
		Label(self.Frame_lbu, text =  "Enter Username", font  =('Goudy old style',15,"bold"), fg = "grey", bg = "white" ).place(x= 90,  y = 120)
		Label(self.Frame_lbu, text =  "NOTE: Enter without @ and in Lowercase", font  =('Times new roman',9), fg = "#b0b0ae", bg = "white" ).place(x= 90,  y = 145)
		name_entry =  Entry (self.Frame_lbu, text = "Enter Id in small letters without @", textvariable =  self.name_var, font = ('Goudy old style', 15), bg = "#E7E6E6")
		name_entry.place(x = 90,y  = 175, width = 320, height= 30)

		# Creating Label and Entry for Number of Likes
		self.like_var = StringVar()
		Label(self.Frame_lbu, text =  "Number of Likes", font  =('Goudy old style',15,"bold"), fg = "grey", bg = "white" ).place(x= 90,  y = 215)
		like_entry =  Entry (self.Frame_lbu, font = ('Goudy old style', 15), textvariable = self.like_var, bg = "#E7E6E6")
		like_entry.place(x = 90,y  = 250, width = 320, height= 30)

		# Creating the Like Button
		Button(self.Frame_lbu, text =  "Like", font  =('Goudy old style',12,"bold"), command = self.like_by_username, fg = "white", bg = "grey", height = 2, width = 7).place(x= 220,  y = 320)
		
		# Creating the Back Button
		self.Back = Button(self.root, text = 'Back', font =('Goudy old style',13,"bold"), command = self.back, fg = "black", bg = "white", height = 1, width = 5)
		self.Back.place(x = 725, y = 510)


	# Command Function for Like By Username Button of Function frame
	# To Like on posts based on the Username
	def like_by_username(self):
		username = self.name_var.get()
		num_likes = int(self.like_var.get())
		mybot.like_by_username(username, num_likes)
		self.Back.place_forget()
		self.Frame_lbu.place_forget()
		self.show_funcs()


	# Function to Create Like & Comment By Username Frame on the Window
	def comment_by_username_frame(self):

		# Create Like & Comment By Username frame
		self.Frame_Func.place_forget()
		self.Frame_lcbu =  Frame(self.root , bg =  'white')
		self.Frame_lcbu.place(x =  145, y = 150, width =  500, height = 400)
		Label(self.Frame_lcbu, text = "Like & Comment By Username", font  =('Impact',28,"bold"), fg = "#E70A6A", bg = "white" ).pack()
		
		# Creating Label and Entry for Username
		self.name_var = StringVar()
		Label(self.Frame_lcbu, text =  "Enter Username", font  =('Goudy old style',15,"bold"), fg = "grey", bg = "white" ).place(x= 90,  y = 120)
		Label(self.Frame_lcbu, text =  "NOTE: Enter without @", font  =('Times new roman',9), fg = "#b0b0ae", bg = "white" ).place(x= 90,  y = 145)
		name_entry =  Entry (self.Frame_lcbu, text = "Enter Id in small letters without @", textvariable =  self.name_var, font = ('Goudy old style', 15), bg = "#E7E6E6")
		name_entry.place(x = 90,y  = 175, width = 320, height= 30)

		# Creating Label and Entry for Number of Likes
		self.like_var = StringVar()
		Label(self.Frame_lcbu, text =  "Number of Likes", font  =('Goudy old style',15,"bold"), fg = "grey", bg = "white" ).place(x= 90,  y = 215)
		like_entry =  Entry (self.Frame_lcbu, font = ('Goudy old style', 15), textvariable = self.like_var, bg = "#E7E6E6")
		like_entry.place(x = 90,y  = 250, width = 320, height= 30)

		# Creating the Like & Comment Button
		Button(self.Frame_lcbu, text =  "Like & Comment", font  =('Goudy old style',12,"bold"), command = self.comment_by_username, fg = "white", bg = "grey", height = 2, width = 15).place(x= 200,  y = 320)
		
		# Creating the Back Button
		self.Back = Button(self.root, text = 'Back', font =('Goudy old style',13,"bold"), command = self.back, fg = "black", bg = "white", height = 1, width = 5)
		self.Back.place(x = 725, y = 510)


	# Command Function for Like & Comment By Username Button of Function frame
	# To Like & Comment on posts based on the Username
	def comment_by_username(self):
		username = self.name_var.get()
		num_likes = int(self.like_var.get())
		mybot.comment_by_username(username, num_likes)
		self.Back.place_forget()
		self.Frame_lcbu.place_forget()
		self.show_funcs()


	# Function to Create Follow People Frame on the Window
	def follow_frame(self):

		# Create Follow People frame
		self.Frame_Func.place_forget()
		self.Frame_follow =  Frame(self.root , bg =  'white')
		self.Frame_follow.place(x =  145, y = 150, width =  500, height = 400)
		Label(self.Frame_follow, text = "Follow People", font  =('Impact',30,"bold"), fg = "#E70A6A", bg = "white" ).pack()
		
		# Creating Label and Entry for Username / Usernames
		self.name_var = StringVar()
		Label(self.Frame_follow, text =  "Enter Username / Usernames", font  =('Goudy old style',15,"bold"), fg = "grey", bg = "white" ).place(x= 90,  y = 120)
		Label(self.Frame_follow, text =  "NOTE: if multiple, it should be separated by ;(Semicolon)", font  =('Times new roman',9), fg = "#b0b0ae", bg = "white" ).place(x= 90,  y = 145)
		names_entry =  Entry(self.Frame_follow, text = "Enter Id in small letters without @", textvariable =  self.name_var, font = ('Goudy old style', 15), bg = "#E7E6E6")
		names_entry.place(x = 90,y  = 175, width = 320, height= 50)

		# Creating the Follow Button
		Button(self.Frame_follow, text =  "Follow", font  =('Goudy old style',12,"bold"), command = self.follow, fg = "white", bg = "grey", height = 2, width = 12).place(x= 200,  y = 280)
		
		# Creating the Back Button
		self.Back = Button(self.root, text = 'Back', font =('Goudy old style',13,"bold"), command = self.back, fg = "black", bg = "white", height = 1, width = 5)
		self.Back.place(x = 725, y = 510)


	# Command Function for Follow People Button of Function frame
	# To Follow people based on the Username or Usernames
	def follow(self):
		usernames = self.name_var.get()
		usernames = usernames.split(';')
		mybot.follow_by_usernames(usernames)
		self.Back.place_forget()
		self.Frame_follow.place_forget()
		self.show_funcs()


	# Function to Create Share Post Frame on the Window
	def share_frame(self):

		# Create Share Post frame
		self.Frame_Func.place_forget()
		self.Frame_share =  Frame(self.root , bg =  'white')
		self.Frame_share.place(x =  145, y = 150, width =  500, height = 400)
		Label(self.Frame_share, text = "Share Post", font  =('Impact',30,"bold"), fg = "#E70A6A", bg = "white" ).pack()
		
		# Creating Label and Entry for Post URLs
		self.url_var = StringVar()
		Label(self.Frame_share, text =  "Enter Post URL", font  =('Goudy old style',15,"bold"), fg = "grey", bg = "white" ).place(x= 90,  y = 100)
		Label(self.Frame_share, text =  "NOTE: if multiple, it should be separated by ;(Semicolon)", font  =('Times new roman',9), fg = "#b0b0ae", bg = "white" ).place(x= 90,  y = 125)
		url_entry =  Entry(self.Frame_share, text = "Enter Id in small letters without @", textvariable =  self.url_var, font = ('Goudy old style', 15), bg = "#E7E6E6")
		url_entry.place(x = 90,y  = 155, width = 320, height= 30)

		# Creating Label and Entry for Username / Usernames
		self.names_var = StringVar()
		Label(self.Frame_share, text =  "Enter Username / Usernames", font  =('Goudy old style',15,"bold"), fg = "grey", bg = "white" ).place(x= 90,  y = 195)
		Label(self.Frame_share, text =  "NOTE: if multiple, it should be separated by ;(Semicolon)", font  =('Times new roman',9), fg = "#b0b0ae", bg = "white" ).place(x= 90,  y = 220)
		self.names_entry =  Entry (self.Frame_share, font = ('Goudy old style', 15), textvariable = self.names_var, bg = "#E7E6E6")
		self.names_entry.place(x = 90, y  = 250, width = 320, height= 30)

		# Creating the Share Button
		Button(self.Frame_share, text =  "Share", font  =('Goudy old style',12,"bold"), command = self.share, fg = "white", bg = "grey", height = 2, width = 12).place(x= 200,  y = 320)
		
		# Creating the Back Button
		self.Back = Button(self.root, text = 'Back', font =('Goudy old style',13,"bold"), command = self.back, fg = "black", bg = "white", height = 1, width = 5)
		self.Back.place(x = 725, y = 510)


	# Command Function for Share Post Button of Function frame
	# To Share posts to the Username or Usernames
	def share(self):
		urls = self.url_var.get()
		urls = urls.split(";")
		usernames = self.names_var.get()
		usernames = usernames.split(";")
		mybot.share_post(usernames, urls)
		self.Back.place_forget()
		self.Frame_share.place_forget()
		self.show_funcs()


	# Command Function for LogOut Button
	# To Logout from the Instagram
	def logout(self):
		mybot.logout()
		self.Back.place_forget()
		self.Logout.place_forget()
		self.login_frame()


	# Command Function for Back Button
	# To go back from Current Window to Previous Window 
	def back(self):
		self.Back.place_forget()
		self.show_funcs()



# Main Function
def main():
	root =  myTK()
	UI(root)
	root.mainloop()
	

if __name__ == "__main__":
	main()

