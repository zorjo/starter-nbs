import httpx
import asyncio
from bs4 import BeautifulSoup
urlraw = """https://flipkart.com/campus-sutra-men-solid-casual-blue-shirt/p/itm4af004efa60d0?pid=SHTH28GU6RCHKDT4&lid=LSTSHTH28GU6RCHKDT41UJQAN&marketplace=FLIPKART&q=campusstura&store=clo&srno=s_1_1&otracker=search&fm=organic&iid=b34ff6aa-ca04-421c-8473-d3a70b7d3028.SHTH28GU6RCHKDT4.SEARCH&ppt=None&ppn=None&ssid=e6xu8qn8680000001722578248116&qH=7a3ae33810fb2b2f
https://flipkart.com/campus-sutra-men-printed-casual-multicolor-shirt/p/itmdbdd7447a8974?pid=SHTH28GURVZEGZPM&lid=LSTSHTH28GURVZEGZPMFP1ERI&marketplace=FLIPKART&q=campusstura&store=clo&srno=s_1_2&otracker=search&fm=organic&iid=b34ff6aa-ca04-421c-8473-d3a70b7d3028.SHTH28GURVZEGZPM.SEARCH&ppt=None&ppn=None&ssid=e6xu8qn8680000001722578248116&qH=7a3ae33810fb2b2f
https://flipkart.com/campus-sutra-solid-women-crew-neck-black-t-shirt/p/itm435d3d31db762?pid=TSHH27TZ3G4XWADT&lid=LSTTSHH27TZ3G4XWADTPKRDFN&marketplace=FLIPKART&q=campusstura&store=clo&srno=s_1_3&otracker=search&fm=organic&iid=b34ff6aa-ca04-421c-8473-d3a70b7d3028.TSHH27TZ3G4XWADT.SEARCH&ppt=None&ppn=None&ssid=e6xu8qn8680000001722578248116&qH=7a3ae33810fb2b2f
https://flipkart.com/campus-sutra-solid-women-crew-neck-pink-t-shirt/p/itm7734d73b722df?pid=TSHH27TZDHHXBHHZ&lid=LSTTSHH27TZDHHXBHHZ0L0NRX&marketplace=FLIPKART&q=campusstura&store=clo&srno=s_1_4&otracker=search&fm=organic&iid=b34ff6aa-ca04-421c-8473-d3a70b7d3028.TSHH27TZDHHXBHHZ.SEARCH&ppt=None&ppn=None&ssid=e6xu8qn8680000001722578248116&qH=7a3ae33810fb2b2f
https://flipkart.com/campus-sutra-solid-women-crew-neck-blue-t-shirt/p/itmc3dc296177e4c?pid=TSHH27TZZCUCYAMT&lid=LSTTSHH27TZZCUCYAMTS5K4MV&marketplace=FLIPKART&q=campusstura&store=clo&srno=s_1_5&otracker=search&fm=organic&iid=b34ff6aa-ca04-421c-8473-d3a70b7d3028.TSHH27TZZCUCYAMT.SEARCH&ppt=None&ppn=None&ssid=e6xu8qn8680000001722578248116&qH=7a3ae33810fb2b2f
https://flipkart.com/campus-sutra-casual-solid-women-red-top/p/itm6c79b7398862c?pid=TOPH27T8XWHFFJG4&lid=LSTTOPH27T8XWHFFJG47ID8J1&marketplace=FLIPKART&q=campusstura&store=clo&srno=s_1_6&otracker=search&fm=organic&iid=b34ff6aa-ca04-421c-8473-d3a70b7d3028.TOPH27T8XWHFFJG4.SEARCH&ppt=None&ppn=None&ssid=e6xu8qn8680000001722578248116&qH=7a3ae33810fb2b2f
https://flipkart.com/campus-sutra-men-checkered-casual-white-shirt/p/itm1950a3d1beb32?pid=SHTH27SGKZW5JBU4&lid=LSTSHTH27SGKZW5JBU4ECBBG2&marketplace=FLIPKART&q=campusstura&store=clo&srno=s_1_7&otracker=search&fm=organic&iid=b34ff6aa-ca04-421c-8473-d3a70b7d3028.SHTH27SGKZW5JBU4.SEARCH&ppt=None&ppn=None&ssid=e6xu8qn8680000001722578248116&qH=7a3ae33810fb2b2f
https://flipkart.com/campus-sutra-men-solid-casual-green-shirt/p/itma75c75393eefb?pid=SHTH27SG8MHTZNEM&lid=LSTSHTH27SG8MHTZNEM8OCAS0&marketplace=FLIPKART&q=campusstura&store=clo&srno=s_1_8&otracker=search&fm=organic&iid=b34ff6aa-ca04-421c-8473-d3a70b7d3028.SHTH27SG8MHTZNEM.SEARCH&ppt=None&ppn=None&ssid=e6xu8qn8680000001722578248116&qH=7a3ae33810fb2b2f
https://flipkart.com/campus-sutra-solid-men-round-neck-blue-t-shirt/p/itmc7fe0951c399a?pid=TSHH27SKHBPEFZ2G&lid=LSTTSHH27SKHBPEFZ2GDTNWR2&marketplace=FLIPKART&q=campusstura&store=clo&srno=s_1_9&otracker=search&fm=organic&iid=b34ff6aa-ca04-421c-8473-d3a70b7d3028.TSHH27SKHBPEFZ2G.SEARCH&ppt=None&ppn=None&ssid=e6xu8qn8680000001722578248116&qH=7a3ae33810fb2b2f
https://flipkart.com/campus-sutra-casual-graphic-print-women-red-top/p/itmd223a24fa9803?pid=TOPH27T6ZVPQ39HT&lid=LSTTOPH27T6ZVPQ39HTRZN6SW&marketplace=FLIPKART&q=campusstura&store=clo&srno=s_1_10&otracker=search&fm=organic&iid=b34ff6aa-ca04-421c-8473-d3a70b7d3028.TOPH27T6ZVPQ39HT.SEARCH&ppt=None&ppn=None&ssid=e6xu8qn8680000001722578248116&qH=7a3ae33810fb2b2f
https://flipkart.com/campus-sutra-men-graphic-print-black-top-shorts-set/p/itm08955385d5040?pid=NSTH27SZNKZFXJPV&lid=LSTNSTH27SZNKZFXJPVCIK7WR&marketplace=FLIPKART&q=campusstura&store=clo&srno=s_1_11&otracker=search&fm=organic&iid=b34ff6aa-ca04-421c-8473-d3a70b7d3028.NSTH27SZNKZFXJPV.SEARCH&ppt=None&ppn=None&ssid=e6xu8qn8680000001722578248116&qH=7a3ae33810fb2b2f
https://flipkart.com/campus-sutra-men-checkered-casual-multicolor-shirt/p/itmb09b43460c3c4?pid=SHTH27SGNWE3XAGT&lid=LSTSHTH27SGNWE3XAGTSPIRRP&marketplace=FLIPKART&q=campusstura&store=clo&srno=s_1_12&otracker=search&fm=organic&iid=b34ff6aa-ca04-421c-8473-d3a70b7d3028.SHTH27SGNWE3XAGT.SEARCH&ppt=None&ppn=None&ssid=e6xu8qn8680000001722578248116&qH=7a3ae33810fb2b2f
https://flipkart.com/campus-sutra-colorblock-men-henley-neck-multicolor-t-shirt/p/itm1dd5752f68a9a?pid=TSHH27SNWDDHFHCS&lid=LSTTSHH27SNWDDHFHCSM4FFYS&marketplace=FLIPKART&q=campusstura&store=clo&srno=s_1_13&otracker=search&fm=organic&iid=b34ff6aa-ca04-421c-8473-d3a70b7d3028.TSHH27SNWDDHFHCS.SEARCH&ppt=None&ppn=None&ssid=e6xu8qn8680000001722578248116&qH=7a3ae33810fb2b2f
https://flipkart.com/campus-sutra-colorblock-men-henley-neck-green-t-shirt/p/itm31d679b83db1b?pid=TSHH27SNSGZH8UPY&lid=LSTTSHH27SNSGZH8UPYTSTU4K&marketplace=FLIPKART&q=campusstura&store=clo&srno=s_1_14&otracker=search&fm=organic&iid=b34ff6aa-ca04-421c-8473-d3a70b7d3028.TSHH27SNSGZH8UPY.SEARCH&ppt=None&ppn=None&ssid=e6xu8qn8680000001722578248116&qH=7a3ae33810fb2b2f
https://flipkart.com/campus-sutra-men-graphic-print-green-top-shorts-set/p/itmcda9219eb1b86?pid=NSTH27SZMCFN9N9J&lid=LSTNSTH27SZMCFN9N9JQGLVH5&marketplace=FLIPKART&q=campusstura&store=clo&srno=s_1_15&otracker=search&fm=organic&iid=b34ff6aa-ca04-421c-8473-d3a70b7d3028.NSTH27SZMCFN9N9J.SEARCH&ppt=None&ppn=None&ssid=e6xu8qn8680000001722578248116&qH=7a3ae33810fb2b2f
https://flipkart.com/campus-sutra-colorblock-men-crew-neck-blue-t-shirt/p/itm9db3a1641dc6b?pid=TSHH27SKGUNQBUFJ&lid=LSTTSHH27SKGUNQBUFJMVLAZS&marketplace=FLIPKART&q=campusstura&store=clo&srno=s_1_16&otracker=search&fm=organic&iid=b34ff6aa-ca04-421c-8473-d3a70b7d3028.TSHH27SKGUNQBUFJ.SEARCH&ppt=None&ppn=None&ssid=e6xu8qn8680000001722578248116&qH=7a3ae33810fb2b2f
https://flipkart.com/campus-sutra-men-graphic-print-green-top-shorts-set/p/itm78a18831340af?pid=NSTH27SSZRCY5CFV&lid=LSTNSTH27SSZRCY5CFV2JVYPA&marketplace=FLIPKART&q=campusstura&store=clo&srno=s_1_17&otracker=search&fm=organic&iid=b34ff6aa-ca04-421c-8473-d3a70b7d3028.NSTH27SSZRCY5CFV.SEARCH&ppt=None&ppn=None&ssid=e6xu8qn8680000001722578248116&qH=7a3ae33810fb2b2f
https://flipkart.com/campus-sutra-women-two-piece-dress-pink/p/itm05b49eee81e07?pid=DREH27TZHD4G3VQG&lid=LSTDREH27TZHD4G3VQGRQZNBQ&marketplace=FLIPKART&q=campusstura&store=clo&srno=s_1_18&otracker=search&fm=organic&iid=b34ff6aa-ca04-421c-8473-d3a70b7d3028.DREH27TZHD4G3VQG.SEARCH&ppt=None&ppn=None&ssid=e6xu8qn8680000001722578248116&qH=7a3ae33810fb2b2f
https://flipkart.com/campus-sutra-men-printed-casual-multicolor-shirt/p/itma2fbfef950c55?pid=SHTH27SGEH9QXV4B&lid=LSTSHTH27SGEH9QXV4BAWNWFZ&marketplace=FLIPKART&q=campusstura&store=clo&srno=s_1_19&otracker=search&fm=organic&iid=b34ff6aa-ca04-421c-8473-d3a70b7d3028.SHTH27SGEH9QXV4B.SEARCH&ppt=None&ppn=None&ssid=e6xu8qn8680000001722578248116&qH=7a3ae33810fb2b2f
https://flipkart.com/campus-sutra-casual-printed-women-multicolor-top/p/itm7da0c1f4bfc5d?pid=TOPH27T2S5BPNZGM&lid=LSTTOPH27T2S5BPNZGMZWLVME&marketplace=FLIPKART&q=campusstura&store=clo&srno=s_1_20&otracker=search&fm=organic&iid=b34ff6aa-ca04-421c-8473-d3a70b7d3028.TOPH27T2S5BPNZGM.SEARCH&ppt=None&ppn=None&ssid=e6xu8qn8680000001722578248116&qH=7a3ae33810fb2b2f
https://flipkart.com/campus-sutra-casual-solid-women-yellow-top/p/itmd2c372dbc3946?pid=TOPH27T83STGQPVB&lid=LSTTOPH27T83STGQPVB317YLT&marketplace=FLIPKART&q=campusstura&store=clo&srno=s_1_21&otracker=search&fm=organic&iid=b34ff6aa-ca04-421c-8473-d3a70b7d3028.TOPH27T83STGQPVB.SEARCH&ppt=None&ppn=None&ssid=e6xu8qn8680000001722578248116&qH=7a3ae33810fb2b2f
https://flipkart.com/campus-sutra-men-checkered-casual-grey-shirt/p/itmf3fc00fd9f2e3?pid=SHTH27SGWB2Z4AXM&lid=LSTSHTH27SGWB2Z4AXMSYW9BA&marketplace=FLIPKART&q=campusstura&store=clo&srno=s_1_22&otracker=search&fm=organic&iid=b34ff6aa-ca04-421c-8473-d3a70b7d3028.SHTH27SGWB2Z4AXM.SEARCH&ppt=None&ppn=None&ssid=e6xu8qn8680000001722578248116&qH=7a3ae33810fb2b2f
https://flipkart.com/campus-sutra-women-two-piece-dress-grey/p/itm78cd17ad8cdb0?pid=DREH27TU8GTG6DMN&lid=LSTDREH27TU8GTG6DMNVYQ31E&marketplace=FLIPKART&q=campusstura&store=clo&srno=s_1_23&otracker=search&fm=organic&iid=b34ff6aa-ca04-421c-8473-d3a70b7d3028.DREH27TU8GTG6DMN.SEARCH&ppt=None&ppn=None&ssid=e6xu8qn8680000001722578248116&qH=7a3ae33810fb2b2f
https://flipkart.com/campus-sutra-women-two-piece-dress-red/p/itm79432b6d67ff9?pid=DREH27TUNBEJZAFZ&lid=LSTDREH27TUNBEJZAFZNK5AWT&marketplace=FLIPKART&q=campusstura&store=clo&srno=s_1_24&otracker=search&fm=organic&iid=b34ff6aa-ca04-421c-8473-d3a70b7d3028.DREH27TUNBEJZAFZ.SEARCH&ppt=None&ppn=None&ssid=e6xu8qn8680000001722578248116&qH=7a3ae33810fb2b2f
https://flipkart.com/campus-sutra-men-graphic-print-black-top-shorts-set/p/itma58d5a0dcd3be?pid=NSTH27SZTDZGZVXK&lid=LSTNSTH27SZTDZGZVXKUDANC7&marketplace=FLIPKART&q=campusstura&store=clo&srno=s_1_25&otracker=search&fm=organic&iid=b34ff6aa-ca04-421c-8473-d3a70b7d3028.NSTH27SZTDZGZVXK.SEARCH&ppt=None&ppn=None&ssid=e6xu8qn8680000001722578248116&qH=7a3ae33810fb2b2f
https://flipkart.com/campus-sutra-men-solid-casual-white-shirt/p/itm6bcf4abb21407?pid=SHTH27SGGPYDRZSA&lid=LSTSHTH27SGGPYDRZSAMEHM3V&marketplace=FLIPKART&q=campusstura&store=clo&srno=s_1_26&otracker=search&fm=organic&iid=b34ff6aa-ca04-421c-8473-d3a70b7d3028.SHTH27SGGPYDRZSA.SEARCH&ppt=None&ppn=None&ssid=e6xu8qn8680000001722578248116&qH=7a3ae33810fb2b2f
https://flipkart.com/campus-sutra-men-graphic-print-black-top-shorts-set/p/itme579c0bec4d1a?pid=NSTH27SSZKHC3YSM&lid=LSTNSTH27SSZKHC3YSMCHYLSV&marketplace=FLIPKART&q=campusstura&store=clo&srno=s_1_27&otracker=search&fm=organic&iid=b34ff6aa-ca04-421c-8473-d3a70b7d3028.NSTH27SSZKHC3YSM.SEARCH&ppt=None&ppn=None&ssid=e6xu8qn8680000001722578248116&qH=7a3ae33810fb2b2f
https://flipkart.com/campus-sutra-men-graphic-print-pink-top-shorts-set/p/itm205dd3c7cf4d8?pid=NSTH27SZJTNMNHVJ&lid=LSTNSTH27SZJTNMNHVJN2RZIX&marketplace=FLIPKART&q=campusstura&store=clo&srno=s_1_28&otracker=search&fm=organic&iid=b34ff6aa-ca04-421c-8473-d3a70b7d3028.NSTH27SZJTNMNHVJ.SEARCH&ppt=None&ppn=None&ssid=e6xu8qn8680000001722578248116&qH=7a3ae33810fb2b2f
https://flipkart.com/campus-sutra-men-solid-black-top-shorts-set/p/itm753af9989fad5?pid=NSTH22ZUDX2BHZBY&lid=LSTNSTH22ZUDX2BHZBYVQLPD2&marketplace=FLIPKART&q=campusstura&store=clo&srno=s_1_29&otracker=search&fm=organic&iid=b34ff6aa-ca04-421c-8473-d3a70b7d3028.NSTH22ZUDX2BHZBY.SEARCH&ppt=None&ppn=None&ssid=e6xu8qn8680000001722578248116&qH=7a3ae33810fb2b2f
https://flipkart.com/campus-sutra-men-self-design-white-top-shorts-set/p/itm700406c5fdd86?pid=NSTH22ZUFQZJRCBW&lid=LSTNSTH22ZUFQZJRCBWBUKZTI&marketplace=FLIPKART&q=campusstura&store=clo&srno=s_1_30&otracker=search&fm=organic&iid=b34ff6aa-ca04-421c-8473-d3a70b7d3028.NSTH22ZUFQZJRCBW.SEARCH&ppt=None&ppn=None&ssid=e6xu8qn8680000001722578248116&qH=7a3ae33810fb2b2f
https://flipkart.com/campus-sutra-men-self-design-grey-top-shorts-set/p/itmb5828d19caac7?pid=NSTH22ZUSHYRBTEP&lid=LSTNSTH22ZUSHYRBTEPFJV0LB&marketplace=FLIPKART&q=campusstura&store=clo&srno=s_1_31&otracker=search&fm=organic&iid=b34ff6aa-ca04-421c-8473-d3a70b7d3028.NSTH22ZUSHYRBTEP.SEARCH&ppt=None&ppn=None&ssid=e6xu8qn8680000001722578248116&qH=7a3ae33810fb2b2f
https://flipkart.com/campus-sutra-regular-fit-men-brown-trousers/p/itmcaf4a0bdc122b?pid=TROH22ZPNN5YDDUF&lid=LSTTROH22ZPNN5YDDUFCUBD6L&marketplace=FLIPKART&q=campusstura&store=clo&srno=s_1_32&otracker=search&fm=organic&iid=b34ff6aa-ca04-421c-8473-d3a70b7d3028.TROH22ZPNN5YDDUF.SEARCH&ppt=None&ppn=None&ssid=e6xu8qn8680000001722578248116&qH=7a3ae33810fb2b2f
https://flipkart.com/campus-sutra-regular-men-blue-jeans/p/itm41c26aa5faafb?pid=JEAH22YRRZA9W8AX&lid=LSTJEAH22YRRZA9W8AXECWCNX&marketplace=FLIPKART&q=campusstura&store=clo&srno=s_1_33&otracker=search&fm=organic&iid=b34ff6aa-ca04-421c-8473-d3a70b7d3028.JEAH22YRRZA9W8AX.SEARCH&ppt=None&ppn=None&ssid=e6xu8qn8680000001722578248116&qH=7a3ae33810fb2b2f
https://flipkart.com/campus-sutra-solid-men-brown-casual-shorts/p/itmebe96ea4f0127?pid=SRTH23YEWEHT4FFN&lid=LSTSRTH23YEWEHT4FFNH1XGZT&marketplace=FLIPKART&q=campusstura&store=clo&srno=s_1_34&otracker=search&fm=organic&iid=b34ff6aa-ca04-421c-8473-d3a70b7d3028.SRTH23YEWEHT4FFN.SEARCH&ppt=None&ppn=None&ssid=e6xu8qn8680000001722578248116&qH=7a3ae33810fb2b2f
https://flipkart.com/campus-sutra-regular-men-blue-jeans/p/itm6c30bf0fd69a9?pid=JEAH22YSSAESYJG5&lid=LSTJEAH22YSSAESYJG5FKUCD9&marketplace=FLIPKART&q=campusstura&store=clo&srno=s_1_35&otracker=search&fm=organic&iid=b34ff6aa-ca04-421c-8473-d3a70b7d3028.JEAH22YSSAESYJG5.SEARCH&ppt=None&ppn=None&ssid=e6xu8qn8680000001722578248116&qH=7a3ae33810fb2b2f
https://flipkart.com/campus-sutra-men-solid-blue-top-shorts-set/p/itma19a722ae386c?pid=NSTH22ZUHVHSPP9G&lid=LSTNSTH22ZUHVHSPP9GEIYIYP&marketplace=FLIPKART&q=campusstura&store=clo&srno=s_1_36&otracker=search&fm=organic&iid=b34ff6aa-ca04-421c-8473-d3a70b7d3028.NSTH22ZUHVHSPP9G.SEARCH&ppt=None&ppn=None&ssid=e6xu8qn8680000001722578248116&qH=7a3ae33810fb2b2f
https://flipkart.com/campus-sutra-regular-fit-men-beige-trousers/p/itm5617247bf02a0?pid=TROH22ZPQXZHW39Q&lid=LSTTROH22ZPQXZHW39Q7WJMQA&marketplace=FLIPKART&q=campusstura&store=clo&srno=s_1_37&otracker=search&fm=organic&iid=b34ff6aa-ca04-421c-8473-d3a70b7d3028.TROH22ZPQXZHW39Q.SEARCH&ppt=None&ppn=None&ssid=e6xu8qn8680000001722578248116&qH=7a3ae33810fb2b2f
https://flipkart.com/campus-sutra-men-self-design-casual-blue-shirt/p/itm86f589c5a0944?pid=SHTH225JCTFHDZDF&lid=LSTSHTH225JCTFHDZDF29AX7H&marketplace=FLIPKART&q=campusstura&store=clo&srno=s_1_38&otracker=search&fm=organic&iid=b34ff6aa-ca04-421c-8473-d3a70b7d3028.SHTH225JCTFHDZDF.SEARCH&ppt=None&ppn=None&ssid=e6xu8qn8680000001722578248116&qH=7a3ae33810fb2b2f
https://flipkart.com/campus-sutra-men-printed-casual-beige-shirt/p/itm1146d17734dcb?pid=SHTH225GT4GWGKGG&lid=LSTSHTH225GT4GWGKGGRSUS98&marketplace=FLIPKART&q=campusstura&store=clo&srno=s_1_39&otracker=search&fm=organic&iid=b34ff6aa-ca04-421c-8473-d3a70b7d3028.SHTH225GT4GWGKGG.SEARCH&ppt=None&ppn=None&ssid=e6xu8qn8680000001722578248116&qH=7a3ae33810fb2b2f
https://flipkart.com/campus-sutra-men-printed-casual-blue-shirt/p/itm297e47c156684?pid=SHTH225GYCGMMYE5&lid=LSTSHTH225GYCGMMYE5M2NQ35&marketplace=FLIPKART&q=campusstura&store=clo&srno=s_1_40&otracker=search&fm=organic&iid=b34ff6aa-ca04-421c-8473-d3a70b7d3028.SHTH225GYCGMMYE5.SEARCH&ppt=None&ppn=None&ssid=e6xu8qn8680000001722578248116&qH=7a3ae33810fb2b2f
https://flipkart.com/campus-sutra-men-solid-casual-brown-shirt/p/itm89a9eb6d64d92?pid=SHTH225GRFGJAAHZ&lid=LSTSHTH225GRFGJAAHZFCO2EU&marketplace=FLIPKART&q=campusstura&store=clo&srno=s_2_41&otracker=search&fm=organic&iid=89c2f18f-dc22-4df6-9ae9-9489816b8f72.SHTH225GRFGJAAHZ.SEARCH&ppt=None&ppn=None&ssid=js9arsybi80000001722578249761&qH=7a3ae33810fb2b2f
https://flipkart.com/campus-sutra-men-self-design-casual-black-shirt/p/itm53f5401d32ade?pid=SHTH225G8KVHUEUK&lid=LSTSHTH225G8KVHUEUKX9CZMN&marketplace=FLIPKART&q=campusstura&store=clo&srno=s_2_42&otracker=search&fm=organic&iid=89c2f18f-dc22-4df6-9ae9-9489816b8f72.SHTH225G8KVHUEUK.SEARCH&ppt=None&ppn=None&ssid=js9arsybi80000001722578249761&qH=7a3ae33810fb2b2f
https://flipkart.com/campus-sutra-men-striped-casual-white-shirt/p/itme9a17c3dd1430?pid=SHTH225GAGZFDCZZ&lid=LSTSHTH225GAGZFDCZZIGLMNC&marketplace=FLIPKART&q=campusstura&store=clo&srno=s_2_43&otracker=search&fm=organic&iid=89c2f18f-dc22-4df6-9ae9-9489816b8f72.SHTH225GAGZFDCZZ.SEARCH&ppt=None&ppn=None&ssid=js9arsybi80000001722578249761&qH=7a3ae33810fb2b2f
https://flipkart.com/campus-sutra-men-solid-casual-pink-shirt/p/itmb801bc3f25cea?pid=SHTH225GFBDWDVGV&lid=LSTSHTH225GFBDWDVGVLQGPCE&marketplace=FLIPKART&q=campusstura&store=clo&srno=s_2_44&otracker=search&fm=organic&iid=89c2f18f-dc22-4df6-9ae9-9489816b8f72.SHTH225GFBDWDVGV.SEARCH&ppt=None&ppn=None&ssid=js9arsybi80000001722578249761&qH=7a3ae33810fb2b2f
https://flipkart.com/campus-sutra-men-solid-casual-purple-shirt/p/itm3ce258e3f3a76?pid=SHTH225GGHHQMY2H&lid=LSTSHTH225GGHHQMY2H4T4YIC&marketplace=FLIPKART&q=campusstura&store=clo&srno=s_2_45&otracker=search&fm=organic&iid=89c2f18f-dc22-4df6-9ae9-9489816b8f72.SHTH225GGHHQMY2H.SEARCH&ppt=None&ppn=None&ssid=js9arsybi80000001722578249761&qH=7a3ae33810fb2b2f
https://flipkart.com/campus-sutra-men-printed-casual-blue-shirt/p/itm2d5b1ba1e4a4c?pid=SHTH225GUZHWZ6YH&lid=LSTSHTH225GUZHWZ6YHQYAVMQ&marketplace=FLIPKART&q=campusstura&store=clo&srno=s_2_46&otracker=search&fm=organic&iid=89c2f18f-dc22-4df6-9ae9-9489816b8f72.SHTH225GUZHWZ6YH.SEARCH&ppt=None&ppn=None&ssid=js9arsybi80000001722578249761&qH=7a3ae33810fb2b2f
https://flipkart.com/campus-sutra-men-solid-self-design-casual-orange-shirt/p/itm9afcae68ef03e?pid=SHTH225JE45HU9YN&lid=LSTSHTH225JE45HU9YNJXPWWO&marketplace=FLIPKART&q=campusstura&store=clo&srno=s_2_47&otracker=search&fm=organic&iid=89c2f18f-dc22-4df6-9ae9-9489816b8f72.SHTH225JE45HU9YN.SEARCH&ppt=None&ppn=None&ssid=js9arsybi80000001722578249761&qH=7a3ae33810fb2b2f
https://flipkart.com/campus-sutra-men-printed-casual-green-shirt/p/itm6a6a33f20bf54?pid=SHTH225G6QZE5FFZ&lid=LSTSHTH225G6QZE5FFZQDXAEX&marketplace=FLIPKART&q=campusstura&store=clo&srno=s_2_48&otracker=search&fm=organic&iid=89c2f18f-dc22-4df6-9ae9-9489816b8f72.SHTH225G6QZE5FFZ.SEARCH&ppt=None&ppn=None&ssid=js9arsybi80000001722578249761&qH=7a3ae33810fb2b2f
https://flipkart.com/campus-sutra-men-solid-self-design-casual-green-shirt/p/itmad527fe3b44c6?pid=SHTH225JQZGQHQZM&lid=LSTSHTH225JQZGQHQZMIITDWJ&marketplace=FLIPKART&q=campusstura&store=clo&srno=s_2_49&otracker=search&fm=organic&iid=89c2f18f-dc22-4df6-9ae9-9489816b8f72.SHTH225JQZGQHQZM.SEARCH&ppt=None&ppn=None&ssid=js9arsybi80000001722578249761&qH=7a3ae33810fb2b2f
https://flipkart.com/campus-sutra-men-striped-casual-green-shirt/p/itm0fd0db200fe00?pid=SHTH225JNZHA8Q3R&lid=LSTSHTH225JNZHA8Q3RULEGJT&marketplace=FLIPKART&q=campusstura&store=clo&srno=s_2_50&otracker=search&fm=organic&iid=89c2f18f-dc22-4df6-9ae9-9489816b8f72.SHTH225JNZHA8Q3R.SEARCH&ppt=None&ppn=None&ssid=js9arsybi80000001722578249761&qH=7a3ae33810fb2b2f
https://flipkart.com/campus-sutra-men-printed-casual-blue-shirt/p/itmfa64179c3561c?pid=SHTH225G3DMFRGC2&lid=LSTSHTH225G3DMFRGC2S0IZBG&marketplace=FLIPKART&q=campusstura&store=clo&srno=s_2_51&otracker=search&fm=organic&iid=89c2f18f-dc22-4df6-9ae9-9489816b8f72.SHTH225G3DMFRGC2.SEARCH&ppt=None&ppn=None&ssid=js9arsybi80000001722578249761&qH=7a3ae33810fb2b2f
https://flipkart.com/campus-sutra-men-solid-casual-black-shirt/p/itmb9d1a96e73d7c?pid=SHTH225GUPKNZGAU&lid=LSTSHTH225GUPKNZGAURZXSVG&marketplace=FLIPKART&q=campusstura&store=clo&srno=s_2_52&otracker=search&fm=organic&iid=89c2f18f-dc22-4df6-9ae9-9489816b8f72.SHTH225GUPKNZGAU.SEARCH&ppt=None&ppn=None&ssid=js9arsybi80000001722578249761&qH=7a3ae33810fb2b2f
https://flipkart.com/campus-sutra-men-printed-casual-multicolor-shirt/p/itm1287db44a8da6?pid=SHTH225G4Y8GERJ2&lid=LSTSHTH225G4Y8GERJ2BZ3H9U&marketplace=FLIPKART&q=campusstura&store=clo&srno=s_2_53&otracker=search&fm=organic&iid=89c2f18f-dc22-4df6-9ae9-9489816b8f72.SHTH225G4Y8GERJ2.SEARCH&ppt=None&ppn=None&ssid=js9arsybi80000001722578249761&qH=7a3ae33810fb2b2f
https://flipkart.com/campus-sutra-men-solid-casual-blue-shirt/p/itm5c1bd0ecd0275?pid=SHTH225GCMRUQWD6&lid=LSTSHTH225GCMRUQWD6USMFCJ&marketplace=FLIPKART&q=campusstura&store=clo&srno=s_2_54&otracker=search&fm=organic&iid=89c2f18f-dc22-4df6-9ae9-9489816b8f72.SHTH225GCMRUQWD6.SEARCH&ppt=None&ppn=None&ssid=js9arsybi80000001722578249761&qH=7a3ae33810fb2b2f
https://flipkart.com/campus-sutra-men-embroidered-casual-cream-shirt/p/itm1599aa8a457e8?pid=SHTH225JAZSXSHJH&lid=LSTSHTH225JAZSXSHJHIO2BSE&marketplace=FLIPKART&q=campusstura&store=clo&srno=s_2_55&otracker=search&fm=organic&iid=89c2f18f-dc22-4df6-9ae9-9489816b8f72.SHTH225JAZSXSHJH.SEARCH&ppt=None&ppn=None&ssid=js9arsybi80000001722578249761&qH=7a3ae33810fb2b2f
https://flipkart.com/campus-sutra-men-checkered-casual-grey-shirt/p/itmcebb8f14e8163?pid=SHTH225GFZGJBHMX&lid=LSTSHTH225GFZGJBHMXXOQQJ3&marketplace=FLIPKART&q=campusstura&store=clo&srno=s_2_56&otracker=search&fm=organic&iid=89c2f18f-dc22-4df6-9ae9-9489816b8f72.SHTH225GFZGJBHMX.SEARCH&ppt=None&ppn=None&ssid=js9arsybi80000001722578249761&qH=7a3ae33810fb2b2f
https://flipkart.com/campus-sutra-men-self-design-casual-beige-shirt/p/itm727d27771d564?pid=SHTH225JJZNHXWKG&lid=LSTSHTH225JJZNHXWKG2LUBRA&marketplace=FLIPKART&q=campusstura&store=clo&srno=s_2_57&otracker=search&fm=organic&iid=89c2f18f-dc22-4df6-9ae9-9489816b8f72.SHTH225JJZNHXWKG.SEARCH&ppt=None&ppn=None&ssid=js9arsybi80000001722578249761&qH=7a3ae33810fb2b2f
https://flipkart.com/campus-sutra-men-printed-casual-green-shirt/p/itma76bb876c36a0?pid=SHTH225JZESAGEKZ&lid=LSTSHTH225JZESAGEKZL14JSZ&marketplace=FLIPKART&q=campusstura&store=clo&srno=s_2_58&otracker=search&fm=organic&iid=89c2f18f-dc22-4df6-9ae9-9489816b8f72.SHTH225JZESAGEKZ.SEARCH&ppt=None&ppn=None&ssid=js9arsybi80000001722578249761&qH=7a3ae33810fb2b2f
https://flipkart.com/campus-sutra-men-printed-casual-beige-shirt/p/itme2583ef73034c?pid=SHTH225GWHZR3FY9&lid=LSTSHTH225GWHZR3FY9JNCHF4&marketplace=FLIPKART&q=campusstura&store=clo&srno=s_2_59&otracker=search&fm=organic&iid=89c2f18f-dc22-4df6-9ae9-9489816b8f72.SHTH225GWHZR3FY9.SEARCH&ppt=None&ppn=None&ssid=js9arsybi80000001722578249761&qH=7a3ae33810fb2b2f
https://flipkart.com/campus-sutra-men-self-design-casual-grey-shirt/p/itm1c266d706a1aa?pid=SHTH225JKWUARH3Z&lid=LSTSHTH225JKWUARH3ZJKJWON&marketplace=FLIPKART&q=campusstura&store=clo&srno=s_2_60&otracker=search&fm=organic&iid=89c2f18f-dc22-4df6-9ae9-9489816b8f72.SHTH225JKWUARH3Z.SEARCH&ppt=None&ppn=None&ssid=js9arsybi80000001722578249761&qH=7a3ae33810fb2b2f
https://flipkart.com/campus-sutra-men-printed-casual-black-shirt/p/itm01563df1fa5e2?pid=SHTH225GTBC2E4EQ&lid=LSTSHTH225GTBC2E4EQP2BVMB&marketplace=FLIPKART&q=campusstura&store=clo&srno=s_2_61&otracker=search&fm=organic&iid=89c2f18f-dc22-4df6-9ae9-9489816b8f72.SHTH225GTBC2E4EQ.SEARCH&ppt=None&ppn=None&ssid=js9arsybi80000001722578249761&qH=7a3ae33810fb2b2f
https://flipkart.com/campus-sutra-men-self-design-casual-green-shirt/p/itm4d4cfb5e86e87?pid=SHTH225GECSWUX52&lid=LSTSHTH225GECSWUX52OS4VCF&marketplace=FLIPKART&q=campusstura&store=clo&srno=s_2_62&otracker=search&fm=organic&iid=89c2f18f-dc22-4df6-9ae9-9489816b8f72.SHTH225GECSWUX52.SEARCH&ppt=None&ppn=None&ssid=js9arsybi80000001722578249761&qH=7a3ae33810fb2b2f
https://flipkart.com/campus-sutra-men-printed-casual-green-shirt/p/itm4f4ddd97e52dc?pid=SHTH225GRUHFAVJS&lid=LSTSHTH225GRUHFAVJSQCXO9X&marketplace=FLIPKART&q=campusstura&store=clo&srno=s_2_63&otracker=search&fm=organic&iid=89c2f18f-dc22-4df6-9ae9-9489816b8f72.SHTH225GRUHFAVJS.SEARCH&ppt=None&ppn=None&ssid=js9arsybi80000001722578249761&qH=7a3ae33810fb2b2f
https://flipkart.com/campus-sutra-men-solid-casual-purple-shirt/p/itm14a98f22f4a0e?pid=SHTH225GJ9YSM9WS&lid=LSTSHTH225GJ9YSM9WSJQ9F06&marketplace=FLIPKART&q=campusstura&store=clo&srno=s_2_64&otracker=search&fm=organic&iid=89c2f18f-dc22-4df6-9ae9-9489816b8f72.SHTH225GJ9YSM9WS.SEARCH&ppt=None&ppn=None&ssid=js9arsybi80000001722578249761&qH=7a3ae33810fb2b2f
https://flipkart.com/campus-sutra-men-checkered-casual-brown-shirt/p/itm9ad08760769d8?pid=SHTH225GF8MZ9NTJ&lid=LSTSHTH225GF8MZ9NTJEKZHZE&marketplace=FLIPKART&q=campusstura&store=clo&srno=s_2_65&otracker=search&fm=organic&iid=89c2f18f-dc22-4df6-9ae9-9489816b8f72.SHTH225GF8MZ9NTJ.SEARCH&ppt=None&ppn=None&ssid=js9arsybi80000001722578249761&qH=7a3ae33810fb2b2f
https://flipkart.com/campus-sutra-men-printed-casual-white-shirt/p/itm50772da0006f1?pid=SHTH225HVFHTTYRJ&lid=LSTSHTH225HVFHTTYRJNU8WTY&marketplace=FLIPKART&q=campusstura&store=clo&srno=s_2_66&otracker=search&fm=organic&iid=89c2f18f-dc22-4df6-9ae9-9489816b8f72.SHTH225HVFHTTYRJ.SEARCH&ppt=None&ppn=None&ssid=js9arsybi80000001722578249761&qH=7a3ae33810fb2b2f
https://flipkart.com/campus-sutra-men-printed-casual-black-shirt/p/itm8c4540b3c3a1b?pid=SHTH225HW6UDJNMZ&lid=LSTSHTH225HW6UDJNMZYNL4X8&marketplace=FLIPKART&q=campusstura&store=clo&srno=s_2_67&otracker=search&fm=organic&iid=89c2f18f-dc22-4df6-9ae9-9489816b8f72.SHTH225HW6UDJNMZ.SEARCH&ppt=None&ppn=None&ssid=js9arsybi80000001722578249761&qH=7a3ae33810fb2b2f
https://flipkart.com/campus-sutra-men-printed-casual-multicolor-shirt/p/itm5ecb81c56af81?pid=SHTH225JNCMZYHZF&lid=LSTSHTH225JNCMZYHZFGQNPDS&marketplace=FLIPKART&q=campusstura&store=clo&srno=s_2_68&otracker=search&fm=organic&iid=89c2f18f-dc22-4df6-9ae9-9489816b8f72.SHTH225JNCMZYHZF.SEARCH&ppt=None&ppn=None&ssid=js9arsybi80000001722578249761&qH=7a3ae33810fb2b2f
https://flipkart.com/campus-sutra-regular-men-dark-blue-jeans/p/itm295d10500b32a?pid=JEAHFMEZJUQZGZFH&lid=LSTJEAHFMEZJUQZGZFHHKYOY7&marketplace=FLIPKART&q=campusstura&store=clo&srno=s_2_69&otracker=search&fm=organic&iid=89c2f18f-dc22-4df6-9ae9-9489816b8f72.JEAHFMEZJUQZGZFH.SEARCH&ppt=None&ppn=None&ssid=js9arsybi80000001722578249761&qH=7a3ae33810fb2b2f
https://flipkart.com/campus-sutra-regular-fit-women-black-trousers/p/itm43f564e02d914?pid=TROHFJ99VX3QKUMP&lid=LSTTROHFJ99VX3QKUMPA5RDCX&marketplace=FLIPKART&q=campusstura&store=clo&srno=s_2_70&otracker=search&fm=organic&iid=89c2f18f-dc22-4df6-9ae9-9489816b8f72.TROHFJ99VX3QKUMP.SEARCH&ppt=None&ppn=None&ssid=js9arsybi80000001722578249761&qH=7a3ae33810fb2b2f
https://flipkart.com/campus-sutra-solid-women-regular-blue-skirt/p/itmcadb387a1bbbf?pid=SKIHFJ8PTJP72TMU&lid=LSTSKIHFJ8PTJP72TMUZP49VH&marketplace=FLIPKART&q=campusstura&store=clo&srno=s_2_71&otracker=search&fm=organic&iid=89c2f18f-dc22-4df6-9ae9-9489816b8f72.SKIHFJ8PTJP72TMU.SEARCH&ppt=None&ppn=None&ssid=js9arsybi80000001722578249761&qH=7a3ae33810fb2b2f
https://flipkart.com/campus-sutra-regular-women-blue-jeans/p/itm87e568ef3e3ec?pid=JEAHFG64QTSREURY&lid=LSTJEAHFG64QTSREURYKIAJSW&marketplace=FLIPKART&q=campusstura&store=clo&srno=s_2_72&otracker=search&fm=organic&iid=89c2f18f-dc22-4df6-9ae9-9489816b8f72.JEAHFG64QTSREURY.SEARCH&ppt=None&ppn=None&ssid=js9arsybi80000001722578249761&qH=7a3ae33810fb2b2f
https://flipkart.com/campus-sutra-women-striped-casual-multicolor-shirt/p/itm29257eef8a26a?pid=SHTHFG6GKPUHYXSG&lid=LSTSHTHFG6GKPUHYXSGHLPSEX&marketplace=FLIPKART&q=campusstura&store=clo&srno=s_2_73&otracker=search&fm=organic&iid=89c2f18f-dc22-4df6-9ae9-9489816b8f72.SHTHFG6GKPUHYXSG.SEARCH&ppt=None&ppn=None&ssid=js9arsybi80000001722578249761&qH=7a3ae33810fb2b2f
https://flipkart.com/campus-sutra-women-cargos/p/itm449c5e8d392a7?pid=CRGHFG6VV7R9D6FE&lid=LSTCRGHFG6VV7R9D6FEBSZW8Q&marketplace=FLIPKART&q=campusstura&store=clo&srno=s_2_74&otracker=search&fm=organic&iid=89c2f18f-dc22-4df6-9ae9-9489816b8f72.CRGHFG6VV7R9D6FE.SEARCH&ppt=None&ppn=None&ssid=js9arsybi80000001722578249761&qH=7a3ae33810fb2b2f
https://flipkart.com/campus-sutra-regular-women-blue-jeans/p/itmd68dbd2c1b0aa?pid=JEAHFG64RYZERAGK&lid=LSTJEAHFG64RYZERAGK5PNGF1&marketplace=FLIPKART&q=campusstura&store=clo&srno=s_2_75&otracker=search&fm=organic&iid=89c2f18f-dc22-4df6-9ae9-9489816b8f72.JEAHFG64RYZERAGK.SEARCH&ppt=None&ppn=None&ssid=js9arsybi80000001722578249761&qH=7a3ae33810fb2b2f
https://flipkart.com/campus-sutra-regular-women-blue-jeans/p/itm895b9bc270fee?pid=JEAHFG64RZFVUGXN&lid=LSTJEAHFG64RZFVUGXNRALRUI&marketplace=FLIPKART&q=campusstura&store=clo&srno=s_2_76&otracker=search&fm=organic&iid=89c2f18f-dc22-4df6-9ae9-9489816b8f72.JEAHFG64RZFVUGXN.SEARCH&ppt=None&ppn=None&ssid=js9arsybi80000001722578249761&qH=7a3ae33810fb2b2f
https://flipkart.com/campus-sutra-regular-women-blue-jeans/p/itm8e5d570e5f6cf?pid=JEAHFG64TVHPEQKX&lid=LSTJEAHFG64TVHPEQKXSCOGFI&marketplace=FLIPKART&q=campusstura&store=clo&srno=s_2_77&otracker=search&fm=organic&iid=89c2f18f-dc22-4df6-9ae9-9489816b8f72.JEAHFG64TVHPEQKX.SEARCH&ppt=None&ppn=None&ssid=js9arsybi80000001722578249761&qH=7a3ae33810fb2b2f
https://flipkart.com/campus-sutra-regular-women-blue-jeans/p/itme4c090cd8fe2e?pid=JEAHFG64DE87SUKZ&lid=LSTJEAHFG64DE87SUKZTCAKGJ&marketplace=FLIPKART&q=campusstura&store=clo&srno=s_2_78&otracker=search&fm=organic&iid=89c2f18f-dc22-4df6-9ae9-9489816b8f72.JEAHFG64DE87SUKZ.SEARCH&ppt=None&ppn=None&ssid=js9arsybi80000001722578249761&qH=7a3ae33810fb2b2f
https://flipkart.com/campus-sutra-regular-women-blue-jeans/p/itm1cacfe7087644?pid=JEAHFG64TVHGSEGK&lid=LSTJEAHFG64TVHGSEGKV937CZ&marketplace=FLIPKART&q=campusstura&store=clo&srno=s_2_79&otracker=search&fm=organic&iid=89c2f18f-dc22-4df6-9ae9-9489816b8f72.JEAHFG64TVHGSEGK.SEARCH&ppt=None&ppn=None&ssid=js9arsybi80000001722578249761&qH=7a3ae33810fb2b2f
https://flipkart.com/campus-sutra-casual-solid-women-blue-top/p/itm63130b8204d2d?pid=TOPHFG6MC5FZUEQG&lid=LSTTOPHFG6MC5FZUEQG0CTNOV&marketplace=FLIPKART&q=campusstura&store=clo&srno=s_2_80&otracker=search&fm=organic&iid=89c2f18f-dc22-4df6-9ae9-9489816b8f72.TOPHFG6MC5FZUEQG.SEARCH&ppt=None&ppn=None&ssid=js9arsybi80000001722578249761&qH=7a3ae33810fb2b2f
https://flipkart.com/campus-sutra-men-striped-casual-white-shirt/p/itme9a17c3dd1430?pid=SHTH225GMBCZWUTT&lid=LSTSHTH225GMBCZWUTTYHTHCT&marketplace=FLIPKART&q=campusstura&store=clo&srno=s_3_81&otracker=search&fm=organic&iid=499e0f50-244a-4dd5-9926-7ca32bfa00c8.SHTH225GMBCZWUTT.SEARCH&ppt=None&ppn=None&ssid=toayyzocds0000001722578251188&qH=7a3ae33810fb2b2f
https://flipkart.com/campus-sutra-regular-men-dark-blue-jeans/p/itm295d10500b32a?pid=JEAHFMEZJUQZGZFH&lid=LSTJEAHFMEZJUQZGZFHHKYOY7&marketplace=FLIPKART&q=campusstura&store=clo&srno=s_3_82&otracker=search&fm=organic&iid=499e0f50-244a-4dd5-9926-7ca32bfa00c8.JEAHFMEZJUQZGZFH.SEARCH&ppt=None&ppn=None&ssid=toayyzocds0000001722578251188&qH=7a3ae33810fb2b2f
https://flipkart.com/campus-sutra-solid-women-regular-blue-skirt/p/itmcadb387a1bbbf?pid=SKIHFJ8PTJP72TMU&lid=LSTSKIHFJ8PTJP72TMUZP49VH&marketplace=FLIPKART&q=campusstura&store=clo&srno=s_3_83&otracker=search&fm=organic&iid=499e0f50-244a-4dd5-9926-7ca32bfa00c8.SKIHFJ8PTJP72TMU.SEARCH&ppt=None&ppn=None&ssid=toayyzocds0000001722578251188&qH=7a3ae33810fb2b2f
https://flipkart.com/campus-sutra-regular-fit-women-black-trousers/p/itm43f564e02d914?pid=TROHFJ99VX3QKUMP&lid=LSTTROHFJ99VX3QKUMPA5RDCX&marketplace=FLIPKART&q=campusstura&store=clo&srno=s_3_84&otracker=search&fm=organic&iid=499e0f50-244a-4dd5-9926-7ca32bfa00c8.TROHFJ99VX3QKUMP.SEARCH&ppt=None&ppn=None&ssid=toayyzocds0000001722578251188&qH=7a3ae33810fb2b2f
https://flipkart.com/campus-sutra-women-striped-casual-multicolor-shirt/p/itm29257eef8a26a?pid=SHTHFG6GKPUHYXSG&lid=LSTSHTHFG6GKPUHYXSGHLPSEX&marketplace=FLIPKART&q=campusstura&store=clo&srno=s_3_85&otracker=search&fm=organic&iid=499e0f50-244a-4dd5-9926-7ca32bfa00c8.SHTHFG6GKPUHYXSG.SEARCH&ppt=None&ppn=None&ssid=toayyzocds0000001722578251188&qH=7a3ae33810fb2b2f
https://flipkart.com/campus-sutra-women-cargos/p/itm449c5e8d392a7?pid=CRGHFG6VAXFBA8FU&lid=LSTCRGHFG6VAXFBA8FUJYPOQM&marketplace=FLIPKART&q=campusstura&store=clo&srno=s_3_86&otracker=search&fm=organic&iid=499e0f50-244a-4dd5-9926-7ca32bfa00c8.CRGHFG6VAXFBA8FU.SEARCH&ppt=None&ppn=None&ssid=toayyzocds0000001722578251188&qH=7a3ae33810fb2b2f
https://flipkart.com/campus-sutra-regular-women-black-jeans/p/itm934b215e13240?pid=JEAHFG64NFGHBKEH&lid=LSTJEAHFG64NFGHBKEHDAI8LT&marketplace=FLIPKART&q=campusstura&store=clo&srno=s_3_87&otracker=search&fm=organic&iid=499e0f50-244a-4dd5-9926-7ca32bfa00c8.JEAHFG64NFGHBKEH.SEARCH&ppt=None&ppn=None&ssid=toayyzocds0000001722578251188&qH=7a3ae33810fb2b2f
https://flipkart.com/campus-sutra-regular-women-blue-jeans/p/itmf8ba479dbcbd1?pid=JEAHFG64S9KBKHME&lid=LSTJEAHFG64S9KBKHMESTZLA1&marketplace=FLIPKART&q=campusstura&store=clo&srno=s_3_88&otracker=search&fm=organic&iid=499e0f50-244a-4dd5-9926-7ca32bfa00c8.JEAHFG64S9KBKHME.SEARCH&ppt=None&ppn=None&ssid=toayyzocds0000001722578251188&qH=7a3ae33810fb2b2f
https://flipkart.com/campus-sutra-regular-women-blue-jeans/p/itm53d4ad2d28d80?pid=JEAHFG6468AQHHSA&lid=LSTJEAHFG6468AQHHSA2CPJ1V&marketplace=FLIPKART&q=campusstura&store=clo&srno=s_3_89&otracker=search&fm=organic&iid=499e0f50-244a-4dd5-9926-7ca32bfa00c8.JEAHFG6468AQHHSA.SEARCH&ppt=None&ppn=None&ssid=toayyzocds0000001722578251188&qH=7a3ae33810fb2b2f
https://flipkart.com/campus-sutra-women-cargos/p/itm3a47bf1748850?pid=CRGHFG6VHVKVYKRV&lid=LSTCRGHFG6VHVKVYKRV5DUHXO&marketplace=FLIPKART&q=campusstura&store=clo&srno=s_3_90&otracker=search&fm=organic&iid=499e0f50-244a-4dd5-9926-7ca32bfa00c8.CRGHFG6VHVKVYKRV.SEARCH&ppt=None&ppn=None&ssid=toayyzocds0000001722578251188&qH=7a3ae33810fb2b2f
https://flipkart.com/campus-sutra-regular-women-blue-jeans/p/itmc9cc925bbc05a?pid=JEAHFG64YT9CHAHD&lid=LSTJEAHFG64YT9CHAHDCEYYMP&marketplace=FLIPKART&q=campusstura&store=clo&srno=s_3_91&otracker=search&fm=organic&iid=499e0f50-244a-4dd5-9926-7ca32bfa00c8.JEAHFG64YT9CHAHD.SEARCH&ppt=None&ppn=None&ssid=toayyzocds0000001722578251188&qH=7a3ae33810fb2b2f
https://flipkart.com/campus-sutra-regular-women-blue-jeans/p/itm6622d9d878a5e?pid=JEAHFG64EHZJCHAX&lid=LSTJEAHFG64EHZJCHAXUAXBKI&marketplace=FLIPKART&q=campusstura&store=clo&srno=s_3_92&otracker=search&fm=organic&iid=499e0f50-244a-4dd5-9926-7ca32bfa00c8.JEAHFG64EHZJCHAX.SEARCH&ppt=None&ppn=None&ssid=toayyzocds0000001722578251188&qH=7a3ae33810fb2b2f
https://flipkart.com/campus-sutra-regular-women-blue-jeans/p/itmdf2bed0de6675?pid=JEAHFG658CRRMAU9&lid=LSTJEAHFG658CRRMAU90IMWYS&marketplace=FLIPKART&q=campusstura&store=clo&srno=s_3_93&otracker=search&fm=organic&iid=499e0f50-244a-4dd5-9926-7ca32bfa00c8.JEAHFG658CRRMAU9.SEARCH&ppt=None&ppn=None&ssid=toayyzocds0000001722578251188&qH=7a3ae33810fb2b2f
https://flipkart.com/campus-sutra-regular-women-blue-jeans/p/itm25a09dc99f884?pid=JEAHFG64NCUWT26K&lid=LSTJEAHFG64NCUWT26KUXCOIH&marketplace=FLIPKART&q=campusstura&store=clo&srno=s_3_94&otracker=search&fm=organic&iid=499e0f50-244a-4dd5-9926-7ca32bfa00c8.JEAHFG64NCUWT26K.SEARCH&ppt=None&ppn=None&ssid=toayyzocds0000001722578251188&qH=7a3ae33810fb2b2f
https://flipkart.com/campus-sutra-regular-women-blue-jeans/p/itm927a7a953d7b9?pid=JEAHFG6444JZYP9Q&lid=LSTJEAHFG6444JZYP9QQOI2QF&marketplace=FLIPKART&q=campusstura&store=clo&srno=s_3_95&otracker=search&fm=organic&iid=499e0f50-244a-4dd5-9926-7ca32bfa00c8.JEAHFG6444JZYP9Q.SEARCH&ppt=None&ppn=None&ssid=toayyzocds0000001722578251188&qH=7a3ae33810fb2b2f
https://flipkart.com/campus-sutra-casual-solid-women-green-top/p/itmf0d66775ab225?pid=TOPHFG6MG8XZCQKM&lid=LSTTOPHFG6MG8XZCQKM4ZMQH4&marketplace=FLIPKART&q=campusstura&store=clo&srno=s_3_96&otracker=search&fm=organic&iid=499e0f50-244a-4dd5-9926-7ca32bfa00c8.TOPHFG6MG8XZCQKM.SEARCH&ppt=None&ppn=None&ssid=toayyzocds0000001722578251188&qH=7a3ae33810fb2b2f
https://flipkart.com/campus-sutra-regular-women-blue-jeans/p/itm49817785d8ef2?pid=JEAHFG64CGNX7Z7K&lid=LSTJEAHFG64CGNX7Z7KNSB8EZ&marketplace=FLIPKART&q=campusstura&store=clo&srno=s_3_97&otracker=search&fm=organic&iid=499e0f50-244a-4dd5-9926-7ca32bfa00c8.JEAHFG64CGNX7Z7K.SEARCH&ppt=None&ppn=None&ssid=toayyzocds0000001722578251188&qH=7a3ae33810fb2b2f
https://flipkart.com/campus-sutra-women-cargos/p/itm50ce62e6eb7f2?pid=CRGHFG6VQ63FR9SD&lid=LSTCRGHFG6VQ63FR9SDZQTNSG&marketplace=FLIPKART&q=campusstura&store=clo&srno=s_3_98&otracker=search&fm=organic&iid=499e0f50-244a-4dd5-9926-7ca32bfa00c8.CRGHFG6VQ63FR9SD.SEARCH&ppt=None&ppn=None&ssid=toayyzocds0000001722578251188&qH=7a3ae33810fb2b2f
https://flipkart.com/campus-sutra-women-striped-casual-multicolor-shirt/p/itm97c606c3c4231?pid=SHTHFG6GWCRW2HWA&lid=LSTSHTHFG6GWCRW2HWASQMFHY&marketplace=FLIPKART&q=campusstura&store=clo&srno=s_3_99&otracker=search&fm=organic&iid=499e0f50-244a-4dd5-9926-7ca32bfa00c8.SHTHFG6GWCRW2HWA.SEARCH&ppt=None&ppn=None&ssid=toayyzocds0000001722578251188&qH=7a3ae33810fb2b2f"""
listofurls = urlraw.split('\n')
listofcodes="""700025408_blue
464946029_navy
467238492_grey
466790110_white
466800767_white
463512087_black
467093951_multi
465073691_black
466063877_white
462637449_blue
467118860_black
700129394_brown
466551266_red
466939468_multi
464075326_blue
466137554_black
466448605_blue
466061614_black
466256074_teal
466826632_grey
467168108_white
466063966_white
466255445_multi
465323756_white
466812010_brown
700024146_grey
700024344_blue
467154108_beige
467292999_black
464939823_pink
465960202_green
461224278_grey
463867815_yellow
466626160_green
700129100_green
466798638_black
466448638_teal
466707001_blue
466637319_black
700129152_grey
466637319_blue
462616529_blue
467118860_brown
466448463_navy
467155374_multi
466063949_blue
466063927_white
466410842_blue
462737837_green
463512087_grey
466065079_green
467254464_pink
464995341_navy
466825791_grey
467244358_black
466334995_multi
466255088_green
463611338_blue
465836315_white
467310590_multi
465068852_olive
466798758_green
463601615_navy
465664737_grey
466111077_multi
464680800_multi
463530624_blue
466502265_green
466807222_white
466813372_black
466711655_multi
462616174_blue
467238300_multi
466066914_white
467292831_white
467118844_black
465991640_navy
465836320_white
466830403_yellow
463376560_beige
466448463_grey
462617340_green
467254464_green
466790160_brown
466798242_white
464078194_green
467093957_multi
465212826_blue
466063941_white
467310597_multi
464939823_green
467286179_pink
463348864_navy
466449048_black
461224277_green
467292991_brown
700024190_multi
467209700_yellow
463298317_black
700026130_grey"""
headers = {
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'Referer': 'https://www.myntra.com/',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}
#follow redirects
async def request_data(client, url):
    resp = await client.get(url, headers=headers, follow_redirects=True)

    return BeautifulSoup(resp.text, 'html.parser')



async def main():
    async with httpx.AsyncClient() as client:
        tasks = []
        for i in range(99):
            tasks.append(request_data(client, listofurls[i]))
        print("Starting")
        characters = await asyncio.gather(*tasks)
        for i,c in enumerate(characters):

            if "This item is currently out of stock" in c.body.text:
                print("Out of stock")
                #print(c.body.text)
                #print(i)
                #print(listofurls[i])
                #print(c.body.select_one('h1').text if c.body.select_one('h1') else "No h1")
                #print(c.body.select_one('div.col-12-12>.row').text if c.body.select_one('div.col-12-12>.row') else "No row")
            else:
                print("In stock")



asyncio.run(main())