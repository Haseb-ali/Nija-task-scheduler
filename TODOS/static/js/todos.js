function doLogin(){
    useremail=document.getElementById("useremail").value;
    password=document.getElementById("password").value;
    var req=new XMLHttpRequest();
    url="/login?useremail="+useremail+"&"+"password="+password;
    req.onreadystatechange=function(){
        if(this.readyState==4 && this.status==200){

        }
    }
    req.open("GET",url,true);
    req.send();



}

function fetchAll(){
    // alert("fetch all");
    var req=new XMLHttpRequest;
    req.onreadystatechange=function(){
        if(req.readyState==4 && req.status==200){
            var data=eval(this.responseText);
            console.log(data);
        }
    }
    req.open("GET",'/fetchall',true);
    req.send();
}   


function loadData(param){
    todoId=param.value
    var url='/fetchrecord?todoId='+todoId;
    var req=new XMLHttpRequest;
    req.onreadystatechange=function(){
        if(this.readyState==4 && this.status==200){
            let data=eval(req.responseText);
            let todoTextField=document.getElementById("updatedTodoText");
            todoTextField.value=data[0].todo_text;
            document.getElementById("hidetodoId").value=data[0].todo_id;
            console.log(data[0].todo_text);
            console.log(data[0].todo_priporty);
            console.log(todoTextField);
           
        }
    }
    req.open("GET",url,true)
    req.send();
}
function saveChanges(){
       todo_id=document.getElementById("hidetodoId").value;
       todo_text=document.getElementById("updatedTodoText").value;
       todo_priporty=""
       let normal=document.getElementById("normal");
       let high=document.getElementById("high");
       let none=document.getElementById("none");
       if(normal.checked){
        todo_priporty="normal";
       }
       else if (high.checked){
        todo_priporty="high";
       }
       else if(none.checked){
        todo_priporty="none";
       }
       else{
        todo_priporty="normal";
       }
       url="/savechanges?todo_id="+todo_id+"&"+"todo_text="+todo_text+"&"+"todo_priporty="+todo_priporty;
       var req=new XMLHttpRequest;
       req.onreadystatechange=function(){
           if(this.readyState==4 && this.status==200){
            document.getElementById("aalert").classList.remove("d-none");
            document.getElementById("aalert").classList.remove("alert-danger");
            document.getElementById("aalert").classList.add("alert-info");
            document.getElementById("updateResponse").innerHTML=this.responseText;
        }
        else{
            document.getElementById("aalert").classList.remove("d-none");
            document.getElementById("aalert").classList.remove("alert-info");
            document.getElementById("aalert").classList.add("alert-danger");
            document.getElementById("updateResponse").innerHTML=this.responseText;
        }
       }
       req.open("GET",url,true);
       req.send();
}
function reloadPage(){
    location.reload();
}
function confirmDelete(){
    event.preventDefault();
    var forms=event.target.form;
    options={}
    swal({
        title: "Are you sure?",
        text: "Once deleted, you will not be able to recover this TODO!",
        icon: "warning",
        buttons: true,
        dangerMode: true,
      })
      .then((willDelete) => {
        if (willDelete) {
            forms.submit();      
        } else {
        }
      });

}
