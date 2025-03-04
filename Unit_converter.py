import streamlit as st

# Set page configuration
st.set_page_config(page_title="Advanced Unit Converter", page_icon="🔢", layout="centered")

# Improved Styling with a Dark Theme
st.markdown("""
    <style>
    /* Global Styles */
    body { 
        background-color: #0A0A0A; 
        color: #E0E0E0; 
        font-family: 'Arial', sans-serif; 
    }

    /* Header with Gradient */
    .main-header { 
        font-size: 2.8rem; 
        font-weight: bold; 
        color: #FFFFFF; 
        text-align: center; 
        padding: 18px; 
        background: linear-gradient(to right, #8A2BE2, #4B0082); 
        border-radius: 12px; 
        box-shadow: 0px 5px 15px rgba(138, 43, 226, 0.4);
        transition: all 0.3s ease-in-out;
    }
    .main-header:hover {
        transform: scale(1.02);
        box-shadow: 0px 6px 18px rgba(138, 43, 226, 0.6);
    }
    .category-card:hover {
        transform: scale(1.01);
        box-shadow: 0px 8px 15px rgba(255, 255, 255, 0.1);
    }

    /* Input Fields & Dropdowns */
    .stSelectbox, .stNumberInput { 
        background-color: #2D2D2D; 
        color: #FFFFFF; 
        border: 2px solid #8A2BE2; 
        border-radius: 8px; 
        padding: 10px; 
        font-size: 1.1rem; 
        transition: all 0.3s ease-in-out;
    }
    .stSelectbox:hover, .stNumberInput:hover { 
        border: 2px solid #FFD700; 
        transform: scale(1.02);
    }

    /* Value Display Box */
    .value-display { 
        font-size: 2.4rem; 
        font-weight: bold; 
        color: #00E676; 
        text-align: center; 
        padding: 14px; 
        background: #222222; 
        border-radius: 12px; 
        border: 2px solid #00E676; 
        box-shadow: 0px 5px 10px rgba(0, 230, 118, 0.3);
        transition: all 0.3s ease-in-out;
    }
    .value-display:hover {
        transform: scale(1.05);
        box-shadow: 0px 8px 20px rgba(0, 230, 118, 0.5);
    }

    /* Formula Box */
    .formula-box { 
        background: linear-gradient(to right, #FFD700, #FFA500); 
        color: #121212; 
        padding: 10px 14px; 
        font-weight: bold; 
        border-radius: 8px; 
        display: inline-block; 
        box-shadow: 0px 4px 8px rgba(255, 140, 0, 0.3);
        transition: all 0.3s ease-in-out;
    }
    .formula-box:hover {
        transform: scale(1.05);
        box-shadow: 0px 6px 12px rgba(255, 140, 0, 0.5);
    }

    /* Footer Section */
    .footer { 
        text-align: center; 
        margin-top: 3rem; 
        font-size: 1rem; 
        padding: 14px; 
        border-radius: 12px; 
        background: linear-gradient(to right, #03DAC5, #018786); 
        color: #121212; 
        font-weight: bold; 
        box-shadow: 0px 4px 10px rgba(3, 218, 197, 0.4);
        transition: all 0.3s ease-in-out;
    }
    .footer:hover {
        transform: scale(1.02);
        box-shadow: 0px 6px 15px rgba(3, 218, 197, 0.6);
    }

    /* Button Styles */
    .stButton>button {
        background-color: #8A2BE2;
        color: white;
        border-radius: 8px;
        padding: 10px 20px;
        font-size: 1rem;
        border: none;
        transition: all 0.3s ease-in-out;
    }
    .stButton>button:hover {
        background-color: #FFD700;
        color: #121212;
        transform: scale(1.05);
    }

</style>
""", unsafe_allow_html=True)

