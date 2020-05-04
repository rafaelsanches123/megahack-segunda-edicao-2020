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
                    @scanResult="scanResult"
                    v-if="isIOS">
                </BarcodeScanner>
            </StackLayout>

            

        </StackLayout>

    </Page>
</template>

<script>
    import * as utils from "~/shared/utils";
    import SelectedPageService from "../shared/selected-page-service";
    const BarcodeScanner = require("nativescript-barcodescanner").BarcodeScanner;

    export default {
        components: {
		"BarcodeScanner": require("nativescript-barcodescanner").BarcodeScannerView
	    },
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
        created(){
        },
        mounted() {
            SelectedPageService.getInstance().updateSelectedPage("Tips");
        },
        computed: {
            usuario(){
                return this.$store.state.usuario
            },
            meta(){
                return this.$store.state.meta
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
            onScan() {
			this.scanner.scan({
				formats: "QR_CODE, EAN_13",
				showFlipCameraButton: true,   
				preferFrontCamera: false,     
				showTorchButton: true,        
				beepOnScan: true,             
				torchOn: false,               
				resultDisplayDuration: 500,   
				openSettingsIfPermissionWasPreviouslyDenied: true //ios only 
			}).then((result) => {
                //atualizar tabela que armazena os gastos mensais
                console.log({
					title: "You Scanned ",
					message: "Format: " + result.format + ",\nContent: " + result.text,
					okButtonText: "OK"
                });
                
			}, (errorMessage) => {
                console.log("Error when scanning " + errorMessage);
                console.log("Você parou de scannear o QR CODE e clicou em voltar!");
			});
		},
		scanResult(result) {
			console.log(`Format: ${ result.format }, Value: ${ result.text }`);
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
