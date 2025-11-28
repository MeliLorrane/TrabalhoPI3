const API_BASE = "http://localhost:8000/api";

function authHeaders() {
  const token = localStorage.getItem('token');
  return token ? { 'Authorization': `Token ${token}` } : {};
}

export async function login(username, password) {
  const res = await fetch(`${API_BASE}/login/`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ username, password })
  });
  if (!res.ok) throw new Error('Erro ao autenticar');
  return res.json();
}

export async function register(data) {
  const res = await fetch(`${API_BASE}/register_user/`, { // ver rota custom conforme backend
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data)
  });
  return res.json();
}

export async function listarPerfis() {
  const res = await fetch(`${API_BASE}/perfis/`, { headers: { ...authHeaders() }});
  return res.json();
}

export async function meuPerfil() {
  const res = await fetch(`${API_BASE}/perfil/`, { headers: { ...authHeaders() }});
  return res.json();
}

export async function enviarConvite(perfilId) {
  const res = await fetch(`${API_BASE}/convites/enviar/${perfilId}/`, {
    method: 'POST',
    headers: { ...authHeaders() }
  });
  return res.json();
}

export async function listarConvites() {
  const res = await fetch(`${API_BASE}/convites/`, { headers: { ...authHeaders() }});
  return res.json();
}

export async function aceitarConvite(conviteId) {
  const res = await fetch(`${API_BASE}/convites/aceitar/${conviteId}/`, {
    method: 'POST',
    headers: { ...authHeaders() }
  });
  return res.json();
}
