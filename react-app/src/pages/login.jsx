import { useState, useEffect, useRef } from "react";
import { useNavigate } from "react-router-dom";
import { motion, AnimatePresence } from "framer-motion";
import "../index.css";
import axios from "axios";

import NET from "vanta/dist/vanta.net.min";
import * as THREE from "three";


export default function Login() {
  const [page,setPage] = useState("");
  const [username,setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const navigate = useNavigate();
  const API_URL = "http://127.0.0.1:8000"

   // Ref pour Vanta
   const vantaRef = useRef(null);
   const [vantaEffect, setVantaEffect] = useState(null);
 
   // Initialisation de Vanta
   useEffect(() => {
     if (!vantaEffect) {
       setVantaEffect(
         NET({
           el: vantaRef.current,
           THREE,
           mouseControls: true,
           touchControls: true,
           gyroControls: false,
           minHeight: 200.0,
           minWidth: 200.0,
           scale: 1.0,
           scaleMobile: 1.0,
           color: 0x553fff
         })
       );
     }
     return () => {
       if (vantaEffect) vantaEffect.destroy();
     };
   }, [vantaEffect]);
  
  // =========================================
  //login request


  const handleLogin = async () => {
    try {
      const response = await axios.post(`${API_URL}/login`,{
        username,      
        password,
      });
  
      const { token } = response.data;
  
      localStorage.setItem("authToken", token);
      alert("Login réussi !");
      navigate("/dashboard");

    } catch (error) {
      if (error.response && error.response.status === 401) {
        alert("Identifiants incorrects !");
      } else {
        alert("Erreur serveur !");
      }
    }
  };

//Signup request
  const handleSignup = async () => {
    try {
      const response = await axios.post(`${API_URL}/register`,{
        username,
        email,
        password,
      });

      alert("Inscription réussie !");
    } catch (error) {
      if (error.response && error.response.status === 400) {
        alert("Utilisateur existe déjà.");
     } else {
        alert("Erreur serveur !");
      }
   }
  };

  return (
    
    <div className="main" ref={vantaRef}>
      <div className="card">

        <div className="switch">
          <button className="button-left" onClick={() => setPage("login")} >Login</button>
          <button className="button-right" onClick={() => setPage("signup")} >Signup</button>
        </div>

        <div className="title">
          <h2>MaribenTranslate</h2>
          <h4>Break Language Barriers in Seconds</h4>
        </div>

        <AnimatePresence mode="wait">
          {page === "login" && (
            <motion.div
              key="login"
              initial={{ opacity: 0, x: -50 }}
              animate={{ opacity: 1, x: 0 }}
              exit={{ opacity: 0, x: 50 }}
              transition={{ duration: 0.35 }}
              className="content"
            >
              <h2>Login</h2>
              <input 
              placeholder="Username"
              value={username}
              onChange={(e) => setUsername(e.target.value)} />
              
              <input 
              placeholder="Password" 
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)} 
              />
              <button className="btn" onClick={handleLogin}>Login</button>
            </motion.div>
          )}

          {page === "signup" && (
            <motion.div
              key="signup"
              initial={{ opacity: 0, x: 50 }}
              animate={{ opacity: 1, x: 0 }}
              exit={{ opacity: 0, x: -50 }}
              transition={{ duration: 0.35 }}
              className="content transparent"
            >
              <h2>Signup</h2>
              <input 
              placeholder="Username" 
              value={username}
              onChange={(e) => setUsername(e.target.value)} 
              />
              <input 
              placeholder="Email" 
              value={email}
              onChange={(e) => setEmail(e.target.value)} 
              />
              <input 
              placeholder="Password" 
              type="password" 
              value={password}
              onChange={(e) => setPassword(e.target.value)} />

              <button className="btn" onClick={handleSignup}>Signup</button>

            </motion.div>
          )}
        </AnimatePresence>
      </div>
    </div>
  );
}