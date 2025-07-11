<h1 align="center">🍷 Wine Classifier Flask Application</h1>

<p align="center">
  <em>A web-based application that uses machine learning to classify red and white wines based on their physicochemical properties</em>
</p>

<hr/>

<h2>🎯 Objective</h2>

<p>
  This project demonstrates the practical application of machine learning in the field of oenology (the science of wine). It combines a user-friendly web interface with a predictive model to automatically classify wines as red or white based on their measured characteristics.
</p>

<h2>⚙️ Project Architecture</h2>

The project consists of two main components:

<ol>
  <li><strong>Frontend</strong>
    <ul>
      <li>The homepage (<code>/</code>) displays an interactive table where users can enter the physicochemical features of each wine sample. The inputs include:
        <ul>
          <li><code>fixed_acidity</code>, <code>volatile_acidity</code>, <code>citric_acid</code>, <code>residual_sugar</code></li>
          <li><code>chlorides</code>, <code>free_sulfur_dioxide</code>, <code>total_sulfur_dioxide</code>, <code>density</code></li>
          <li><code>pH</code>, <code>sulphates</code>, <code>alcohol</code>, <code>quality</code></li>
        </ul>
      </li>
      <li>The interface offers two main buttons:
        <ul>
          <li><strong>"Add Row"</strong>: Dynamically adds new rows to enter data for multiple wines at once.</li>
          <li><strong>"Classify"</strong>: Sends the entered data to the backend for prediction.</li>
        </ul>
      </li>
      <li>After prediction, the classification results (Red Wine or White Wine) are displayed in an additional column in the same table.</li>
    </ul>
  </li>

  <li><strong>Backend</strong>
    <ul>
      <li>The backend is built with Flask, a lightweight Python web framework.</li>
      <li>Submitted data is processed as follows:
        <ul>
          <li>Each table row is converted into a dictionary representing the features of one wine sample.</li>
          <li>All dictionaries are combined into a list, which is transformed into a Pandas DataFrame.</li>
          <li>The DataFrame is fed into a pre-trained machine learning model loaded with <code>joblib</code>.</li>
          <li>The model predicts whether each wine is red or white:
            <ul>
              <li><code>Prediction = 1</code>: White Wine</li>
              <li><code>Prediction = 0</code>: Red Wine</li>
            </ul>
          </li>
          <li>The predictions are returned to the frontend for display.</li>
        </ul>
      </li>
    </ul>
  </li>
</ol>

<h2>🧰 Technologies Used</h2>

<ul>
  <li><strong>Frontend</strong>:
    <ul>
      <li>HTML, CSS, and JavaScript for building the interactive web interface.</li>
      <li>Dynamic form controls for adding rows and submitting data.</li>
    </ul>
  </li>
  <li><strong>Backend</strong>:
    <ul>
      <li>Flask: For handling HTTP requests and routing.</li>
      <li>Pandas: For creating and processing DataFrames.</li>
      <li>Joblib: For loading the pre-trained model.</li>
      <li>Python: The main backend programming language.</li>
    </ul>
  </li>
  <li><strong>Machine Learning</strong>:
    <ul>
      <li>A pre-trained classifier (likely trained on a dataset of red and white wines) predicts the wine type.</li>
    </ul>
  </li>
</ul>

<h2>✨ Key Features</h2>

<ul>
  <li><strong>Dynamic Data Entry</strong>:
    <ul>
      <li>Users can add as many rows as needed to classify multiple samples in a single submission.</li>
    </ul>
  </li>
  <li><strong>Automated Classification</strong>:
    <ul>
      <li>Wine features are sent to the backend where the model predicts the type of wine instantly.</li>
    </ul>
  </li>
  <li><strong>Results Display</strong>:
    <ul>
      <li>Predictions are seamlessly integrated back into the table for a smooth user experience.</li>
    </ul>
  </li>
  <li><strong>Practical Applications</strong>:
    <ul>
      <li>Used by wine industry professionals to verify product specifications.</li>
      <li>Serves as an educational tool for students and enthusiasts learning about wine and machine learning.</li>
    </ul>
  </li>
</ul>

<h2>🌍 Real-World Impact</h2>

<p>
  This project highlights how modern technologies can be applied to solve domain-specific challenges. Real-world use cases include:
</p>

<ul>
  <li><strong>Wine Industry</strong>:
    <ul>
      <li>Rapid, automated classification of wines to ensure compliance with production standards.</li>
      <li>Analysis of chemical properties to improve vinification processes.</li>
    </ul>
  </li>
  <li><strong>Education</strong>:
    <ul>
      <li>An accessible tool to teach the differences between red and white wines and demonstrate machine learning concepts.</li>
    </ul>
  </li>
  <li><strong>Wine Enthusiasts</strong>:
    <ul>
      <li>A friendly way to explore wine characteristics and better understand their composition.</li>
    </ul>
  </li>
</ul>

<h2>✅ Conclusion</h2>

<p>
  The <strong>Wine Classifier Flask Application</strong> is a complete example of integrating machine learning into a web application. It showcases how predictive models can address real-world problems while providing a simple, intuitive interface. Whether for professionals, educators, or hobbyists, this project demonstrates the potential of modern technology to transform ideas into innovative solutions.

  <hr/>

<p align="center">
  <img src="https://media.giphy.com/media/hvRJCLFzcasrR4ia7z/giphy.gif" width="300" alt="Done"/>
</p>

</p>
