# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 17:44:15 2022

@author: amrit
"""

import streamlit as st
from streamlit_folium import folium_static
from streamlit_option_menu import option_menu
import branca
import numpy as np
import pandas as pd
from bokeh.models.widgets import Button
from bokeh.models import CustomJS
from streamlit_bokeh_events import streamlit_bokeh_events
import os
from io import StringIO
import folium
from streamlit_folium import folium_static
import base64





st.set_page_config(
    page_title='Traker Comparison',page_icon=None,layout="wide",initial_sidebar_state="expanded",)


selected = option_menu(None, ["Home", "PDO NOOR",  "About HTC", 'Help'], 
    icons=['house', 'cloud-upload', "list-task", 'gear'], 
    menu_icon="cast", default_index=0, orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "#fafafa"},
        "icon": {"color": "orange", "font-size": "25px"}, 
        "nav-link": {"font-size": "25px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "green"},
    }
)

if selected=="Home":
    col1,col2,col3=st.columns((.85,1.3,.85))
    col2.title(f'Welcome')
    
    with st.sidebar.form(key="sidebar1-form"):
        t0=st.write(f'<b>Please Share your Personal Details</b>', unsafe_allow_html=True)
        name= st.text_input("Your Full Name")
        email=st.text_input("Your E-mail ID")
        ph=st.text_input("Your Contact Number")
        city=st.text_input("Your Current City")
        governate=st.text_input("Governate You Are located In")
        employee_id=st.text_input("Your Employee ID")
        dept=st.text_input("Your Department at PDO")
        position=st.text_input("Your Designation")
        submitted=st.form_submit_button('SUBMIT')
    
    if submitted==True:
        st.balloons()
        st.sidebar.success("🎉 Your Inputs Have Been Saved!")
        st.write("\n")
        
    else:
        col1,col2,col3=st.columns((0.001,2.994,0.005))
        st.write(f'<p style="background-color:#1F306B;color:#FFFFFF;text-align:center;padding:0.4rem;font-size:26px;border-radius:7px 7px 7px 7px;"><b>PLEASE FILL OUT THE FORM ON YOUR LEFT WITH YOUR PERSONAL INFO TO BEGIN WITH</b></p>', unsafe_allow_html=True)
    
    
    d2={'name':[name],
           'email':[email],
           'ph':[ph],
           'city':[city],
           'governate':[governate],
           'employee_id':[employee_id],
           'dept':[dept],
           'position':[position],
           
           }
    
    
    d2 = pd.DataFrame(data=d2)
    #st.write(d2)
    
    #st.write(d2['employee_id'])
    f_name=st.write(d2.employee_id.max())
    

    
    col1,col2=st.columns(2)
    with st.form(key="project1-form"):
        col1,col2=st.columns(2)
        #t0=col1.write(f'<b>Please Share the Project Details</b>', unsafe_allow_html=True)
        grid=col1.selectbox('Select Your Electricity Distribution Company',
                          ('MEDC','MZEC','MJEC'))
        e_consume=col1.select_slider('Average Monthly Energy Consumption (kWh):',options=range(0,2001),value=150)
        e_acc=col1.text_input("Your Electricity Meter Account Number",help="Please check Help Sectin for More Details")
        floor=col1.number_input("Please Share Number of Floors :")
        area=col1.number_input("Please Share Approax. Roof Area (m\u00b2):")
        layout_file =col2.file_uploader("Please Upload Buiilding's Roof Layout Plan", type = ['pdf', 'png','jpg','jpeg'])
        site_photo1 =col2.file_uploader("Please Share Roof's Photo from Stair-Case Door", type = ['pdf', 'png','jpg','jpeg'],help='Please Check Help Section for More Details')
        site_photo2 =col2.file_uploader("Please Share Roof's Photo from the Left Side Stair-Case Door", type = ['pdf', 'png','jpg','jpeg'],help='Please Check Help Section for More Details')
        site_photo3 =col2.file_uploader("Please Share Roof's Photo from  the right Side Stair-Case Door", type = ['pdf', 'png','jpg','jpeg'],help='Please Check Help Section for More Details')
        site_photo4 =col2.file_uploader("Please Share Roof's Photo from the Oposite End of Stair-Case Door", type = ['pdf', 'png','jpg','jpeg'],help='Please Check Help Section for More Details')
        sld =col2.file_uploader("Please Share Building SLD if Available", type = ['pdf', 'png','jpg','jpeg'],help='Please Check Help Section for More Details')
        mlp_photo =col2.file_uploader("Please Share a High-Res Clean Picture of Building's Main LV Panel", type = ['pdf', 'png','jpg','jpeg'],help='Please Check Help Section for More Details')
        parapet=col1.number_input('Height of the Parapet (m):')
        stair_case=col1.number_input('Height of the Stair Case Room (m):')
        obstacles = col1.multiselect(
     'Are There any Significant Objects on the roof Above parapet Height',
     ['AC Blower', 'Chimney Duct', 'Water Tank', 'Antenas'],
     )
        col1,col2, col3,col4,col5,col6,col7 = st.columns(7)
        submitted1 = col4.form_submit_button('SUBMIT')
    
    if submitted1==True:
        st.balloons()
        st.success("🎉 Your Inputs Have Been Saved!")
        st.write("\n")
        
        
        
        
        dirName1 = f'{e_acc}'
        try:
    # Create target Directory
            os.mkdir(dirName1)
            print("Directory " , dirName1 ,  " Created ") 
        except FileExistsError:
            print("Directory " , dirName1 ,  " already exists")
            
        
        
    else:
        
        st.write(f'<p style="background-color:#1F306B;color:#FFFFFF;text-align:center;padding:0.4rem;font-size:26px;border-radius:7px 7px 7px 7px;"><b>PLEASE FILL OUT THE FORM TO PROCEED TO NEXT STEP</b></p>', unsafe_allow_html=True)
        
  #-----------------------------------File Upload & Save Section----------------------------------  
            #site_photo_1
        #submitted2=st.form_submit_button('SUBMIT')
    if layout_file is not None:
        with open(os.path.join(f'{dirName1}',layout_file.name),"wb") as f: 
            f.write(layout_file.getbuffer())         
            st.success("Saved File")
        
    if site_photo1 is not None:
        with open(os.path.join(f'{dirName1}',site_photo1.name),"wb") as f: 
            f.write(site_photo1.getbuffer())         
            st.success("Saved File")
            
    if site_photo2 is not None:
        with open(os.path.join(f'{dirName1}',site_photo2.name),"wb") as f: 
            f.write(site_photo2.getbuffer())         
            st.success("Saved File")
            
    if site_photo3 is not None:
        with open(os.path.join(f'{dirName1}',site_photo3.name),"wb") as f: 
            f.write(site_photo3.getbuffer())         
            st.success("Saved File")       
            
            
    if site_photo4 is not None:
        with open(os.path.join(f'{dirName1}',site_photo4.name),"wb") as f: 
            f.write(site_photo4.getbuffer())         
            st.success("Saved File")
            
            
            
    if sld is not None:
        with open(os.path.join(f'{dirName1}',sld.name),"wb") as f: 
            f.write(sld.getbuffer())         
            st.success("Saved File")
            
            
            
    if mlp_photo is not None:
        with open(os.path.join(f'{dirName1}',mlp_photo.name),"wb") as f: 
            f.write(mlp_photo.getbuffer())         
            st.success("Saved File")
            
    
    
   #------------------------------------------------------------------------------------- 
    
    d3={
        'grid':[grid],
        'e_consume':[e_consume],
        'e_acc':[e_acc],
        'floor':[floor],
        'area':[area],
        'parapet':[parapet],
        'stair_case':[stair_case],
        'obstacles':[obstacles]
        }
    
    d3 = pd.DataFrame(data=d3)
    
    
    df0=pd.concat([d2,d3],axis=1)
    #st.write(df0)
    
    
    #st.write(dirName1)
    loc_button = Button(label="Get Location")
    loc_button.js_on_event("button_click", CustomJS(code="""
