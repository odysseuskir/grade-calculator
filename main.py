print("Επιλέξτε τάξη:\nα) Α' Λυκείου\nβ) Β' Λυκείου\nγ) Γ' Λυκείου\n")
grade = input("Επιλογή (α, β ή γ): ")

def tenth_grade():
    ancient_greek = [0, 0, 0]
    ancient_greek[0] = int(input("\nΒαθμός Αρχαίας Ελληνικής Γλώσσας και Γραμματείας (Α' Τετράμηνο): "))
    ancient_greek[1] = int(input("Βαθμός Αρχαίας Ελληνικής Γλώσσας και Γραμματείας (Β' Τετράμηνο): "))
    ancient_greek[2] = int(input("Βαθμός Αρχαίας Ελληνικής Γλώσσας και Γραμματείας (Γραπτό εξετάσεων): "))

    average_ancient_greek = (((ancient_greek[0] + ancient_greek[1]) / 2) + ancient_greek[2]) / 2

    modern_greek = [0, 0, 0]
    modern_greek[0] = int(input("\nΒαθμός Νεοελληνικής Γλώσσας και Λογοτεχνίας (Α' Τετράμηνο): "))
    modern_greek[1] = int(input("Βαθμός Νεοελληνικής Γλώσσας και Λογοτεχνίας (Β' Τετράμηνο): "))
    modern_greek[2] = int(input("Βαθμός Νεοελληνικής Γλώσσας και Λογοτεχνίας (Γραπτό εξετάσεων): "))

    average_modern_greek = (((modern_greek[0] + modern_greek[1]) / 2) + modern_greek[2]) / 2

    history = [0, 0, 0]
    history[0] = int(input("\nΒαθμός Ιστορίας (Α' Τετράμηνο): "))
    history[1] = int(input("Βαθμός Ιστορίας (Β' Τετράμηνο): "))
    history[2] = int(input("Βαθμός Ιστορίας (Γραπτό εξετάσεων): "))

    average_history = (((history[0] + history[1]) / 2) + history[2]) / 2

    algebra = [0, 0, 0]
    algebra[0] = int(input("\nΒαθμός Άλγεβρας (Α' Τετράμηνο): "))
    algebra[1] = int(input("Βαθμός Άλγεβρας (Β' Τετράμηνο): "))
    algebra[2] = int(input("Βαθμός Άλγεβρας (Γραπτό εξετάσεων): "))

    average_algebra = (((algebra[0] + algebra[1]) / 2) + algebra[2]) / 2

    geometry = [0, 0, 0]
    geometry[0] = int(input("\nΒαθμός Γεωμετρίας (Α' Τετράμηνο): "))
    geometry[1] = int(input("Βαθμός Γεωμετρίας (Β' Τετράμηνο): "))
    geometry[2] = int(input("Βαθμός Γεωμετρίας (Γραπτό εξετάσεων): "))

    average_geometry = (((geometry[0] + geometry[1]) / 2) + geometry[2]) / 2

    physics = [0, 0, 0]
    physics[0] = int(input("\nΒαθμός Φυσικής (Α' Τετράμηνο): "))
    physics[1] = int(input("Βαθμός Φυσικής (Β' Τετράμηνο): "))
    physics[2] = int(input("Βαθμός Φυσικής (Γραπτό εξετάσεων): "))
    
    average_physics = (((physics[0] + physics[1]) / 2) + physics[2]) / 2

    chemistry = [0, 0, 0]
    chemistry[0] = int(input("\nΒαθμός Χημείας (Α' Τετράμηνο): "))
    chemistry[1] = int(input("Βαθμός Χημείας (Β' Τετράμηνο): "))
    chemistry[2] = int(input("Βαθμός Χημείας (Γραπτό εξετάσεων): "))

    average_chemistry = (((chemistry[0] + chemistry[1]) / 2) + chemistry[2]) / 2

    english = [0, 0, 0]
    english[0] = int(input("\nΒαθμός Αγγλικών (Α' Τετράμηνο): "))
    english[1] = int(input("Βαθμός Αγγλικών (Β' Τετράμηνο): "))
    english[2] = int(input("Βαθμός Αγγλικών (Γραπτό εξετάσεων): "))

    average_english = (((english[0] + english[1]) / 2) + english[2]) / 2

    religious_studies = [0, 0]
    religious_studies[0] = int(input("\nΒαθμός Θρησκευτικών (Α' Τετράμηνο): "))
    religious_studies[1] = int(input("Βαθμός Θρησκευτικών (Β' Τετράμηνο): "))

    average_religious_studies = (religious_studies[0] + religious_studies[1]) / 2

    biology = [0, 0]
    biology[0] = int(input("\nΒαθμός Βιολογίας (Α' Τετράμηνο): "))
    biology[1] = int(input("Βαθμός Βιολογίας (Β' Τετράμηνο): "))

    average_biology = (biology[0] + biology[1]) / 2

    second_foreign_language = [0, 0]
    second_foreign_language[0] = int(input("\nΒαθμός Δεύτερης Ξένης Γλώσσας (Γαλλικά ή Γερμανικά) (Α' Τετράμηνο): "))
    second_foreign_language[1] = int(input("Βαθμός Δεύτερης Ξένης Γλώσσας (Γαλλικά ή Γερμανικά) (Β' Τετράμηνο): "))

    average_second_foreign_language = (second_foreign_language[0] + second_foreign_language[1]) / 2

    political_studies = [0, 0]
    political_studies[0] = int(input("\nΒαθμός Πολιτικής Παιδείας (Α' Τετράμηνο): "))
    political_studies[1] = int(input("Βαθμός Πολιτικής Παιδείας (Β' Τετράμηνο): "))

    average_political_studies = (political_studies[0] + political_studies[1]) / 2

    cs = [0, 0]
    cs[0] = int(input("\nΒαθμός Εφαρμογών Πληροφορικής (Α' Τετράμηνο): "))
    cs[1] = int(input("Βαθμός Εφαρμογών Πληροφορικής (Β' Τετράμηνο): "))

    average_cs = (cs[0] + cs[1]) / 2

    pe = [0, 0]
    pe[0] = int(input("\nΒαθμός Φυσικής Αγωγής (Α' Τετράμηνο): "))
    pe[1] = int(input("Βαθμός Φυσικής Αγωγής (Β' Τετράμηνο): "))

    average_pe = (pe[0] + pe[1]) / 2

    average_greek_language = (average_modern_greek + average_ancient_greek) / 2
    average_math = (average_algebra + average_geometry) / 2
    average_sciences = (average_physics + average_chemistry + average_biology) / 2

    average = (average_greek_language + average_history + average_math + average_sciences + average_english + average_religious_studies + average_second_foreign_language + average_political_studies + average_cs + average_pe) / 10
    print(f"Γενικός Μέσος Όρος: {average}\n\n")
    print(f"Μέσος Όρος Ελληνικής Γλώσσας: {average_greek_language}")
    print(f"Μέσος Όρος Ιστορίας: {average_history}")
    print(f"Μέσος Όρος Μαθηματικών: {average_math}")
    print(f"Μέσος Όρος Φυσικών Επιστημών: {average_sciences}")
    print(f"Μέσος Όρος Αγγλικών: {average_english}")
    print(f"Μέσος Όρος Θρησκευτικών: {average_religious_studies}")
    print(f"Μέσος Όρος Δεύτερης Ξένης Γλώσσας: {average_second_foreign_language}")
    print(f"Μέσος Όρος Πολιτικής Παιδείας: {average_political_studies}")
    print(f"Μέσος Όρος Εφαρμογών Πληροφορικής: {average_cs}")
    print(f"Μέσος Όρος Φυσικής Αγωγής: {average_pe}")

