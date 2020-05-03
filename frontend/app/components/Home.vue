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
            <Label class="action-bar-title" text="Home"></Label>
        </ActionBar>

        <StackLayout class="page__content">
            
            <StackLayout class="">
                <Image class="logo" src="~/images/ranking.png" width="100" height="100" stretch="aspectFill" />
                <Label class="header" text="MINHA META!" />
                <Label class="sub-header" :text="meta" />
                <Label class="time-meta" :text="tempo_meta" />
            </StackLayout>

             <StackLayout orientation="horizontal" class="resultado-diario">
                <StackLayout class="gastando">
                    <StackLayout width="40%" class="">
                        <Label text="GASTANDO" />
                    </StackLayout>
                    <StackLayout width="40%" class="">
                        <Label>
                            <FormattedString>
                                <Span text="R$ " />
                                <Span :text="formatPrice(400.00)" />
                            </FormattedString>
                        </Label>
                    </StackLayout>
                </StackLayout>
                <StackLayout class="economizando">
                    <StackLayout width="60%" class="">
                        <Label text="ECONOMIZANDO" />
                    </StackLayout>
                    <StackLayout width="60%" class="">
                        <Label>
                            <FormattedString>
                                <Span text="R$ " />
                                <Span :text="formatPrice(600.00)" />
                            </FormattedString>
                        </Label>
                    </StackLayout>
                </StackLayout>
            </StackLayout>
        

            <StackLayout class="">
                <Label class="extrato" text="EXTRATO MENSAL DE CONSUMO" />
            </StackLayout>

            <ListView class="list-view" for="item in gasto_mensal">
            <v-template>
                <GridLayout columns="2*, *" rows="*, *" class="lista-item"> 
                    <StackLayout row="0" col="0" class="titulo-parceiro">
                        <Label textWrap="true" :text="item.nome" />
                    </StackLayout>
                    <StackLayout row="0" col="1" class="valor-produto-parceiro">
                        <Label>
                            <FormattedString>
                                <Span text="R$ -" />
                                <Span :text="formatPrice(item.valor)" />
                            </FormattedString>
                        </Label>
                    </StackLayout>
                    <StackLayout row="1" col="0" class="">
                        <Label :text="item.tipo" />
                    </StackLayout>
                    <StackLayout row="1" col="1" class="">
                        <Label :text="item.data" />
                    </StackLayout>
                </GridLayout>
            </v-template>
            </ListView>

        </StackLayout>

    </Page>
</template>

<script>
    import * as utils from "~/shared/utils";
    import SelectedPageService from "../shared/selected-page-service";

    export default {
        data() {
            return {
                input: {
                    email: "",
                    senha: ""
                },
                meta:"Comprar um carro modelo HB20 ano 2008",
                valor_meta:40000.00,
                inicio_meta: 'Quando comecei a meta: 01/05/2020',
                fim_meta: 'Quando terminará a meta: 25/08/2020',
                tempo_meta: 'Dias para finalizar a sua meta: 45 dias!',
                gasto:"1000",
                renda:"4000",
                data_atual:"04/05/2020",
                gasto_mensal : [
                        {
                            nome:"Rancho da Picanha",
                            data:"01/05/2020",
                            valor:50.00,
                            tipo:"Restaurante",
                        },
                        {
                            nome:"Cachaçaria Água Doce",
                            data:"02/05/2020",
                            valor:25.75,
                            tipo:"Restaurante"
                        },
                        {
                            nome:"Burguer King",
                            data:"03/05/2020",
                            valor:55.10,
                            tipo:"Fastfood"
                        },
                        {
                            nome:"MacDonald",
                            data:"01/05/2020",
                            valor:52.00,
                            tipo:"Fastfood"
                        },
                        {
                            nome:"Pagani Pizzas e Esfirras",
                            data:"02/05/2020",
                            valor:14.75,
                            tipo:"Pizzaria"
                        },
                        {
                            nome:"Lanchonete do Juca",
                            data:"03/05/2020",
                            valor:12.10,
                            tipo:"Lanchonete"
                        },
                        {
                            nome:"Donatello Pizzaria",
                            data:"01/05/2020",
                            valor:32.00,
                            tipo:"Pizzaria"
                        },
                        {
                            nome:"Sorveteria Parra",
                            data:"02/05/2020",
                            valor:19.75,
                            tipo:"Sorveteria"
                        },
                        {
                            nome:"Self Service Trevo",
                            data:"03/05/2020",
                            valor:45.10,
                            tipo:"Restaurante"
                        }
                    ]
            }
        },
        mounted() {
            SelectedPageService.getInstance().updateSelectedPage("Home");
            this.input = load()
            if(this.input.email != ""){
                alert(this.input.email)
            }
        },
        computed: {
            meta(){
                return this.meta
            }
        },
        methods: {
            load() {
                this.$store.commit("load");
            },
            onDrawerButtonTap() {
                utils.showDrawer();
            },
            formatPrice(value) {
                let val = (value/1).toFixed(2).replace('.', ',')
                return val.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ".")
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
    .logo {
        margin-top: 100px;
        horizontal-align: center;
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
        font-size: 18;
        font-weight: 500;
        margin-bottom: 15;
        text-align: center;
    }
    .time-meta{
        horizontal-align: center;
        font-size: 16;
        font-weight: 500;
        margin-bottom: 5;
        text-align: center;
    }
    .extrato{
        horizontal-align: center;
        font-size: 16;
        font-weight: 500;
        margin-top: 25;
        margin-bottom: 15;
        text-align: center;
    }
    .extrato-data{
        horizontal-align: center;
        font-weight: 500;
        font-size: 18;
        
        padding-left: 15%;
    }
    body{
        background-color: #EFF4F7;
    }
    .lista-item{
        font-weight: 300;
        font-size: 14;
        background-color: #FFFFFF;
    }
    .list-view{
        padding: 0px 20%;
    }
    .resultado-diario{
        horizontal-align: center;
        text-align: center;
        font-size: 15%;
    }
    .gastando{
        color: red;
        horizontal-align: center;
        text-align: center;
    }
    .economizando{
        color: green;
        horizontal-align: center;
        text-align: center;
    }
    .titulo-parceiro{
        font-weight: 500;
    }
    .valor-produto-parceiro{
        color: red;
        font-weight: 500;
    }
</style>
