
# IPL score predictor and dashboard

A website to predict scores of live IPL matches and also visualize statistical and graphical dashboard.


## Contributors

 - [Shreyas Jain](https://www.linkedin.com/in/shreyas-jain-2a00a51ab/) : https://github.com/shrey0912
 - [Yatree Ladani](https://www.linkedin.com/in/yatree-ladani-3578b81b4/) :https://github.com/YatreeLadani
 - [Prachi Jethava](https://www.linkedin.com/in/prachi-jethava-a6b493170/) :https://github.com/prachi1211

  
## Website URL
https://ipl-cricfreak.herokuapp.com/



  
## Tech Stack

**Frontend:** HTML, CSS, Javascript, Chartjs(for dashboard), Bootstrap

**Backend:** Python framework Django

**ML model for predictor:** Gradient boost regression model

  
## Deployment

To deploy this project we have used Heroku platform and connected that to our project's github repository.

## How to setup this project on your local machine

 1. Clone This Project `git clone https://github.com/darsh295/IPL-score-predictor-and-dashboard.git`
 2. Go to Project Directory `cd IPL-score-predictor-and-dashboard`
 3. Create a Virtual Environment `python3 -m venv env`
 4. Activate Virtual Environment `source env/bin/activate`
 5. Install Requirements Package `pip install -r requirements.txt`
 6. Migrate Database `python manage.py migrate`
 7. Create Super User `python manage.py createsuperuser`
 8. Finally Run The Project `python manage.py runserver`


  
