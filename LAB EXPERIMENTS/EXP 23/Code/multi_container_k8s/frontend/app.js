const API="/api/tasks";
async function load(){try{const r=await fetch(API);const tasks=await r.json();document.querySelector("#tasks").innerHTML=tasks.map(t=>`<li class="${t.done?'done':''}"><span onclick="toggle(${t.id})">${t.title}</span><button onclick="del(${t.id})">Delete</button></li>`).join("");document.querySelector("#status").textContent="Connected to backend and database";}catch(e){document.querySelector("#status").textContent="Backend connection error";}}
document.querySelector("#form").addEventListener("submit",async e=>{e.preventDefault();await fetch(API,{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({title:document.querySelector("#title").value})});e.target.reset();load();});
async function toggle(id){await fetch(API+"/"+id,{method:"PATCH"});load();}
async function del(id){await fetch(API+"/"+id,{method:"DELETE"});load();}
load();