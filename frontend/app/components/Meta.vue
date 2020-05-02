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
            <Label class="action-bar-title" text="Minha Meta"></Label>
        </ActionBar>

        <ScrollView class="page__content">
        <StackLayout class="">    
            <StackLayout class="">
                <Image class="logo" src="~/images/target.png" stretch="none" />
                <Label class="header" text="MINHA META" />
                <Label class="sub-header" textWrap="true" text="Chegou a hora de começar a mudar sua vida financeira!" />
            </StackLayout>
            
            <StackLayout class="">
            <TextField class="inputs-text" v-model="textFieldDescription"  hint="DESCREVER SUA META AQUI..."/>
            <HtmlView html="<br>" />
            </StackLayout>
            
            <StackLayout class="inputs-text-date">
            <Label class="text-meta" text="SUA META INICIA HOJE!"></Label>
            </StackLayout>

            <StackLayout class="">
            <Label class="inputs-text-date" text="E QUANDO TERMINA ESSA META?"></Label>
            <DatePicker v-model="textFieldInitialDate" :date="textFieldInitialDate" />
            </StackLayout>

            <StackLayout class="">
            <TextField class="inputs-text" v-model="textFieldValue"  hint="QUANTO CUSTA SUA META (ex:15000)"/>
            </StackLayout>

            <StackLayout class="">
            <HtmlView html="<div></div><br><br></div>" />
            <Button class="btn-primary" text="SALVAR META" @tap="validateMeta" />
            </StackLayout>
        </StackLayout>    
        </ScrollView>

    </Page>
</template>

<script>
    import * as utils from "~/shared/utils";
    import SelectedPageService from "../shared/selected-page-service";

    export default {
        data() {
            return {
                textFieldDescription          : "",
                textFieldInitialDate          : new Date(),
                textFieldFinalDate            : new Date(),
                textFieldValue                : "",
            }
        },
        mounted() {
            SelectedPageService.getInstance().updateSelectedPage("Meta");
        },
        computed: {
            
        },
        methods: {
            onDrawerButtonTap() {
                utils.showDrawer();
            },
            formatPrice(value) {
                let val = (value/1).toFixed(2).replace('.', ',')
                return val.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ".")
            },
            validateMeta() {
                if (this.textFieldDescryption == "" || this.textFieldValue == "") {
                    this.alert(
                        "Por favor, todos os dados são obrigatórios o seu preenchimento!"
                    )
                }
                else {
                    http.request({
                    url: "http://10.0.2.2:8000/meta/",
                    method: "POST",
                    headers: { "Content-Type": "application/json" },
                    content: JSON.stringify({
                        'descricao'     :    this.textFieldDescryption,
                        'valor'  :    this.textFieldValue,
                        'inicio'    :    this.textFieldInitialDate,
                        'fim'    :    this.textFieldFinalDate,
                    })
                    }).then(response => {
                    
                    var result = response.content.toJSON();
                    this.alert(result.message)
                    if (response.statusCode == 200){
                        this.$navigateTo(Login);
                    }

                    }, error => {
                        console.error(error);
                        this.alert("Erro com a conexão ao servidor. Tente novamente mais tarde!")
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

    // Custom styles
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
    .logo {
        margin-top: 80px;
        horizontal-align: center;
    }
    .inputs-text-date{
        padding-left: 15%;
    }
    .text-meta{
        font-weight: 600;
    }
</style>
