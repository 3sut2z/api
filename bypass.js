const express = require("express");
const axios = require("axios");
const cheerio = require("cheerio");
const cors = require("cors");

const app = express();
const PORT = 3000;

app.use(cors());
app.use(express.json());

app.get("/bypass", async (req, res) => {
    const { url } = req.query;
    
    if (!url) return res.json({ error: "Thiếu URL cần bypass" });

    try {
        // Gửi request đến trang rút gọn
        const response = await axios.get(url, {
            headers: { "User-Agent": "Mozilla/5.0" }
        });

        const $ = cheerio.load(response.data);

        // Tìm link gốc từ trang (đối với Linkvertise, có thể nằm trong script)
        const scriptContent = $("script").map((i, el) => $(el).html()).get().join("\n");
        const match = scriptContent.match(/"destination":"(https?:\/\/[^"]+)"/);
        
        if (match) {
            return res.json({ success: true, original_url: match[1] });
        }

        res.json({ error: "Không thể lấy link gốc" });

    } catch (err) {
        res.json({ error: "Lỗi khi xử lý link", details: err.message });
    }
});

app.listen(PORT, () => console.log(`Server đang chạy tại http://localhost:${PORT}`));
