
if (m == "Wylogowano"){
    Swal.fire({
        icon: 'success',
        text: m,
        showConfirmButton: false,
        color: 'black',
        background: 'white',
        timer: 1000,
        showClass: {
                    popup: 'my-icon'                     
                    },
            });
    
}
else{
    Swal.fire({
        position: "top-centre",
        icon: "success",
        title: m,
        showConfirmButton: false,
        timer: 1000,
        showClass: {
                    popup: 'my-icon'                     
                    },
            });
}

        
