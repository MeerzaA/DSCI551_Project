import { Component, NgModule, OnInit  } from '@angular/core';
import { CUSTOM_ELEMENTS_SCHEMA, Output, EventEmitter  } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { CommonModule} from '@angular/common';
import { ActivatedRoute,Router, Params } from '@angular/router';
import axios from 'axios';


/*const ENDPOINT = [
  'https://dsci-studyyelp-1-default-rtdb.firebaseio.com/spots.json',
  'https://dsci-studyyelp-2-288ca-default-rtdb.firebaseio.com/spots.json'  
];

async function fetchBusinessZip(businessZip: string): Promise<string[]> {
  const results: any[] = [];
  //const results: string[] = [];
  for (let dbIndex = 0; dbIndex < ENDPOINT.length; dbIndex++) {
    try {
      const url = `${ENDPOINT[dbIndex]}?orderBy="name"&equalTo="${businessZip}"`;

      const response = await axios.get(url); // Await the response
      const data = response.data;
      console.log(`Firebase data loaded from database ${dbIndex}:`, data);
      results.push(data);

      //results.push(JSON.stringify(data));
    } catch (error: any) {
      console.error('Fetch failed', error.message);
    }
  }
  return results; 
}*/

const ENDPOINT = {

  0 : 'https://dsci551proj-cafe-yelp-b8035-default-rtdb.firebaseio.com/business_1.json',
  1 : 'https://dsci551proj-cafe-yelp-b8035-default-rtdb.firebaseio.com/business_2.json',
  2 : 'https://dsci551proj-cafe-yelp-b8035-default-rtdb.firebaseio.com/business_3.json',
  3 : 'https://dsci551proj-cafe-yelp-b8035-default-rtdb.firebaseio.com/business_4.json',
  4 : 'https://dsci551proj-cafe-yelp-b8035-default-rtdb.firebaseio.com/business_5.json'
  
}
async function fetchBusinessZip(businessZip: string): Promise<any[]> {
  try {

    const url = `${ENDPOINT[0]}?orderBy="postal_code"&equalTo="${businessZip}"`;

    const response = await axios.get(url); // Await the response

    const data = response.data;
    const dataArray = Object.keys(data).map(key => data[key]);
    console.log('Fetch business zip:', dataArray);

    return dataArray; 
  } catch (error: any) {
    console.error('Fetch failed', error.message);
    return []; // empty string error 
  }
}


@Component({

  selector: 'app-component',
  standalone: true,
  imports: [RouterOutlet, CommonModule],
  templateUrl: './content.component.html',
  styleUrl: './content.component.css',
  schemas: [CUSTOM_ELEMENTS_SCHEMA]

})

export class ContentComponent implements OnInit {

  sidebarVisible: boolean = false;
  @Output() toggleSidebarEvent = new EventEmitter();

  toggleSidebar() {
    console.log('Sidebar Visible:');
    this.sidebarVisible = !this.sidebarVisible;

  }

  businessZip: string | null = null;
  retrievedData: any[] = [];

  constructor(private route: ActivatedRoute,private router: Router) {}
  

  ngOnInit(): void {
    this.businessZip = history.state.businessZip;

    if (this.businessZip) {
      fetchBusinessZip(this.businessZip).then((data: any) => {
        this.retrievedData = data;
        console.log('ngOnInit:', this.retrievedData);
      });
    }
  }

}
