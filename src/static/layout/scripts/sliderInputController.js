let volumeSlider = document.getElementById('level_en');
let volumeSlider_de = document.getElementById('level_de');

let readabilityVolumeSlider_de = document.getElementById('readability_level_de');
let readabilityVolumeSlider = document.getElementById('read_level_en');




function setEnglishAbstractTechnicalityLevel(wert) {
    document.getElementById('output_en').value = wert;
}
function setGermanAbstractTechnicalityLevel(wert) {
    document.getElementById('output_de').value = wert;
}

function setGermanAbstractReadabilityLevel(wert) {
    document.getElementById('readability_output_de').value = wert;
}
function setEnglishAbstractReadabilityLevel(wert) {
    document.getElementById('readability_output_en').value = wert;
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
    if (readabilityVolumeSlider_de != null) {
        readabilityVolumeSlider_de.addEventListener('input', function (event) {
            setGermanAbstractReadabilityLevel(event.target.value);
        });
        setGermanAbstractReadabilityLevel(readabilityVolumeSlider_de.value);
    }

    if (readabilityVolumeSlider != null) {
        readabilityVolumeSlider.addEventListener('input', function (event) {
            setEnglishAbstractReadabilityLevel(event.target.value);
        });
        setEnglishAbstractReadabilityLevel(readabilityVolumeSlider.value);
    }


}
