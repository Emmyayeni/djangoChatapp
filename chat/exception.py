class ClientError(Exception):

	def __init__(self,code,message):
		 
		super().__init__(code)
		self.code = code
		self.message = message