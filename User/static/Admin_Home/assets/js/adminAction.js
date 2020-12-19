$(document).ready(function () {
    $("#proceed_btn").click(function () {
        lang = $("#LangType").find(":selected").text()
        
        console.log(lang)
        $.ajax({
            
            url: '/Dashboard/getByLanguage/'+lang,
            type: 'GET', 
            dataType:'json'
          }).done(function(data){
            $("#listAcademicBody").empty()
              console.log(data[0])
        for (i = 0; i < data.length; i ++) {
                template = `
                         <tr>
                         <td>   ${i+1}</td>
                                <td>${data[i].fields['Name']}</td>
                                <td>${data[i].fields['Type']}</td>
                                <td>${data[i].fields['Language']}</td>
                                <td>${data[i].fields['Owner']}</td>
                                </tr>
                            
                         `
                         $("#listAcademicBody").append(template)
            }

        });
    });
});
 