from django.shortcuts import get_object_or_404

from .atomic_exception import MyCustomError

from Marketplace.models import *


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
				if self.view_name in ['morder', 'mproduct', 'mbusket', 'mcourier']:
					if obj.service.get('id', None) in self.service_id_list:
						return obj

				
				elif obj.service in self.service_id_list or obj.service.id in self.service_id_list:
						
						return obj
			
			elif self.view_name == 'service' and (None in self.service_id_list or obj.id in self.service_id_list):
				return obj
		
		except:
			pass



		raise MyCustomError('You do not have permission to perform this action.', 403)



class CustomFilterQueryset:
	def filter_queryset(self, queryset):
		try:
			marketplace_data = {
				"mproduct": MProduct,
				"mbusket": MBusket,
				"morder":MOrder,
				"mcourier":MCourier
			}

			self.request.GET._mutable =  True
			if self.view_name == 'service':

				organization = self.request.query_params.get('organization', None)
				if organization is not None:
					del self.request.query_params['organization']
					self.request.query_params['organization__id'] = organization

				return super().filter_queryset(queryset)


			else:
				service = self.request.query_params.get('service', None)
				
				if service is not None:

					if int(service) in self.service_id_list:
						if self.view_name in marketplace_data:

							return super().filter_queryset(queryset.filter(service={"id":int(service)}))
						else:
							del self.request.query_params['service']
							self.request.query_params['service__id'] = service
					else:
						raise MyCustomError('You do not have permission to perform this action.', 403)

				else:

					if self.view_name in marketplace_data:
						return super().filter_queryset(marketplace_data[self.view_name].objects.mongo_aggregate([{
							"$match":{
	      						"service.id": {
	        						"$in": self.service_id_list
	      						}
	      					}
	    				}]))
					else:
						return super().filter_queryset(queryset.filter(service__id__in=self.service_id_list))
						
				return super().filter_queryset(queryset)
		except:
			pass


		raise MyCustomError('You do not have permission to perform this action.', 403)
			