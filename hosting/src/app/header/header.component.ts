import { Component } from '@angular/core';
import { EventEmitter, Input, Output } from '@angular/core';
import { Router } from '@angular/router';
import { RouterOutlet } from '@angular/router';
import { CommonModule} from '@angular/common';




@Component({
  selector: 'app-header',
  standalone: true,
  imports: [RouterOutlet,CommonModule],
  templateUrl: './header.component.html',
  styleUrl: './header.component.css'
})
export class HeaderComponent {
  sidebarVisible: boolean = false;
  @Output() toggleSidebarEvent = new EventEmitter();

  toggleSidebar() {
    //console.log('Sidebar Visible:');
    this.sidebarVisible = !this.sidebarVisible;
  }


  constructor(private router: Router) {}

  ngOnInit(): void {
  }

  navigateHome() {
    this.router.navigate(['/home']);
  }
}

