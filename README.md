# HR Attrition Analytics & Prediction

## Steps

1. Install dependencies:
pip install -r requirements.txt

2. Generate data:
python data/generate_data.py

3. Train model:
python model/train_model.py

4. Run API:
uvicorn backend.app:app --reload

5. Run dashboard:
streamlit run dashboard/streamlit_app.py
