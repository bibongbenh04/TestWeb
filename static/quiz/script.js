const optionList = document.querySelector('.option-list');
const startBtn = document.querySelector('.start-btn');
const nextBtn = document.querySelector('.next-btn');
const backbtn = document.querySelector('.back-btn');
const popupInfo = document.querySelector('.popup-info');
const exitBtn = document.querySelector('.exit-btn'); 
const main = document.querySelector('.main'); 
const continueBtn = document.querySelectorAll('.popup-info .continue-btn');  
const quizSection = document.querySelector('.quiz-section');  
const quizBox = document.querySelector('.quiz-box');
const clock = document.querySelector('.clock');  
const resultBox = document.querySelector('.result-box');  
const retryBox = document.querySelector('.retry-btn');
const goHomeButton = document.querySelector('.goHome-btn'); 

//get Question 
var questionsDataText = document.getElementById('questions-data').textContent.slice(55);

var questions = JSON.parse(questionsDataText);
var questionsfillurl = questions;
var typeCategory = 'TEST_ONL';
// console.log(questions);
// Hàm xáo trộn mảng
function shuffleArray(array) {
    for (let i = array.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [array[i], array[j]] = [array[j], array[i]];
    }
}


startBtn.onclick = () => {
    popupInfo.classList.add('active');
    main.classList.add('active');
}

backbtn.onclick = () => {
    quizSection.classList.remove('active');   
    quizBox.classList.remove('active');   
    // after 1 second
    setTimeout(() => {
        popupInfo.classList.add('active');
        main.classList.add('active');
    }, 1000); 
}

exitBtn.onclick = () => {
    popupInfo.classList.remove('active'); 
    main.classList.remove('active');
}

goHomeButton.onclick = () => {
    quizSection.classList.remove('active');   
    quizBox.classList.remove('active');   
    resultBox.classList.remove('active');
    // after 1 second
    setTimeout(() => {
        popupInfo.classList.add('active');
        main.classList.add('active');
    }, 1000); 
}

shuffleArray(questionsfillurl);

continueBtn.forEach(btn => {
    // Xử lý cho từng nút tiếp tục ở đây
    btn.addEventListener('click', () => {
        const url = btn.getAttribute('data-url');
        typeCategory = btn.getAttribute('type');
        questionsfillurl = findQuizDataByUrl(url);
        if (!questionsfillurl) {
            console.error("Không tìm thấy dữ liệu bài thi cho môn học này.");
            return;
        }
        // console.log(questionsfillurl);
        shuffleArray(questionsfillurl);
        quizSection.classList.add('active');   
        quizBox.classList.add('active');   
        popupInfo.classList.remove('active'); 
        main.classList.remove('active');
        
        questionsCount = 0;
        questionsNum = 1;
        userScore = 0;
        
        showQuestion(0);
        questionCounter(1);
        headerScore();
    });
});


function findQuizDataByUrl(url) {
    let quizfillbyurl = new Array(); 
    for (const quiz of questions) {
        // console.log(quiz.url);
        if (quiz.url === url) {
            quizfillbyurl.push(quiz);
        }
    }
    // console.log(quizfillbyurl);
    if (quizfillbyurl.length == 0) return null;
    return quizfillbyurl;
}
// continueBtn.onclick = () => {
//     shuffleArray(questions);
//     quizSection.classList.add('active');   
//     quizBox.classList.add('active');   
//     popupInfo.classList.remove('active'); 
//     main.classList.remove('active');

//     questionsCount = 0;
//     questionsNum = 1;
//     userScore = 0;

//     showQuestion(0);
//     questionCounter(1);
//     headerScore();
// }

let countdownTime = 15;
let countdown;

function startCountdown() {
    countdown = setInterval(function() {
        countdownTime--;
        if (countdownTime < 0) {
            clearInterval(countdown);
            const nullOption = document.createElement('div');
            nullOption.classList.add('option');
            nullOption.textContent = 'null';
            optionSeleceted(nullOption); // Gọi hàm khi hết thời gian
            if(typeCategory == "CONTEST") {
                nextBtn.click();
                return;
            }
        } else {
            updateClock(countdownTime);
        }
    }, 1000);
}

function resetCountdown() {
    clearInterval(countdown);
    countdownTime = 15;
}

function updateClock(time) {
    let minutes = Math.floor(time / 60);
    let seconds = time % 60;

    let formattedTime = `${padZero(minutes)}:${padZero(seconds)}`;
    clock.innerHTML = formattedTime;
}

