import streamlit as st
from transformers import RobertaForSequenceClassification, RobertaTokenizer
from analyze import analyze_code
from Optimizations import suggest_optimizations

model = RobertaForSequenceClassification.from_pretrained('checkpoint-best-acc')
tokenizer = RobertaTokenizer.from_pretrained('microsoft/codebert-base')


# Streamlit app
st.title("AI-Powered Code Analysis and Optimization Tool")

uploaded_file = st.file_uploader("Upload your code file", type=["py", "txt"])

if uploaded_file:
    # Read the uploaded file
    code = uploaded_file.read().decode("utf-8")
    st.subheader("Uploaded Code")
    st.code(code, language="python")

    bottlenecks = analyze_code(code)
    suggestions = suggest_optimizations(bottlenecks)

    # Display results
    st.subheader("Analysis Results")
    if bottlenecks:
        st.write("### Detected Bottlenecks")
        for idx, issue in enumerate(bottlenecks, 1):
            st.write(f"**{idx}.** {issue}")
        
        st.write("### Optimization Suggestions")
        for issue, suggestion in suggestions.items():
            st.write(f"**For Bottleneck:** {issue}")
            st.write(f"- **Suggestion:** {suggestion}")
    else:
        st.write("No bottlenecks detected in the provided code.")
