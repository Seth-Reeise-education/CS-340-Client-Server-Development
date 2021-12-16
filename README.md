# CS-340-Client-Server-Development

# How do you write programs that are maintainable, readable, and adaptable? Especially consider your work on the CRUD Python module from Project One, which you used to connect the dashboard widgets to the database in Project Two. What were the advantages of working in this way? How else could you use this CRUD Python module in the future?
To write programs that are maintainable, readable, and adaptable, you must write them in a modularized way. The benefits of an writing an API is 
reusability which is what the CRUD Python module is for. The module is set up to adaptive to different database collections. Therefore I could use
this module to work with an entirely different data set and change very little. To make this module more reusable, I can instead set it up where 
the database collection is also passed in as an argument so that the module will not need to be changed for each collection. I can also expand on
this module to provide more functionality such as deleting an entire collection. 

# How do you approach a problem as a computer scientist? Consider how you approached the database or dashboard requirements that Grazioso Salvare requested. How did your approach to this project differ from previous assignments in other courses? What techniques or strategies would you use in the future to create databases to meet other client requests?
From what I’ve found, the best way to approach a problem as a computer scientist is to break it up into smaller problems. Take for example, the 
CRUD module, each part of the acronym I broke down, developed, and put together to achieve the final result. I developed the dashboard in much of 
the same way. For example, the need to filter data, first thing to figure out is what will perform the filtering? Buttons? A dropdown? Lets decide
on buttons, so first I create the buttons, ensure they display and make sure function correctly. Next is, what do I need to filter? So I gather the 
requirements for what data needs to be shown, then I build the queries and lastly I test them out. The final step of the problem is merging the 
queries together with the buttons so that they function seamlessly. The filtering problem was broken up into smaller problems to make it more 
manageable. In the end, you come out with a result that is also maintainable, readable, and adaptable. 

# What do computer scientists do, and why does it matter? How would your work on this type of project help a company, like Grazioso Salvare, to do their work better?
Computer scientists solve problems. Typically these problems are solved with computer programming to automate or perform repetitive tasks. My work
on this project would help the company by letting them focus their work on what’s important. Normal operations for a company in this business would 
be an employee looking at the data one by one, writing down which animals are between a certain age and categorizing by breed etc.., or even 
better, using an excel sheet and filtering each column until they find what they need. With my dashboard I created, the company can save a massive
amount of time by clicking one button or selecting one option from the drop down and getting all they data they need at once automatically filtered 
to their liking. In addition to showing their data in a table view, I also added additional features such as the geo location map that updates 
every time they change their filter, allowing them to get an understanding of the area around the animals location and seeing just how close other 
animals are to each other. 
