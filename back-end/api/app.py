from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from pydantic import BaseModel
from typing import Optional
import secrets

secutiry = HTTPBasic()
app = FastAPI()
tasks = []
    
class Task(BaseModel):
    nome : str
    descricao : str
    concluida : Optional[bool] = False
    
user = 'admin'
password = 'admin'

def autenticar_usuario(credentials: HTTPBasicCredentials = Depends(secutiry)):
    is_correct_username = secrets.compare_digest(credentials.username, user)
    is_correct_password = secrets.compare_digest(credentials.password, user)
    
    if not (is_correct_password and is_correct_username):
        raise HTTPException(status_code=401, detail='unauthorized user')

@app.post("/adicionar")
async def adicionar_Task(Task: Task, credentials: HTTPBasicCredentials = Depends(autenticar_usuario)):
    if any(t.nome == Task.nome for t in tasks):
        raise HTTPException(status_code=400, detail="Essa Task já existe.")
    else:
        tasks.append(Task)
        return {'message': 'Task adicionada com sucesso.'}
    
@app.get("/tasks")
async def ler_tasks(page:int = 1, limit:int =10, credentials: HTTPBasicCredentials = Depends(autenticar_usuario)):
    
    if page <1 or limit <1:
        raise HTTPException(status_code=400, detail='limit or page invalid')
    
    start = (page-1)*limit
    end = page + limit
    
    if len(tasks) == 0:
       return {'message': 'Não existe nenhuma Task.'} 
   
    sorted_tasks = sorted(tasks, key=lambda x: x.nome)
   
    return {
        'page': page,
        'limit': limit,
        'total': len(tasks),
        'tasks': sorted_tasks[start:end]
    }

@app.put("/atualizar_status/{nome}")
async def atualizar_status(nome: str, credentials: HTTPBasicCredentials = Depends(autenticar_usuario)):
    Task = next((t for t in tasks if t.nome == nome), None)
    if Task is None:
        raise HTTPException(status_code=404, detail='Task não encontrada.')
    else:
        Task.concluida = True
        return {'message': 'Task concluida.'}
    
@app.delete("/deletar/{nome}")
async def deletar_Task(nome: str, credentials: HTTPBasicCredentials = Depends(autenticar_usuario)):
    Task = next((t for t in tasks if t.nome == nome), None)
    if Task is None:
        raise HTTPException(status_code=404, detail='Task não encontrada.')
    else:
        tasks.remove(Task)
        return {'message': 'Task deletada com sucesso.'}