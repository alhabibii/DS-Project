import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import base64

model = joblib.load('rf_model.joblib')

# Fungsi input user

def user_input_features():

    Marital_status = st.selectbox('Marital Status', options=['1 – Single',
                                                             '2 – Married',
                                                             '3 – Widower',
                                                             '4 – Divorced',
                                                             '5 – Facto Union',
                                                             '6 – Legally Separated'])

    Application_mode = st.selectbox('Application Mode', options=['1 - 1st phase - general contingent',
                                                                 '2 - Ordinance No. 612/93',
                                                                 '5 - 1st phase - special contingent (Azores Island)',
                                                                 '7 - Holders of other higher courses',
                                                                 '10 - Ordinance No. 854-B/99',
                                                                 '15 - International student (bachelor)',
                                                                 '16 - 1st phase - special contingent (Madeira Island)',
                                                                 '17 - 2nd phase - general contingent',
                                                                 '18 - 3rd phase - general contingent',
                                                                 '26 - Ordinance No. 533-A/99, item b2) (Different Plan)',
                                                                 '27 - Ordinance No. 533-A/99, item b3 (Other Institution)',
                                                                 '39 - Over 23 years old',
                                                                 '42 - Transfer',
                                                                 '43 - Change of course',
                                                                 '44 - Technological specialization diploma holders',
                                                                 '51 - Change of institution/course',
                                                                 '53 - Short cycle diploma holders',
                                                                 '57 - Change of institution/course (International)'])

    Application_order = st.number_input('Application Order')
    Daytime_evening_attendance = st.selectbox('Daytime Evening Attendance', options=['1 – Daytime', '0 - Evening'])

    Previous_qualification = st.selectbox('Previous Qualification', options=['1 - Secondary education',
                                                                             '2 - Higher education - bachelor\'s degree',
                                                                             '3 - Higher education - degree',
                                                                             '4 - Higher education - master\'s',
                                                                             '5 - Higher education - doctorate',
                                                                             '6 - Frequency of higher education',
                                                                             '9 - 12th year of schooling - not completed',
                                                                             '10 - 11th year of schooling - not completed',
                                                                             '12 - Other - 11th year of schooling',
                                                                             '14 - 10th year of schooling',
                                                                             '15 - 10th year of schooling - not completed',
                                                                             '19 - Basic education 3rd cycle (9th/10th/11th year) or equiv',
                                                                             '38 - Basic education 2nd cycle (6th/7th/8th year) or equiv',
                                                                             '39 - Technological specialization course',
                                                                             '40 - Higher education - degree (1st cycle)',
                                                                             '42 - Professional higher technical course',
                                                                             '43 - Higher education - master (2nd cycle)'])
    
    Previous_qualification_grade = st.number_input('Previous Qualification Grade')
    Admission_grade = st.number_input('Admission Grade')

    Displaced = st.selectbox('Displaced', options=['1 – Yes', '0 – No'])
    Debtor = st.selectbox('Debtor', options=['1 – Yes', '0 – No'])
    Tuition_fees_up_to_date = st.selectbox('Tuition Fees Up To Date', options=['1 – Yes', '0 – No'])
    
    Gender = st.selectbox('Gender', options=['1 – male', '0 – female'])
    Scholarship_holder = st.selectbox('Scholarship Holder', options=['1 – Yes', '0 – No'])
    Age_at_enrollment = st.number_input('Age at Enrollment')
    
    Curricular_units_1st_sem_enrolled = st.number_input('Curricular_units_1st_sem_enrolled')
    Curricular_units_1st_sem_approved = st.number_input('Curricular_units_1st_sem_approved')
    Curricular_units_1st_sem_grade = st.number_input('Curricular_units_1st_sem_grade')
    Curricular_units_1st_sem_without_evaluations = st.number_input('Curricular_units_1st_sem_without_evaluations')
    Curricular_units_2nd_sem_enrolled = st.number_input('Curricular_units_2nd_sem_enrolled')
    Curricular_units_2nd_sem_evaluations = st.number_input('Curricular_units_2nd_sem_evaluations')
    Curricular_units_2nd_sem_approved = st.number_input('Curricular_units_2nd_sem_approved')
    Curricular_units_2nd_sem_grade = st.number_input('Curricular_units_2nd_sem_grade')
    Curricular_units_2nd_sem_without_evaluations = st.number_input('Curricular_units_2nd_sem_without_evaluations')
    
    # Dictionary untuk membuat DataFrame
    data = {
        'Marital_status': Marital_status,
        'Application_mode': Application_mode,
        'Application_order': Application_order,
        'Daytime_evening_attendance': Daytime_evening_attendance,
        'Previous_qualification': Previous_qualification,
        'Previous_qualification_grade': Previous_qualification_grade,
        'Admission_grade': Admission_grade,
        'Displaced': Displaced,
        'Debtor': Debtor,
        'Tuition_fees_up_to_date': Tuition_fees_up_to_date,
        'Gender': Gender,
        'Scholarship_holder': Scholarship_holder,
        'Age_at_enrollment': Age_at_enrollment,
        'Curricular_units_1st_sem_enrolled': Curricular_units_1st_sem_enrolled,
        'Curricular_units_1st_sem_approved': Curricular_units_1st_sem_approved,
        'Curricular_units_1st_sem_grade': Curricular_units_1st_sem_grade,
        'Curricular_units_1st_sem_without_evaluations': Curricular_units_1st_sem_without_evaluations,
        'Curricular_units_2nd_sem_enrolled': Curricular_units_2nd_sem_enrolled,
        'Curricular_units_2nd_sem_evaluations': Curricular_units_2nd_sem_evaluations,
        'Curricular_units_2nd_sem_approved': Curricular_units_2nd_sem_approved,
        'Curricular_units_2nd_sem_grade': Curricular_units_2nd_sem_grade,
        'Curricular_units_2nd_sem_without_evaluations': Curricular_units_2nd_sem_without_evaluations,
    }
    features = pd.DataFrame(data, index=[0])
    return features

