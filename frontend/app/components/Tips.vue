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
            <Label class="action-bar-title" text="Dica do Dia"></Label>
        </ActionBar>

        <StackLayout class="page__content">
            
            <StackLayout class="">
                <Image class="logo" src="~/images/tips.png" width="100" height="100" stretch="aspectFill" />
                <Label class="header" text="DICA DO DIA!" />
                <Label class="sub-header" textWrap="true" :text="sub_text" />
            </StackLayout>
    
            <StackLayout class="">
                <Label class="text-tip" textWrap="true" :text="descricao_dica" />
                <Label textWrap="true" class="text-tip-partner">
                    <FormattedString>
                        <Span :text="partner" />
                        <Span text=" " />
                        <Span :text="partner_name" />
                        <Span text="..." />
                    </FormattedString>
                </Label>
                <StackLayout class="tip-partner">
                    <Webview src="https://www.youtube.com/watch?v=shfYMvEXqm4&feature=emb_title"></Webview>
                </StackLayout>
            </StackLayout>

            

        </StackLayout>

    </Page>
</template>

<script>
    import * as utils from "~/shared/utils";
    import SelectedPageService from "../shared/selected-page-service";

    export default {
        data() {
            return {
                descricao_dica:"Você sabe o que é reserva de emergência? Uma reserva de emergência é quantia de dinheiro referente ao quanto você gasta de dinheiro para viver durante 1 mês e você multiplica esse valor por 6! Esse dinheiro você usa para situações nas quais aconteça algum problema com você como perder o emprego e até mesmo em uma pandemia! Reflita sobre isso e comece agora mesmo a montar sua reserva de emergência e não se preocupe, vamos te ajudar!",
                data_atual: new Date(),
                sub_text: "Bora aprender mais sobre educação financeira!",
                partner: "Continue aprendendo sobre esse conteúdo com a nossa parceira",
                partner_name: "Nathalia Arcuri",
                link_partner: 'https://www.youtube.com/watch?v=shfYMvEXqm4&feature=emb_title'
            }
        },
        mounted() {
            SelectedPageService.getInstance().updateSelectedPage("Tips");
        },
        computed: {
            meta(){
                return this.meta
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
        padding: 20px 0px;
    }
    .text-tip{
        font-size: 18;
        font-weight: 300;
        padding-left: 60px;
        padding-right: 60px;
        padding-top: 10px;
        padding-bottom: 25%;
    }
    .tip-partner{
        padding-left: 60px;
        padding-right: 10px;
        padding-bottom: 20%;
    }
    .text-tip-partner{
        font-size: 18;
        font-weight: 300;
        padding-left: 60px;
        padding-right: 60px;
        padding-top: 0px;
        padding-bottom: 25%;
    }
</style>
