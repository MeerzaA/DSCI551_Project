import { bootstrapApplication } from '@angular/platform-browser';
import { appConfig } from './app/app.config';
import { AppComponent } from './app/app.component';

import axios from 'axios'; // Install this library using npm/yarn

bootstrapApplication(AppComponent, appConfig)
  .catch((err) => console.error(err));

  // Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyCIivIZb3ynRlkS61dZ9aLL31QvywjT578",
  authDomain: "dsci551-finalproject-756e6.firebaseapp.com",
  projectId: "dsci551-finalproject-756e6",
  storageBucket: "dsci551-finalproject-756e6.appspot.com",
  messagingSenderId: "82476881800",
  appId: "1:82476881800:web:1507c004c26f2e54c14c3d",
  measurementId: "G-FC10Y5Y0QV"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);

// Using curl commands in TS

const ENDPOINT = [
  'https://dsci-studyyelp-1-default-rtdb.firebaseio.com/spots.json',
  'https://dsci-studyyelp-2-288ca-default-rtdb.firebaseio.com/spots.json'  
];


// search by name
async function fetchBusinessName(businessName: string): Promise<string[]> {
  const results: string[] = [];
  for (let dbIndex = 0; dbIndex < ENDPOINT.length; dbIndex++) {
    try {
      const url = `${ENDPOINT[dbIndex]}?orderBy="name"&equalTo="${businessName}"`;

      const response = await axios.get(url); // Await the response
      const data = response.data;
      console.log(`Firebase data loaded from database ${dbIndex}:`, data);
      results.push(JSON.stringify(data));
    } catch (error: any) {
      console.error('Fetch failed', error.message);
    }
  }
  return results; // return array of results
}

// Call the async function within an async context
/* const nameSearch = 'Our House Cafe';
(async () => {
  const retrievedData: string[] = await fetchBusinessName(nameSearch);
  const dataContainer = document.getElementById('data-container');
  if (dataContainer) {
    dataContainer.textContent = retrievedData.join('\n');
  }
})(); */


// search by zip
async function fetchBusinessZip(businessZip: string): Promise<string[]> {
  const results: string[] = [];
  for (let dbIndex = 0; dbIndex < ENDPOINT.length; dbIndex++) {
    try {
      const url = `${ENDPOINT[dbIndex]}?orderBy="name"&equalTo="${businessZip}"`;

      const response = await axios.get(url); // Await the response
      const data = response.data;
      console.log(`Firebase data loaded from database ${dbIndex}:`, data);
      results.push(JSON.stringify(data));
    } catch (error: any) {
      console.error('Fetch failed', error.message);
    }
  }
  return results; // return array of results
}

// Call the async function within an async context
/*const ZipSearch = '46038';
(async () => {
  const retrievedData: string[] = await fetchBusinessZip(ZipSearch);
  const dataContainer = document.getElementById('data-container');
  if (dataContainer) {
    dataContainer.textContent = retrievedData.join('\n');
  }
})();*/

// search by address
async function fetchBusinessAddress(businessAddress: string): Promise<string[]> {
  const results: string[] = [];
  for (let dbIndex = 0; dbIndex < ENDPOINT.length; dbIndex++) {
    try {
      const url = `${ENDPOINT[dbIndex]}?orderBy="address"&equalTo="${businessAddress}"`;

      const response = await axios.get(url); // Await the response
      const data = response.data;
      console.log(`Firebase data loaded from database ${dbIndex}:`, data);
      results.push(JSON.stringify(data));
    } catch (error: any) {
      console.error('Fetch failed', error.message);
    }
  }
  return results; // return array of results
}

// Call the async function within an async context
/*const addresSearch = '11850 Allisonville Rd';
(async () => {
  const retrievedData: string[] = await fetchBusinessName(addresSearch);
  const dataContainer = document.getElementById('data-container');
  if (dataContainer) {
    dataContainer.textContent = retrievedData.join('\n');
  }
})(); */