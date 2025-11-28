import React, { useEffect, useState } from 'react';
import { listarConvites, aceitarConvite } from '../api';

export default function MeusConvites() {
  const [convites, setConvites] = useState([]);

  useEffect(() => { fetchConvites(); }, []);

  async function fetchConvites() {
    const data = await listarConvites();
    setConvites(data);
  }

  async function handleAceitar(id) {
    await aceitarConvite(id);
    fetchConvites();
  }

  return (
    <div>
      <h3>Meus Convites</h3>
      {convites.map(c => (
        <div key={c.id}>
          <div>De: {c.solicitante.user.first_name} {c.solicitante.user.last_name}</div>
          <button onClick={() => handleAceitar(c.id)}>Aceitar</button>
        </div>
      ))}
    </div>
  );
}
