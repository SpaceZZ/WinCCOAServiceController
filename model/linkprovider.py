import model.links as l


class LinkProvider:

	@staticmethod
	def get_links():
		"""
		Method returns a dictionary of links to be started or stopped from the links.py
		:return: dictionary of links
		"""
		return l.links
