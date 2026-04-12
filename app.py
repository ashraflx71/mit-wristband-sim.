
import streamlit as st
import numpy as np
import pandas as pd

# 1. إعدادات الصفحة (تظهر في تبويب المتصفح)
st.set_page_config(page_title="MIT Wristband Sim", layout="centered")

# 2. التنسيق البصري الخاص بهوية MIT (رمادي وأحمر كاردينال)
st.markdown("""
    <style>
    /* تنسيق القائمة الجانبية */
    [data-testid="stSidebar"] { background-color: #333333; }
    [data-testid="stSidebar"] .stMarkdown p, [data-testid="stSidebar"] label, [data-testid="stSidebar"] h2 { color: #ffffff !important; }
    
    /* تنسيق السلايدر (المؤشرات) باللون الأحمر */
    div[data-baseweb="slider"] > div > div { background-color: #A31F34 !important; }
    
    /* تنسيق العناوين والمؤشرات الرقمية */
    h1, h2, h3 { color: #A31F34 !important; }
    .stMetric { background-color: #f8f9fa; padding: 15px; border-radius: 10px; border-right: 5px solid #A31F34; }
    </style>
    """, unsafe_allow_html=True)

# 3. واجهة التحكم الجانبية (Sidebar)
with st.sidebar:
    st.header("🎛️ مدخلات العضلات")
    st.write("حرك المؤشرات لمحاكاة انقباض الأوتار")
    muscle_1 = st.slider("انقباض العضلة القابضة (Flexor)", 0, 100, 30)
    muscle_2 = st.slider("انقباض وتر الإبهام (Thumb)", 0, 100, 50)
    st.divider()
    st.write("💻 تطوير: Creative 2026")
    st.write("👤 المبرمج: أشرف حسن")

# 4. المحتوى الرئيسي للمقال التفاعلي
st.title("🚀 محاكي سوار MIT للموجات فوق الصوتية")
st.write("تحويل أبحاث معهد MIT إلى تجربة تفاعلية حية. هذا المحاكي يحلل إشارات الموجات فوق الصوتية المنبعثة من معصم اليد.")

# 5. عرض النتائج وتحليل الذكاء الاصطناعي
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
        <div style="text-align: center; margin-bottom: 15px; padding: 10px; border-radius: 10px; background-color: #f8f9fa; border-left: 5px solid #A31F34;">
            <h4 style="margin:0; color: #333;">مختبر MIT التفاعلي</h4>
            <p style="font-size: 0.8rem; color: #666; margin-top:5px;">حالة النظام: تحليل نشط ✅</p>
        </div>
    """, unsafe_allow_html=True)
    
    # محاكاة دقة النظام بناءً على قوة الإشارة
    accuracy = 94 + (muscle_1 / 250) + (muscle_2 / 250)
    st.metric(label="دقة التنبؤ بالحركة", value=f"{min(accuracy, 99.8):.2f}%")

with col2:
    st.subheader("🤖 الحركة المكتشفة")
    # منطق تصنيف الحركة
    if muscle_1 > 75 and muscle_2 > 75:
        st.success("✊ قبضة كاملة (Grasp)")
    elif muscle_1 > 75:
        st.info("☝️ إشارة السبابة (Point)")
    elif muscle_2 > 75:
        st.info("👍 إشارة الإبهام (Thumb Up)")
    elif muscle_1 < 10 and muscle_2 < 10:
        st.warning("💤 وضع الراحة (Rest)")
    else:
        st.write("🔄 جاري تحليل الحركة...")

# 6. الرسم البياني للموجات (توليد بيانات وهمية تعتمد على السلايدر)
st.subheader("📊 مخطط إشارات الموجات فوق الصوتية (Real-time)")
t = np.linspace(0, 2*np.pi, 100)
# إشارة تتفاعل مع قوة انقباض العضلة
signal_a = (muscle_1 / 40) * np.sin(5 * t) + np.random.normal(0, 0.1, 100)
signal_b = (muscle_2 / 40) * np.cos(3 * t) + np.random.normal(0, 0.1, 100)

chart_df = pd.DataFrame({
    "إشارة العضلة (Flexor)": signal_a,
    "إشارة الإبهام (Thumb)": signal_b
})

st.line_chart(chart_df, color=["#A31F34", "#333333"])

# 7. التوقيع النهائي
st.divider()
st.caption("تمت البرمجة بواسطة أشرف حسن | جميع الحقوق محفوظة لمدونة Creative 2026")
