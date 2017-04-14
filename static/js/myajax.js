function myAjax(url,command,success,error){
    $.ajax(
        {
            url:url,
            type:"post",
            data:command,
            async:false,
            success:success,
            error:error
        }
    )
}