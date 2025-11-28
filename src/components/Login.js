import React, { useState } from 'react';
import { login } from '../api';

export default function Login({ onLogin }) {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [err, setErr] = useState(null);

  const submit = async e => {
    e.preventDefault();
    try {
      const data = await login(username, password);
      localStorage.setItem('token', data.token);
      onLogin();
    } catch (e) {
      setErr('Falha ao logar');
    }
  };

  return (
    <form onSubmit={submit}>
      <input placeholder="Usuário" value={username} onChange={e => setUsername(e.target.value)} />
      <input type="password" placeholder="Senha" value={password} onChange={e => setPassword(e.target.value)} />
      <button type="submit">Entrar</button>
      {err && <div>{err}</div>}
    </form>
  );
}
