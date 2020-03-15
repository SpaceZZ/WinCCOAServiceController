import model.services as s


class ServiceProvider:

	@staticmethod
	def get_services():
		"""
		Method returns a dictionary of services to be started or stopped from the services.py
		:return: dictionary of services
		"""
		return s.services
