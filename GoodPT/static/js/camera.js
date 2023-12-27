const recordButton = document.querySelector(".record-button");
const stopButton =document.querySelector(".stop-button");
const playButton =document.querySelector(".play-button");
// const downloadButton =document.querySelector(".download-button"); 
const previewPlayer = document.querySelector("#preview");
const recordingPlayer = document.querySelector("#recording"); let recorder;let recordedChunks; //functionsfunction videoStart() {    navigator.mediaDevices.getUserMedia({ video:true,audio:true })    .then(stream => {        previewPlayer.srcObject = stream;        startRecording(previewPlayer.captureStream())    })    } function startRecording(stream) {    recordedChunks=[];    recorder = new MediaRecorder(stream);    recorder.ondataavailable = (e)=>{ recordedChunks.push(e.data) }    recorder.start();} function stopRecording() {    previewPlayer.srcObject.getTracks().forEach(track => track.stop());    recorder.stop();} function playRecording() {    const recordedBlob = new Blob(recordedChunks, {type:"video/webm"});    recordingPlayer.src=URL.createObjectURL(recordedBlob);    recordingPlayer.play();    downloadButton.href=recordingPlayer.src;    downloadButton.download =`recording_${new Date()}.webm`;    console.log(recordingPlayer.src);} //eventrecordButton.addEventListener("click",videoStart);stopButton.addEventListener("click",stopRecording);playButton.addEventListener("click",playRecording);
 
function videoStart(event) {    
	navigator.mediaDevices.getUserMedia({ video:true,audio:true })
		.then(stream => {        
			previewPlayer.srcObject = stream;        
			startRecording(previewPlayer.captureStream())    })

    recordButton.style.display = 'none';
    playButton.style.display = 'none';
    stopButton.style.display = "inline";
    recordingPlayer.style.display = "none";
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
} 
function playRecording() {    
    const recordedBlob = new Blob(recordedChunks, {type:"video/webm"});
    console.log(recordedBlob)    
    recordingPlayer.src=URL.createObjectURL(recordedBlob);    
    recordingPlayer.play();    
    // downloadButton.href=recordingPlayer.src;    
    // downloadButton.download =`recording_${new Date()}.webm`;    
    console.log(recordingPlayer.src);
} 
//event
recordButton.addEventListener("click",videoStart);
stopButton.addEventListener("click",stopRecording);
playButton.addEventListener("click",playRecording);