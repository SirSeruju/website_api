import uvicorn
from fastapi import FastAPI, HTTPException

import sys
from app import db
from app import model
from app import log

fastapi_app = FastAPI()

@fastapi_app.get(
    "/apiv1/article/{name}",
    response_model=model.Article,
    responses={
        404: { "description": "The item was not found" },
        503: { "description": "Some problems with services" }
    }
)
async def get_article(name: str):
    try:
        session = db.Session()
        article = session.query(db.Article).filter(db.Article.name == name).first()
    except:
        raise HTTPException(status_code=503, detail="Database is down")
    finally:
        session.close()

    if article:
        return model.Article.from_orm(article)
    else:
        raise HTTPException(status_code=404, detail="Item not found")


if __name__ == '__main__':
    server = uvicorn.Server(
        uvicorn.Config(
            "app.main:fastapi_app",
            host="0.0.0.0"
        ),
    )

    log.setup_logging()

    server.run()
