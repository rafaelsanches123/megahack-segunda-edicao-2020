<template>
    <Page class="page">
        <ActionBar class="action-bar">
            <!--
            Use the NavigationButton as a side-drawer button in Android
            because ActionItems are shown on the right side of the ActionBar
            -->
            <!--
            <NavigationButton ios:visibility="collapsed" icon="res://menu" @tap="onDrawerButtonTap"></NavigationButton>
            -->
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
                    <Image class="logo" src="~/images/logo.png" stretch="none" />
                    <Label class="header" text="ME SALVE" />
                    <Label class="sub-header" text="O app que vai mudar sua saúde financeira!" />
                </StackLayout>

                <TextField class="inputs-text" v-model="textFieldLogin"  hint="LOGIN"/>
            
                <TextField class="inputs-text" v-model="textFieldPassword"  hint="SENHA"/>
            
                <Button class="btn-primary" text="ENTRAR" @tap="validaLogin" />

                <Button class="btn-primary" text="CADASTRAR-ME" @tap="onButtonTap" />

                <Label class="lost-password" text="Esqueci minha senha!" />

            </StackLayout>

        </GridLayout>

    </Page>
</template>

<script>
    import * as utils from "~/shared/utils";
    import SelectedPageService from "../shared/selected-page-service";

    export default {
        data() {
            return {
                textFieldLogin    : "",
                textFieldPassword : ""
            }
        },
        mounted() {
            SelectedPageService.getInstance().updateSelectedPage("Login");
        },
        computed: {
            
        },
        methods: {
            onDrawerButtonTap() {
                utils.showDrawer();
            },
            validaLogin() {
                
                if (this.textFieldLogin == "" || this.textFieldPassword == "") {
                    this.alert(
                        "Por favor, seu email e senha são obrigatórios!"
                    )
                }
                // recuperar os valores do inputs e validar com a base de dados se os mesmos estão ok para dar permissão para o usuário proceguir no app para as demais telas
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
