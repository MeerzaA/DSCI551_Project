import { Component } from '@angular/core';
import { CUSTOM_ELEMENTS_SCHEMA } from '@angular/core';
import { Router } from '@angular/router';
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common'; 

import axios from 'axios';
import * as $ from 'jquery';





@Component({
  selector: 'app-home',
  standalone: true,
  imports: [FormsModule, CommonModule],
  templateUrl: './home.component.html',
  styleUrl: './home.component.css',
  //schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class HomeComponent {
  searchCriteria: string = 'zipcode';
  constructor(private router: Router) {}
  city: string = ''; 
  state: string = ''; 
  onSearchZip(businessZip: string) {
    if (businessZip) {
      this.router.navigate(['/search'], { state: { businessZip: businessZip } });    
    }
  }
  onSearchName(businessName: string) {
    if (businessName) {
      this.router.navigate(['/search'], { state: { businessName: businessName } });    
    }
  }

//https://api-ninjas.com/api/geocoding
getUserCoords(city: string, state: string) {
  //npm install --save-dev @types/jquery
    $.ajax({
        method: 'GET',
        url: 'https://api.api-ninjas.com/v1/geocoding?city=' + city,
        headers: { 'X-Api-Key': 'S7ZzbnQD1T2J4qnYVixIGw==rFMp3Y5sieHrFGsP'},
        contentType: 'application/json',
        success: function(result: any) {
            const stateResult = (result.find((item: any) => item.state.toLowerCase() === state.toLowerCase()));
            const lat = stateResult.latitude;
            const long = stateResult.longitude;
            console.log('info', stateResult);
            console.log('lat', lat);
            console.log('long', long);

        },
        error: function ajaxError(jqXHR: any) {
            console.error('Error: ', jqXHR.responseText);
        }
    });
  }
}
