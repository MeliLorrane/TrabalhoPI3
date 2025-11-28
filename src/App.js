import React, { useState } from 'react';
import Login from './components/Login';
import ListaPerfis from './components/ListaPerfis';
import MeusConvites from './components/MeusConvites';

function App() {
  const [autenticado, setAutenticado] = useState(!!localStorage.getItem('token'));

  function onLogout() {
    localStorage.removeItem('token');
    setAutenticado(false);
  }

  return (
    <div>
      {autenticado ? (
        <div>
          <button onClick={onLogout}>Sair</button>
          <ListaPerfis />
          <MeusConvites />
        </div>
      ) : (
        <Login onLogin={() => setAutenticado(true)} />
      )}
    </div>
  );
}

export default App;
