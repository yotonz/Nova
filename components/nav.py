# components/nav.py

import streamlit as st
from streamlit_option_menu import option_menu

def render_sidebar():
    with st.sidebar:
        selected = option_menu(
            menu_title="Navigation",
            options=[
                "Home",
                "Create Assistant",
                "Chat Assistant",
                "How it Works",
                "InfoSec",
                "About Us",
                "Contact Us"
            ],
            icons=[
                "house",
                "plus-circle",
                "chat-dots",
                "info-circle",
                "shield-lock",
                "info",
                "envelope"
            ],
            menu_icon="rocket",
            default_index=0,
            styles={
                "container": {"padding": "5px", "background-color": "#0E1117"},
                "icon": {"color": "white", "font-size": "18px"},
                "nav-link": {
                    "color": "white",
                    "font-size": "16px",
                    "text-align": "left",
                    "margin": "0px"
                },
                "nav-link-selected": {"background-color": "#4A90E2"}
            }
        )
        return selected