# Fungsi Replace ke numerik

def replace(df):

    df['Marital_status'].replace({'1 – Single': 1,
                                  '2 – Married': 2,
                                  '3 – Widower': 3,
                                  '4 – Divorced': 4,
                                  '5 – Facto Union': 5,
                                  '6 – Legally Separated': 6
    }, inplace=True)

    df['Application_mode'].replace({
                                '1 - 1st phase - general contingent': 1,
                                '2 - Ordinance No. 612/93' : 2,
                                '5 - 1st phase - special contingent (Azores Island)': 5,
                                '7 - Holders of other higher courses': 7,
                                '10 - Ordinance No. 854-B/99': 10,
                                '15 - International student (bachelor)': 15,
                                '16 - 1st phase - special contingent (Madeira Island)': 16,
                                '17 - 2nd phase - general contingent': 17,
                                '18 - 3rd phase - general contingent': 18,
                                '26 - Ordinance No. 533-A/99, item b2) (Different Plan)': 26,
                                '27 - Ordinance No. 533-A/99, item b3 (Other Institution)': 27,
                                '39 - Over 23 years old': 39,
                                '42 - Transfer': 42,
                                '43 - Change of course': 43,
                                '44 - Technological specialization diploma holders': 44,
                                '51 - Change of institution/course': 51,
                                '53 - Short cycle diploma holders': 53,
                                '57 - Change of institution/course (International)': 57
    }, inplace=True)

    df['Daytime_evening_attendance'].replace({'1 – Daytime': 1, '0 - Evening': 0}, inplace=True)
    df['Previous_qualification'].replace({'1 - Secondary education': 1,
                                          '2 - Higher education - bachelor\'s degree': 2,
                                          '3 - Higher education - degree': 3,
                                          '4 - Higher education - master\'s': 4,
                                          '5 - Higher education - doctorate': 5,
                                          '6 - Frequency of higher education': 6,
                                          '9 - 12th year of schooling - not completed': 9,
                                          '10 - 11th year of schooling - not completed': 10,
                                          '12 - Other - 11th year of schooling': 12,
                                          '14 - 10th year of schooling': 14,
                                          '15 - 10th year of schooling - not completed': 15,
                                          '19 - Basic education 3rd cycle (9th/10th/11th year) or equiv': 19,
                                          '38 - Basic education 2nd cycle (6th/7th/8th year) or equiv': 38,
                                          '39 - Technological specialization course': 39,
                                          '40 - Higher education - degree (1st cycle)': 40,
                                          '42 - Professional higher technical course': 42,
                                          '43 - Higher education - master (2nd cycle)': 43}, inplace=True)
    
    df['Displaced'].replace({'1 – Yes': 1, 
                             '0 – No': 0}, inplace=True)
    
    df['Debtor'].replace({'1 – Yes': 1,
                          '0 – No': 0}, inplace=True)
    
    df['Tuition_fees_up_to_date'].replace({'1 – Yes': 1,
                                           '0 – No': 0}, inplace=True)
    
    df['Gender'].replace({'1 – male': 1,
                          '0 – female': 0}, inplace=True)
    
    df['Scholarship_holder'].replace({'1 – Yes': 1,
                                      '0 – No': 0}, inplace=True) 
    
    return df

