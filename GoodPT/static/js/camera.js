const recordButton = document.querySelector(".record-button");
const stopButton =document.querySelector(".stop-button");
const playButton =document.querySelector(".play-button");
// const downloadButton =document.querySelector(".download-button"); 
const previewPlayer = document.querySelector("#preview");
const recordingPlayer = document.querySelector("#recording"); 
let recorder;
let recordedChunks;
let recordedBlob
const analyzeButton = document.querySelector('.analyze-button')
function videoStart(event) {    
	navigator.mediaDevices.getUserMedia({ video:true,audio:true })
		.then(stream => {        
			previewPlayer.srcObject = stream;        
			startRecording(previewPlayer.captureStream())    })

    recordButton.style.display = 'none';
    playButton.style.display = 'none';
    stopButton.style.display = "inline";
    recordingPlayer.style.display = "none";
    analyzeButton.style.display = "none";
    previewPlayer.style.display = "inline";
    } 
function startRecording(stream) {    
    recordedChunks=[];    
    recorder = new MediaRecorder(stream, {        
        mimeType: 'video/webm; codecs=vp9,opus',    
    });
    recorder.ondataavailable = (e)=>{ 
    recordedChunks.push(e.data) }    
    recorder.start();
} 
function stopRecording() {    
    previewPlayer.srcObject.getTracks().forEach(track => track.stop());
    recorder.stop();

    recordButton.style.display = 'inline';
    playButton.style.display = 'inline';
    stopButton.style.display = "none";
    recordingPlayer.style.display = "inline";
    previewPlayer.style.display = "none";
    analyzeButton.style.display = "inline";

} 
function playRecording() {    
    recordedBlob = new Blob(recordedChunks, {type:"video/webm"});
    console.log(recordedBlob)    
    recordingPlayer.src=URL.createObjectURL(recordedBlob);    
    recordingPlayer.play();    
  
    console.log(recordingPlayer.src);
} 

function sendRecording() {
    let recordedBlob = new Blob(recordedChunks, { type: "video/webm" });
    const data = new FormData();
    data.append('recordedData', recordedBlob);
    fetch('', {
        method: 'post',
        headers: {
            "X-CSRFToken": getCSRFToken(),
            'enctype': 'multipart/form-data'
        },
        body: data
    })
        .then((res) => {return res.json()})
        .then(json => {
        })
        .catch(err => {
            console.log(err)
        });
}
function getCSRFToken() {
    const cookieValue = document.cookie
        .split('; ')
        .find(row => row.startsWith('csrftoken='))
        .split('=')[1];

    return cookieValue;
}

recordButton.addEventListener("click",videoStart);
stopButton.addEventListener("click",stopRecording);
playButton.addEventListener("click",playRecording);
analyzeButton.addEventListener("click",sendRecording);