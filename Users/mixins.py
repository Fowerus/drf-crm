class GroupPermissionMixin():
    def api_has_perm(self, perm: str) -> list:
        #Получаем все группы с пермом == perm
        groups = self.groups.filter(organization=self.current_org_id , permissions__codename=perm)
        
        services_id = list()
        if groups:
            # если список не пуст создаем список id сервисов
            services_id = list(map(lambda g: g.service, groups))
               
        if None in services_id:
            # если есть None то отправляем список из изера добавив None
            services_id = self.list_services_id
                   
        return services_id