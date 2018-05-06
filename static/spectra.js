$(document).ready(() => {
  console.log('FE image ready')
  $('#textInputPoints').text($('#points').val())
  $('#textInputTime').text($('#time').val())

  $('#inputFiles').change(function(e) {
    //inputFiles is JS iterable object, we can call Array.from and
    //transform it to array and call map to get name
    const filenames = Array.from($(this)[0].files).map(f => f.name)
    console.log("files:", filenames)
    $('#selectedFiles').empty()
    if (filenames.length > 1) {
      for (filename of filenames) {
        $('#selectedFiles').append(`<p>${filename}</p>`)
      }
    }
  })

  $('#points').change((e) => {
    console.log(e.target.value, 'Points slider changed')
    $('#textInputPoints').text(e.target.value)
  })

  $('#time').change((e) => {
    console.log(e.target.value, 'Time slider changed')
    $('#textInputTime').text(e.target.value)
  })

  $("#postForm").submit(function(e) {
    e.preventDefault()
    const formData = new FormData($(this)[0]);
    console.log('Show button clicked', formData)
    $.ajax({
      url: 'spectra/show',
      type: 'POST',
      data: formData,
      cache: false,
      contentType: false,
      enctype: 'multipart/form-data',
      processData: false,
      success: (response) => {
        console.log(response)
        $("#plotImg").attr("src", response.image)
        console.log($("#plotImg").attr("src"))
      },
      error: (err) => {
        alert('err', err)
      }
    })
  })
})
