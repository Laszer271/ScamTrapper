//alert('Grrr.')
// chrome.runtime.onMessage.addListener(function (request, sender, sendResponse) {
//   const re = new RegExp('bear', 'gi')
//   const matches = document.documentElement.innerHTML.match(re)
//   sendResponse({count: matches.length})
// })


var frazy = ['bear', 'inwestycja bez ryzyka', 'zysk bez ryzyka', 'wysoka stopa zwrotu ', 'wysoki zwrot z inwestycji',
    'szybka pewna inwestycja', 'szybki wysoki zysk', 'gwarancja twojego kapitału', 'ogromny zwrot z inwestycji',
    'pomnóż swoje pieniądze', 'zyskaj dodatkowy kapitał', 'rocznie bez wysiłku', 'zarabiaj z domu', 'zarabiaj przez internet',
    'sprawdzone numer kont', 'gwarantowane wysokie zarobki', 'firma w pełni legalna', 'legalnie działająca firma', 'firma w pełni wypłacalna',
    'legalny darmowy program', 'Gwarancja regularnych zarobków', 'Oferta limitowana czasowo', 'oferta ograniczona czasowo', 'elitarna wysoka inwestycja',
    'ekskluzywna inwestycja dla Ciebie', 'wysokie szybkie zarobki', 'łatwe proste zarabianie', 'bez żadnego ryzyka', 'warto w to zainwestować',
    'odmień swoje życie', 'propozycja zarobienia gotówki', 'skorzystasz i zarobisz', 'elitarny klub posiadaczy', 'nie przegap szansy',
    'zostało kilka miejsc', 'szansa na zarobienie milionów', 'zarabianie jest możliwe', 'wykorzystanie najnowszej technologii',
    'gwarantowany sukces finansowy', 'kupił bitcoin i zarobił', 'zarabiać na bitcoinie', 'kapitał na inwestycje', 'niezwykła okazja finansowa',
    'łatwa bezpieczna inwestycja', 'alternatywne inwestycje finansowe', 'zarabianie w internecie', 'zarabiaj darmowe kryptowaluty',
    'stwórz własny token', 'zarabiaj darmowe tokeny', 'zgarnij darmowe pieniądze', 'każdą poleconą osobę', 'pieniądze za darmo',
    'wysłać przelewem złotówkę', 'konkursy z atrakcyjnymi nagrodami', 'założyć darmowe konto', 'usługa całkowicie darmowa',
    'polecać tę promocję', 'szansa na wygranie', 'świetne, darmowe usługi', 'zarabianie w programie poleceń', 'jak szybko zarobić',
    'dochód pasywny bez inwestycji', 'bez żadnej inwestycji', 'Zarabianie na kryptowalutach', 'nowa giełda kryptowalut', 'okazję do zarobienia',
    'możemy zgarnąć bonusy', 'twój pakiet VIP', 'proste pakiety inwestycyjne', 'inwestycje w złoto', 'inwestycje w diamenty', 'możesz zgarnąć bonusy',
    'możliwości zarobienia pieniędzy', 'gwarantujemy wysokie premie', 'zostań naszym partnerem', 'pierwsza taka platforma',
    'oszczędzanie i pomnażanie kapitału', 'otrzymuj dotacje i zarabiaj', 'nie wymaga ryzyka', 'nie wymaga wiedzy', 'nie wymaga doświadczenia',
    'nie wymaga inwestycji', 'wspólnie zarabiać pieniądze', 'zysk w krótkim czasie', 'zarabiać z nami', 'wykorzystujemy efekt dźwigni',
    'otrzymasz pierwsze dotacje', 'zarób bez pośredników', 'biznes jest uczciwy', 'budowanie kapitału na życie', 'inwestycja w altcoiny',
    'bardzo wysoka kapitalizacja', 'inwestuj w nowe altcoiny', 'nowy sposób inwestowania', 'łatwy trading na aktywach', 'inwestycje w realne aktywa',
    'znaczna reedukacja kosztów', 'dobry moment na wejście', 'wysoki zysk inwestycje', 'gwarantowany zysk bez ryzyka', 'pasywny dochód', 'szybki zysk',
    'szybki zwrot z inwestycji', 'ubezpieczenia oszczędnościowe', 'oszczędzaj przez inwestowanie', 'rekomenduję', 'polecam', 'podtrzymuję prognozę',
    'sygnały zakupowe', 'odjazd', 'wystrzał', 'zasięg wzrostu', 'niedoszacowanie', 'fala wzrostowa', 'spółka perspektywiczna', 'wzrost kursu',
    'wzrost obrotu', 'wzrost kapitalizacji', 'dochód bez ryzyka', 'pewny zysk', 'pewne zyski', 'gwarantowany zysk', 'pewna stopa zwrotu',
    'wysoka stopa zwrotu ', 'gwarantowana stopa zwrotu', 'gwarantowany dochód', 'obligacje bez ryzyka', 'szybki dochód', 'pewne obligacje',
    'sprzedam akcje', 'sprzedam obligacje', 'inwestycja gwarantowana', 'inwestycje gwarantowane', 'pewna inwestycja', 'lokata bez ryzyka',
    'zainwestuj bez ryzyka', 'zyskaj więcej niż w banku', 'bezpieczne akcje', 'pewne akcje', 'zarabiaj bez ryzyka', 'zarabiaj bez ograniczeń',
    'zarabiaj bezpiecznie', 'bezpieczna kasa', 'pewna kasa', 'kasa bez ryzyka', 'szybki hajs', 'szybka kasa', 'wysoki kupon', 'pewny dochód',
    'stały dochód', 'pewny wykup', 'wysoki zwrot bez ryzyka', 'obligacje bez defaultu', 'defaultowe obligacje', 'kupię niewykupione obligacje',
    'kupię przeterminowane obligacje', 'działanie bez licencji', 'podszywanie się pod działalność licencjonowaną na rynku finansowym',
    'podszywanie się pod działalność regulowaną na rynku finansowym', 'pranie pieniędzy', 'oszukiwanie klientów instytucji finansowych',
    'oszustwo klientów instytucji finansowych', 'brak rozliczenia z klientami instytucji finansowych', 'Porywanie URL / typosquatting',
    'cryptoscam', 'oszustwo z wykorzystaniem kryptowaluty', 'oszustwa związane z kryptowalutami', 'Oszustwa Bitcoin', 'finansowe ataki phishingowe',
    'oszustwa związane z marketingiem partnerskim', 'oszustwa związane z programami partnerskim', 'gwarantowany zysk z inwestycji',
    'okazja inwestycyjna limitowana', 'oferta inwestycyjna limitowana ', 'niezamówione porady dotyczące inwestycji', 'podejrzane transakcje',
    'nielicencjonowany / nieautoryzowany / niezarejestrowany broker', 'nielicencjonowany / nieautoryzowany / niezarejestrowany agent',
    'nielicencjonowany / nieautoryzowany / niezarejestrowany doradca inwestycyjny', 'sfałszowane dokumenty finansowe', 'sfabrykowane raporty finansowe',
    'rachunkowość kreatywna', 'oszustwa związane z rachunkowością kreatywną', 'Oszustwa na rynku Forex', 'nielicencjonowany broker forex',
    'dźwignia finansowa inwestycje', 'fałszywe roszczenie', 'zawyżone roszczenie', 'phishing, kradzież danych', 'wyłudzenie', 'ransomware',
    'oszustwo związane z wnioskiem ubezpieczeniowym', 'Fałszywe roszczenia dotyczące oszustwa', 'nieuzasadniona odmowa wypłaty ubezpiezenia',
    'ustawiane wypadki celowe stłuczki', 'fałszywe zgłoszenia policyjne', 'nieuzasadnione koszty napraw zawyżanie odszkodowania', 'fałszywe akty zgonów',
    'nieuprawnione pobieranie prowizji przez pośredników ', 'udziałowiec lub prezes z krajów spoza unii europejskiej',
    'podmiot wpisywany na inne listy sankcyjne (shame lists)'];

var i;
var matches = [];
var m = 0;
for (i = 0; i < frazy.length; i++) {
    var re = new RegExp(frazy[i], 'gi')
    var match = document.documentElement.innerHTML.match(re) || []
    m += match.length
    if (match.length > 0)
        matches.push(frazy[i])
}
//const re = new RegExp('bear', 'gi')
//const matches = document.documentElement.innerHTML.match(re) || []

chrome.runtime.sendMessage({
    url: window.location.href,
    count: m,
    f: matches
})