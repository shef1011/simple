import { Component } from '@angular/core';
@Component
({
    selector:'my-employee',
    templateUrl: './employee.component.html',
    styleUrls: ['./employee.component.css']
})

export class EmployeeComponent
{
    email="me123@example.com";
    classesToApply: string='boldClass italicsClass';
    applyBold: Boolean=true;
    applyItalics: Boolean=true;
    apply()
    {
        let classes=
        {
            boldClass: this.applyBold,
            italicsClass: this.applyItalics
        };
        return classes;
    }
    onclick()
    {
       
        console.log(this.email);
    }
    
}