def eleventh_grade():
    print("Επιλέξτε ομάδα προσανατολισμού:\nα) Ομάδα Προσανατολισμού Ανθρωπιστικών Σπουδών\nβ) Ομάδα Προσανατολισμού Θετικών Σπουδών")
    study_field = input("Επιλογή (α ή β): ")

    modern_greek = [0, 0, 0]
    modern_greek[0] = int(input("\n\nΒαθμός Νεοελληνικής Γλώσσας και Λογοτεχνίας (Α' Τετράμηνο): "))
    modern_greek[1] = int(input("Βαθμός Νεοελληνικής Γλώσσας και Λογοτεχνίας (Β' Τετράμηνο): "))
    modern_greek[2] = int(input("Βαθμός Νεοελληνικής Γλώσσας και Λογοτεχνίας (Γραπτό εξετάσεων): "))

    average_modern_greek = (((modern_greek[0] + modern_greek[1]) / 2)  + modern_greek[2]) / 2

    history = [0, 0, 0]
    history[0] = int(input("\nΒαθμός Ιστορίας (Α' Τετράμηνο): "))
    history[1] = int(input("Βαθμός Ιστορίας (Β' Τετράμηνο): "))
    history[2] = int(input("Βαθμός Ιστορίας (Γραπτό εξετάσεων): "))

    average_history = (((history[0] + history[1]) / 2)  + history[2]) / 2

    algebra = [0, 0, 0]
    algebra[0] = int(input("\nΒαθμός Άλγεβρας (Α' Τετράμηνο): "))
    algebra[1] = int(input("Βαθμός Άλγεβρας (Β' Τετράμηνο): "))
    algebra[2] = int(input("Βαθμός Άλγεβρας (Γραπτό εξετάσεων): "))

    average_algebra = (((algebra[0] + algebra[1]) / 2)  + algebra[2]) / 2

    geometry = [0, 0, 0]
    geometry[0] = int(input("\nΒαθμός Γεωμετρίας (Α' Τετράμηνο): "))
    geometry[1] = int(input("Βαθμός Γεωμετρίας (Β' Τετράμηνο): "))
    geometry[2] = int(input("Βαθμός Γεωμετρίας (Γραπτό εξετάσεων): "))

    average_geometry = (((geometry[0] + geometry[1]) / 2)  + geometry[2]) / 2

    biology = [0, 0, 0]
    biology[0] = int(input("\nΒαθμός Βιολογίας (Α' Τετράμηνο): "))
    biology[1] = int(input("Βαθμός Βιολογίας (Β' Τετράμηνο): "))
    biology[2] = int(input("Βαθμός Βιολογίας (Γραπτό εξετάσεων): "))

    average_biology = (((biology[0] + biology[1]) / 2)  + biology[2]) / 2

    english = [0, 0, 0]
    english[0] = int(input("\nΒαθμός Αγγλικής Γλώσσας (Α' Τετράμηνο): "))
    english[1] = int(input("Βαθμός Αγγλικής Γλώσσας (Β' Τετράμηνο): "))
    english[2] = int(input("Βαθμός Αγγλικής Γλώσσας (Γραπτό εξετάσεων): "))

    average_english = (((english[0] + english[1]) / 2)  + english[2]) / 2

    if study_field == "α":
        ancient_greek_field = [0, 0, 0]
        ancient_greek_field[0] = int(input("\nΒαθμός Αρχαίας Ελληνικής Γλώσσας και Γραμματείας (Α' Τετράμηνο) (Προσανατολισμού): "))
        ancient_greek_field[1] = int(input("Βαθμός Αρχαίας Ελληνικής Γλώσσας και Γραμματείας (Β' Τετράμηνο) (Προσανατολισμού): "))
        ancient_greek_field[2] = int(input("Βαθμός Αρχαίας Ελληνικής Γλώσσας και Γραμματείας (Γραπτό εξετάσεων) (Προσανατολισμού): "))

        average_ancient_greek_field = (((ancient_greek_field[0] + ancient_greek_field[1]) / 2)  + ancient_greek_field[2]) / 2

        latin_field = [0, 0, 0]
        latin_field[0] = int(input("\nΒαθμός Λατινικών (Α' Τετράμηνο) (Προσανατολισμού): "))
        latin_field[1] = int(input("Βαθμός Λατινικών (Β' Τετράμηνο) (Προσανατολισμού): "))
        latin_field[2] = int(input("Βαθμός Λατινικών (Γραπτό εξετάσεων) (Προσανατολισμού): "))

        average_latin_field = (((latin_field[0] + latin_field[1]) / 2)  + latin_field[2]) / 2

        average_humanities = (average_ancient_greek_field + average_latin_field) / 2

    elif study_field == "β":
        math_field = [0, 0, 0]
        math_field[0] = int(input("\nΒαθμός Μαθηματικών (Α' Τετράμηνο) (Προσανατολισμού): "))
        math_field[1] = int(input("Βαθμός Μαθηματικών (Β' Τετράμηνο) (Προσανατολισμού): "))
        math_field[2] = int(input("Βαθμός Μαθηματικών (Γραπτό εξετάσεων) (Προσανατολισμού): "))

        average_math_field = (((math_field[0] + math_field[1]) / 2)  + math_field[2]) / 2

        physics_field = [0, 0, 0]
        physics_field[0] = int(input("\nΒαθμός Φυσικής (Α' Τετράμηνο) (Προσανατολισμού): "))
        physics_field[1] = int(input("Βαθμός Φυσικής (Β' Τετράμηνο) (Προσανατολισμού): "))
        physics_field[2] = int(input("Βαθμός Φυσικής (Γραπτό εξετάσεων) (Προσανατολισμού): "))

        average_physics_field = (((physics_field[0] + physics_field[1]) / 2)  + physics_field[2]) / 2

        average_positive_sciences = (average_math_field + average_physics_field) / 2

    else:
        print("Σφάλμα. Επιλέξτε α ή β.")

    ancient_greek = [0, 0]
    ancient_greek[0] = int(input("\nΒαθμός Αρχαίας Ελληνικής Γλώσσας και Γραμματείας (Α' Τετραμήνου): "))
    ancient_greek[1] = int(input("Βαθμός Αρχαίας Ελληνικής Γλώσσας και Γραμματείας (Β' Τετραμήνου): "))

    average_ancient_greek = (ancient_greek[0] + ancient_greek[1]) / 2

    physics = [0, 0]
    physics[0] = int(input("\nΒαθμός Φυσικής (Α' Τετραμήνου): "))
    physics[1] = int(input("Βαθμός Φυσικής (Β' Τετραμήνου): "))

    average_physics = (physics[0] + physics[1]) / 2

    chemistry = [0, 0]
    chemistry[0] = int(input("\nΒαθμός Χημείας (Α' Τετραμήνου): "))
    chemistry[1] = int(input("Βαθμός Χημείας (Β' Τετραμήνου): "))

    average_chemistry = (chemistry[0] + chemistry[1]) / 2

    cs = [0, 0]
    cs[0] = int(input("\nΒαθμός Εισαγωγής στις Αρχές της Επιστήμης των Η/Υ (Α' Τετραμήνου): "))
    cs[1] = int(input("Βαθμός Εισαγωγής στις Αρχές της Επιστήμης των Η/Υ (Β' Τετραμήνου): "))

    average_cs = (cs[0] + cs[1]) / 2

    philosophy = [0, 0]
    philosophy[0] = int(input("\nΒαθμός Φιλοσοφίας (Α' Τετραμήνου): "))
    philosophy[1] = int(input("Βαθμός Φιλοσοφίας (Β' Τετραμήνου): "))

    average_philosophy = (philosophy[0] + philosophy[1]) / 2

    religious_studies = [0, 0]
    religious_studies[0] = int(input("\nΒαθμός Θρησκευτικών (Α' Τετραμήνου): "))
    religious_studies[1] = int(input("Βαθμός Θρησκευτικών (Β' Τετραμήνου): "))

    average_religious_studies = (religious_studies[0] + religious_studies[1]) / 2

    second_foreign_language = [0, 0]
    second_foreign_language[0] = int(input("\nΒαθμός Δεύτερης Ξένης Γλώσσας (Γαλλικά ή Γερμανικά) (Α' Τετραμήνου): "))
    second_foreign_language[1] = int(input("Βαθμός Δεύτερης Ξένης Γλώσσας (Γαλλικά ή Γερμανικά) (Β' Τετραμήνου): "))

    average_second_foreign_language = (second_foreign_language[0] + second_foreign_language[1]) / 2

    pe = [0, 0]
    pe[0] = int(input("\nΒαθμός Φυσικής Αγωγής (Α' Τετραμήνου): "))
    pe[1] = int(input("Βαθμός Φυσικής Αγωγής (Β' Τετραμήνου): "))

    average_pe = (pe[0] + pe[1]) / 2

    average_greek_language = (average_modern_greek + average_ancient_greek) / 2
    average_math = (average_algebra + average_geometry) / 2
    average_sciences = (average_biology + average_physics + average_chemistry) / 3

    if study_field == "α":
        average = (average_greek_language + average_history + average_math + average_sciences + average_english + average_philosophy + average_religious_studies + average_second_foreign_language + average_pe + average_humanities) / 10
        print(f"Γενικός Μέσος Όρος: {average}\n\n")
        print(f"Μέσος Όρος Ελληνικής Γλώσσας: {average_greek_language}")
        print(f"Μέσος Όρος Ιστορίας: {average_history}")
        print(f"Μέσος Όρος Μαθηματικών: {average_math}")
        print(f"Μέσος Όρος Φυσικών Επιστημών: {average_sciences}")
        print(f"Μέσος Όρος Αγγλικής Γλώσσας: {average_english}")
        print(f"Μέσος Όρος Φιλοσοφίας: {average_philosophy}")
        print(f"Μέσος Όρος Θρησκευτικών: {average_religious_studies}")
        print(f"Μέσος Όρος Δεύτερης Ξένης Γλώσσας: {average_second_foreign_language}")
        print(f"Μέσος Όρος Φυσικής Αγωγής: {average_pe}")
        print(f"Μέσος Όρος Ανθρωπιστικών Σπουδών: {average_humanities}")

    if study_field == "β":
        average = (average_greek_language + average_history + average_math + average_sciences + average_english + average_philosophy + average_religious_studies + average_second_foreign_language + average_pe + average_positive_sciences) / 10
        print(f"Γενικός Μέσος Όρος: {average}\n\n")
        print(f"Μέσος Όρος Ελληνικής Γλώσσας και Λογοτεχνίας: {average_greek_language}")
        print(f"Μέσος Όρος Ιστορίας: {average_history}")
        print(f"Μέσος Όρος Μαθηματικών: {average_math}")
        print(f"Μέσος Όρος Φυσικών Επιστημών: {average_sciences}")
        print(f"Μέσος Όρος Αγγλικής Γλώσσας: {average_english}")
        print(f"Μέσος Όρος Φιλοσοφίας: {average_philosophy}")
        print(f"Μέσος Όρος Θρησκευτικών: {average_religious_studies}")
        print(f"Μέσος Όρος Δεύτερης Ξένης Γλώσσας: {average_second_foreign_language}")
        print(f"Μέσος Όρος Φυσικής Αγωγής: {average_pe}")
        print(f"Μέσος Όρος Θετικών Σπουδών: {average_positive_sciences}")

