print("Επιλέξτε τάξη:\nα) Α' Λυκείου\nβ) Β' Λυκείου\nγ) Γ' Λυκείου\n")
grade = input("Επιλογή (α, β ή γ): ")

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

    if study_field == "β":
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
        print(f"Μέσος Όρος Νεοελληνικής Γλώσσας και Λογοτεχνίας: {average_modern_greek}")
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
        print(f"Μέσος Όρος Νεοελληνικής Γλώσσας και Λογοτεχνίας: {average_modern_greek}")
        print(f"Μέσος Όρος Ιστορίας: {average_history}")
        print(f"Μέσος Όρος Μαθηματικών: {average_math}")
        print(f"Μέσος Όρος Φυσικών Επιστημών: {average_sciences}")
        print(f"Μέσος Όρος Αγγλικής Γλώσσας: {average_english}")
        print(f"Μέσος Όρος Φιλοσοφίας: {average_philosophy}")
        print(f"Μέσος Όρος Θρησκευτικών: {average_religious_studies}")
        print(f"Μέσος Όρος Δεύτερης Ξένης Γλώσσας: {average_second_foreign_language}")
        print(f"Μέσος Όρος Φυσικής Αγωγής: {average_pe}")
        print(f"Μέσος Όρος Θετικών Σπουδών: {average_positive_sciences}")

if grade == "β":
    eleventh_grade()
