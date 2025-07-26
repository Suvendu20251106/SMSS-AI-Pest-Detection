import { useState } from "react";
import { useTranslation } from 'react-i18next';

export default function App() {
  const [image, setImage] = useState(null);
  const [result, setResult] = useState(null);
  const { t, i18n } = useTranslation();

  const handleUpload = async (e) => {
    const file = e.target.files[0];
    setImage(URL.createObjectURL(file));
    setTimeout(() => {
      setResult({
        crop: "Maize",
        pest: "Fall Armyworm",
        severity: "High",
        suggestion: "Spray Emamectin Benzoate 5% SG"
      });
    }, 2000);
  };

  return (
    <div>
      <button onClick={() => i18n.changeLanguage('bn')}>বাংলা</button>
      <button onClick={() => i18n.changeLanguage('en')}>English</button>
      <h1>{t('title')}</h1>
      <input type="file" onChange={handleUpload} />
      {result && (
        <ul>
          <li>{t('crop')}: {result.crop}</li>
          <li>{t('pest')}: {result.pest}</li>
          <li>{t('severity')}: {result.severity}</li>
          <li>{t('suggestion')}: {result.suggestion}</li>
        </ul>
      )}
    </div>
  );
}
