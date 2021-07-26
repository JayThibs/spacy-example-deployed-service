# Example NLP Service with SpaCy

This is an example NER service using SpaCy and was built to show Data Scientists & Analysts a quick way to turn their models into deployable services. 

Tools used: FastAPI, SpaCy, Docker, and Poetry.

## How to use

    git clone https://github.com/JayThibs/spacy-example-deployed-service
    cd spacy-example-deployed-service
    docker build -t spacy-example-deployed-service .
    docker run -d -p 80:80 spacy-example-deployed-service:latest

Then, head to `http://localhost/docs` to see the docs and test the app by clicking Try It Out, changing `content` to whatever text you would like to get NERs from with SpaCy, and hitting Execute. Scroll down to find the output entities in the Response body.

On the Swagger UI, you can Try It Out here:

![try-it-out-content](https://github.com/JayThibs/spacy-example-deployed-service/imgs/try-it-out-content.png)

Once you've executed the request, you can see the output entities in the Response body:

![response-body](https://github.com/JayThibs/spacy-example-deployed-service/imgs/response-body.png]

### If you only want to test FastAPI's Swagger UI



## References

As a way to get better at quickly deploying useful ml / data science apps, I worked through this [reference video walkthrough](https://youtu.be/Maj9v-Ev7-4) to get going quickly for future projects.
