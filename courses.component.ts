import { Component } from '@angular/core';
import { CoursesService } from './courses.service';

@Component({
    selector: 'courses',
    templateUrl: "./courses.component.html",
    styleUrls: ["./courses.component.css"]
})
export class CoursesComponent
{
    courses1: any[];
    colSpan:number=4;
    showcourses:boolean=false;
    register:boolean=false; 
    login:boolean=false;
    look: boolean=false;
    title: string="My Styles";
    src: string="C:\\Users\\Admin\\Desktop\\js-basics\\start\\course.png";
    getcourses(): void
    {
        this.showcourses=true;
        this.courses1=[{course_id:'101',course_name:'Angular',price:700},
                   {course_id:'102',course_name:'Python Fundamentals',price:1000},
                   {course_id:'103',course_name:'Data Analytics',price:500},
                   {course_id:'104',course_name:'Devops',price:900}];
    }
    toggleDetails(): void
    {
        this.showcourses=!this.showcourses;
    }
    clicked(): void
    {
        this.register=true;
        this.login=false;

    }
    data():void{
        this.login=true;
        this.register=false;
    }
    /*--func()
    {
        this.look=true;
        this.clicked();
        this.data();
    }*/

}