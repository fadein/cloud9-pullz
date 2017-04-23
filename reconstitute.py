import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pullz-project.settings")

import django
django.setup()
from muck.models import Person, IDTyp, IDNum, Skill, ContactTyp, Contact

IDTyp.objects.get_or_create(abbr="DL", desc="Drivers License")
IDTyp.objects.get_or_create(abbr="SSN", desc="Social Security Number")
IDTyp.objects.get_or_create(abbr="FBI", desc="FBI Number")
IDTyp.objects.get_or_create(abbr="SCH", desc="School ID Card")
IDTyp.objects.get_or_create(abbr="FSH", desc="Fishing License")

ContactTyp.objects.get_or_create(abbr="email", desc="Email Address")
ContactTyp.objects.get_or_create(abbr="landl", desc="Landline Phone Number")
ContactTyp.objects.get_or_create(abbr="cell", desc="Cellular Phone Number")
ContactTyp.objects.get_or_create(abbr="skype", desc="Skype ID")
ContactTyp.objects.get_or_create(abbr="faceb", desc="Facebook Username")
ContactTyp.objects.get_or_create(abbr="linkd", desc="LinkedIn Username")
ContactTyp.objects.get_or_create(abbr="AOL", desc="AOL Username")
ContactTyp.objects.get_or_create(abbr="ICQ", desc="ICQ Number")
ContactTyp.objects.get_or_create(abbr="CB", desc="CB Handle")



Person.objects.get_or_create(first="Erik", middle="W", last="Falor", dob="1980-04-12")
Person.objects.get_or_create(first="Garth", middle="L", last="Falor", dob="2011-10-16")
Person.objects.get_or_create(first="Matilda", middle="C", last="Falor", dob="1985-04-23")
Person.objects.get_or_create(first="Tyrone", middle="E", last="Falor", dob="2005-02-25")
Person.objects.get_or_create(first="Hannah", middle="M", last="Falor", dob="2007-04-02")

IDNum.objects.get_or_create(person=Person.objects.get(first="Erik"), idtype=IDTyp.objects.get(abbr="DL"), number="UT123456", issued="2005-04-12")
IDNum.objects.get_or_create(person=Person.objects.get(first="Erik"), idtype=IDTyp.objects.get(abbr="SSN"), number="123-45-7890", issued="1980-04-01")
IDNum.objects.get_or_create(person=Person.objects.get(first="Matilda"), idtype=IDTyp.objects.get(abbr="DL"), number="UT987654", issued="2013-02-23")
IDNum.objects.get_or_create(person=Person.objects.get(first="Matilda"), idtype=IDTyp.objects.get(abbr="SSN"), number="801-66-7777", issued="1985-04-28")
IDNum.objects.get_or_create(person=Person.objects.get(first="Tyrone"), idtype=IDTyp.objects.get(abbr="SSN"), number="649-66-7777", issued="2004-02-28")
IDNum.objects.get_or_create(person=Person.objects.get(first="Hannah"), idtype=IDTyp.objects.get(abbr="SSN"), number="689-88-9999", issued="2007-04-07")
IDNum.objects.get_or_create(person=Person.objects.get(first="Garth"), idtype=IDTyp.objects.get(abbr="SSN"), number="668-33-9999", issued="2011-10-27")

Contact.objects.get_or_create(person=Person.objects.get(first="Erik"), contyp=ContactTyp.objects.get(abbr="email"), detail="ewfalor@gmail.com")
Contact.objects.get_or_create(person=Person.objects.get(first="Erik"), contyp=ContactTyp.objects.get(abbr="skype"), detail="thatdude")
Contact.objects.get_or_create(person=Person.objects.get(first="Erik"), contyp=ContactTyp.objects.get(abbr="cell"), detail="(435) 867-5309")
Contact.objects.get_or_create(person=Person.objects.get(first="Erik"), contyp=ContactTyp.objects.get(abbr="AOL"), detail="Darth_Grunge")
Contact.objects.get_or_create(person=Person.objects.get(first="Erik"), contyp=ContactTyp.objects.get(abbr="CB"), detail="Peter Pan's Shadow")
Contact.objects.get_or_create(person=Person.objects.get(first="Erik"), contyp=ContactTyp.objects.get(abbr="ICQ"), detail="22-909-909")



Contact.objects.get_or_create(person=Person.objects.get(first="Matilda"), contyp=ContactTyp.objects.get(abbr="email"), detail="mcfalor@gmail.com")
Contact.objects.get_or_create(person=Person.objects.get(first="Matilda"), contyp=ContactTyp.objects.get(abbr="skype"), detail="thatchick")
Contact.objects.get_or_create(person=Person.objects.get(first="Matilda"), contyp=ContactTyp.objects.get(abbr="cell"), detail="(435) 867-5999")
Contact.objects.get_or_create(person=Person.objects.get(first="Matilda"), contyp=ContactTyp.objects.get(abbr="AOL"), detail="Padme Amidala")
Contact.objects.get_or_create(person=Person.objects.get(first="Matilda"), contyp=ContactTyp.objects.get(abbr="CB"), detail="Wendy")
Contact.objects.get_or_create(person=Person.objects.get(first="Matilda"), contyp=ContactTyp.objects.get(abbr="ICQ"), detail="36-365-365")


Contact.objects.get_or_create(person=Person.objects.get(first="Tyrone"), contyp=ContactTyp.objects.get(abbr="email"), detail="chicken_nuggets@gmail.com")
Contact.objects.get_or_create(person=Person.objects.get(first="Tyrone"), contyp=ContactTyp.objects.get(abbr="skype"), detail="chicken_nuggets")
Contact.objects.get_or_create(person=Person.objects.get(first="Tyrone"), contyp=ContactTyp.objects.get(abbr="landl"), detail="(435) 532-4310")

Skill.objects.get_or_create(person=Person.objects.get(first="Erik"), desc="Computers")
Skill.objects.get_or_create(person=Person.objects.get(first="Erik"), desc="Wit")
Skill.objects.get_or_create(person=Person.objects.get(first="Erik"), desc="Wearing Shirts")
Skill.objects.get_or_create(person=Person.objects.get(first="Erik"), desc="Chess")
Skill.objects.get_or_create(person=Person.objects.get(first="Tyrone"), desc="Loading the dishwasher")
Skill.objects.get_or_create(person=Person.objects.get(first="Tyrone"), desc="Sweeping the floor")
Skill.objects.get_or_create(person=Person.objects.get(first="Tyrone"), desc="Shoveling Snow")
Skill.objects.get_or_create(person=Person.objects.get(first="Tyrone"), desc="Cave Story")
Skill.objects.get_or_create(person=Person.objects.get(first="Tyrone"), desc="Minecraft")
Skill.objects.get_or_create(person=Person.objects.get(first="Tyrone"), desc="Chess")
