import streamlit as st


def main():
    st.title("LangChain Chat Interface")

    # Text input for user to type messages
    user_input = st.text_input("Enter a message:")

    if st.button("Send"):
        # Get response from LangChain model when button is clicked
        # response = langchain_model.generate_response(user_input)
        # st.text_area("LangChain:", value=response, height=100)
        pass


if __name__ == "__main__":
    main()
