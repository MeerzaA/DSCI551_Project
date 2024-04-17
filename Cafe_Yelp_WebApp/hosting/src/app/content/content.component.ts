import { Component, NgModule, OnInit  } from '@angular/core';
import { CUSTOM_ELEMENTS_SCHEMA, Output, EventEmitter  } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { CommonModule} from '@angular/common';
import { ActivatedRoute,Router, Params } from '@angular/router';
import axios from 'axios';
import 'bootstrap';


const ENDPOINT = [
  'https://dsci-studyyelp-1-default-rtdb.firebaseio.com/spots.json',
  'https://dsci-studyyelp-2-288ca-default-rtdb.firebaseio.com/spots.json'  
];


async function fetchBusinessZip(businessZip: string): Promise<string[]> {
  const results: string[] = [];
  for (let dbIndex = 0; dbIndex < ENDPOINT.length; dbIndex++) {
    try {
      const url = `${ENDPOINT[dbIndex]}?orderBy="postal_code"&equalTo="${businessZip}"`;
      const response = await axios.get(url); // Await the response
      const data = response.data;
      
      const dataArray = Object.keys(data).map(key => data[key]);
      console.log('Fetch business zip:', dataArray);
  
      return dataArray; 
    } catch (error: any) {
      console.error('Fetch failed', error.message);
    }
  }
  return results; 
}

async function fetchBusinessName(businessName: string): Promise<string[]> {
  const results: string[] = [];
  for (let dbIndex = 0; dbIndex < ENDPOINT.length; dbIndex++) {
    try {
      //find a way to change to include (first 3-4 characters)

      const truncatedName = businessName.substring(0, 7);

      const url = `${ENDPOINT[dbIndex]}?orderBy="name"&equalTo="${truncatedName}"`;

      const response = await axios.get(url); // Await the response
      const data = response.data;
      const dataArray = Object.keys(data).map(key => data[key]);
      console.log('Fetch business name:', dataArray);
  
      return dataArray; 
    } catch (error: any) {
      console.error('Fetch failed', error.message);
    }
  }
  return results; // return array of results
}


function showStar(rating: number): string {
  let starsHTML = '';
  //Only show number of stars that correspond to rating
  for (let i = 0; i < rating; i++) {
    starsHTML += `<svg width="30px" height="30px" viewBox="0 3 24 24" fill="#FFFFFF" xmlns="http://www.w3.org/2000/svg">
    <path d="M11.2691 4.41115C11.5006 3.89177 11.6164 3.63208 11.7776 3.55211C11.9176 3.48263 12.082 3.48263 12.222 3.55211C12.3832 3.63208 
    12.499 3.89177 12.7305 4.41115L14.5745 8.54808C14.643 8.70162 14.6772 8.77839 14.7302 8.83718C14.777 8.8892 14.8343 8.93081 14.8982 
    8.95929C14.9705 8.99149 15.0541 9.00031 15.2213 9.01795L19.7256 9.49336C20.2911 9.55304 20.5738 9.58288 20.6997 9.71147C20.809 9.82316 
    20.8598 9.97956 20.837 10.1342C20.8108 10.3122 20.5996 10.5025 20.1772 10.8832L16.8125 13.9154C16.6877 14.0279 16.6252 14.0842 16.5857 
    14.1527C16.5507 14.2134 16.5288 14.2807 16.5215 14.3503C16.5132 14.429 16.5306 14.5112 16.5655 14.6757L17.5053 19.1064C17.6233 19.6627 
    17.6823 19.9408 17.5989 20.1002C17.5264 20.2388 17.3934 20.3354 17.2393 20.3615C17.0619 20.3915 16.8156 20.2495 16.323 19.9654L12.3995 
    17.7024C12.2539 17.6184 12.1811 17.5765 12.1037 17.56C12.0352 17.5455 11.9644 17.5455 11.8959 17.56C11.8185 17.5765 11.7457 17.6184 
    11.6001 17.7024L7.67662 19.9654C7.18404 20.2495 6.93775 20.3915 6.76034 20.3615C6.60623 20.3354 6.47319 20.2388 6.40075 20.1002C6.31736 
    19.9408 6.37635 19.6627 6.49434 19.1064L7.4341 14.6757C7.46898 14.5112 7.48642 14.429 7.47814 14.3503C7.47081 14.2807 7.44894 14.2134 
    7.41394 14.1527C7.37439 14.0842 7.31195 14.0279 7.18708 13.9154L3.82246 10.8832C3.40005 10.5025 3.18884 10.3122 3.16258 10.1342C3.13978 
    9.97956 3.19059 9.82316 3.29993 9.71147C3.42581 9.58288 3.70856 9.55304 4.27406 9.49336L8.77835 9.01795C8.94553 9.00031 9.02911 8.99149 
    9.10139 8.95929C9.16534 8.93081 9.2226 8.8892 9.26946 8.83718C9.32241 8.77839 9.35663 8.70162 9.42508 8.54808L11.2691 4.41115Z" 
    stroke="#000000" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
    </svg>`;
  }
  return starsHTML;
}

