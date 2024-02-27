from fastapi import Depends

from app.core.database import get_session

SessionDeps = Depends(get_session)
