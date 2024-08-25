import streamlit as st
from statsmodels.stats.proportion import proportion_confint

st.set_page_config(
    layout="wide",
    page_icon=':bar_chart:',
    page_title="Confidence interval estimate"
)

def change_label_style(label, font_size='12px', font_color='white', font_family='sans-serif'):
    html = f"""
    <script>
        var elems = window.parent.document.querySelectorAll('p');
        var elem = Array.from(elems).find(x => x.innerText == '{label}');
        elem.style.fontSize = '{font_size}';
        elem.style.color = '{font_color}';
        elem.style.fontFamily = '{font_family}';
    </script>
    """
    st.components.v1.html(html)


st.title("Confidence interval of binomial observations")
st.write("Handy little form to compute confidence interval of the probability of a process given observations.")
st.header("What are your observations?")
col1a, col1b, col1c = st.columns([1, 1, 1])
col2a, col2b = st.columns([1, 1])
n_obs = col1a.number_input("\# observations", value=20, min_value=1, max_value=100000000000)
n_pos = col1b.number_input("\# positive labels", value=2, min_value=0, max_value=100000000000)
ci = col1c.number_input("Confidence level", value=0.95, min_value=0.75, max_value=0.999999)
n_decimals = col2a.number_input("# decimals", value=4, min_value=2, max_value=12)
font_size = col2b.number_input("font size", value=20, min_value=5, max_value=100)

col3a, col3b = st.columns([1,1])
col3a.header("Your confidence interval:")
ci_lower, ci_upper = proportion_confint(n_pos, n_obs, alpha=1-ci, method='beta')
ci_str = f'p = {str(round(ci_lower, n_decimals))} - {str(round(ci_upper, n_decimals))}'
col3b.write(ci_str)
change_label_style(ci_str, f'{font_size}px')