function padZero(number) {
    return number < 10 ? '0' + number : number;
}

nextBtn.onclick = () => {
    if (questionsCount >= questionsfillurl.length-1) {
        showResultBox();
        return;
    }
    nextBtn.classList.remove('active');
    showQuestion(++questionsCount);
    questionCounter(++questionsNum);
}

retryBox.onclick = () => {
    quizBox.classList.add('active');
    resultBox.classList.remove('active');
    nextBtn.classList.remove('active');
    
    questionsCount = 0;
    questionsNum = 1;
    userScore = 0;
    showQuestion(questionsCount);
    questionCounter(questionsNum);
    
    headerScore();
    shuffleArray(questionsfillurl);
}

let questionsCount = 0;
let questionsNum = 1;
let userScore = 0;
let correctChoice;
let answerCorrect;


function showQuestion(index) {
    resetCountdown();
    startCountdown();
    updateClock(countdownTime);
    const questionText = document.querySelector('.question-text');
    questionText.textContent = `Question ${index+1}: ${questionsfillurl[index].question_text} ?`;
    correctChoice = questionsfillurl[questionsCount].correctChoice;
    let option1234 = [questionsfillurl[index].option1, questionsfillurl[index].option2, questionsfillurl[index].option3, questionsfillurl[index].option4];
    answerCorrect = option1234[correctChoice-1];
    shuffleArray(option1234);
    // after suffle array, find the correct answer
    for (let i = 1; i <= 4; i++) {
        if(option1234[i-1] == answerCorrect) {
            correctChoice = i;
        }
    }
    let optionTag = `<div class="option"><span>A. ${option1234[0]}</span></div>
    <div class="option"><span>B. ${option1234[1]}</span></div>
    <div class="option"><span>C. ${option1234[2]}</span></div>
    <div class="option"><span>D. ${option1234[3]}</span></div>`;

    optionList.innerHTML = optionTag;

    const option = document.querySelectorAll('.option');
    for (let i = 0; i < option.length; i++) {
        option[i].setAttribute('onclick', 'optionSeleceted(this)');
    }
}

function optionSeleceted(answer) {
    resetCountdown();
    let userAnswer = answer.textContent[0].charCodeAt(0) - 'A'.charCodeAt(0) + 1;
    // correctChoice = questions[questionsCount].correctChoice;
    let allOptions = optionList.children.length;
    
    nextBtn.classList.add('active');

    if(userAnswer == correctChoice) {
        ++userScore;
        if(typeCategory == "CONTEST") {
            nextBtn.click();
            return;
        }
        answer.classList.add('correct');
        headerScore();
    } else {
        if(typeCategory == "CONTEST") {
            nextBtn.click();
            return;
        }
        answer.classList.add('incorrect');

        for (let i = 0; i < allOptions; i++) {
            if  (optionList.children[i].textContent[0].charCodeAt(0) - 'A'.charCodeAt(0) + 1 == correctChoice) {
                optionList.children[i].setAttribute('class', 'option correct');
            }
        }
    }

    for (let i = 0; i < allOptions; i++) {
        optionList.children[i].classList.add('disabled');
    }

}

function questionCounter(index) {
    const questionTotal = document.querySelector('.question-total');
    questionTotal.textContent = `${index} of ${questionsfillurl.length} Questions`;
}

function headerScore() {
    const headerScoreText = document.querySelector('.header-score');
    headerScoreText.textContent = `Score: ${userScore} / ${questionsfillurl.length}`;
}

function showResultBox() {
    quizBox.classList.remove('active');
    resultBox.classList.add('active');

    const scoreText = document.querySelector('.score-text');
    const circularProgress = document.querySelector('.circular-progress');
    const progressValue = document.querySelector('.progress-value');
    let progressStartValue = -1;
    let progressEndValue = userScore/questionsfillurl.length*100;
    let speed = 20;

    scoreText.textContent = `Your Score: ${userScore} out of  ${questionsfillurl.length}`;

    let progress = setInterval(() => {
        progressStartValue++;
        progressValue.textContent = `${progressStartValue}%`;
        circularProgress.style.background = `conic-gradient(#ff00bf ${progressStartValue * 3.6 }deg, rgba(255, 255, 255, .1) 0deg)`;
        if (progressStartValue >= progressEndValue) {
            clearInterval(progress);
        }
    }, speed);
}

