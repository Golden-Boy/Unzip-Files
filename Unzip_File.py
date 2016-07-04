import zipfile

'''
Unzips files
'''
class UnzipFile(object):
	def __init__(self, filename, filePath, password):
		self.filename = filename
		self.filePath = filePath
		self.password = password
		
	def unzip(self):
		try:
			zFile = zipfile.ZipFile(self.filename)
			zFile.extractall(path=self.filePath, pwd=self.password)
			print("File succesfully extracted to: "+ str(self.filePath))

		except Exception as e:
			print("Error: ", e)

#Zip = UnzipFile('zipfile.zip',None,"home/vylade/Desktop/")
#Zip.unzip()


'''
Create a Tkinter gui application 
that utilizes this unzip script


Add argparse commands for file(-f), password(-p if none specify None), directory(-d) 

'''