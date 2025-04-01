// Password Toggle Function
function togglePassword() {
    let passwordInput = document.getElementById("password");
    let toggleIcon = document.querySelector(".toggle-password");

    if (passwordInput.type === "password") {
        passwordInput.type = "text";
        toggleIcon.textContent = "🙈"; // Change icon when visible
    } else {
        passwordInput.type = "password";
        toggleIcon.textContent = "👁"; // Change back to eye icon
    }
}

// Form Validation
document.getElementById("loginForm").addEventListener("submit", function(event) {
    event.preventDefault();

    let username = document.getElementById("username").value.trim();
    let password = document.getElementById("password").value.trim();
    let userError = document.getElementById("userError");
    let passError = document.getElementById("passError");

    userError.style.display = "none";
    passError.style.display = "none";

    if (username === "") {
        userError.textContent = "Username is required!";
        userError.style.display = "block";
        return;
    }

    if (password === "") {
        passError.textContent = "Password is required!";
        passError.style.display = "block";
        return;
    }

    // Simulate Backend Request (Future)
    setTimeout(() => {
        // Simulating login success
        
        window.location.href = "farmer dashboard.html"; // Redirect after login (replace with actual URL)
    }, 1000);
});
