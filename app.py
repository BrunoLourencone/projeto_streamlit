import streamlit as st

st.set_page_config(page_title="projeto Streamlit", layout="wide")
st.markdown('# testando o streamlit')

def main():
    abas = st.tabs([
        "clientes",
        "cadastrar clientes",
        "editar",
        "deletar"

    ])

    with abas [0]:
        st.title('clientes')

    with abas [1]:
        st.title('cadastrar clientes')
        with st.form(key='add_clientes', clear_on_submit=True):
            nome = st.text_input("nome", placeholder="nome")
            email = st.text_input("email", placeholder="email")
            idade = st.number_input("idade", placeholder="idade", format="%d", step=1)
            telefone = st.number_input("telefone", placeholder="telefone", format="%d", step=1)
            profissao = st.selectbox("selecione a profissao", options=[
                
                "Faxineiro", "Policial", "Bombeiro", "Comerciante", 
                "Contador", "Psicólogo", "Jornalista", "Designer", 
                "Analista de Sistemas"
            ])

            btn_cadastrar = st.form_submit_button("Cadastrar Cliente")

        if btn_cadastrar:
            if not nome or not email or idade == 0:
                st.error('todos os campos precisam ser preenchidos!')
            else:
                data_cliente = {
                "nome": nome,
                "email" : email,
                "idade" : idade,
                "telefone" : telefone,
                "profissao" : profissao
            }

                st.write(data_cliente) 

    with abas [2]:
        st.title('editar')

    with abas [3]:
        st.title('deletar')

main()