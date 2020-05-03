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
            <Label class="action-bar-title" text="Recomendação do Dia"></Label>
        </ActionBar>

        <StackLayout class="page__content">
            <StackLayout class="">
                <Image class="logo" src="~/images/recomendation.png" width="100" height="100" stretch="aspectFill" />
                <Label class="header" text="RECOMENDAÇÃO DO DIA" />
                <Label class="sub-header" textWrap="true" text="Coma por um preço justo, com boa qualidade e por indicação de outros salvadores!" />
            </StackLayout>

            <ListView height="100%" class="list-view" for="item in lista_ranking">
            <v-template>
                <GridLayout columns="2*, *" rows="*, *" class="lista-item"> 
                    <StackLayout row="0" col="0" class="titulo-parceiro">
                        <Label :text="item.nome" />
                    </StackLayout>
                    <StackLayout row="0" col="1">
                        <Label>
                            <FormattedString>
                                <Span  text="R$ " fontWeight="bold" />
                                <Span :text="formatPrice(item.valor)" fontWeight="bold" />
                            </FormattedString>
                        </Label>
                    </StackLayout>
                    <StackLayout class="" orientation="horizontal" row="1" col="0">
                        <StarRating emptyBorderColor="black" emptyColor="white" filledBorderColor="black" filledColor="yellow" :value="item.numero_estrelas_prato" max="5"/>
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
            }
        },
        created(){
            //criar o objeto meta com seus respectivos valores
            this.$store.dispatch("getRanking", {url:"http://10.0.2.2:8000/ranking/"})
        },
        mounted() {
            SelectedPageService.getInstance().updateSelectedPage("Ranking");
        },
        computed: {
            lista_ranking(){
                return this.$store.state.ranking
            }
        },
        methods: {
            onDrawerButtonTap() {
                utils.showDrawer();
            },
            formatPrice(value) {
                let val = (value/1).toFixed(2).replace('.', ',')
                return val.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ".")
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
    .lista-item{
        font-weight: 300;
        font-size: 14;
        background-color: #FFFFFF;
    }
    .list-view{
        padding: 0px 5%;
    }
    .titulo-parceiro{
        font-weight: 500;
    }
</style>
