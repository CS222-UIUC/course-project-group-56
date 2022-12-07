import "./App.css";
import { useState, useEffect } from "react";
import {
  ref,
  uploadBytes,
  getDownloadURL,
  listAll,
  list,
} from "firebase/storage";
import { storage } from "./firebase";
import { v4 } from "uuid";
import React from "react";


function App() {
  const [pdfUpload, setPdfUpload] = useState(null);
  const [imageUrls, setImageUrls] = useState([]);

  const pdfListRef = ref(storage, "scheudles/");
  const uploadFile = () => {
    if (pdfUpload == null) return;
    const pdfRef = ref(storage, `schedules/${pdfUpload.name + v4()}`);
    uploadBytes(pdfRef, pdfUpload).then((/*snapshot*/) => {
      // getDownloadURL(snapshot.ref).then((url) => {
      //   setImageUrls((prev) => [...prev, url]);
      // });
    });
  };

  // useEffect(() => {
  //   listAll(pdfListRef).then((response) => {
  //     response.items.forEach((item) => {
  //       getDownloadURL(item).then((url) => {
  //         setImageUrls((prev) => [...prev, url]);
  //       });
  //     });
  //   });
  // }, []);

  return (
    <div className="App">
      <input
        type="file"
        onChange={(event) => {
          setPdfUpload(event.target.files[0]);
        }}
      />
      <button onClick={uploadFile}> Upload PDF</button>
      {/* {imageUrls.map((url) => {
        return <img src={url} />;
      })} */}
    </div>
  );
}

export default App;