navigator.geolocation.getCurrentPosition(
    (loc) => {
        document.dispatchEvent(new CustomEvent("GET_LOCATION", {detail: {lat: loc.coords.latitude, lon: loc.coords.longitude}}))
    }
)
"""))
    result = streamlit_bokeh_events(
    loc_button,
    events="GET_LOCATION",
    key="get_location",
    refresh_on_update=False,
    override_height=75,
    debounce_time=0)
    
    if result:
        if "GET_LOCATION" in result:
            #st.write(result.get("GET_LOCATION"))
            d4=pd.DataFrame(data=[result.get("GET_LOCATION")])
            #st.write(d4)
            df=pd.concat([df0,d4],axis=1)
            #st.write(df)
            
    
        #st.write(d4)
        #st.write(df)
        df.to_csv(f'data/{e_acc}.csv', index=False)
        pv_size=df.area.max()/6.05
        #st.write(pv_size)
        spec_e=1650
        yearly_e=spec_e*pv_size
        lat=d4.lat.max()
        lon=d4.lon.max()
        if pv_size<=5:
            inv='5kW or Less';
        elif pv_size>5 and pv_size<=6:
            inv='5kW';
        elif pv_size>6 and pv_size<=7:
            inv='6kW';
        elif pv_size>7 and pv_size<=9:
            inv='8kW';
        elif pv_size>9 and pv_size<=11:
            inv='10kW';
        else:
            inv='Higher than 10kW'
        #st.write(inv)
        pv_size1=value="{:.2f}".format(df.area.max()/6.05)
        yearly_e1=value="{:.2f}".format(spec_e*pv_size)
        col1,col2=st.columns((.95,1.05))
        col1_text=f"""
                <div id="wb_Text14" style="">
        <ul style="font-size:12px;list-style-type:disc;box-shadow: 1px 1px 1px 1px grey;border-radius:7px 7px 7px 7px;padding:0.9rem;line-height: 2.1;">
        <li style="margin:0 0 0 18px;"><b>Approx PV System Capacity: {pv_size1}</b>
        </li>
        <li style="margin:0 0 0 18px;"><b>Specific Annual Energy Yield: {spec_e} kWh/kWp/Year</b>
        </li>
        <li style="margin:0 0 0 18px;"><b>Approx. Annual Energy Yield: {yearly_e1} kWh</b>
        </li>
        <li style="margin:0 0 0 18px;"><b>Suggested PV Module Size: 540 Wp</b>
        </li>
        <li style="margin:0 0 0 18px;"><b>Suggested Solar Inverter Size: {inv}</b>
        </li>
        </ul>
        </div>
        """
        col1.markdown(col1_text, unsafe_allow_html=True)

                
        with col2:
            
            st.write(f'<p style="background-color:#1F306B;color:#FFFFFF;text-align:center;padding:0.4rem;font-size:16px;border-radius:7px 7px 7px 7px;"><b>PROPOSED LOCATION FOR PV INSTALLATION</b></p>', unsafe_allow_html=True)
            m = branca.element.Figure()
            fm = folium.Map(location=(lat,lon), zoom_start=16,
                                   width='75%',height='75%',control_scale=True,
                                   position='relative',zoom_control=True)
            tooltip = "Proposed PV Site"
            folium.Marker(
                        (lat,lon), popup="Proposed PV Site", tooltip=tooltip
                        ).add_to(fm)
            m.add_child(fm)
            folium_static(m)
        
        st.write(f'<p style="background-color:#1F306B;color:#FFFFFF;text-align:center;padding:0.4rem;font-size:24px;border-radius:7px 7px 7px 7px;"><b>THANK YOU!! WE HAVE RECIEVED YOUR REQUEST DETAILS. WE WILL SHORTLY CONTACT YOU. <br>FOR FURTHER QUERIES, PLEASE CONTCAT US AT SALES@HTC.OM </b></p>', unsafe_allow_html=True)
    
    
    
#________________________________________________________________    
if selected=="PDO NOOR":
    col1,col2,col3=st.columns((.85,1.3,.85))
    col2.title(f'Welcome to {selected}')
    
    
    
if selected=="About HTC":
    padding_top=0
    m="""<style>
        .appview-container .main .block-container{{
            padding-top: {padding_top}rem;    }}
    </style>
    """

    st.markdown(m, unsafe_allow_html=True)
    def set_bg_hack(main_bg):
        '''
    A function to unpack an image from root folder and set as bg.
 
    Returns
    -------
    The background.
        '''
    # set bg name
        main_bg_ext = "images/solar-img.jpg"
        
        st.markdown(
         f"""
         <style>
         .stApp {{
             background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()});
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
    
