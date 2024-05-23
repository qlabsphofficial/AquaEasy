<template>
    <div id="questions-container">
        <h1>FAQs</h1>

        <div id="all-questions">
            <div class="question">
                <h3>How does the app collect water quality data?</h3>
                <p>
                    The app collects data from various sensors strategically placed in water bodies. 
                    These sensors measure parameters such as pH, temperature, dissolved oxygen, and more.
                    The collected data is then processed and displayed in the app.
                </p>
            </div>

            <div class="question">
                <h3>Is the water quality information accurate and reliable?</h3>
                <p>
                    Yes, the app uses sensors and technologies to ensure accurate and reliable water quality data.
                     Regular calibrations and quality checks are performed to maintain the accuracy of the information.
                </p>
            </div>

            <div class="question">
                <h3>Can I view historical water quality data?</h3>
                <p>
                    Yes, the app allows users to access historical water quality data.
                     You can view trends over time, compare different periods, and analyze changes in water quality.
                </p>
            </div>

            <div class="question">
                <h3>How frequently is the data updated in the app?</h3>
                <p>
                    The app provides real-time data updates, ensuring that users have access to the latest information about water quality.
                </p>
            </div>

            <div class="question">
                <h3>What actions should I take if I receive a water quality alert?</h3>
                <p>             
                    If you receive a water quality alert, consider adjusting your plans based on the app's recommendations.
                     The alert may provide insights on conditions affecting fish behavior or the quality of the fishing experience.
                </p>
            </div>

            <div class="question">
                <h3>How can I report issues or provide feedback about the app?</h3>
                <p>
                    Users can report issues, offer feedback, or suggest improvements by using the app's built-in feedback feature or by contacting
                     our support team through the provided channels on the app.
                </p>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'FaqPage'
}
</script>

<style scoped lang="scss">
#questions-container {
    text-align: left;
    height: 80%;
    width: 80%;
}

#all-questions {
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    justify-content: center;
    width: 100%;
    height: 70%;
}

.question {
    height: 43%;
    width: 25%;
    overflow-y: scroll;
    padding: 2%;
    margin: 2%;
    border: none;
    border-radius: 15px;
    box-shadow: 2px 2px 2px 2px #B4B4B4;
}

.question::-webkit-scrollbar {
  width: 8px;
  border-radius: 15px;
}

.question::-webkit-scrollbar-thumb {
  background-color: #1497DD;
  border-radius: 6px;
}

.question::-webkit-scrollbar-track {
  background: #f1f1f1;
}
</style>