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
            <Label class="action-bar-title" text="Faça seu Checking Aqui!"></Label>
        </ActionBar>

        <StackLayout class="page__content">
            
            <StackLayout class="">
                <Image class="logo" src="~/images/location.png" width="100" height="100" stretch="aspectFit" />
                <Label class="header" text="CHECKING" />
                <Label class="sub-header" textWrap="true" :text="sub_text" />
            </StackLayout>
    
            <StackLayout class="">
                <Button class="btn btn-primary" @tap="onScan">LER QR CODE</Button>
                <BarcodeScanner
                    row="1"
                    height="300"
                    formats="QR_CODE, EAN_13, UPC_A"
                    beepOnScan="true"
                    reportDuplicates="true"
                    preferFrontCamera="false"
                    :pause="pause"
                    @scanResult="onScanResult"
                    v-if="isIOS">
                </BarcodeScanner>
            </StackLayout>

            

        </StackLayout>

    </Page>
</template>

<script>
    import * as utils from "~/shared/utils";
    import SelectedPageService from "../shared/selected-page-service";
    import Home from "./Home";
    import * as http from "http";
    import {isIOS} from "tns-core-modules/platform";
    import {BarcodeScanner} from "nativescript-barcodescanner";

    export default {
        data() {
            return {
                scanner: null,
                sub_text: "Nessa área você faz a leitura do QR CODE no parceiro e válida sua presença e com isso automaticamente nós atualizamos seu gasto mensal e quanto você está economizando", 
                isIOS: false,
                pause: false
            }
        },
        async created() {
		    this.scanner = new BarcodeScanner();
        },
        mounted() {
            SelectedPageService.getInstance().updateSelectedPage("Checking");
        },
        computed: {
            usuario(){
                return this.$store.state.usuario
            }
        },
        methods: {
            onDrawerButtonTap() {
                utils.showDrawer();
            },
            formatPrice(value) {
                let val = (value/1).toFixed(2).replace('.', ',')
                return val.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ".")
            },
            onScanResult(evt) {
                console.log(`onScanResult: ${evt.text} (${evt.format})`);
            },
            onScan(front) {
                    new BarcodeScanner().scan({
                    cancelLabel: "EXIT. Also, try the volume buttons!", // iOS only, default 'Close'
                    cancelLabelBackgroundColor: "#333333", // iOS only, default '#000000' (black)
                    message: "Use the volume buttons for extra light", // Android only, default is 'Place a barcode inside the viewfinder rectangle to scan it.'
                    preferFrontCamera: front,     // Android only, default false
                    showFlipCameraButton: true,   // default false
                    showTorchButton: true,        // iOS only, default false
                    torchOn: false,               // launch with the flashlight on (default false)
                    resultDisplayDuration: 500,   // Android only, default 1500 (ms), set to 0 to disable echoing the scanned text
                    beepOnScan: true,             // Play or Suppress beep on scan (default true)
                    openSettingsIfPermissionWasPreviouslyDenied: true, // On iOS you can send the user to the settings app if access was previously denied
                    closeCallback: () => {
                        console.log("Scanner closed @ " + new Date().getTime());
                    }
                    }).then(
                        (result) => {
                        console.log("--- scanned: " + result.text);
                        // Note that this Promise is never invoked when a 'continuousScanCallback' function is provided
                        setTimeout( () => {
                            
                            //console.log( JSON.parse(JSON.stringify(result.text)) )
                            var res_json = JSON.parse(result.text)
                            //console.log( res_json )
                            http.request({
                            url: "http://10.0.2.2:8000/checking/",
                            method: "POST",
                            headers: { "Content-Type": "application/json" },
                            content: JSON.stringify({
                                'nome'  : res_json.nome,
                                'valor' : res_json.valor,
                                'data'  : res_json.data
                            })
                            }).then(response => {
                            
                            var res = response.content.toJSON();
                            console.log(res)
                            this.$navigateTo(Home)
                            //if (res.statusCode == 200){    
                            //}
                            }, error => {
                                console.error(error);
                                this.alert("Erro com a conexão ao servidor. Tente novamente mais tarde!")
                            });
                            
                        }, 500);
                    },
                    function (errorMessage) {
                    console.log("No scan. " + errorMessage);
                    }
                );
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
    
</style>
