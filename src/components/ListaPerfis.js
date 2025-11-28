import React, { useEffect, useState } from 'react';
import { listarPerfis, enviarConvite } from '../api';

export default function ListaPerfis() {
  const [perfis, setPerfis] = useState([]);

  useEffect(() => { fetchPerfis(); }, []);

  async function fetchPerfis() {
    const data = await listarPerfis();
    setPerfis(data);
  }

  async function handleConvidar(id) {
    await enviarConvite(id);
    fetchPerfis();
  }

  return (
    <div>
      <h3>Perfis</h3>
      {perfis.map(p => (
        <div key={p.id}>
          <div>{p.user.first_name} {p.user.last_name} - {p.user.email}</div>
          {p.pode_convidar ? <button onClick={() => handleConvidar(p.id)}>Convidar</button> : <span>Já contato</span>}
        </div>
      ))}
    </div>
  );
}
