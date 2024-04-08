import { Component } from '@angular/core';
import { CUSTOM_ELEMENTS_SCHEMA } from '@angular/core';
import { Router } from '@angular/router';
import axios from 'axios';

@Component({
  selector: 'app-home',
  //standalone: true,
  //imports: [],
  templateUrl: './home.component.html',
  styleUrl: './home.component.css',
  //schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class HomeComponent {
  constructor(private router: Router) {}

  onSearch(businessZip: string) {
    if (businessZip) {
      this.router.navigate(['/search'], { state: { businessZip: businessZip } });    
    }
    // Redirect to another page
    //this.router.navigate(['/search']);

    /*const ENDPOINT = {

      0 : 'https://dsci551proj-cafe-yelp-b8035-default-rtdb.firebaseio.com/business_1.json',
      1 : 'https://dsci551proj-cafe-yelp-b8035-default-rtdb.firebaseio.com/business_2.json',
      2 : 'https://dsci551proj-cafe-yelp-b8035-default-rtdb.firebaseio.com/business_3.json',
      3 : 'https://dsci551proj-cafe-yelp-b8035-default-rtdb.firebaseio.com/business_4.json',
      4 : 'https://dsci551proj-cafe-yelp-b8035-default-rtdb.firebaseio.com/business_5.json'
      
    }

    async function fetchBusinessZip(businessZip: string): Promise<string> {
      try {
    
        const url = `${ENDPOINT[0]}?orderBy="postal_code"&equalTo="${businessZip}"`;
    
        const response = await axios.get(url); // Await the response
        const data = response.data;
        //console.log('Firebase data loaded:', data);
        return JSON.stringify(data); 
      } catch (error: any) {
        console.error('Fetch failed', error.message);
        return ''; // empty string error 
      }
    }
    if (businessZip) {
      /*fetchBusinessZip(businessZip)
        .then(data => {
          this.router.navigate(['/search'], { state: { businesses: data } });
        })
        .catch(error => {
          console.error('Fetch failed', error.message);
        });*/
        /*(async () => {
          const retrievedData: string = await fetchBusinessZip(businessZip);
          /*const dataContainer = document.getElementById('data-container');
          if (dataContainer) {
            dataContainer.textContent = retrievedData;*/
          /*console.log('Firebase:', retrievedData)
          this.router.navigate(['/search'], { state: { retrievedData: retrievedData} });

          })();
    }*/
  }
}
