const fetchButton = document.getElementById('fetch-button');
fetchButton.addEventListener('click', function() {
  fetch('/data')
  .then(response => response.json())
  .then(data => {
    const nameElement = document.getElementById('name');

    // Set the innerHTML of the element to the new data
    nameElement.innerHTML = data.name;
  });
});
  const recordButton = document.getElementById('record-button');

  recordButton.addEventListener('click', function() {
  recordButton.classList.toggle('clicked');
  value = 1;
  if (recordButton.classList.contains('clicked')) {
    value = "1"
  } else {
    value = "0"
  }

  fetch('/button-click', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ value: value })
    });
  });
const submitButton = document.getElementById('btn-submit');
submitButton.addEventListener('click', function() {
  dic = {}
  dic["location"] = document.getElementById("location").value
  dic["date"] = document.getElementById("date").value
  dic["time"] = document.getElementById("time").value
  dic["firstName"] = document.getElementById("firstName").value
  dic["lastName"] = document.getElementById("lastName").value
  dic["idNumber"] = document.getElementById("idNumber").value
  dic["medicName"] = document.getElementById("medicName").value
  dic["ticketNumber"] = document.getElementById("ticketNumber").value
  dic["age"] = document.getElementById("age").value
  dic["sex"] = document.getElementById("sex").value
  dic["address"] = document.getElementById("address").value
  dic["telephone"] = document.getElementById("telephone").value
  dic["mainConcern"] = document.getElementById("mainConcern").value
  dic["scenarioDetailed"] = document.getElementById("scenarioDetailed").value
  dic["breathsPerMinuteTime1"] = document.getElementById("breathsPerMinuteTime1").value
  dic["breathsPerMinuteTime2"] = document.getElementById("breathsPerMinuteTime2").value
  dic["importantmetrics"] = document.getElementById("importantmetrics").value
  dic["consciencenesslevel1"] = document.getElementById("consciencenesslevel1").value
  dic["consciencenesslevel2"] = document.getElementById("consciencenesslevel2").value
  dic["breathingstatus1"] = document.getElementById("breathingstatus1").value
  dic["breathingstatus2"] = document.getElementById("breathingstatus2").value
  dic["saturation1"] = document.getElementById("saturation1").value
  dic["saturation2"] = document.getElementById("saturation2").value
  dic["pulsesserminute1"] = document.getElementById("pulsesserminute1").value
  dic["pulsesperminute2"] = document.getElementById("pulsesperminute2").value
  dic["strengthofpulse1"] = document.getElementById("strengthofpulse1").value
  dic["strengthofpulse2"] = document.getElementById("strengthofpulse2").value
  dic["pulseregularity1"] = document.getElementById("pulseregularity1").value
  dic["pulseregularity2"] = document.getElementById("pulseregularity2").value
  dic["systolicbloodpressure1"] = document.getElementById("systolicbloodpressure1").value
  dic["systolicbloodpressure2"] = document.getElementById("systolicbloodpressure2").value
  dic["diastolicbloodpressure1"] = document.getElementById("diastolicbloodpressure1").value
  dic["diastolicbloodpressure2"] = document.getElementById("diastolicbloodpressure2").value
  dic["glucosetest1"] = document.getElementById("glucosetest1").value
  dic["glucosetest2"] = document.getElementById("glucosetest2").value
  dic["allergies"] = document.getElementById("allergies").value
  dic["temperaturepopr1"] = document.getElementById("temperaturepopr1").value
  dic["temperaturepopr2"] = document.getElementById("temperaturepopr2").value
  dic["treatmentsgiven"] = document.getElementById("treatmentsgiven").value
  dic["alsleveltreatments"] = document.getElementById("alsleveltreatments").value
  dic["alsdrugtherapy"] = document.getElementById("alsdrugtherapy").value
  dic["methodofevacuation"] = document.getElementById("methodofevacuation").value
  dic["evacuationdestination"] = document.getElementById("evacuationdestination").value
  dic["reasonforreferral"] = document.getElementById("reasonforreferral").value
  dic["patientnameanddriversnumber"] = document.getElementById("patientnameanddriversnumber").value
  dic["attendingdoctorandliscencenumber"] = document.getElementById("attendingdoctorandliscencenumber").value
  dic["signature"] = document.getElementById("signature").value
  dic["namerefusalofhospitalization"] = document.getElementById("namerefusalofhospitalization").value
  dic["idrefusalofhospitalization"] = document.getElementById("idrefusalofhospitalization").value
  dic["signaturerefusalofhospitalization"] = document.getElementById("signaturerefusalofhospitalization").value
  dic["currentlocation"] = document.getElementById("currentlocation").value

});
  fetch('/submit', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ value: dic })
  });

  (function () {
$(document).on('click', '.btn-submit', function() {
if(!$(this).hasClass('loading')){
  $(this).addClass('loading');
  let self = this;
  
  setTimeout(function() {
    $(self).removeClass('loading');
    $(self).addClass('checked');
  },1500);
  
  setTimeout(function() {
    $(self).removeClass('checked');
  }, 3000);
}
});
})();