// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getStorage } from "firebase/storage";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyDXcI8UcEJj9aDCanalHdkfwfTL80zqu9A",
  authDomain: "ontime-74e2f.firebaseapp.com",
  projectId: "ontime-74e2f",
  storageBucket: "ontime-74e2f.appspot.com",
  messagingSenderId: "18900135127",
  appId: "1:18900135127:web:8dd121b0017d68e41f5492",
  measurementId: "G-ERXJSX1YJF"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
export const storage = getStorage(app);


// import { initializeApp } from "firebase/app";
// import { getStorage } from "firebase/storage";
// const firebaseConfig = {
//   apiKey: "AIzaSyCe8-IJKGUd-yXoYR0xQKMdSuIv5YsznDE",
//   authDomain: "fileuploads-be0db.firebaseapp.com",
//   projectId: "fileuploads-be0db",
//   storageBucket: "fileuploads-be0db.appspot.com",
//   messagingSenderId: "832032829361",
//   appId: "1:832032829361:web:f2079f619d4aad32ae9790",
// };

// // Initialize Firebase
// const app = initializeApp(firebaseConfig);
// export const storage = getStorage(app);
