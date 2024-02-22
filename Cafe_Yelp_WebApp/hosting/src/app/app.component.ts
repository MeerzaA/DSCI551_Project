import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
//import { HeaderComponent } from './header/header.component';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'dsci551proj-cafe-yelp-b8035';
}
