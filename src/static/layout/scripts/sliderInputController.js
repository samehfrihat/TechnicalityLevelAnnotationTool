let volumeSlider = document.getElementById('level_en');
let volumeSlider_de = document.getElementById('level_de');

function setEnglishAbstractTechnicalityLevel(wert) {
    document.getElementById('output_en').value = wert;
}

function setGermanAbstractTechnicalityLevel(wert) {
    document.getElementById('output_de').value = wert;
}


window.onload = function () {
    if (volumeSlider != null) {

        volumeSlider.addEventListener('input', function (event) {
            setEnglishAbstractTechnicalityLevel(event.target.value);
        });
        setEnglishAbstractTechnicalityLevel(volumeSlider.value);
    }
    if (volumeSlider_de != null) {
        volumeSlider_de.addEventListener('input', function (event) {
            setGermanAbstractTechnicalityLevel(event.target.value);
        });
        setGermanAbstractTechnicalityLevel(volumeSlider_de.value);
    }
}