def twelfth_grade():
    print("Επιλέξτε ομάδα προσανατολισμού:\nα) Ομάδα Προσανατολισμού Ανθρωπιστικών Σπουδών\nβ) Ομάδα Προσανατολισμού Θετικών Σπουδών\nγ) Ομάδα Προσανατολισμού Σπουδών Υγείας\nδ) Ομάδα Προσανατολισμού Σπουδών Οικονομίας και Πληροφορικής\n")
    study_field = input("Επιλογή (α, β, γ ή δ): ")

    modern_greek = [0, 0, 0]
    modern_greek[0] = int(input("\n\nΒαθμός Νεοελληνικής Γλώσσας και Λογοτεχνίας (Α' Τετράμηνο): "))
    modern_greek[1] = int(input("Βαθμός Νεοελληνικής Γλώσσας και Λογοτεχνίας (Β' Τετράμηνο): "))
    modern_greek[2] = int(input("Βαθμός Νεοελληνικής Γλώσσας και Λογοτεχνίας (Γραπτό εξετάσεων): "))

    average_modern_greek = (((modern_greek[0] + modern_greek[1]) / 2)  + modern_greek[2]) / 2

    if study_field == "α":
        ancient_greek_field = [0, 0, 0]
        ancient_greek_field[0] = int(input("\nΒαθμός Αρχαίας Ελληνικής Γλώσσας και Γραμματείας (Α' Τετράμηνο) (Προσανατολισμού): "))
        ancient_greek_field[1] = int(input("Βαθμός Αρχαίας Ελληνικής Γλώσσας και Γραμματείας (Β' Τετράμηνο) (Προσανατολισμού): "))
        ancient_greek_field[2] = int(input("Βαθμός Αρχαίας Ελληνικής Γλώσσας και Γραμματείας (Γραπτό εξετάσεων) (Προσανατολισμού): "))

        average_ancient_greek_field = (((ancient_greek_field[0] + ancient_greek_field[1]) / 2)  + ancient_greek_field[2]) / 2

        history_field = [0, 0, 0]
        history_field[0] = int(input("\nΒαθμός Ιστορίας (Α' Τετράμηνο) (Προσανατολισμού): "))
        history_field[1] = int(input("Βαθμός Ιστορίας (Β' Τετράμηνο) (Προσανατολισμού): "))
        history_field[2] = int(input("Βαθμός Ιστορίας (Γραπτό εξετάσεων) (Προσανατολισμού): "))

        average_history_field = (((history_field[0] + history_field[1]) / 2)  + history_field[2]) / 2

        latin_field = [0, 0, 0]
        latin_field[0] = int(input("\nΒαθμός Λατινικών (Α' Τετράμηνο) (Προσανατολισμού): "))
        latin_field[1] = int(input("Βαθμός Λατινικών (Β' Τετράμηνο) (Προσανατολισμού): "))
        latin_field[2] = int(input("Βαθμός Λατινικών (Γραπτό εξετάσεων) (Προσανατολισμού): "))

        average_latin_field = (((latin_field[0] + latin_field[1]) / 2)  + latin_field[2]) / 2

        average_humanities = (average_ancient_greek_field + average_history_field + average_latin_field) / 3

        math = [0, 0, 0]
        math[0] = int(input("\nΒαθμός Μαθηματικών (Α' Τετράμηνο): "))
        math[1] = int(input("Βαθμός Μαθηματικών (Β' Τετράμηνο): "))
        math[2] = int(input("Βαθμός Μαθηματικών (Γραπτό εξετάσεων): "))

        average_math = (((math[0] + math[1]) / 2)  + math[2]) / 2

    elif study_field == "β":
        math_field = [0, 0, 0]
        math_field[0] = int(input("\nΒαθμός Μαθηματικών (Α' Τετράμηνο) (Προσανατολισμού): "))
        math_field[1] = int(input("Βαθμός Μαθηματικών (Β' Τετράμηνο) (Προσανατολισμού): "))
        math_field[2] = int(input("Βαθμός Μαθηματικών (Γραπτό εξετάσεων) (Προσανατολισμού): "))

        average_math_field = (((math_field[0] + math_field[1]) / 2)  + math_field[2]) / 2

        physics_field = [0, 0, 0]
        physics_field[0] = int(input("\nΒαθμός Φυσικής (Α' Τετράμηνο) (Προσανατολισμού): "))
        physics_field[1] = int(input("Βαθμός Φυσικής (Β' Τετράμηνο) (Προσανατολισμού): "))
        physics_field[2] = int(input("Βαθμός Φυσικής (Γραπτό εξετάσεων) (Προσανατολισμού): "))

        average_physics_field = (((physics_field[0] + physics_field[1]) / 2)  + physics_field[2]) / 2

        chemistry_field = [0, 0, 0]
        chemistry_field[0] = int(input("\nΒαθμός Χημείας (Α' Τετράμηνο) (Προσανατολισμού): "))
        chemistry_field[1] = int(input("Βαθμός Χημείας (Β' Τετράμηνο) (Προσανατολισμού): "))
        chemistry_field[2] = int(input("Βαθμός Χημείας (Γραπτό εξετάσεων) (Προσανατολισμού): "))

        average_chemistry_field = (((chemistry_field[0] + chemistry_field[1]) / 2)  + chemistry_field[2]) / 2

        average_positive_sciences = (average_math_field + average_physics_field + average_chemistry_field) / 3

        history = [0, 0, 0]
        history[0] = int(input("\nΒαθμός Ιστορίας (Α' Τετράμηνο): "))
        history[1] = int(input("Βαθμός Ιστορίας (Β' Τετράμηνο): "))
        history[2] = int(input("Βαθμός Ιστορίας (Γραπτό εξετάσεων): "))

    elif study_field == "γ":
        biology_field = [0, 0, 0]
        biology_field[0] = int(input("\nΒαθμός Βιολογίας (Α' Τετράμηνο) (Προσανατολισμού): "))
        biology_field[1] = int(input("Βαθμός Βιολογίας (Β' Τετράμηνο) (Προσανατολισμού): "))
        biology_field[2] = int(input("Βαθμός Βιολογίας (Γραπτό εξετάσεων) (Προσανατολισμού): "))

        average_biology_field = (((biology_field[0] + biology_field[1]) / 2)  + biology_field[2]) / 2

        physics_field = [0, 0, 0]
        physics_field[0] = int(input("\nΒαθμός Φυσικής (Α' Τετράμηνο) (Προσανατολισμού): "))
        physics_field[1] = int(input("Βαθμός Φυσικής (Β' Τετράμηνο) (Προσανατολισμού): "))
        physics_field[2] = int(input("Βαθμός Φυσικής (Γραπτό εξετάσεων) (Προσανατολισμού): "))

        average_physics_field = (((physics_field[0] + physics_field[1]) / 2)  + physics_field[2]) / 2

        chemistry_field = [0, 0, 0]
        chemistry_field[0] = int(input("\nΒαθμός Χημείας (Α' Τετράμηνο) (Προσανατολισμού): "))
        chemistry_field[1] = int(input("Βαθμός Χημείας (Β' Τετράμηνο) (Προσανατολισμού): "))
        chemistry_field[2] = int(input("Βαθμός Χημείας (Γραπτό εξετάσεων) (Προσανατολισμού): "))

        average_chemistry_field = (((chemistry_field[0] + chemistry_field[1]) / 2)  + chemistry_field[2]) / 2

        average_health_sciences = (average_biology_field + average_physics_field + average_chemistry_field) / 2

        history = [0, 0, 0]
        history[0] = int(input("\nΒαθμός Ιστορίας (Α' Τετράμηνο): "))
        history[1] = int(input("Βαθμός Ιστορίας (Β' Τετράμηνο): "))
        history[2] = int(input("Βαθμός Ιστορίας (Γραπτό εξετάσεων): "))

    elif study_field == "δ":
        math_field = [0, 0, 0]
        math_field[0] = int(input("\nΒαθμός Μαθηματικών (Α' Τετράμηνο) (Προσανατολισμού): "))
        math_field[1] = int(input("Βαθμός Μαθηματικών (Β' Τετράμηνο) (Προσανατολισμού): "))
        math_field[2] = int(input("Βαθμός Μαθηματικών (Γραπτό εξετάσεων) (Προσανατολισμού): "))

        average_math_field = (((math_field[0] + math_field[1]) / 2)  + math_field[2]) / 2

        cs_field = [0, 0, 0]
        cs_field[0] = int(input("\nΒαθμός Πληροφορικής (Α' Τετράμηνο) (Προσανατολισμού): "))
        cs_field[1] = int(input("Βαθμός Πληροφορικής (Β' Τετράμηνο) (Προσανατολισμού): "))
        cs_field[2] = int(input("Βαθμός Πληροφορικής (Γραπτό εξετάσεων) (Προσανατολισμού): "))

        average_cs_field = (((cs_field[0] + cs_field[1]) / 2)  + cs_field[2]) / 2

        economics_field = [0, 0, 0]
        economics_field[0] = int(input("\nΒαθμός Αρχών Οικονομικής Θεωρίας (Α' Τετράμηνο) (Προσανατολισμού): "))
        economics_field[1] = int(input("Βαθμός Αρχών Οικονομικής Θεωρίας (Β' Τετράμηνο) (Προσανατολισμού): "))
        economics_field[2] = int(input("Βαθμός Αρχών Οικονομικής Θεωρίας (Γραπτό εξετάσεων) (Προσανατολισμού): "))

        average_economics_field = (((economics_field[0] + economics_field[1]) / 2)  + economics_field[2]) / 2

        average_cs_economics = (average_math_field + average_cs_field + average_economics_field) / 3

        history = [0, 0, 0]
        history[0] = int(input("\nΒαθμός Ιστορίας (Α' Τετράμηνο): "))
        history[1] = int(input("Βαθμός Ιστορίας (Β' Τετράμηνο): "))
        history[2] = int(input("Βαθμός Ιστορίας (Γραπτό εξετάσεων): "))

        average_history = (((history[0] + history[1]) / 2)  + history[2]) / 2

    else:
        print("Σφάλμα. Επιλέξτε α, β, γ ή δ")
        twelfth_grade()

    religious_studies = [0, 0]
    religious_studies[0] = int(input("\nΒαθμός Θρησκευτικών (Α' Τετραμήνου): "))
    religious_studies[1] = int(input("Βαθμός Θρησκευτικών (Β' Τετραμήνου): "))

    average_religious_studies = (religious_studies[0] + religious_studies[1]) / 2

    english = [0, 0]
    english[0] = int(input("\nΒαθμός Αγγλικής Γλώσσας (Α' Τετραμήνου): "))
    english[1] = int(input("Βαθμός Αγγλικής Γλώσσας (Β' Τετραμήνου): "))

    average_english = (english[0] + english[1]) / 2

    pe = [0, 0]
    pe[0] = int(input("\nΒαθμός Φυσικής Αγωγής (Α' Τετραμήνου): "))
    pe[1] = int(input("Βαθμός Φυσικής Αγωγής (Β' Τετραμήνου): "))

    average_pe = (pe[0] + pe[1]) / 2

    if study_field == "α":
        average = (average_modern_greek + average_humanities + average_math + average_religious_studies + average_english + average_pe) / 6
        print(f"Γενικός Μέσος Όρος: {average}\n\n")
        print(f"Μέσος Όρος Νεοελληνικής Γλώσσας και Λογοτεχνίας: {average_modern_greek}")
        print(f"Μέσος Όρος Ανθρωπιστικών Σπουδών: {average_humanities}")
        print(f"Μέσος Όρος Μαθηματικών: {average_math}")
        print(f"Μέσος Όρος Θρησκευτικών: {average_religious_studies}")
        print(f"Μέσος Όρος Αγγλικής Γλώσσας: {average_english}")
        print(f"Μέσος Όρος Φυσικής Αγωγής: {average_pe}")

    if study_field == "β":
        average = (average_modern_greek + average_history + average_religious_studies + average_english + average_pe + average_positive_sciences) / 6
        print(f"Γενικός Μέσος Όρος: {average}\n\n")
        print(f"Μέσος Όρος Νεοελληνικής Γλώσσας και Λογοτεχνίας: {average_modern_greek}")
        print(f"Μέσος Όρος Φυσικών Επιστημών: {average_positive_sciences}")
        print(f"Μέσος Όρος Ιστορίας: {average_history}")
        print(f"Μέσος Όρος Θρησκευτικών: {average_religious_studies}")
        print(f"Μέσος Όρος Αγγλικής Γλώσσας: {average_english}")
        print(f"Μέσος Όρος Φυσικής Αγωγής: {average_pe}")

    if study_field == "γ":
        average = (average_modern_greek + average_health_sciences + average_history + average_religious_studies + average_english + average_pe) / 6
        print(f"Γενικός Μέσος Όρος: {average}\n\n")
        print(f"Μέσος Όρος Νεοελληνικής Γλώσσας και Λογοτεχνίας: {average_modern_greek}")
        print(f"Μέσος Όρος Επιστημών Υγείας: {average_health_sciences}")
        print(f"Μέσος Όρος Ιστορίας: {average_history}")
        print(f"Μέσος Όρος Θρησκευτικών: {average_religious_studies}")
        print(f"Μέσος Όρος Αγγλικής Γλώσσας: {average_english}")
        print(f"Μέσος Όρος Φυσικής Αγωγής: {average_pe}")

    if study_field == "δ":
        average = (average_modern_greek + average_cs_economics + average_history + average_religious_studies + average_english + average_pe) / 6
        print(f"Γενικός Μέσος Όρος: {average}\n\n")
        print(f"Μέσος Όρος Νεοελληνικής Γλώσσας και Λογοτεχνίας: {average_modern_greek}")
        print(f"Μέσος Όρος Οικονομίας και Πληροφορικής: {average_cs_economics}")
        print(f"Μέσος Όρος Ιστορίας: {average_history}")
        print(f"Μέσος Όρος Θρησκευτικών: {average_religious_studies}")
        print(f"Μέσος Όρος Αγγλικής Γλώσσας: {average_english}")
        print(f"Μέσος Όρος Φυσικής Αγωγής: {average_pe}")

if grade == "α":
    tenth_grade()
elif grade == "β":
    eleventh_grade()
elif grade == "γ":
    twelfth_grade()
else:
    print("Σφάλμα. Επιλέξτε α, β, ή γ.")