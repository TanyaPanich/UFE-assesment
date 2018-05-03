$(document).ready(() => {
  console.log('Test document ready')
  const button = $('#ndbel').text()
  console.log('button', button)

  // $('#ndbel').click(event => {
  //   event.preventDefault()
  //   let requestParams = {
  //     type: 'POST'
  //     data: {
  //       button
  //     },
  //     url: '/test'
  //   }
  //
  //   $.ajax(requestParams){
  //     done((data) => {
  //       window.location.href = '/test'
  //     })
  //     .fail(($xhr) => {
  //       console.log('Error adding a bike')
  //     })
  //   }
  // })
})
