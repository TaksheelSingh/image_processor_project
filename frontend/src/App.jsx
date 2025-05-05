import React, { useState } from "react";
import axios from "axios";
import { motion } from "framer-motion";

const App = () => {
  const [image, setImage] = useState(null);
  const [previewURL, setPreviewURL] = useState(null);
  const [processedURL, setProcessedURL] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleImageChange = (e) => {
    const file = e.target.files[0];
    if (file) {
      setImage(file);
      setPreviewURL(URL.createObjectURL(file));
      setProcessedURL(null);
    }
  };

  const applyFilter = async (filter) => {
    if (!image) return;
    setLoading(true);
    const formData = new FormData();
    formData.append("image", image);
    formData.append("filter", filter);

    try {
      const response = await axios.post("/process", formData, {
        responseType: "blob",
      });
      const resultBlob = new Blob([response.data], { type: "image/png" });
      const resultURL = URL.createObjectURL(resultBlob);
      setProcessedURL(resultURL);
    } catch (error) {
      console.error("Processing error:", error);
      alert("Error processing image.");
    }
    setLoading(false);
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-gray-900 to-gray-700 text-white font-sans">
      <header className="p-6 shadow-xl bg-black bg-opacity-40 backdrop-blur-lg">
        <h1 className="text-5xl font-extrabold text-center text-cyan-400 animate-pulse">
          AI Image Processor
        </h1>
        <p className="text-center mt-2 text-gray-300">
          Upload an image and enhance it with smart filters
        </p>
      </header>

      <main className="max-w-5xl mx-auto p-6 mt-10 bg-white bg-opacity-10 backdrop-blur-md rounded-2xl shadow-2xl">
        <div className="text-center mb-6">
          <input
            type="file"
            accept="image/*"
            onChange={handleImageChange}
            className="block w-full text-sm text-gray-200 file:mr-4 file:py-2 file:px-4 file:rounded-full file:border-0 file:text-sm file:font-semibold file:bg-cyan-600 file:text-white hover:file:bg-cyan-700 cursor-pointer"
          />
        </div>

        <div className="flex flex-wrap justify-center gap-4 mb-6">
          {["blur", "sharpen", "edge"].map((filter) => (
            <motion.button
              key={filter}
              whileHover={{ scale: 1.05 }}
              whileTap={{ scale: 0.95 }}
              onClick={() => applyFilter(filter)}
              className="bg-cyan-500 hover:bg-cyan-600 text-white px-6 py-2 rounded-full font-semibold shadow-lg transition-all"
            >
              {filter.toUpperCase()}
            </motion.button>
          ))}
        </div>

        {loading && (
          <div className="text-center text-cyan-400 text-lg animate-pulse">⏳ Processing...</div>
        )}

        <div className="flex flex-wrap justify-center items-start gap-12 mt-10">
          {previewURL && (
            <div className="text-center">
              <h3 className="text-xl font-semibold text-cyan-300 mb-2">Original Image</h3>
              <img
                src={previewURL}
                alt="Original"
                className="max-w-xs rounded-xl shadow-md border-2 border-cyan-400"
              />
            </div>
          )}

          {processedURL && (
            <div className="text-center">
              <h3 className="text-xl font-semibold text-green-300 mb-2">Processed Image</h3>
              <img
                src={processedURL}
                alt="Processed"
                className="max-w-xs rounded-xl shadow-md border-2 border-green-400"
              />
              <a
                href={processedURL}
                download="processed.png"
                className="inline-block mt-3 px-4 py-2 text-sm font-medium text-white bg-green-500 hover:bg-green-600 rounded-full"
              >
                ⬇ Download
              </a>
            </div>
          )}
        </div>
      </main>

      <footer className="mt-12 text-center text-sm text-gray-400 py-4">
        Made with ❤️ using React, Flask & OpenCV
      </footer>
    </div>
  );
};

export default App;
