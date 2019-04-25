import { Injectable } from '@angular/core';
import { MainService } from './main.service';
import { HttpClient } from '@angular/common/http';
import { ITaskList, IAuthResponse } from '../models/todo';
import { ITask } from '../models/todo';
import { promise } from 'protractor';

@Injectable({
  providedIn: 'root'
})
export class ProviderService extends MainService{
  constructor(http: HttpClient) {
    super(http);
  }


    getTaskList(): Promise<ITaskList[]>{
      return this.get('http://localhost:8000/task_lists/',{});
    }

    getTasks(id:number){
      return  this.get(`http://localhost:8000/task_lists/${id}/tasks/`,{});
    }

    updateTaskList(tasklist: ITaskList): Promise<ITaskList>{
      return this.put(`http://localhost:8000/task_lists/${tasklist.id}/`,{
        name: tasklist.name
      });
    }

    deleteTaskList(id: number) : Promise<any>{
        return this.delet(`http://localhost:8000/task_lists/${id}/`,{});
    }

    createTaskList(name: any) : Promise<ITaskList>{
      return this.post(`http://localhost:8000/task_lists/`, {
         name: name
      });
    }
    auth(login: any, password: any): Promise<IAuthResponse> {
      return this.post(`http://localhost:8000/login/`, {
        username: login,
        password: password
      });
    }

    logout(): Promise<any> {
      return this.post(`http://localhost:8000/logout/`, {
      });
    }
  }
