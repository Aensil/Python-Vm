import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get('/')
def get_list():
    return [1, 2, 3, 4, 5, 6, 7, 8]

@app.get('/contact', response_class=HTMLResponse)
def get_list():
    return """
        <h1>Hi This is my Page</h1>
        <p>Today it's your lucky day!</p>
    """

def run():
    store.get_categories()

if __name__ == '__main__':
    run()