function addCard(retrievedData: any[]): void {
  const businessCardsContainer = document.getElementById("businesses");

  if (businessCardsContainer && retrievedData && Array.isArray(retrievedData)) {
      retrievedData.forEach((item: any) => { // Arrow function here
          const businessCard = document.createElement("div");
          businessCard.className = "business-card";
          /*businessCard.innerHTML = `
              <p>${item.name}</p>
              <p>Stars: ${item.stars}</p>
              <p>${item.address}, ${item.city}, ${item.state}, ${item.postal_code}</p>
              <p>Friday: ${item.hours.Friday}</p>
          `;*/
          //CSS is not working for these
          businessCard.style.backgroundColor = "#597c47";
          businessCard.style.width = "600px";
          businessCard.style.height = "800px";
          businessCard.style.padding = "20px";
          businessCard.style.marginTop = "20px";

          let cardContent = `<p style="font-size: 40px;">${item.name}</p>`;
          
          if (item.stars) {
            cardContent += `<p> Rating: ${showStar(item.stars)}, ${item.stars} </p>`;
          }
          if (item.address && item.city && item.state && item.postal_code) {
            cardContent += `<p style="font-size: 20px;">${item.address}, ${item.city}, ${item.state}, ${item.postal_code}</p>`;
          }
          if (item.attributes) {
            if (item.attributes.BikeParking) {
              cardContent += `<p>Bike Parking: ${item.attributes.BikeParking}</p>`;}
            //If true, display what type of parking is available
            if (item.attributes.BusinessParking) {
              cardContent += `<p>Business Parking: ${item.attributes.BusinessParking}</p>`;}
            if (item.attributes.DogsAllowed) {
              cardContent += `<p>Dog Friendly: ${item.attributes.DogsAllowed}</p>`;}
            if (item.attributes.NoiseLevel) {
              cardContent += `<p>Noise Level: ${item.attributes.NoiseLevel}</p>`;}
            if (item.attributes.OutdoorSeating) {
              cardContent += `<p>Outdoor Seating: ${item.attributes.OutdoorSeating}</p>`;}
            if (item.attributes.RestaurantsGoodForGroups) {
              cardContent += `<p>Group Friendly: ${item.attributes.RestaurantsGoodForGroups}</p>`;}
            if (item.attributes.WiFi) {
              cardContent += `<p>WiFi: ${item.attributes.WiFi}</p>`;}

              ;
          }

          //https://getbootstrap.com/docs/4.0/components/collapse/
          if (item.hours) {
            cardContent += `<button class="btn btn-primary" type="button" data-toggle="collapse" 
            data-target="#allHoursCollapse" aria-expanded="false" aria-controls="allHoursCollapse">
            Hours of Operation
          </button>
          <div class="collapse" id="allHoursCollapse">
            <div class="card card-body">`;
            if (item.hours.Monday) {
              cardContent += `<p>Monday: ${item.hours.Monday}</p>`;}
            if (item.hours.Tuesday) {
              cardContent += `<p>Tuesday: ${item.hours.Tuesday}</p>`;}
            if (item.hours.Wednesday) {
              cardContent += `<p>Wednesday: ${item.hours.Wednesday}</p>`;}
            if (item.hours.Thursday) {
              cardContent += `<p>Thursday: ${item.hours.Thursday}</p>`;}
            if (item.hours.Friday) {
              cardContent += `<p>Friday: ${item.hours.Friday}</p>`;}
            if (item.hours.Saturday) {
              cardContent += `<p>Saturday: ${item.hours.Saturday}</p>`;}
            if (item.hours.Sunday) {
              cardContent += `<p>Sunday: ${item.hours.Sunday}</p>`;}
            cardContent += `</div></div>`;
          }
          
          if (item.reviews) {
            cardContent += `<button class="btn btn-primary" type="button" data-toggle="collapse" 
            data-target="#reviews" aria-expanded="false" aria-controls="reviews">
            Reviews
          </button>
          <div class="collapse" id="reviews">
            <div class="card card-body">`;
            cardContent += `<p> ${item.reviews.text} </p>`;
          }

          businessCard.innerHTML = cardContent;

          businessCardsContainer.appendChild(businessCard);
      });
  } else {
      console.error("retrievedData is not available or not an array.");
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
  businessName: string | null = null;
  retrievedData: any[] = [];

  constructor(private route: ActivatedRoute,private router: Router) {}
  

  ngOnInit(): void {
    this.businessZip = history.state.businessZip;
    this.businessName = history.state.businessName;

    if (this.businessZip) {
      fetchBusinessZip(this.businessZip).then((data: any) => {
        this.retrievedData = data;
        console.log('ngOnInit:', this.retrievedData);
        addCard(this.retrievedData);
      });
    }
    else if (this.businessName) {
      fetchBusinessName(this.businessName).then((data: any) => {
        this.retrievedData = data;
        console.log('ngOnInit:', this.retrievedData);
        addCard(this.retrievedData);
      });
    }
  }

}
