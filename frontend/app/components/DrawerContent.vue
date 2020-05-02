<template lang="html">
<GridLayout rows="auto, *" class="nt-drawer__content">
            <StackLayout row="0" class="nt-drawer__header">
                <Image class="nt-drawer__header-image fas t-36" src.decode="font://&#xf2bd;"></Image>
                <Label class="nt-drawer__header-brand" text="User Name"></Label>
                <Label class="nt-drawer__header-footnote" text="username@mail.com"></Label>
            </StackLayout>
        
            <ScrollView row="1" class="nt-drawer__body">
                <StackLayout>
                    <GridLayout columns="auto, *" :class="'nt-drawer__list-item' + (selectedPage === 'Home' ? ' -selected': '')" @tap="onNavigationItemTap(Home)">
                        <Label col="0" text.decode="&#xf015;" class="nt-icon fas"></Label>
                        <Label col="1" text="Home" class="p-r-10"></Label>
                    </GridLayout>

                    <GridLayout columns="auto, *" :class="'nt-drawer__list-item' + (selectedPage === 'Ranking' ? ' -selected': '')" @tap="onNavigationItemTap(Ranking)">
                        <Label col="0" text.decode="&#xf015;" class="nt-icon fas"></Label>
                        <Label col="1" text="Recomendação do Dia" class="p-r-10"></Label>
                    </GridLayout>

                    <GridLayout columns="auto, *" :class="'nt-drawer__list-item' + (selectedPage === 'Meta' ? ' -selected': '')" @tap="onNavigationItemTap(Meta)">
                        <Label col="0" text.decode="&#xf015;" class="nt-icon fas"></Label>
                        <Label col="1" text="Meta" class="p-r-10"></Label>
                    </GridLayout>

                    <GridLayout columns="auto, *" :class="'nt-drawer__list-item' + (selectedPage === 'Tips' ? ' -selected': '')" @tap="onNavigationItemTap(Tips)">
                        <Label col="0" text.decode="&#xf015;" class="nt-icon fas"></Label>
                        <Label col="1" text="Dica do Dia" class="p-r-10"></Label>
                    </GridLayout>

        
                    <StackLayout class="hr"></StackLayout>

                    <GridLayout columns="auto, *" :class="'nt-drawer__list-item' + (selectedPage === 'Settings' ? ' -selected': '')" @tap="onNavigationItemTap(Settings)">
                        <Label col="0" text.decode="&#xf013;" class="nt-icon fas"></Label>
                        <Label col="1" text="Preferências" class="p-r-10"></Label>
                    </GridLayout>
                </StackLayout>
            </ScrollView>
        </GridLayout>
</template>

<script>
    import Login from "./Login";
    import Home from "./Home";
    import Ranking from "./Ranking";
    import Meta from "./Meta";
    import Tips from "./Tips";
    import Settings from "./Settings";
    import * as utils from "~/shared/utils";
    import SelectedPageService from "~/shared/selected-page-service";    
    
    export default {
        mounted() {
            SelectedPageService.getInstance().selectedPage$
                .subscribe((selectedPage) => this.selectedPage = selectedPage);
        },
        data () {
            return {
                Login: Login,
                Home: Home,
                Ranking: Ranking,
                Tips: Tips,
                Settings: Settings,
                Meta: Meta,
                selectedPage: ""
            };
        },
        components: {
            Login,
            Home,
            Ranking,
            Meta,
            Tips,
            Settings
        },
        methods: {
            onNavigationItemTap(component) {
                this.$navigateTo(component, {
                    clearHistory: true
                });
                utils.closeDrawer();
            }
        }
    };
</script>

<style scoped lang="scss">
    // Start custom common variables
    @import '~@nativescript/theme/scss/variables/blue';
    // End custom common variables

    // Custom styles
</style>
