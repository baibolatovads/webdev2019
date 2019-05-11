	import { Component, OnInit } from '@angular/core';
import { ProviderService } from './services/provider.service';
import { ITaskList } from './models/todo';
import {ITask} from './models/todo';

@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.css']
})
export class MainComponent implements OnInit {

  public tasklist: ITaskList[]=[];
  public taskList_current: ITaskList;
  public loading = false;
  public search_name='';  
  public search_list='';
  public tasks: ITask[]=[]; 

  public name: any='';
  public logged = false;

  public login:any='';
  public password:any='';


  constructor(private provider: ProviderService) { }

  ngOnInit() {
    const token=localStorage.getItem('token');
    if(token){
      this.logged=true;
    }
    if(this.logged){
      this.provider.getTaskList().then(res =>{
        this.tasklist = res;
        setTimeout( () => {
          this.loading=true;
        }, 2000);
      });
    }
    
  }

  getTasks(task:ITaskList){
    //this.selected=selected;
    this.provider.getTasks(task.id).then(res =>{
      this.tasks = res;
    });

  }

  updateTaskList(c: ITaskList){
    this.provider.updateTaskList(c).then(res =>{
      console.log(c.name+'updated');
    });
  }

  deleteTaskList(c: ITaskList){
    this.provider.deleteTaskList(c.id).then(res => {
      console.log(c.name + 'deleted');
      this.provider.getTaskList().then( res => {
        this.tasklist = res;
      })
    })
  }

  createTaskList(){
    if(this.name !== '') {
    this.provider.createTaskList(this.name).then( res => {
      this.name = '';
      this.tasklist.push(res);
      })
    }
  }

  filter1(){
    this.provider.getTasksByName(this.taskList_current.id, this.search_name).then(r=>{
      this.tasks=r;
      console.log(this.taskList_current.id);
    });
  }

  searchList(){
    this.provider.searchListByName(this.search_list).then(res=>{
      this.tasklist=res;
    });
  }

  auth() {
    console.log(this.login+" "+this.password);
    if (this.login !== '' && this.password !== '') {
      this.provider.auth(this.login, this.password).then(res => {
        localStorage.setItem('token', res.token);
        console.log(res);

        this.logged = true;

        this.provider.getTaskList().then(r => {
          this.tasklist = r;
          setTimeout(() => {
            this.loading = true;
          }, 2000);
        });

      });
    }
  }
  logout() {
    this.provider.logout().then(res => {
      localStorage.clear();
      this.logged = false;
    });
  }
  

}
