import { bootstrapApplication } from '@angular/platform-browser';
import { appConfig } from './app/app.config';
import { AppComponent } from './app/app.component';

import axios from 'axios'; // Install this library using npm/yarn

bootstrapApplication(AppComponent, appConfig)
  .catch((err) => console.error(err));


// Import the functions you need from the SDKs you need
import { initializeApp } from 'firebase/app';
import { getAnalytics } from "firebase/analytics";
import { getAuth } from 'firebase/auth';
import { child, getDatabase, onValue, ref } from 'firebase/database';
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyDfLNVJF4FBY2oUFu33yp30sbL8WjkYwq0",
  authDomain: "dsci551proj-cafe-yelp-b8035.firebaseapp.com",
  projectId: "dsci551proj-cafe-yelp-b8035",
  storageBucket: "dsci551proj-cafe-yelp-b8035.appspot.com",
  messagingSenderId: "999112911079",
  appId: "1:999112911079:web:6f074ed141e6af04a15a42",
  measurementId: "G-9F2HL8N4SF"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);
export const auth = getAuth(app);
export const database = getDatabase(app);


//const rootRef = ref(database);
//const businessRef = child(rootRef, 'business');

//onValue(businessRef, (snapshot) => {
//  const usersData = snapshot.val();
//  console.log(usersData);
//});


// Using curl commands in TS

const ENDPOINT = 'https://dsci551proj-cafe-yelp-b8035-default-rtdb.firebaseio.com/business_1/-0epFLgYq2C1Jo_W4FOBKw.json';

async function fetchDataFromFirebase(): Promise<string> {
  try {
    const response = await axios.get(ENDPOINT); // Await the response
    const data = response.data;
    console.log('Firebase data loaded:', data);
    return JSON.stringify(data); // Assuming you want to display the data as a string
  } catch (error: any) {
    console.error('Fetch failed', error.message);
    return ''; // Return an empty string or handle the error appropriately
  }
}

// Call the async function within an async context
(async () => {
  const retrievedData: string = await fetchDataFromFirebase();
  const dataContainer = document.getElementById('data-container');
  if (dataContainer) {
    dataContainer.textContent = retrievedData;
  }
})();

