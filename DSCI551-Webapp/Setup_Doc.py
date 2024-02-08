'''
Firebase javascript setup instructions

    1.  Make sure npm is avaliable on your CLI than install firebase | npm install -g npm@10.4.0 & npm install firebase  

    2.  initalize firebase project in Javascript
    
        // Import the functions you need from the SDKs you need
        // Import the functions you need from the SDKs you need
        import { initializeApp } from "firebase/app";
        import { getAnalytics } from "firebase/analytics";
        // TODO: Add SDKs for Firebase products that you want to use
        // https://firebase.google.com/docs/web/setup#available-libraries

        // Your web app's Firebase configuration
        // For Firebase JS SDK v7.20.0 and later, measurementId is optional
        const firebaseConfig = {
        apiKey: "AIzaSyBXKzM3bmIriYXUuhnlhqkWwAjyTOWqsRA",
        authDomain: "dsci551-test-project.firebaseapp.com",
        projectId: "dsci551-test-project",
        storageBucket: "dsci551-test-project.appspot.com",
        messagingSenderId: "905128903823",
        appId: "1:905128903823:web:42baca510d6895c5721cfa",
        measurementId: "G-FP0SNEGV78"
        };

        // Initialize Firebase
        const app = initializeApp(firebaseConfig);
        const analytics = getAnalytics(app);

    3.  

'''


'''
Firebase Python setup instructions 

    1.  Install firebase packages | pip install firebase-admin & pip install firebase 
        
    2.  initalize firebase project in python 
    
        import firebase_admin
        from firebase_admin import credentials
        import json

        cred = credentials.Certificate("dsci551-test-project-firebase-adminsdk-lrct5-9425caf0b2.json")
        firebase_admin.initialize_app(cred)

    3.  

'''

'''
GitHub setup project 

    1.  Install firebase packages | pip install firebase-admin & pip install firebase 
        
    2.  initalize firebase project in python 
    
        import firebase_admin
        from firebase_admin import credentials
        import json

        cred = credentials.Certificate("dsci551-test-project-firebase-adminsdk-lrct5-9425caf0b2.json")
        firebase_admin.initialize_app(cred)

    3.  

'''