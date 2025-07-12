const express = require('express');
const fs = require('fs');
const path = require('path');
const app = express();
const port = 3001;

app.use(express.urlencoded({ extended: true }));
app.use(express.static(path.join(__dirname)));

app.post('/login', (req, res) => {
  const { username, password } = req.body;
  const users = JSON.parse(fs.readFileSync('users.json'));

  const user = users.find(u => u.username === username && u.password === password);

  if (user) {
    res.send(`<h2>登入成功，歡迎 ${username}！</h2>`);
  } else {
    res.send('<h2>登入失敗，帳號或密碼錯誤</h2>');
  }
});

app.listen(port, () => {
  console.log(`伺服器啟動：http://localhost:${port}/login.html`);
});
