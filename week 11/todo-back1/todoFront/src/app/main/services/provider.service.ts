  import { EventEmitter, Injectable } from '@angular/core';
  import {ITaskList, ITask} from '../models//todo';
  import {HttpClient, HttpParams} from '@angular/common/http';
  import {MainService} from './main.service';
  @Injectable({
    providedIn: 'root'
  })
  export class ProviderService extends MainService {
    constructor(http: HttpClient) {
      super(http);
    }

    getTaskList(): Promise<ITaskList[]> {
      return this.get('http://localhost:8000/task_lists/',  {});
    }

    getTasks(taskList: ITaskList) {
      return this.get(`http://localhost:8000/task_lists/${taskList.id}/tasks/`, {});
    }

    createTaskList(name: any): Promise<ITaskList>{
      return this.post('http://localhost:8000/task_lists/',{
        name: name
      });
    }
    updateTaskList(taskList: ITaskList): Promise<ITaskList>{
      return this.put(`http://localhost:8000/task_lists/${taskList.id}/`, {
        name: taskList.name
      });
    }

    deleteTaskList(id: number): Promise<any>{
      return this.delet(`http://localhost:8000/task_lists/${id}/`, {});
    }

    updateTask(tl_id: number, t_name: any, t_status: any, task: ITask, task_list: ITaskList): Promise<ITask>{
      return this.put(`http://localhost:8000/task_lists/${task_list.id}/tasks/${task.id}/`, {
        name: t_name,
        status: t_status,
        task_list: tl_id,
      });
    }
    deleteTask(task: ITask, task_list: ITaskList): Promise<ITask>{
      return this.delet(`http://localhost:8000/task_lists/${task_list.id}/tasks/${task.id}/`, {
      });
    }
    createTask(id: number, name: any, status: any): Promise<ITask>{
      return this.post(`http://localhost:8000/task_lists/${id}/tasks/`, {
        name: name,
        status: status,
        task_list: id
      });
    }
  }
