class VIP(object):
	“””
	验证VIP权限
	“””
    def has_permission(self,request,view):
        if request.user.user_type<2:
            return False
        return True
class SVIP(object):
	“””
	验证SVIP权限
	“””
    def has_permission(self,request,view):
        if request.user.user_type<3:
            return False
        return True
