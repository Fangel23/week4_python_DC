full_name = input("Please enter your full name: ")
full_name = (f"<h1> {full_name} </h1>")

DOB = input("Enter your date of birth (dd/mm/yyyy): ")
DOB = (f"<h3> {DOB} <h3>")

POB = input("Enter the city and country you were born in: ")
POB = (f"<h4> {POB} </h4>")

about_Me = input(f"Please enter 3 sentences about yourself one unique thing: \n My name is {full_name} and I was born in {POB} ")
about_Me = (f"<body>\n {about_Me} \n</body>")

workplace = input ("Please enter your last place of employment: ")

how_Long = input("Please enter for how long you worked at this place (in years): ")

prev_Pos = input ("Please enter the title of the previous position you held: ")

work_Info = (f"<div>\n I worked at {workplace} for {how_Long} years and held the position of {prev_Pos}  \n</div>")

print(work_Info)



