# Trip_Planner_using_CrewAI

# Create Conda enviroment 
```
conda create -p trip_planner python=3.12 -y
```

# Activate Conda enviroment
```     
conda activate trip_planner         
```

# create virtual environment using uv
```
uv venv .tripvenv
```
## activate the tripvenv
```
.tripvenv\Scripts\activate
```
### To install the requirements.txt file using uv
```
uv pip install -r requirements.txt
```
## to install JUPYTER NOTEBOOK and Ipynb kernal

```
uv pip install notebook ipykernel
```
## Framework requirements
- Browserless API (www.Browserless.io)
-SERPER API
- OpenAI API
-GEMINI
- Rapid api 