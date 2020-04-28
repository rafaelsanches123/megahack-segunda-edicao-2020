<template>
    <Page class="page">
        <ActionBar class="action-bar">
            <!--
            Use the NavigationButton as a side-drawer button in Android
            because ActionItems are shown on the right side of the ActionBar
            -->
            
            <NavigationButton ios:visibility="collapsed" icon="res://menu" @tap="onDrawerButtonTap"></NavigationButton>
            
            <!--
            Use the ActionItem for IOS with position set to left. Using the
            NavigationButton as a side-drawer button in iOS is not possible,
            because its function is to always navigate back in the application.
            -->
            <ActionItem icon="res://menu"
                android:visibility="collapsed"
                @tap="onDrawerButtonTap"
                ios.position="left">
            </ActionItem>
            <Label class="action-bar-title" text="Seja-bem vindo(a)!"></Label>
        </ActionBar>

        <GridLayout class="page__content">

            <StackLayout class="">

                <StackLayout class="">
                    <Label class="header" text="CADASTRAR-ME" />
                    <Label class="sub-header" text="Aqui é o primeiro passo para mudar a saúde da sua vida financeira!" />
                </StackLayout>

                <TextField class="inputs-text" v-model="textFieldName"  hint="NOME COMPLETO"/>

                <TextField class="inputs-text" v-model="textFieldNickname"  hint="COMO QUER SER CHAMADO (ex:APELIDO)"/>

                <TextField class="inputs-text" v-model="textFieldEmail"  hint="E-MAIL"/>

                <TextField class="inputs-text" v-model="textFieldPassword"  hint="SENHA"/>


                <Button class="btn-primary" text="CRIAR MINHA CONTA" @tap="validateRegistration" />

            </StackLayout>

        </GridLayout>

    </Page>
</template>

<script>
    import * as utils from "~/shared/utils";
    import SelectedPageService from "../shared/selected-page-service";
    import * as http from "http";

    export default {
        data() {
            return {
                textFieldName        : "",
                textFieldNickname    : "",
                textFieldEmail       : "",
                textFieldPassword    : ""
            }
        },
        mounted() {
            SelectedPageService.getInstance().updateSelectedPage("CustomerRegistration");
        },
        computed: {

        },
        methods: {
            onDrawerButtonTap() {
                utils.showDrawer();
            },
            validateRegistration() {
                if (this.textFieldName == "" || this.textFieldNickname == "" || this.textFieldEmail == "" || this.textFieldPassword == "") {
                    this.alert(
                        "Por favor, todos os dados são obrigatórios o seu preenchimento!"
                    )
                }
                else {
                    http.request({
                    url: "http://localhost:8000/cadastro",
                    method: "POST",
                    headers: { "Content-Type": "application/json" },
                    content: JSON.stringify({
                        name: this.textFieldName,
                        nickname: this.textFieldNickname,
                        email: this.textFieldEmail,
                        password: this.textFieldPassword
                    })
                    }).then(response => {
                    
                    var result = response.content.toJSON();
                    if(result == True){
                        this.alert("Parabéns seu cadastro foi realizado com sucesso! Verifique seu email cadastrado nele conterá seu login e senha para acessar o app!")
                    }else{
                        this.alert("Não foi possível realizar seu cadastro. Tente novamente mais tarde!")
                    }
                    

                    }, error => {
                        console.error(error);
                        this.alert("Não foi possível realizar seu cadastro. Tente novamente mais tarde!")
                    });
                }
            },
            alert(message) {
                return alert({
                    title: "ATENÇÃO!",
                    okButtonText: "OK",
                    message: message
                });
            }
        }
    };
</script>

<style scoped lang="scss">
    // Start custom common variables
    @import '~@nativescript/theme/scss/variables/blue';
    // End custom common variables
    .btn-primary {
    margin-top: 50px;
    height: 50;
    border-radius: 5;
    font-size: 20;
    font-weight: 600;
    :disabled {
        opacity: 0.5;
    }
    }
    .header {
        horizontal-align: center;
        font-size: 25;
        font-weight: 600;
        margin-bottom: 0;
        text-align: center;
    }
    .sub-header {
        horizontal-align: center;
        font-size: 16;
        font-weight: 300;
        margin-bottom: 25;
        text-align: center;
    }
    .lost-password{
        horizontal-align: center;
        font-size: 16;
        font-weight: 300;
        margin-top: 10;
        margin-bottom: 25;
        text-align: center;
    }
    .logo {
        margin-top: 80px;
        horizontal-align: center;
    }
    .inputs-text {
        margin-top: 50px
    }
    // Custom styles
</style>
