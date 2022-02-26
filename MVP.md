# Minimum Viable Product (MVP) - iHungy  
Borrowed from CS 196 :)

### What problem is your project trying to solve?  
1. A lot of food sits in your fridge and ends up expiring and going to waste because it is unused.
2. Often people want to try new dishes or make something that they are in the mood for, but don't know what to make.

### Describe your MVP:  
An app that allows users to track the items in their fridge. They can update items, see if items are old, and more.  
There is also meal selection feature that allows users to search for meals to make based on their criteria, or make their own meal. This will automatically update the contents of their fridge.

### What features make up your MVP?  
- Fridge Tracker
    - Enter items in fridge, keep track of when they were entered
    - Update items upon shopping trip, etc.
- Meal Selection
    - Search for meals based on criteria
        - Course (breakfast, lunch, dinner, snack, dessert)
        - Flavor profile
        - Cold/hot
        - Ingredient Preferences
        - Meal prep time/difficulty
    - Rank based on custom ranking
- Make the selected meal
    - Choose portions to make
    - Provide user with ingredient list, recipe instructions
    - Update Fridge after meal is made

### What are the features discussed, but not in the MVP?  
- Meal Selection
    - Ingredient Preferences: Suggest older/unused ingredients and prioritize them
    - Criteria: Texture criteria
    - Review system for meals, factor into ranking system
    - Custom meal/recipe
- Fridge Tracker
    - See old/unused items
    - Alert user of expired/expiring items

### Which does the tech stack look like and why did you choose these over alternatives?  
Flask - Python familiarity  
Vue/Vuetify - Relatively easy to pick up on  
Heroku - Familiarity  
Heroku Postgre - Free, works with heroku for deployment