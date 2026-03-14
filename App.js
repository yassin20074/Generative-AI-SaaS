import { useState } from "react";

function App() {
  const [prompt, setPrompt] = useState("");
  const [url, setUrl] = useState("");

  const generateText = async () => {
    const form = new FormData();
    form.append("prompt", prompt);
    const res = await fetch("http://localhost:8000/generate-text/", {
      method: "POST",
      body: form
    });
    const data = await res.json();
    setUrl(data.s3_url);
  };

  return (
    <div className="App">
      <h1>AI Content Studio</h1>
      <textarea onChange={e => setPrompt(e.target.value)} />
      <button onClick={generateText}>Generate Text</button>
      {url && <p>Download: <a href={url}>{url}</a></p>}
    </div>
  );
}

export default App;
