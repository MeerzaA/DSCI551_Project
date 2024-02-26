import { Component } from '@angular/core';
import { CUSTOM_ELEMENTS_SCHEMA } from '@angular/core';
import { EventEmitter, Input, Output } from '@angular/core';


@Component({
  selector: 'app-header',
  //standalone: true,
  //imports: [],
  templateUrl: './header.component.html',
  styleUrl: './header.component.css'
  //schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class HeaderComponent {
  @Input() sidebarVisible: boolean = false;
  @Output() toggleSidebar = new EventEmitter(); 
  onToggleSidebar() {
    this.sidebarVisible = !this.sidebarVisible;
    this.toggleSidebar.emit();
    //console.log('OnToggle Sidebar Visible:', this.sidebarVisible);

  }
}