# Conversion Data Dictionary
@st.cache_data
def load_conversion_data():
    return {
        "Length": {
            "Kilometre": 1000, "Metre": 1, "Centimetre": 0.01, "Millimetre": 0.001, 
            "Micrometre": 1e-6, "Nanometre": 1e-9, "Mile": 1609.34, "Yard": 0.9144, 
            "Foot": 0.3048, "Inch": 0.0254, "Nautical mile": 1852
        },
        "Area": {
            "Square Metre": 1, "Square Kilometre": 1e6, "Square Centimetre": 0.0001, 
            "Square Millimetre": 1e-6, "Acre": 4046.86, "Hectare": 10000
        },
        "Mass": {
            "Kilogram": 1, "Gram": 0.001, "Milligram": 1e-6, "Metric Ton": 1000, 
            "Pound": 0.453592, "Ounce": 0.0283495, "Stone": 6.35029
        },
        "Volume": {
            "Cubic Metre": 1, "Litre": 0.001, "Millilitre": 1e-6, "Gallon (US)": 0.00378541, 
            "Quart (US)": 0.000946353, "Pint (US)": 0.000473176
        },
        "Speed": {
            "Metre per second": 1, "Kilometre per hour": 0.277778, "Mile per hour": 0.44704, 
            "Knot": 0.514444
        },
        "Temperature": {"Celsius": "C", "Fahrenheit": "F", "Kelvin": "K"},
        "Time": {
            "Second": 1, "Minute": 60, "Hour": 3600, "Day": 86400, "Week": 604800, 
            "Year (365 days)": 31536000
        },
        "Energy": {
            "Joule": 1, "Kilojoule": 1000, "Calorie": 4.184, "Kilocalorie": 4184, 
            "Watt-hour": 3600, "Kilowatt-hour": 3.6e6
        },
        "Digital Storage": {
            "Bit": 1, "Byte": 8, "Kilobyte": 8000, "Megabyte": 8e6, "Gigabyte": 8e9, 
            "Terabyte": 8e12
        },
    }

conversion_data = load_conversion_data()

# Conversion Function
def convert_value(value, from_unit, to_unit, category):
    if category == "Temperature":
        if from_unit == "Celsius" and to_unit == "Fahrenheit":
            return (value * 9/5) + 32
        elif from_unit == "Celsius" and to_unit == "Kelvin":
            return value + 273.15
        elif from_unit == "Fahrenheit" and to_unit == "Celsius":
            return (value - 32) * 5/9
        elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
            return (value - 32) * 5/9 + 273.15
        elif from_unit == "Kelvin" and to_unit == "Celsius":
            return value - 273.15
        elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
            return (value - 273.15) * 9/5 + 32
        return value

    return value * (conversion_data[category][from_unit] / conversion_data[category][to_unit]) if from_unit != to_unit else value

# UI Layout
st.markdown("<h1 class='main-header'>Unit Converter</h1>", unsafe_allow_html=True)
category = st.selectbox("Select Category", list(conversion_data.keys()))

st.markdown(f"<div class='category-card'>", unsafe_allow_html=True)
col_from, col_equal, col_to = st.columns([2, 1, 2])

with col_from:
    from_unit = st.selectbox("From", list(conversion_data[category].keys()))
    from_value = st.number_input("", value=1.0, format="%.8f", key="from_value")

with col_equal:
    st.markdown("<div style='text-align: center; font-size: 2rem; margin-top: 1.7rem;'>=</div>", unsafe_allow_html=True)

with col_to:
    to_unit = st.selectbox("To", list(conversion_data[category].keys()))
    to_value = convert_value(from_value, from_unit, to_unit, category)
    st.markdown(f"<div class='value-display'>{to_value:.4f}</div>", unsafe_allow_html=True)

# Swap Units Button
if st.button("Swap Units"):
    from_unit, to_unit = to_unit, from_unit
    from_value, to_value = to_value, from_value
    st.rerun()

# Reset Button
if st.button("Reset"):
    from_value = 1.0
    st.rerun()

# Copy to Clipboard Button
if st.button("Copy to Clipboard"):
    st.write(f"Copied: {to_value:.4f} {to_unit}")
    st.rerun()

# History Section
if 'history' not in st.session_state:
    st.session_state['history'] = []

if st.button("Add to History"):
    st.session_state['history'].append(f"{from_value:.4f} {from_unit} = {to_value:.4f} {to_unit}")
    if len(st.session_state['history']) > 5:
        st.session_state['history'].pop(0)

st.markdown("### Conversion History")
for i, entry in enumerate(st.session_state['history']):
    st.write(f"{i+1}. {entry}")

st.markdown("</div>", unsafe_allow_html=True)
st.markdown("<div class='footer'>Developed by Muhammad Farooq | © 2025 Unit Converter</div>", unsafe_allow_html=True)
