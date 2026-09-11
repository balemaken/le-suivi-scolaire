from functools import wraps
from django.shortcuts import redirect


def login_required_by_role(*allowed_roles):
    """
    Décorateur qui vérifie en même temps :
    1. Que l'utilisateur est connecté
    2. Qu'il a le bon rôle
    
    Usage :
        @login_required_by_role('admin')
        def ma_vue(request): ...
        
        @login_required_by_role('admin', 'enseignant')
        def vue_partagee(request): ...
    """
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            # 1. Vérifier que l'utilisateur est connecté
            if not request.user.is_authenticated:
                return redirect('login')
            
            # 2. Vérifier le rôle
            if request.user.role not in allowed_roles:
                # Rediriger vers la page d'accueil de son rôle
                redirects = {
                    'parent': 'pageparent',
                    'enseignant': 'pageteacher',
                    'admin': 'dashboard_admin',
                }
                target = redirects.get(request.user.role, 'login')
                return redirect(target)
            
            return view_func(request, *args, **kwargs)
        return wrapper
    return decorator