#image=Image.open('home.jpg')    
    set_bg_hack('images/solar-img.jpg')
    
    col1,col2,col3=st.columns((.85,1.3,.85))
    col2.title(f'Welcome to HTC')
    st.write(f'<p style="background-color:#1F306B;color:#FFFFFF;text-align:left;padding:0.4rem;font-size:20px;border-radius:7px 7px 7px 7px;"><b>In 2016, HTC established a new Renewable Energy’s division, populated with highly experienced staff having a cumulative 50+ years’ experience in photovoltaics and undertaken numerous training courses as well as specific subject matter consultations</b></p>', unsafe_allow_html=True)
    st.write(f'<p style="background-color:#1F306B;color:#FFFFFF;text-align:center;padding:0.4rem;font-size:20px;border-radius:7px 7px 7px 7px;"><b>Further, in just a year from its advent, HTC’s Solar Division has a record of accomplishments:</b></p>', unsafe_allow_html=True)
    
    col1,col2=st.columns((1.2,.8))
    col1_text=f"""
            <div id="wb_Text14" style="">
    <ul style="background-color:#FFFFFF;font-size:12px;list-style-type:disc;box-shadow: 1px 1px 1px 1px grey;border-radius:7px 7px 7px 7px;padding:0.9rem;line-height: 2.1;">
    <li style="margin:0 0 0 18px;"><b>Implementer of Oman’s first set of AER (Authority for Electricity Regulation) compliant grid-connected Solar PV Plant for Shell’s Gift to the Nation: Solar into Schools Projects:</b>
    </li>
    <li style="margin:0 0 0 18px;"><b>One of the first DCRP certified Solar Contractor (Grade-S: Solar PV Installation Certificate) participant in both public & private consultations hosted by AER for Technical Standards and Connection Guidelines of small-scale grid connected solar PV plants.</b>
    </li>
    <li style="margin:0 0 0 18px;"><b>Signed contract to provide consultative services for local statutory and regulatory approvals for the ROP Hospital Solar PV Plant (1.2MWp).</b>
    </li>
    </ul>
    </div>
    """
    col1.markdown(col1_text, unsafe_allow_html=True)
    
    col2_text=f"""
            <div id="wb_Text14" style="">
    <ul style="background-color:#FFFFFF;font-size:12px;list-style-type:disc;box-shadow: 1px 1px 1px 1px grey;border-radius:7px 7px 7px 7px;padding:0.9rem;line-height: 2.1;">
    <li style="margin:0 0 0 18px;"><b>OUR OFFICE ADDRESS: <br> Hussam Technology Company LLC<br> Suite No. 1, Bldg No. 169, Way No. 6105 P.O.Box 2240, <br>Khuwair 133, Muscat, Sultanate of Oman</b>
    </li>
    <li style="margin:0 0 0 18px;"><b>CONTACT LINE <br>Telephone/FAX : +968 2202 0959<br>General Enquiry: info@htc.om || Solar Enquiry: solar@htc.om</b>
    </li>
    </ul>
    </div>
    """
    col2.markdown(col2_text, unsafe_allow_html=True)
#________________________________________________________________
    
if selected=="Help":
    col1,col2,col3=st.columns((.85,1.3,.85))
    col2.title(f'Welcome to {selected}')