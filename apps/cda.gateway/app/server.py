from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from langserve import add_routes
from hybrid_search_weaviate import chain as hybrid_search_weaviate_chain
from rag_weaviate import chain as rag_weaviate_chain
from research_assistant import chain as research_assistant_chain

app = FastAPI()

@app.get("/")
async def redirect_root_to_docs():
    return RedirectResponse("/docs")

add_routes(app, hybrid_search_weaviate_chain, path="/hybrid-search-weaviate")
add_routes(app, chain_ext, path="/rag-weaviate")
add_routes(app, research_assistant_chain, path="/research-assistant")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
