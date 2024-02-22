import { Routes } from '@angular/router';
import { NgModule } from '@angular/core';

import { HeaderComponent } from './header/header.component';
import { HomeComponent } from './home/home.component';
import { SidebarComponent } from './sidebar/sidebar.component';


export const routes: Routes = [
    { path: 'home', component: HomeComponent },
    { path: '', component: HeaderComponent },
    { path: '', component: SidebarComponent }
];
