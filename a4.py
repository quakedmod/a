import concurrent.futures
import urllib.request
import ssl

# This restores the same behavior as before.
context = ssl._create_unverified_context()
#ssl._create_default_https_context = ssl._create_unverified_context

URLS = [
    "https://tvzvezda.ru/",
    "https://m.tvzvezda.ru",
    "https://tvzvezda.ru/assets/favicon/favicon.ico",
    "https://tvzvezda.ru/assets/favicon/apple-touch-icon.png?v=e",
    "https://tvzvezda.ru/assets/favicon/favicon-32x32.png?v=e",
    "https://tvzvezda.ru/assets/favicon/favicon-16x16.png?v=e",
    "https://tvzvezda.ru/assets/favicon/manifest.json?v=1.3",
    "https://tvzvezda.ru/assets/favicon/safari-pinned-tab.svg?v=e",
    "https://tvzvezda.ru/assets/favicon/favicon.ico?v=e",
    "https://tvzvezda.ru/assets/css/vendor/vendor.css?v=3",
    "https://tvzvezda.ru/assets/css/style.css?v=6",
    "http://tvzvezda.ru/export/rss.xml",
    "https://tvzvezda.ru/news/vstrane_i_mire/economics/?utm_source=tvzvezda&utm_medium=header&utm_campaign=currency",
    "http://old.tvzvezda.ru/login.user",
    "https://tvzvezda.ru/",
    "https://tvzvezda.ru/schedule/",
    "https://tvzvezda.ru/schedule/programs/",
    "https://tvzvezda.ru/person/",
    "https://m.tvzvezda.ru/newstar/",
    "https://tvzvezda.ru/sp/zvezda-plus/",
    "http://radiozvezda.ru",
    "https://tvzvezda.ru/news/forces/",
    "https://tvzvezda.ru/news/armygames2021/",
    "https://tvzvezda.ru/news/tank-biathlon-2021/",
    "https://tvzvezda.ru/news/forces/cathedral/",
    "https://tvzvezda.ru/news/forces/technopolis-era/",
    "https://tvzvezda.ru/news/forces/parkpatriot/",
    "https://tvzvezda.ru/news/forces/youngarmy/",
    "https://tvzvezda.ru/news/vstrane_i_mire/",
    "https://tvzvezda.ru/news/vstrane_i_mire/201610102306-u666.htm/",
    "https://tvzvezda.ru/news/vstrane_i_mire/ukraine/",
    "https://tvzvezda.ru/news/vstrane_i_mire/inosmi/",
    "https://tvzvezda.ru/news/opinion/",
    "https://tvzvezda.ru/news/vstrane_i_mire/economics/",
    "https://tvzvezda.ru/news/opk/",
    "https://tvzvezda.ru/news/army-forum2021/",
    "https://tvzvezda.ru/news/opk/rusarmyexpo2020/",
    "https://tvzvezda.ru/news/qhistory/",
    "https://tvzvezda.ru/news/75-years-of-victory/",
    "https://tvzvezda.ru/news/vstrane_i_mire/society/",
    "https://tvzvezda.ru/news/vstrane_i_mire/financial-competence/",
    "https://tvzvezda.ru/news/vstrane_i_mire/health/",
    "https://tvzvezda.ru/news/sport/",
    "https://tvzvezda.ru/news/science_n_tech/",
    "https://tvzvezda.ru/photo-gallery/",
    "https://zvezdaweekly.ru",
    "https://tvzvezda.ru/news/20223101325-IGoK4.html",
    "https://tvzvezda.ru/news/tags/?q=%D0%A0%D0%BE%D1%81%D1%81%D0%B8%D1%8F",
    "https://tvzvezda.ru/news/tags/?q=%D0%B2+%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B5+%D0%B8+%D0%BC%D0%B8%D1%80%D0%B5",
    "https://tvzvezda.ru/news/tags/?q=%D0%A3%D0%BA%D1%80%D0%B0%D0%B8%D0%BD%D0%B0",
    "https://tvzvezda.ru/news/tags/?q=%D0%92%D0%BB%D0%B0%D0%B4%D0%B8%D0%BC%D0%B8%D1%80+%D0%9F%D1%83%D1%82%D0%B8%D0%BD",
    "https://tvzvezda.ru/news/tags/?q=%D0%92%D0%BB%D0%B0%D0%B4%D0%B8%D0%BC%D0%B8%D1%80+%D0%97%D0%B5%D0%BB%D0%B5%D0%BD%D1%81%D0%BA%D0%B8%D0%B9",
    "https://tvzvezda.ru/news/tags/?q=%D0%BF%D0%B5%D1%80%D0%B5%D0%B3%D0%BE%D0%B2%D0%BE%D1%80%D1%8B",
    "https://tvzvezda.ru/news/20223101325-IGoK4.html",
    "https://tvzvezda.ru/news/20223101033-5fv9m.html",
    "https://tvzvezda.ru/news/tags/?q=%D0%B0%D1%80%D0%BC%D0%B8%D1%8F",
    "https://tvzvezda.ru/news/tags/?q=%D0%9C%D0%B8%D0%BD%D0%BE%D0%B1%D0%BE%D1%80%D0%BE%D0%BD%D1%8B+%D0%A0%D0%BE%D1%81%D1%81%D0%B8%D0%B8",
    "https://tvzvezda.ru/news/tags/?q=%D0%A3%D0%BA%D1%80%D0%B0%D0%B8%D0%BD%D0%B0",
    "https://tvzvezda.ru/news/tags/?q=%D0%A0%D0%A4",
    "https://tvzvezda.ru/news/tags/?q=%D0%B1%D0%B8%D0%BE%D0%BB%D0%B0%D0%B1%D0%BE%D1%80%D0%B0%D1%82%D0%BE%D1%80%D0%B8%D0%B8",
    "https://tvzvezda.ru/news/20223101033-5fv9m.html",
    "https://tvzvezda.ru/news/202231097-Bq8Na.html",
    "https://tvzvezda.ru/news/tags/?q=%D0%A0%D0%BE%D1%81%D1%81%D0%B8%D1%8F",
    "https://tvzvezda.ru/news/tags/?q=%D0%B0%D1%80%D0%BC%D0%B8%D1%8F",
    "https://tvzvezda.ru/news/tags/?q=%D0%BA%D0%B0-52",
    "https://tvzvezda.ru/news/tags/?q=%D0%B2%D0%BA%D1%81",
    "https://tvzvezda.ru/news/tags/?q=%D0%9C%D0%B8%D0%BD%D0%BE%D0%B1%D0%BE%D1%80%D0%BE%D0%BD%D1%8B+%D0%A0%D0%A4",
    "https://tvzvezda.ru/news/tags/?q=%D0%A3%D0%BA%D1%80%D0%B0%D0%B8%D0%BD%D0%B0",
    "https://tvzvezda.ru/news/tags/?q=%D0%9C%D0%B8-28%D0%9D",
    "https://tvzvezda.ru/news/202231097-Bq8Na.html",
    "https://tvzvezda.ru/news/20223101611-NfYx0.html",
    "https://tvzvezda.ru/news/tags/?q=%D0%B0%D1%80%D0%BC%D0%B8%D1%8F",
    "https://tvzvezda.ru/news/tags/?q=%D0%A3%D0%BA%D1%80%D0%B0%D0%B8%D0%BD%D0%B0",
    "https://tvzvezda.ru/news/tags/?q=%D1%81%D1%88%D0%B0",
    "https://tvzvezda.ru/news/tags/?q=%D0%93%D1%80%D1%83%D0%B7%D0%B8%D1%8F",
    "https://tvzvezda.ru/news/tags/?q=%D0%B1%D0%B8%D0%BE%D0%BE%D1%80%D1%83%D0%B6%D0%B8%D0%B5",
    "https://tvzvezda.ru/news/tags/?q=%D0%98%D1%81%D1%81%D0%BB%D0%B5%D0%B4%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F",
    "https://tvzvezda.ru/news/tags/?q=%D0%B4%D0%BE%D0%BA%D1%83%D0%BC%D0%B5%D0%BD%D1%82%D1%8B",
    "https://tvzvezda.ru/news/tags/?q=%D0%BB%D0%B5%D1%82%D1%83%D1%87%D0%B8%D0%B5+%D0%BC%D1%8B%D1%88%D0%B8",
    "https://tvzvezda.ru/news/tags/?q=%D0%BF%D0%B0%D1%82%D0%BE%D0%B3%D0%B5%D0%BD%D1%8B",
    "https://tvzvezda.ru/news/20223101611-NfYx0.html",
    "https://tvzvezda.ru/news/2022310160-fRLMR.html",
    "https://tvzvezda.ru/news/tags/?q=%D0%B0%D1%80%D0%BC%D0%B8%D1%8F",
    "https://tvzvezda.ru/news/tags/?q=%D0%9C%D0%B8%D0%BD%D0%BE%D0%B1%D0%BE%D1%80%D0%BE%D0%BD%D1%8B+%D0%A0%D0%BE%D1%81%D1%81%D0%B8%D0%B8",
    "https://tvzvezda.ru/news/tags/?q=%D0%A3%D0%BA%D1%80%D0%B0%D0%B8%D0%BD%D0%B0",
    "https://tvzvezda.ru/news/tags/?q=%D0%BC%D0%B8%D0%B3%D1%80%D0%B8%D1%80%D1%83%D1%8E%D1%89%D0%B8%D0%B5+%D0%BF%D1%82%D0%B8%D1%86%D1%8B",
    "https://tvzvezda.ru/news/2022310160-fRLMR.html",
    "https://tvzvezda.ru/news/20223101325-IGoK4.html",
    "https://tvzvezda.ru/news/tags/?q=%D0%A0%D0%BE%D1%81%D1%81%D0%B8%D1%8F",
    "https://tvzvezda.ru/news/tags/?q=%D0%B2+%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B5+%D0%B8+%D0%BC%D0%B8%D1%80%D0%B5",
    "https://tvzvezda.ru/news/tags/?q=%D0%A3%D0%BA%D1%80%D0%B0%D0%B8%D0%BD%D0%B0",
    "https://tvzvezda.ru/news/tags/?q=%D0%92%D0%BB%D0%B0%D0%B4%D0%B8%D0%BC%D0%B8%D1%80+%D0%9F%D1%83%D1%82%D0%B8%D0%BD",
    "https://tvzvezda.ru/news/tags/?q=%D0%92%D0%BB%D0%B0%D0%B4%D0%B8%D0%BC%D0%B8%D1%80+%D0%97%D0%B5%D0%BB%D0%B5%D0%BD%D1%81%D0%BA%D0%B8%D0%B9",
    "https://tvzvezda.ru/news/tags/?q=%D0%BF%D0%B5%D1%80%D0%B5%D0%B3%D0%BE%D0%B2%D0%BE%D1%80%D1%8B",
    "https://tvzvezda.ru/news/20223101325-IGoK4.html",
    "https://tvzvezda.ru/news/20223101033-5fv9m.html",
    "https://tvzvezda.ru/news/tags/?q=%D0%B0%D1%80%D0%BC%D0%B8%D1%8F",
    "https://tvzvezda.ru/news/tags/?q=%D0%9C%D0%B8%D0%BD%D0%BE%D0%B1%D0%BE%D1%80%D0%BE%D0%BD%D1%8B+%D0%A0%D0%BE%D1%81%D1%81%D0%B8%D0%B8",
    "https://tvzvezda.ru/news/tags/?q=%D0%A3%D0%BA%D1%80%D0%B0%D0%B8%D0%BD%D0%B0",
    "https://tvzvezda.ru/news/tags/?q=%D0%A0%D0%A4",
    "https://tvzvezda.ru/news/tags/?q=%D0%B1%D0%B8%D0%BE%D0%BB%D0%B0%D0%B1%D0%BE%D1%80%D0%B0%D1%82%D0%BE%D1%80%D0%B8%D0%B8",
    "https://tvzvezda.ru/news/20223101033-5fv9m.html",
    "https://tvzvezda.ru/news/202231097-Bq8Na.html",
    "https://tvzvezda.ru/news/tags/?q=%D0%A0%D0%BE%D1%81%D1%81%D0%B8%D1%8F",
    "https://tvzvezda.ru/news/tags/?q=%D0%B0%D1%80%D0%BC%D0%B8%D1%8F",
    "https://tvzvezda.ru/news/tags/?q=%D0%BA%D0%B0-52",
    "https://tvzvezda.ru/news/tags/?q=%D0%B2%D0%BA%D1%81",
    "https://tvzvezda.ru/news/tags/?q=%D0%9C%D0%B8%D0%BD%D0%BE%D0%B1%D0%BE%D1%80%D0%BE%D0%BD%D1%8B+%D0%A0%D0%A4",
    "https://tvzvezda.ru/news/tags/?q=%D0%A3%D0%BA%D1%80%D0%B0%D0%B8%D0%BD%D0%B0",
    "https://tvzvezda.ru/news/tags/?q=%D0%9C%D0%B8-28%D0%9D",
    "https://tvzvezda.ru/news/202231097-Bq8Na.html",
    "https://tvzvezda.ru/news/20223101611-NfYx0.html",
    "https://tvzvezda.ru/news/tags/?q=%D0%B0%D1%80%D0%BC%D0%B8%D1%8F",
    "https://tvzvezda.ru/news/tags/?q=%D0%A3%D0%BA%D1%80%D0%B0%D0%B8%D0%BD%D0%B0",
    "https://tvzvezda.ru/news/tags/?q=%D1%81%D1%88%D0%B0",
    "https://tvzvezda.ru/news/tags/?q=%D0%93%D1%80%D1%83%D0%B7%D0%B8%D1%8F",
    "https://tvzvezda.ru/news/tags/?q=%D0%B1%D0%B8%D0%BE%D0%BE%D1%80%D1%83%D0%B6%D0%B8%D0%B5",
    "https://tvzvezda.ru/news/tags/?q=%D0%98%D1%81%D1%81%D0%BB%D0%B5%D0%B4%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F",
    "https://tvzvezda.ru/news/tags/?q=%D0%B4%D0%BE%D0%BA%D1%83%D0%BC%D0%B5%D0%BD%D1%82%D1%8B",
    "https://tvzvezda.ru/news/tags/?q=%D0%BB%D0%B5%D1%82%D1%83%D1%87%D0%B8%D0%B5+%D0%BC%D1%8B%D1%88%D0%B8",
    "https://tvzvezda.ru/news/tags/?q=%D0%BF%D0%B0%D1%82%D0%BE%D0%B3%D0%B5%D0%BD%D1%8B",
    "https://tvzvezda.ru/news/20223101611-NfYx0.html",
    "https://tvzvezda.ru/news/2022310160-fRLMR.html",
    "https://tvzvezda.ru/news/tags/?q=%D0%B0%D1%80%D0%BC%D0%B8%D1%8F",
    "https://tvzvezda.ru/news/tags/?q=%D0%9C%D0%B8%D0%BD%D0%BE%D0%B1%D0%BE%D1%80%D0%BE%D0%BD%D1%8B+%D0%A0%D0%BE%D1%81%D1%81%D0%B8%D0%B8",
    "https://tvzvezda.ru/news/tags/?q=%D0%A3%D0%BA%D1%80%D0%B0%D0%B8%D0%BD%D0%B0",
    "https://tvzvezda.ru/news/tags/?q=%D0%BC%D0%B8%D0%B3%D1%80%D0%B8%D1%80%D1%83%D1%8E%D1%89%D0%B8%D0%B5+%D0%BF%D1%82%D0%B8%D1%86%D1%8B",
    "https://tvzvezda.ru/news/2022310160-fRLMR.html",
    "https://tvzvezda.ru/news/20223101325-IGoK4.html",
    "https://tvzvezda.ru/news/tags/?q=%D0%A0%D0%BE%D1%81%D1%81%D0%B8%D1%8F",
    "https://tvzvezda.ru/news/tags/?q=%D0%B2+%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B5+%D0%B8+%D0%BC%D0%B8%D1%80%D0%B5",
    "https://tvzvezda.ru/news/tags/?q=%D0%A3%D0%BA%D1%80%D0%B0%D0%B8%D0%BD%D0%B0",
    "https://tvzvezda.ru/news/tags/?q=%D0%92%D0%BB%D0%B0%D0%B4%D0%B8%D0%BC%D0%B8%D1%80+%D0%9F%D1%83%D1%82%D0%B8%D0%BD",
    "https://tvzvezda.ru/news/tags/?q=%D0%92%D0%BB%D0%B0%D0%B4%D0%B8%D0%BC%D0%B8%D1%80+%D0%97%D0%B5%D0%BB%D0%B5%D0%BD%D1%81%D0%BA%D0%B8%D0%B9",
    "https://tvzvezda.ru/news/tags/?q=%D0%BF%D0%B5%D1%80%D0%B5%D0%B3%D0%BE%D0%B2%D0%BE%D1%80%D1%8B",
    "https://tvzvezda.ru/news/20223101325-IGoK4.html",
    "https://tvzvezda.ru/news/2022310165-y3zqS.html",
    "https://tvzvezda.ru/news/20223101611-NfYx0.html",
    "https://tvzvezda.ru/news/20223101529-uQiiH.html",
    "https://tvzvezda.ru/news/2022310158-IsF9v.html",
    "https://tvzvezda.ru/news/20223101312-utbCi.html",
    "https://tvzvezda.ru/schedule/programs/201808241352-z30e.htm",
    "https://tvzvezda.ru/schedule/programs/201808241352-z30e.htm/2022381012-cjR9Q.html",
    "https://tvzvezda.ru/schedule/programs/201808241352-z30e.htm/202238105-k3QAK.html",
    "https://tvzvezda.ru/schedule/programs/201808241352-z30e.htm/2022351830-bpbOA.html",
    "https://tvzvezda.ru/schedule/programs/201808241352-z30e.htm/2022351829-tlyDF.html",
    "https://tvzvezda.ru/schedule/programs/201808241352-z30e.htm/2022351244-jwSHz.html",
    "https://tvzvezda.ru/schedule/programs/201808241352-z30e.htm/2022351243-MuXoO.html",
    "https://tvzvezda.ru/news/",
    "https://tvzvezda.ru/news/20223101626-FYQET.html",
    "https://tvzvezda.ru/news/20223101623-oofpJ.html",
    "https://tvzvezda.ru/news/20223101616-2oFsz.html",
    "https://tvzvezda.ru/news/20223101611-NfYx0.html",
    "https://tvzvezda.ru/news/2022310165-y3zqS.html",
    "https://tvzvezda.ru/news/2022310160-fRLMR.html",
    "https://tvzvezda.ru/news/2022310165-tNYaX.html",
    "https://tvzvezda.ru/news/20223101540-AoEjA.html",
    "https://tvzvezda.ru/news/20223101540-MCFCu.html",
    "https://tvzvezda.ru/news/20223101529-uQiiH.html",
    "https://tvzvezda.ru/news/2022310158-IsF9v.html",
    "https://tvzvezda.ru/news/20223101455-y3xw6.html",
    "https://tvzvezda.ru/news/20223101422-bTdtB.html",
    "https://tvzvezda.ru/news/20223101421-abU4x.html",
    "https://tvzvezda.ru/news/20223101346-U9g8V.html",
    "https://tvzvezda.ru/news/20223101325-IGoK4.html",
    "https://tvzvezda.ru/news/20223101322-8l5hM.html",
    "https://tvzvezda.ru/news/20223101317-ZAMol.html",
    "https://tvzvezda.ru/news/",
    "https://tvzvezda.ru/news/202239151-Zk6Ie.html",
    "https://tvzvezda.ru/news/202238359-Yk3EJ.html",
    "https://tvzvezda.ru/news/2022362339-4MBBn.html",
    "https://tvzvezda.ru/news/202231053-JCWPN.html",
    "https://tvzvezda.ru/news/202239151-Zk6Ie.html",
    "https://tvzvezda.ru/news/202238359-Yk3EJ.html",
    "https://tvzvezda.ru/news/2022362339-4MBBn.html",
    "https://tvzvezda.ru/news/202231053-JCWPN.html",
    "https://tvzvezda.ru/news/202239151-Zk6Ie.html",
    "https://tvzvezda.ru/news/202238359-Yk3EJ.html",
    "https://tvzvezda.ru/news/2022391221-KfdmP.html",
    "https://tvzvezda.ru/news/2022391059-jleaE.html",
    "https://tvzvezda.ru/news/2022391012-CYmTd.html",
    "https://tvzvezda.ru/news/20223101134-DCu0X.html",
    "https://tvzvezda.ru/news/2022391830-NfWWt.html",
    "https://tvzvezda.ru/news/2022391221-KfdmP.html",
    "https://tvzvezda.ru/news/2022391059-jleaE.html",
    "https://tvzvezda.ru/news/2022391012-CYmTd.html",
    "https://tvzvezda.ru/news/20223101134-DCu0X.html",
    "https://tvzvezda.ru/news/2022391830-NfWWt.html",
    "https://tvzvezda.ru/news/2022392014-Sn1n4.html",
    "https://tvzvezda.ru/news/202237120-nu7aD.html",
    "https://tvzvezda.ru/news/article/",
    "https://tvzvezda.ru/news/forces/",
    "https://tvzvezda.ru/news/20223101611-NfYx0.html",
    "https://tvzvezda.ru/news/2022310160-fRLMR.html",
    "https://tvzvezda.ru/news/20223101033-5fv9m.html",
    "https://tvzvezda.ru/news/202231097-Bq8Na.html",
    "https://tvzvezda.ru/news/forces/",
    "https://tvzvezda.ru/news/2022310743-EgmQT.html",
    "https://tvzvezda.ru/news/20223101346-U9g8V.html",
    "https://tvzvezda.ru/news/2022310818-bCzfx.html",
    "https://tvzvezda.ru/news/202239207-faViB.html",
    "https://tvzvezda.ru/news/photo_gallery/",
    "https://tvzvezda.ru/photo-gallery/20221171243-59joQ.html",
    "https://tvzvezda.ru/photo-gallery/202110191048-3liaQ.html",
    "https://tvzvezda.ru/photo-gallery/20211041158-hVwcQ.html",
    "https://tvzvezda.ru/photo-gallery/2022211659-0Ij5H.html",
    "https://tvzvezda.ru/photo-gallery/20221191038-tk082.html",
    "https://tvzvezda.ru/photo-gallery/20221171243-59joQ.html",
    "https://tvzvezda.ru/photo-gallery/202110191048-3liaQ.html",
    "https://tvzvezda.ru/photo-gallery/20211041158-hVwcQ.html",
    "https://tvzvezda.ru/photo-gallery/2022211659-0Ij5H.html",
    "https://tvzvezda.ru/photo-gallery/20221191038-tk082.html",
    "https://tvzvezda.ru/photo-gallery/20221171243-59joQ.html",
    "https://tvzvezda.ru/news/opk/",
    "https://tvzvezda.ru/news/2022361834-2d1gw.html",
    "https://tvzvezda.ru/news/2022351839-5pAwO.html",
    "https://tvzvezda.ru/news/2022351838-qwdlM.html",
    "https://tvzvezda.ru/news/2022351837-6fx76.html",
    "https://tvzvezda.ru/news/opk/",
    "https://tvzvezda.ru/news/opinion/",
    "https://tvzvezda.ru/news/2021221153-SWBf9.html",
    "https://tvzvezda.ru/news/2021121118-2g027.html",
    "https://tvzvezda.ru/news/2021119116-LRJfh.html",
    "https://tvzvezda.ru/news/20211161552-ZKdXV.html",
    "https://tvzvezda.ru/news/20218311421-Jd9nx.html",
    "https://tvzvezda.ru/news/20214301346-31f4o.html",
    "https://tvzvezda.ru/news/2021413134-JX7Ue.html",
    "https://tvzvezda.ru/news/2021331513-rW0CN.html",
    "https://tvzvezda.ru/news/2021221153-SWBf9.html",
    "https://tvzvezda.ru/news/2021121118-2g027.html",
    "https://tvzvezda.ru/news/2021119116-LRJfh.html",
    "https://tvzvezda.ru/news/20211161552-ZKdXV.html",
    "https://tvzvezda.ru/news/20218311421-Jd9nx.html",
    "https://tvzvezda.ru/news/20214301346-31f4o.html",
    "https://tvzvezda.ru/news/2021413134-JX7Ue.html",
    "https://tvzvezda.ru/news/2021331513-rW0CN.html",
    "https://tvzvezda.ru/schedule/",
    "https://tvzvezda.ru/schedule/program-guide/202203102025-vhkvh.html",
    "https://tvzvezda.ru/schedule/program-guide/202203120840-239le.html",
    "https://tvzvezda.ru/schedule/program-guide/202203120945-2dk6p.html",
    "https://tvzvezda.ru/schedule/program-guide/202203101830-g0xtf.html",
    "https://tvzvezda.ru/schedule/program-guide/202203102125-6kaj9.html",
    "https://tvzvezda.ru/schedule/program-guide/202203102305-wr7sq.html",
    "https://tvzvezda.ru/schedule/program-guide/202203102025-vhkvh.html",
    "https://tvzvezda.ru/schedule/program-guide/202203120840-239le.html",
    "https://tvzvezda.ru/schedule/program-guide/202203120945-2dk6p.html",
    "https://tvzvezda.ru/schedule/program-guide/202203101830-g0xtf.html",
    "https://tvzvezda.ru/schedule/program-guide/202203102125-6kaj9.html",
    "https://tvzvezda.ru/schedule/program-guide/202203102305-wr7sq.html",
    "https://tvzvezda.ru/news/vstrane_i_mire/economics/",
    "https://tvzvezda.ru/news/20223101540-AoEjA.html",
    "https://tvzvezda.ru/news/2022310158-IsF9v.html",
    "https://tvzvezda.ru/news/20223101255-rlroS.html",
    "https://tvzvezda.ru/news/20223101134-DCu0X.html",
    "https://tvzvezda.ru/news/vstrane_i_mire/economics/",
    "https://tvzvezda.ru/news/vstrane_i_mire/society/",
    "https://tvzvezda.ru/news/2022310546-zKidn.html",
    "https://tvzvezda.ru/news/2022310235-nwkGl.html",
    "https://tvzvezda.ru/news/2022391834-YF9gC.html",
    "https://tvzvezda.ru/news/2022391638-hCeYw.html",
    "https://tvzvezda.ru/news/vstrane_i_mire/society/",
    "https://tvzvezda.ru/schedule/programs/",
    "https://tvzvezda.ru/schedule/programs/201510291058-7whr.htm/2022391012-0a5ci.html",
    "https://tvzvezda.ru/schedule/programs/201808241352-z30e.htm/202238105-k3QAK.html",
    "https://tvzvezda.ru/schedule/programs/this_morning/2022223947-S0PXz.html",
    "https://tvzvezda.ru/schedule/programs/201605251339-mua8.htm/2022351841-ouXZT.html",
    "https://tvzvezda.ru/schedule/programs/201947915-84uxq.html/2022361736-cBe5s.html",
    "https://tvzvezda.ru/schedule/programs/this_morning/2022310856-0DIWT.html",
    "https://tvzvezda.ru/schedule/programs/202110694-IQrIW.html/2022381026-SovR2.html",
    "https://tvzvezda.ru/schedule/programs/2019961015-Gj7DW.html/2022381023-YEdrd.html",
    "https://tvzvezda.ru/schedule/programs/201808231539-wgb0.htm/2022381013-9cjv5.html",
    "https://tvzvezda.ru/schedule/programs/201808241352-z30e.htm/2022381012-cjR9Q.html",
    "https://tvzvezda.ru/schedule/programs/201510291058-7whr.htm/2022391012-0a5ci.html",
    "https://tvzvezda.ru/schedule/programs/201808241352-z30e.htm/202238105-k3QAK.html",
    "https://tvzvezda.ru/schedule/programs/this_morning/2022223947-S0PXz.html",
    "https://tvzvezda.ru/schedule/programs/201605251339-mua8.htm/2022351841-ouXZT.html",
    "https://tvzvezda.ru/schedule/programs/201947915-84uxq.html/2022361736-cBe5s.html",
    "https://tvzvezda.ru/schedule/programs/this_morning/2022310856-0DIWT.html",
    "https://tvzvezda.ru/schedule/programs/202110694-IQrIW.html/2022381026-SovR2.html",
    "https://tvzvezda.ru/schedule/programs/2019961015-Gj7DW.html/2022381023-YEdrd.html",
    "https://tvzvezda.ru/schedule/programs/201808231539-wgb0.htm/2022381013-9cjv5.html",
    "https://tvzvezda.ru/schedule/programs/201808241352-z30e.htm/2022381012-cjR9Q.html",
    "https://tvzvezda.ru/news/sport/",
    "https://tvzvezda.ru/news/2022322118-LKZEv.html",
    "https://tvzvezda.ru/news/2022321418-W9Lx3.html",
    "https://tvzvezda.ru/news/20222282041-l9hMV.html",
    "https://tvzvezda.ru/news/202222892-Zv0op.html",
    "https://tvzvezda.ru/news/sport/",
    "https://tvzvezda.ru/news/science_n_tech/",
    "https://tvzvezda.ru/news/202231038-mI2aA.html",
    "https://tvzvezda.ru/news/2022382253-Y4kqH.html",
    "https://tvzvezda.ru/news/2022371343-QCVxf.html",
    "https://tvzvezda.ru/news/20223799-6dQQ6.html",
    "https://tvzvezda.ru/news/science_n_tech/",
    "https://tvzvezda.ru/schedule/filmsonline/",
    "https://tvzvezda.ru/schedule/films-online/2022241812-qiWB7.html",
    "https://tvzvezda.ru/schedule/films-online/20221281339-Cfh7W.html",
    "https://tvzvezda.ru/schedule/films-online/20221211759-Z60ls.html",
    "https://tvzvezda.ru/schedule/films-online/20222181638-rfBMJ.html",
    "https://tvzvezda.ru/schedule/films-online/2022218168-WOUyk.html",
    "https://tvzvezda.ru/schedule/films-online/20222111031-QhXUU.html",
    "https://tvzvezda.ru/schedule/films-online/2022241812-qiWB7.html",
    "https://tvzvezda.ru/schedule/films-online/20221281339-Cfh7W.html",
    "https://tvzvezda.ru/schedule/films-online/20221211759-Z60ls.html",
    "https://tvzvezda.ru/schedule/films-online/20222181638-rfBMJ.html",
    "https://tvzvezda.ru/schedule/films-online/2022218168-WOUyk.html",
    "https://tvzvezda.ru/schedule/films-online/20222111031-QhXUU.html",
    "http://tvzvezda.ru/export/rss.xml",
    "https://tvzvezda.ru/webpush_subscribe",
    "http://m.tvzvezda.ru/",
    "https://tvzvezda.ru/news/",
    "https://tvzvezda.ru/news/vstrane_i_mire/",
    "https://tvzvezda.ru/news/vstrane_i_mire/economics/",
    "https://tvzvezda.ru/news/forces/",
    "https://tvzvezda.ru/news/opk/",
    "https://tvzvezda.ru/news/qhistory/",
    "https://tvzvezda.ru/news/vstrane_i_mire/society/",
    "https://tvzvezda.ru/news/sport/",
    "https://tvzvezda.ru/news/science_n_tech/",
    "https://tvzvezda.ru/schedule/",
    "https://tvzvezda.ru/schedule/",
    "https://tvzvezda.ru/schedule/programs/",
    "https://tvzvezda.ru/schedule/programm/",
    "https://tvzvezda.ru/schedule/filmsonline/",
    "https://tvzvezda.ru/about/",
    "https://tvzvezda.ru/weapon/",
    "https://tvzvezda.ru/weapon/aviation/",
    "https://tvzvezda.ru/weapon/flot/",
    "https://tvzvezda.ru/weapon/bron/",
    "https://tvzvezda.ru/weapon/art/",
    "https://tvzvezda.ru/weapon/raketi/",
    "https://tvzvezda.ru/weapon/kosmos/",
    "https://tvzvezda.ru/weapon/prochee/",
    "https://tvzvezda.ru/weapon/infografika/",
    "https://tvzvezda.ru/person/",
    "https://tvzvezda.ru/person/",
    "https://tvzvezda.ru/person/#remember",
    "https://tvzvezda.ru/about/",
    "https://tvzvezda.ru/about/vakansii/",
    "http://old.tvzvezda.ru/partners/",
    "http://glavkino.ru/",
    "https://tvzvezda.ru/about/uchdocs/",
    "https://tvzvezda.ru/about/pravo/",
    "https://tvzvezda.ru/about/license/",
    "https://tvzvezda.ru/about/social-ads/",
    "https://tvzvezda.ru/about/contacts/",
    "https://tvzvezda.ru/sp/zvezda-plus/",
    "https://tvzvezda.ru/about/201510121537-ebpt.htm/",
    "https://www.tvzvezda.ru",
    "https://tvzvezda.ru/about/contacts/",
    "https://tvzvezda.ru/about/pravo/",
    "http://top.mail.ru/jump?from=932097",
    "https://tvzvezda.ru//www.liveinternet.ru/click",
    "https://tvzvezda.ru/bonustv.html"
]


# Retrieve a single page and report the URL and contents
def load_url(url, timeout):
    with urllib.request.urlopen(url, timeout=timeout, context=context) as conn:
        return conn.read()


import random

def main():
    # We can use a with statement to ensure threads are cleaned up promptly
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        # Start the load operations and mark each future with its URL
        future_to_url = {executor.submit(load_url, url, 60): url for url in URLS}

        for future in concurrent.futures.as_completed(future_to_url):
            url = future_to_url[future]
            try:
                data = future.result()
            except Exception as exc:
                print('%r generated an exception: %s' % (url, exc))
            else:
                print('%r page is %d Mbytes' % (url, len(data)/1024))


i = 0
while True:
    random.shuffle(URLS)

    i = i + 1
    print("Round ->", i)

    main()
