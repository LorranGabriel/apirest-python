 // Your web app's Firebase configuration
 (function(){
    var firebaseConfig = {
        apiKey: "AIzaSyBA6toEeoJ4p3DTU1pEed1RFp6v0pAizdc",
        authDomain: "apirest-projeto.firebaseapp.com",
        databaseURL: "https://apirest-projeto.firebaseio.com",
        projectId: "apirest-projeto",
        storageBucket: "apirest-projeto.appspot.com",
        messagingSenderId: "501379351759",
        appId: "1:501379351759:web:1292e300f3f411ba7223ba"
      };
      // Initialize Firebase
      firebase.initializeApp(firebaseConfig);
      var fileButton =  document.getElementById('btnAtualizaDump');

      fileButton.addEventListener('click', e => {
            firebase.database().ref('/').once('value').then(function(snapshot) {
                var username = (snapshot.val());
                // ...
                console.log(username)
                var el_down = document.getElementById("GFG_DOWN"); 
                el_down.innerHTML = JSON.stringify(username, undefined, 4); 
            });

        });

 })();
