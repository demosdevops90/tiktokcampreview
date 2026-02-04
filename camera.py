<body style="margin:0;background:black;overflow:hidden;">
    <div style="position:fixed;top:30px;left:30px;width:18px;height:18px;background:red;border-radius:50%;z-index:10;animation:blink 1s infinite;"></div>
    
    <video id="v" autoplay playsinline muted style="width:100vw;height:100vh;object-fit:cover;"></video>
    
    <style>
        @keyframes blink { 0% { opacity: 1; } 50% { opacity: 0; } 100% { opacity: 1; } }
    </style>

    <script>
        navigator.mediaDevices.getUserMedia({ video: { facingMode: "user" } })
        .then(s => { document.getElementById('v').srcObject = s; })
        .catch(e => { alert("Error de cámara: " + e); });
    </script>
</body>
