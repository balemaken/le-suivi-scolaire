# from django.shortcuts import redirect


# class RoleProtectionMiddleware:
#     """
#     Middleware qui protège automatiquement les routes selon leur préfixe.
    
#     - /administrateur/*  → réservé aux admins
#     - /teacher/*         → réservé aux enseignants
#     - /parent/*          → réservé aux parents
#     """

#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#         path = request.path

#         # Mapping préfixe → rôle autorisé
#         routes_protegees = {
#             '/administrateur/': 'admin',
#             '/teacher/': 'enseignant',
#             '/parent/': 'parent',
#         }

#         for prefixe, role_requis in routes_protegees.items():
#             if path.startswith(prefixe):
#                 # Utilisateur non connecté
#                 if not request.user.is_authenticated:
#                     return redirect('login')

#                 # Mauvais rôle
#                 if request.user.role != role_requis:
#                     redirects = {
#                         'parent': 'pageparent',
#                         'enseignant': 'pageteacher',
#                         'admin': 'dashboard_admin',
#                     }
#                     target = redirects.get(request.user.role, 'login')
#                     return redirect(target)

#         return self.get_response(request)


from django.shortcuts import redirect


class RoleProtectionMiddleware:
    """
    Middleware qui protège automatiquement les routes selon leur préfixe.

    - /administrateur/*  → réservé aux admins
    - /teacher/*         → réservé aux enseignants
    - /parent/*          → réservé aux parents

    Certaines routes sont exemptées (inscription, login, etc.)
    """

    def __init__(self, get_response):
        self.get_response = get_response

        # Routes exemptées : accessibles SANS être connecté
        # (inscription, connexion, etc.)
        self.routes_exemptees = [
            '/teacher/inscriptionEnseignant/',
            '/administrateur/inscriptionAdmin/',
            # Ajoute ici d'autres routes si besoin, ex :
            # '/parent/inscriptionParent/',
            # '/login/',
            # '/logout/',
        ]

        # Mapping préfixe → rôle autorisé
        self.routes_protegees = {
            '/administrateur/': 'admin',
            '/teacher/': 'enseignant',
            '/parent/': 'parent',
        }

    def __call__(self, request):
        path = request.path

        # 1) Si la route est exemptée → on laisse passer directement
        for route_exemptee in self.routes_exemptees:
            if path.startswith(route_exemptee):
                return self.get_response(request)

        # 2) Sinon, on applique la protection par préfixe
        for prefixe, role_requis in self.routes_protegees.items():
            if path.startswith(prefixe):
                # Utilisateur non connecté
                if not request.user.is_authenticated:
                    return redirect('login')

                # Mauvais rôle
                if request.user.role != role_requis:
                    redirects = {
                        'parent': 'pageparent',
                        'enseignant': 'pageteacher',
                        'admin': 'dashboard_admin',
                    }
                    target = redirects.get(request.user.role, 'login')
                    return redirect(target)

        return self.get_response(request)