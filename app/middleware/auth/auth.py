from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import RedirectResponse

class AuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        if request.url.path in ["/login"] or request.url.path.startswith("/static"):
            return await call_next(request)

        user_id = request.cookies.get("user_id")

        if not user_id:
            return RedirectResponse(url="/login")

        response = await call_next(request)
        return response
