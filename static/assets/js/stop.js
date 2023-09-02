// document.addEventListener('keydown', function(event) {
//   if (event.ctrlKey && (event.key === 'U' || event.key === 'u')) {
//     event.preventDefault(alert('He bich nmaga bu kodini ko\'rishga harakat qilyapsan😆🤌'));
//     return false;
//   }
// });


// Foydalanuvchi HTML manzilini ko'rishni qada qo'yish
    window.addEventListener("keydown", function(e) {
        if (e.ctrlKey && e.key === "u") {
            e.preventDefault();
            // Foydalanuvchini boshqa sahifaga yo'naltirish
            window.location.href = "https://shohbozbek.uz/uz";
        }
    });

