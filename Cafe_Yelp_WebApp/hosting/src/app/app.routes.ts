import { Routes } from '@angular/router';

import { NgModule } from '@angular/core';

import { HeaderComponent } from './header/header.component';
import { HomeComponent } from './home/home.component';
import { SidebarComponent } from './sidebar/sidebar.component';
import { LayoutComponent } from './layout/layout.component';
import { ContentComponent } from './content/content.component';

export const routes: Routes = [
    {
        path: 'home',
        component: LayoutComponent,
        children: [
            {
                path: '',
                component: HomeComponent,
                outlet: 'homecomp'
            },
            {
                path: '',
                component: HeaderComponent,
                outlet: 'header'
            },
            {
                path: '',
                component: SidebarComponent,
                outlet: 'sidebar'
            }
        ]
    }
];



