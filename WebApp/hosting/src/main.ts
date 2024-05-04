import { bootstrapApplication } from '@angular/platform-browser';
import { appConfig } from './app/app.config';
import { AppComponent } from './app/app.component';

bootstrapApplication(AppComponent, appConfig)
  .catch((err) => console.error(err));

  // Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Web app configuration
// For Firebase JS SDK v7.20.0 and later
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
