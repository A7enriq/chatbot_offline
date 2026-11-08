import streamlit as st
import utils





st.title('STREAMLIT CHATBOT')





if 'message' not in st.session_state:
    st.session_state['messages'] = [{'role':'ai', 'content':'How Can I Help You?'}]





for message in st.session_state['messages']:
    st.chat_message(message['role']).write(message['content'])    

prompt = st.chat_input('Enter Your Question')
model = 'gemma3:1b' 
if prompt:

    new_prompt ='Describe your  answer with detil and shape' + prompt
    st.chat_message('user').write(prompt)
    st.session_state['messages'].append({'role':'user', 'content':prompt})

    with st.spinner('Generating Response ....'):
        response = utils.call_ollama_model(new_prompt, model)

    st.chat_message('ai').write(response)
    st.session_state['messages'].append({'role':'ai', 'content': prompt})

if st.button('DELETE CHAT'):
    st.session_state['messages'] = []

if st.button('SAVE SUMMARY') and \
    len(st.session_state['messages']) > 0:
    chat = 'Summarize this conersation:' + '\n'
    for msg in st.session_state['messages']:
        chat += msg['role'] + ' : ' + msg['content'] + '\n\n\n\n\n'

    with st.spinner('Generating the summary...'):
        result = utils.call_ollama_model(chat, model)

    with open('SUMMARY.txt', 'w', encoding='utf-8') as f:
        f.write(result)

    st.success('SUMMARY SAVED IN SUMMARY.txt')
