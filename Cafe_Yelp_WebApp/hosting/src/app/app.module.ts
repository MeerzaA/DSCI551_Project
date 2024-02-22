import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { NgModule } from '@angular/core';
import { HeaderComponent } from './header/header.component';



import { AppComponent } from './app.component';


@NgModule({
  imports: [
    BrowserAnimationsModule,
  ],
  declarations: [
    AppComponent,
    HeaderComponent
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
