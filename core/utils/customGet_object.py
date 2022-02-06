from django.shortcuts import get_object_or_404

from .atomic_exception import MyCustomError


class CustomGetObject:
	def get_object(self):
		"""
		Returns the object the view is displaying.

		You may want to override this if you need to provide non-standard
		queryset lookups.  Eg if objects are referenced using multiple
		keyword arguments in the url conf.
		"""
		queryset = self.filter_queryset(self.get_queryset())

		# Perform the lookup filtering.
		lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field

		assert lookup_url_kwarg in self.kwargs, (
			'Expected view %s to be called with a URL keyword argument '
			'named "%s". Fix your URL conf, or set the `.lookup_field` '
			'attribute on the view correctly.' %
			(self.__class__.__name__, lookup_url_kwarg)
		)

		filter_kwargs = {self.lookup_field: self.kwargs[lookup_url_kwarg]}
		obj = get_object_or_404(queryset, **filter_kwargs)

		# May raise a permission denied
		self.check_object_permissions(self.request, obj)

		try:
			if hasattr(obj, 'service'):
				if obj.service in self.service_id_list or obj.service.id in self.service_id_list:
					
					return obj

			elif self.view_name == 'service' and (None in self.service_id_list or obj.id in self.service_id_list):
				return obj

			else:
				return obj

		except:
			pass



		raise MyCustomError("You do not have permission to perform this action.", 403)
			