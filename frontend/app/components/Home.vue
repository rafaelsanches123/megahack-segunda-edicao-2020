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
                <Image class="logo" src="~/images/meta.png" stretch="none" />
                <Label class="header" text="MINHA META!" />
                <Label class="sub-header" :text="meta" />

                <Label class="time-meta" :text="tempo_meta" />

            </StackLayout>

            <StackLayout class="">
                <Label class="extrato" text="EXTRATO MENSAL DE CONSUMO" />
                <Label class="extrato-data" :text="data_atual" />
            </StackLayout>

            <ListView class="list-view" for="item in gasto_mensal">
            <v-template>
                <GridLayout columns="2*, *" rows="*, *" class="lista-item"> 
                    <StackLayout row="0" col="0" class="">
                        <Label :text="item.nome" />
                    </StackLayout>
                    <StackLayout row="0" col="1" class="">
                        <Label :text="item.valor" />
                    </StackLayout>
                    <!--<StackLayout row="1" col="0" class="">
                        <Label :text="item.tipo" />
                    </StackLayout>-->
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
                meta:"Minha meta: comprar um carro HB20",
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
                            nome:"Cachaçaria Água Doce - São Carlos",
                            data:"02/05/2020",
                            valor:25.75,
                            tipo:"Restaurante"
                        },
                        {
                            nome:"Burguer King - São Carlos",
                            data:"03/05/2020",
                            valor:55.10,
                            tipo:"Restaurante"
                        },
                        {
                            nome:"MacDonald - São Carlos",
                            data:"01/05/2020",
                            valor:52.00,
                            tipo:"Restaurante"
                        },
                        {
                            nome:"Pagani Pizzas e Esfirras",
                            data:"02/05/2020",
                            valor:14.75,
                            tipo:"Restaurante"
                        },
                        {
                            nome:"Lanchonete do Juca - São Carlos",
                            data:"03/05/2020",
                            valor:12.10,
                            tipo:"Restaurante"
                        },
                        {
                            nome:"Donatello Pizzaria - São Carlos",
                            data:"01/05/2020",
                            valor:32.00,
                            tipo:"Restaurante"
                        },
                        {
                            nome:"Sorveteria Parra",
                            data:"02/05/2020",
                            valor:19.75,
                            tipo:"Restaurante"
                        },
                        {
                            nome:"Self Service Trevo - São Carlos",
                            data:"03/05/2020",
                            valor:45.10,
                            tipo:"Restaurante"
                        }
                    ]
            }
        },
        mounted() {
            SelectedPageService.getInstance().updateSelectedPage("Home");
        },
        computed: {
            meta(){
                return this.meta
            }
        },
        methods: {
            onDrawerButtonTap() {
                utils.showDrawer();
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
        font-weight: 700;
        font-size: 18;
        font-weight: 300;
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
</style>
