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
                <Label class="sub-header" :text="meta.descricao" />
                <Label class="time-meta" textWrap="true">
                            <FormattedString>
                                <Span text="Dias para finalizar a sua meta: " />
                                <Span :text="retorna_tempo_restante_meta()" />
                                <Span text=" dias!" />
                            </FormattedString>
                        </Label>
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
                                <Span :text="formatPrice(gastos_mensal_total())" />
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
                                <Span :text="formatPrice(usuario.gasto-gastos_mensal_total())" />
                            </FormattedString>
                        </Label>
                    </StackLayout>
                </StackLayout>
            </StackLayout>
        

            <StackLayout class="">
                <!-- <Label class="" :text="meta.valor-(usuario.gasto-gastos_mensal_total())" /> -->
                <Label class="extrato" text="EXTRATO MENSAL DE CONSUMO" />
            </StackLayout>

            <ListView height="100%" class="list-view" for="item in gastos_mensal">
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
                        <!--<Label :text="item.tipo" /> -->
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
    import * as http from "http";
    import * as ApplicationSettings from "application-settings";
    import moment from "moment"

    export default {
        data() {
            return {
            }
        },
        created(){
            //criar o objeto meta com seus respectivos valores
            this.$store.dispatch("getGastosMensal", {url:"http://10.0.2.2:8000/gastos/"})
            this.$store.dispatch("getMeta", {url:"http://10.0.2.2:8000/meta/?email=", email:this.usuario.email})
        },
        mounted(){
            
        },
        updated() {
            SelectedPageService.getInstance().updateSelectedPage("Home")
        },
        computed: {
            usuario(){
                return this.$store.state.usuario
            },
            meta(){
                return this.$store.state.meta
            },
            gastos_mensal(){
                return this.$store.state.gastos_mensal
            }
        },
        methods: {
            retorna_tempo_restante_meta(){
                var data1 = moment(this.meta.data_inicial, "DD_MM_YYYY").locale('pt-br').format('YYYY-MM-DD')
                var data2 = moment(this.meta.data_final, "DD_MM_YYYY").locale('pt-br').format('YYYY-MM-DD')
                var startDate = Date.parse(data1);
                var endDate = Date.parse(data2);
                var timeDiff = endDate - startDate;
                return Math.floor(timeDiff / (1000 * 60 * 60 * 24))
            },
            gastos_mensal_total(){
                var totalGastoMensal = 0
                for(var i = 0; i < this.gastos_mensal.length;i++){
                    totalGastoMensal += this.gastos_mensal[i].valor
                }
                return totalGastoMensal
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
        margin-bottom: 15;
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
