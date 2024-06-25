from fastapi import FastAPI, HTTPException
import pickle
import xgboost as xgb
import warnings
import numpy as np

warnings.filterwarnings('ignore')

app = FastAPI()


def import_modelo():
    modelo = pickle.load(open('model_xgb.sav', 'rb'))
    return modelo


modelo = import_modelo()


def padronizacao(x, y, z):
    h = (x - 14.67) / 9.54
    j = (y - 32.81) / 16.54
    z = (z - 10681.48) / 6238.86
    return [h, j, z]


@app.post('/predict')
async def home(res: dict):
    try:
        x = int(res['text'][0])
        y = int(res['text'][1])
        z = int(res['text'][2])
    except (KeyError, TypeError, ValueError) as e:
        raise HTTPException(status_code=400, detail="Invalid input format") from e

    dados = padronizacao(x, y, z)


    resultado = modelo.predict([dados])[0]
    #dados = np.array([dados]).reshape(1, -1)
    return {"resultado": float(resultado)}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)