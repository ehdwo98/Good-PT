const recordButton = document.querySelector('.record-button');
const stopButton = document.querySelector('.stop-button');
const playButton = document.querySelector('.play-button');
const previewPlayer = document.querySelector('#preview');
const recordingPlayer = document.querySelector('#recording');
let recorder;
let recordedChunks;
let recordedBlob;
const analyzeButton = document.querySelector('.analyze-button');

window.onload = () => {
    navigator.mediaDevices
        .getUserMedia({ video: true, audio: true })
        .then((stream) => {
            previewPlayer.srcObject = stream;
        })
        .catch((error) => {
            console.error('Error accessing camera:', error);
        });
};

function videoStart(event) {
    previewPlayer.srcObject.getTracks().forEach((track) => track.stop());
    navigator.mediaDevices.getUserMedia({ video: true, audio: true }).then((stream) => {
        previewPlayer.srcObject = stream;
        startRecording(previewPlayer.captureStream());
    });

    recordButton.style.display = 'none';
    playButton.style.display = 'none';
    stopButton.style.display = 'inline';
    recordingPlayer.style.display = 'none';
    analyzeButton.style.display = 'none';
    previewPlayer.style.display = 'inline';
}
function startRecording(stream) {
    recordedChunks = [];
    recorder = new MediaRecorder(stream, {
        mimeType: 'video/webm; codecs=vp9,opus',
    });
    recorder.ondataavailable = (e) => {
        recordedChunks.push(e.data);
    };
    recorder.start();
}
function stopRecording() {
    previewPlayer.srcObject.getTracks().forEach((track) => track.stop());
    recorder.stop();

    recordButton.style.display = 'inline';
    playButton.style.display = 'inline';
    stopButton.style.display = 'none';
    recordingPlayer.style.display = 'inline';
    previewPlayer.style.display = 'none';
    analyzeButton.style.display = 'inline';
}
function playRecording() {
    recordedBlob = new Blob(recordedChunks, { type: 'video/webm' });
    console.log(recordedBlob);
    recordingPlayer.src = URL.createObjectURL(recordedBlob);
    recordingPlayer.play();

    console.log(recordingPlayer.src);
}

function sendRecording() {
    let recordedBlob = new Blob(recordedChunks, { type: 'video/webm' });
    const data = new FormData();
    data.append('recordedData', recordedBlob);
    fetch('', {
        method: 'post',
        headers: {
            'X-CSRFToken': getCSRFToken(),
            enctype: 'multipart/form-data',
        },
        body: data,
    })
        .then((res) => {
            return res.json();
        })
        .then((json)=>answerTTSJsonCallback(json))
        .catch((err) => {
            console.log(err);
        });
}
function getCSRFToken() {
    const cookieValue = document.cookie
        .split('; ')
        .find((row) => row.startsWith('csrftoken='))
        .split('=')[1];

    return cookieValue;
}

function answerTTSJsonCallback(json){

    if(json.feedbackData){
        let GPTconsole = document.querySelector('#response');

        let questionList = json.feedbackData[1]
        let mystt = json.feedbackData[0]

        let answer = document.createElement('p');
        answer.innerText = mystt;
        GPTconsole.appendChild(answer);
        console.log(answer)

        let question = document.createElement('p');
        question.innerText = questionList;
        GPTconsole.appendChild(question);
        console.log(question)
        const audio2 = new Audio("http://localhost:8000/media/tmp/question.mp3")
        audio2.play()
    }
    else if(json.redirect){
        window.location.href = '/report';

    }


}

recordButton.addEventListener('click', videoStart);
stopButton.addEventListener('click', stopRecording);
playButton.addEventListener('click', playRecording);
analyzeButton.addEventListener('click', sendRecording);

const pmodalBackground = document.querySelector('.pmodal-background');
pmodalBackground.addEventListener('click', () => {
    pmodalBackground.style.display = 'none';
});

var SpeechRecognition = SpeechRecognition || webkitSpeechRecognition;
var SpeechGrammarList = SpeechGrammarList || webkitSpeechGrammarList;
var SpeechRecognitionEvent = SpeechRecognitionEvent || webkitSpeechRecognitionEvent;
var diagnosticPara = document.querySelector('.output');
function sendSpeech() {
    var recognition = new SpeechRecognition();
    var speechRecognitionList = new SpeechGrammarList();
    recognition.grammars = speechRecognitionList;
    recognition.lang = 'ko-KR';
    recognition.interimResults = false; // true: 중간 결과를 반환, false: 최종 결과만 반환
    recognition.continious = false; // true: 음성인식을 계속해서 수행, false: 음성인식을 한번만 수행
    recognition.maxAlternatives = 1;

    recognition.start();

    recognition.onresult = function (event) {
        var speechResult = event.results[0][0].transcript.toLowerCase();
        console.log('Confidence: ' + event.results[0][0].confidence);
        console.log('Speech Result: ' + speechResult);
        diagnosticPara.textContent = 'Speech received: ' + speechResult + '.';
    };

    recognition.onaudiostart = function (event) {
        //Fired when the user agent has started to capture audio.
        console.log('SpeechRecognition.onaudiostart');
    };

    recognition.onaudioend = function (event) {
        //Fired when the user agent has finished capturing audio.
        console.log('SpeechRecognition.onaudioend');
    };

    recognition.onend = function (event) {
        //Fired when the speech recognition service has disconnected.
        console.log('SpeechRecognition.onend');
    };

    recognition.onnomatch = function (event) {
        //Fired when the speech recognition service returns a final result with no significant recognition. This may involve some degree of recognition, which doesn't meet or exceed the confidence threshold.
        console.log('SpeechRecognition.onnomatch');
    };

    recognition.onsoundstart = function (event) {
        //Fired when any sound — recognisable speech or not — has been detected.
        console.log('SpeechRecognition.onsoundstart');
    };

    recognition.onsoundend = function (event) {
        //Fired when any sound — recognisable speech or not — has stopped being detected.
        console.log('SpeechRecognition.onsoundend');
    };

    recognition.onspeechstart = function (event) {
        //Fired when sound that is recognised by the speech recognition service as speech has been detected.
        console.log('SpeechRecognition.onspeechstart');
    };
    recognition.onstart = function (event) {
        //Fired when the speech recognition service has begun listening to incoming audio with intent to recognize grammars associated with the current SpeechRecognition.
        console.log('SpeechRecognition.onstart');
    };
}
