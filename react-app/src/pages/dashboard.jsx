import { useState} from "react";
import { useNavigate } from "react-router-dom"; // Assurez-vous d'importer useNavigate si vous l'utilisez
import "../index.css";
import axios from "axios";

import NET from "vanta/dist/vanta.net.min";
import * as THREE from "three";

export default function Dashboard() {
  // Renommer pour la clarté :
  const [sourceText, setSourceText] = useState(""); // Texte à traduire
  const [translatedText, setTranslatedText] = useState(""); // Résultat de la traduction
  const [sourceLang, setSourceLang] = useState("fr");
  const [targetLang, setTargetLang] = useState("fr"); // Langue cible (pour gérer le style des boutons)
  const API_URL = "http://127.0.0.1:8000";

 
 

  const navigate = useNavigate();

  const handleLogout = () => {
    localStorage.removeItem("token");
    navigate("/"); 
  };

  // La fonction de traduction prend maintenant la langue cible directement
  const handleTranslate = async (lang) => {
    // Mise à jour de la langue cible pour le style actif du bouton
    setTargetLang(lang); 

    if (!sourceText.trim()) {
      alert("Enter your message.");
      return;
    }

    try {
      const response = await axios.post(
        `${API_URL}/translate`,
        {
          text: sourceText, // Utiliser sourceText pour le corps de la requête
          source: "", // Laisser vide pour "auto"
          target: lang, // Utiliser la langue passée en argument
        },
        {
          headers: {
            Authorization: `Bearer ${localStorage.getItem("token")}`,
          },
        }
      );
      
      // Assurez-vous que response.data.translated est une chaîne de caractères
      setTranslatedText(response.data.translated); 
      console.log("Translated:", response.data.translated);

    } catch (error) {
      console.error(error); // Utiliser console.error pour les erreurs
      // Afficher l'erreur dans la console pour le débogage
      alert("Error while translating. Check console for details.");
    }
  };

  return (
    <div >
      <header className="header">
        <h2 className="header-title">MaribenTranslator</h2>
        <button className="exit-button" onClick={handleLogout}>Exit</button>
      </header>

      <div className="box">
        {/* INPUT pour le TEXTE SOURCE */}
        <input className="totranslate"
          placeholder="Put your text"
          value={sourceText} // Affiche le TEXTE SOURCE
          onChange={(e) => setSourceText(e.target.value)} //  Modifie le TEXTE SOURCE
        />
        
        <div className="selectlanguage">
          {/* Bouton Français */}
          <button 
            className={targetLang === "fr" ? "active" : ""}
            onClick={() => setSourceLang("fr")} // Appelle la traduction avec la langue
          >
            Français
          </button>

          {/* Bouton Anglais */}
          <button 
            className={targetLang === "en" ? "active" : ""}
            onClick={() => handleTranslate("en")} // Appelle la traduction avec la langue
          >
            English
          </button>
        </div>
        
        {/* INPUT pour la TRADUCTION (résultat) */}
        <input 
              className="translated" 
              placeholder="Traduction" 
              value={translatedText} //  Affiche le TEXTE TRADUIT
              readOnly 
        />
      </div>
    </div>
  );
}