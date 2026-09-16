# gen-z-insights
Python-based market research project on Gen-Z consumer behavior, advertising trust and shopping preferences.
Gen-Z Insights
Themen: Education, Income, Social Media, Values, Consumer Behavior
Datensatz
Der Datensatz wurde von Kaggle heruntergeladen:
https://www.kaggle.com/datasets/sadiqguru/gen-z-dataset
Der Datensatz ist frei zugänglich.
Beobachtungen: 5.000
Variablen:
1.	age
2.	gender
3.	region
4.	ethnicity
5.	education
6.	employment
7.	annual_income_usd
8.	primary_platform
9.	daily_screen_hours
10.	val_sustainability_1to5
11.	val_brand_authenticity_1to5
12.	trust_traditional_ads_1to5
13.	trust_influencers_1to5
14.	preferred_shopping_channel
15.	uses_buy_now_pay_later
16.	brand_discovery_channel
17.	monthly_discretionary_usd
Forschungsfrage
Wie unterscheiden sich Werbevertrauen, Shopping-Präferenzen und tägliche Bildschirmzeit innerhalb der vorliegenden Gen-Z-Stichprobe?
Unterfragen
1.	Vertraut die vorliegende Stichprobe traditioneller Werbung oder Influencer-Werbung stärker?
2.	Welche Shopping-Kanäle werden von den Befragten bevorzugt?
3.	Unterscheiden sich diese Präferenzen und das Werbevertrauen nach Geschlecht?
4.	Welche Unterschiede zeigen sich bei der täglichen Bildschirmzeit nach Geschlecht und Alter?
5.	Welche Faktoren hängen mit den monatlichen diskretionären Ausgaben zusammen?
Methoden
•	Deskriptive Statistik
•	Gruppenvergleiche
•	t-Tests für zwei unabhängige Gruppen
•	Pearson-Korrelation
•	Pivot-/Gruppentabellen
•	Multiple lineare Regression
•	Visualisierungen (Boxplot, Streudiagramm)
1. Relevante deskriptive Statistiken zu soziodemografischen Daten
Alter
Durchschnitt: 22,9 Jahre
Minimales Alter: 18 Jahre
Maximales Alter: 28 Jahre
Geschlecht
•	Weiblich: 49,36 %
•	Männlich: 47,90 %
•	Rest: non-binär bzw. nicht angegeben
Bildung
•	Some college: 38,28 %
•	High school: 33,64 %
•	Bachelor's: 23,20 %
•	Graduate: 4,88 %
2. Vertrauen in traditionelle Werbung vs. Influencer-Werbung
Das Vertrauen wurde auf einer Skala von 1 bis 5 gemessen, wobei 1 das niedrigste und 5 das höchste Vertrauen darstellt.
Nur 1,60 % der Befragten gaben für traditionelle Werbung den höchsten Wert (5) an, während 13,74 % für Influencer-Werbung den höchsten Wert angaben.
Umgekehrt gaben 21,56 % der Befragten für traditionelle Werbung den niedrigsten Wert (1) an, während dies bei Influencer-Werbung nur 3,08 % waren.
Das durchschnittliche Vertrauen in Influencer-Werbung liegt bei 3,39, während das durchschnittliche Vertrauen in traditionelle Werbung bei 2,30 liegt.
In der vorliegenden Stichprobe ist damit das durchschnittliche Vertrauen in Influencer-Werbung höher als das Vertrauen in traditionelle Werbung.
Unterschiede nach Geschlecht
Anhand der Pivot-Tabelle zeigen sich keine deutlichen Unterschiede zwischen Männern und Frauen beim Vertrauen in Influencer-Werbung und traditionelle Werbung.
Die durchgeführten t-Tests zeigen ebenfalls keinen statistisch signifikanten Unterschied zwischen Männern und Frauen.
3. Bevorzugte Shopping-Kanäle
Die bevorzugten Shopping-Kanäle verteilen sich folgendermaßen:
•	Mobile App: 39,28 %
•	Website: 25,24 %
•	In-store: 21,14 %
•	Social Commerce: 14,34 %
Mobile Apps und Websites machen zusammen 64,52 % der genannten Präferenzen aus. In der vorliegenden Stichprobe werden somit Online-Shopping-Kanäle häufiger bevorzugt als der Einkauf im stationären Geschäft.
Bei der deskriptiven Betrachtung nach Geschlecht zeigen sich keine deutlichen Unterschiede in den bevorzugten Shopping-Kanälen.
4. Tägliche Bildschirmzeit
Die durchschnittliche tägliche Bildschirmzeit beträgt 5,98 Stunden.
Bildschirmzeit nach Geschlecht
Der Vergleich anhand einer Pivot-Tabelle und eines Boxplots zeigt keinen deutlichen deskriptiven Unterschied zwischen den Geschlechtern.
Zusammenhang zwischen Alter und Bildschirmzeit
Die Pearson-Korrelation zwischen Alter und täglicher Bildschirmzeit beträgt r = 0,005.
Dies entspricht einem praktisch nicht vorhandenen linearen Zusammenhang zwischen Alter und täglicher Bildschirmzeit innerhalb der vorliegenden Stichprobe.
5. Monatliche diskretionäre Ausgaben
Zur Untersuchung der Faktoren, die mit den monatlichen diskretionären Ausgaben zusammenhängen, wurde eine multiple lineare Regression durchgeführt.
Variablen
Abhängige Variable:
•	monatliche diskretionäre Ausgaben (monthly_discretionary_usd)
Unabhängige Variablen:
•	Alter
•	jährliches Einkommen in US-Dollar
•	tägliche Bildschirmzeit
Ergebnisse
Das korrigierte R² beträgt 0,782.
Falls dieser Wert tatsächlich 0,782 im Regressionsoutput beträgt, bedeutet dies, dass das Modell etwa 78,2 % der Varianz der monatlichen diskretionären Ausgaben erklärt.
Die tägliche Bildschirmzeit weist keinen statistisch signifikanten Zusammenhang mit den monatlichen diskretionären Ausgaben auf (p = 0,916).
Zwischen Alter und monatlichen diskretionären Ausgaben besteht ein negativer statistisch signifikanter Zusammenhang (β = -2,1; p = 0,010). Innerhalb der vorliegenden Stichprobe sind höhere Alterswerte somit mit niedrigeren monatlichen diskretionären Ausgaben verbunden, wenn Einkommen und tägliche Bildschirmzeit konstant gehalten werden.
Das jährliche Einkommen weist einen positiven statistisch signifikanten Zusammenhang mit den monatlichen diskretionären Ausgaben auf (β = 0,01; p < 0,001).
Die praktische Bedeutung des Koeffizienten sollte dabei anhand der Skalierung interpretiert werden. Ein Koeffizient von 0,01 bedeutet beispielsweise, dass ein um 10.000 US-Dollar höheres Jahreseinkommen mit etwa 100 US-Dollar höheren monatlichen diskretionären Ausgaben verbunden wäre, sofern die übrigen Variablen konstant gehalten werden.
Schlussfolgerung
Anhand der vorliegenden Stichprobe zeigt sich ein negativer Zusammenhang zwischen Alter und monatlichen diskretionären Ausgaben. Die tägliche Bildschirmzeit weist dagegen keinen statistisch signifikanten Zusammenhang mit den monatlichen diskretionären Ausgaben auf.
Das jährliche Einkommen steht in einem positiven statistisch signifikanten Zusammenhang mit den monatlichen diskretionären Ausgaben. Die praktische Bedeutung dieses Zusammenhangs sollte jedoch anhand der konkreten Skalierung und Effektgröße beurteilt werden.
Limitationen
Der Datensatz wurde von Kaggle bezogen. Die verfügbare Datensatzbeschreibung enthält keine ausreichenden Informationen über die konkrete Stichprobenziehung, Datenerhebung und Repräsentativität.
Die Ergebnisse sind daher als deskriptive bzw. explorative Ergebnisse für die vorliegende Stichprobe zu verstehen und können nicht ohne Weiteres auf die gesamte Generation Z übertragen werden.
