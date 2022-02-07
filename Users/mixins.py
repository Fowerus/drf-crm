class GroupPermissionMixin():
    def api_has_perm(self, perm: str) -> list:
        #Получаем все группы с пермом == perm
        groups = self.groups.all().filter(organization=self.current_org , permissions__codename=perm)
        
        services_id = list()
        if groups:
            # если список не пуст создаем список id сервисов
            services_id = list(map(lambda g: g.getService(), groups))
               
        if None in services_id:
            # если есть None то отправляем список из изера добавив None
            services_id = list(self.services) + [None]
                   
        return services_id