# Fungsi Donut Chart Prediction 

def plot_prediction_proba(proba):

    labels = 'Drop Out', 'Graduates'
    sizes = [proba[0], proba[1]]
    colors = ['#67C6E3','#5356FF']
    explode = (0.1, 0)
    explode=explode,
    wedgeprops = {'width': 0.7, 'edgecolor': 'w'}
    
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, colors=colors, labels=labels, autopct='%1.1f%%', startangle=140, pctdistance=0.85, textprops={'fontsize': 18}, wedgeprops=wedgeprops)
    
    centre_circle = plt.Circle((0,0),0.40,fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)
    
    ax1.axis('equal')  
    plt.tight_layout()
    
    return fig

# Fungsi Utama

def main():

    st.set_page_config(layout='wide',
                       page_title="Graduate or Dropout Prediction",
                       page_icon="🏂",
                       initial_sidebar_state="expanded")

    # Sidebar

    st.sidebar.title('About App and Institute')
    with st.sidebar.expander('What is this app about?'):
        st.markdown("This web application aims to predict whether an individual will graduate or drop out based on certain attributes")
        st.markdown("This web application uses machine learning to predict whether a student will graduate or drop out based on the provided information")

    with st.sidebar.expander('What is the Institute\'s Problem?'):
        st.markdown("""Established in the year 2000, Jaya Jaya Institute stands as a prominent educational institution known for its track record 
                    of producing numerous successful graduates. Despite its commendable reputation, the institute faces a significant challenge 
                    in dealing with a considerable number of students who opt to discontinue their education, commonly referred to as dropouts.""")
        st.markdown("""The institute recognizes that the high dropout rate poses a substantial problem that needs immediate attention. 
                    Therefore, Jaya Jaya Institute is keen on identifying students who show signs of potential dropout tendencies at an early stage. 
                    This proactive approach allows the institute to provide specialized guidance and support to help these students stay on track 
                    with their education.""")

    st.sidebar.title('About the App Creator')
    with st.sidebar.expander('Profile'):
        st.markdown("""The application was created by Adil Latif Habibi, a passionate enthusiast in Machine Learning and Data Science 
                    with a strong interest in data analysis, machine learning, and cloud computing. The purpose of this application is 
                    to meet the prediction needs for graduate and dropout students at Jaya Jaya Institute.""")
        
    with st.sidebar.expander('Contact'):
        st.markdown("Email : adillatif845@gmail.com")
        st.markdown("Linkedin : www.linkedin.com/in/adil-latif-habibi")
        
        st.sidebar.write('@adillatifhabibi. 2024')

    # Menambahkan Gambar

    with open("pic\jaya jaya institute.jpg", "rb") as image_file:
        image_data = base64.b64encode(image_file.read()).decode("utf-8")

    st.markdown(
        f"""
        <div style="display: flex; align-items: center;">
            <img src="data:image/jpeg;base64,{image_data}" alt="Logo" style="width: 300px; height: 300px; margin-right: 10px;">
            <div>
                <h1 style="margin: 0; font-size: 55px;">Student's Performance App</h1>
                <h3 style="margin: 0; font-size: 35px;">Dropout Probability Estimator</h3>
            </div>
        </div>  
        """,
        unsafe_allow_html=True
    )
    st.write('*'*20)

    # Pembuatan kolom Input User dan Prediction Result

    col1, col2 = st.columns([2, 1]) 

    with col1:
        st.subheader('Student Data')
        with st.expander('Please Input Student Data:'):
            df = user_input_features()

        df_final = df.copy()
        df_final = replace(df_final)

        st.subheader('Student Data Summary :')
        with st.expander("Summary:"):
            st.write(df)

        status = model.predict(df_final)
        prediction_proba = model.predict_proba(df_final)

    with col2:
        st.markdown("<h3 style='text-align: center;'>Prediction Result : </h3>", unsafe_allow_html=True)
        status_text = '<h4 style="text-align: center; color: green;">Student GRADUATES !</h4>' if status == 1 else '<h3 style="text-align: center; color: red;">Student Drops Out !!!</h3>'
        st.markdown(status_text, unsafe_allow_html=True)
        st.pyplot(plot_prediction_proba(prediction_proba[0]))
        st.write('*'*20)
        st.write('DATASET SOURCE :')
        st.write('Acknowledgements Realinho,Valentim, Vieira Martins,Mónica, Machado,Jorge, and Baptista,Luís. (2021).') 
        st.write('Predict students\' dropout and academic success.')
        st.write('UCI Machine Learning Repository. https://doi.org/10.24432/C5MC89.')

if __name__ == '__main__':
    main()