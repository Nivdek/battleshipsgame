# Battleships

Battleships is a Python terminal game, which runs in the Code Institute mock terminal on Heroku.



---

## Features

-__Game Window__-

- The Game Window is instantly apparent upon entering the site
- The text prompting you to make a choice immediately let's you start playing without having to sign up or enter any details
![Game Window](/assets/images/rps-readme2.png)
  
-__Gameplay Buttons__-

- The games buttons have good visibility and are of a user-friendly size regardless of screen size
- Clicking a button provides an immediate visual respone depending on what hand you've chosen to play
![Buttons](/assets/images/rps-readme3.png)

-__Score System__-

- A working score system that has been color-coded for user-experience
![Score](/assets/images/rps-readme4.png)

## Planned Features

-__Difficulty Levels__-

- Atleast one new difficulty is planned, where the computer is mathematically more likely to beat you
  
-__Additional Hands__-

- Additional playable hands like "Spock" and "Lizard" are planned to add more interactivity to the game

-__Leaderboards__-

- Leaderboards for score where a user can enter a name and upload their score to a leaderboard

## Testing

- The site has been tested on all different standardized screens and sizes, it has gone through thorough testing of it's interactive components such as buttons, score system.
  
### Validator Testing

- HTML
  - No errors where returned when running the official [W3C validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Fcode-institute-org.github.io%2Flove-running-2.0%2Findex.html)

- CSS
  - No errors where returned when running the official [(Jigsaw) validator](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fvalidator.w3.org%2Fnu%2F%3Fdoc%3Dhttps%253A%252F%252Fcode-institute-org.github.io%252Flove-running-2.0%252Findex.html&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en#css)

- JSHint
  - Passes through [JSHint](https://jshint.com/) only returning warnings that some code runs in ES6, which can be disregarded.

### Lighthouse

- The site has been run through the Lighthouse available in the Chrome Developer Tools and came back with a good score.  
![Lighthouse](/assets/images/lighthouse-rps.png)

### Bugs/Unresolved Issues

- The only possible issues that are left unresolved are the lines of ES6 code that could cause issues for some users.

## Deployment

- The site was deployed to GitHub Pages. The steps to deploy are:
  - In the GitHub repository, go to Settings
  - From the source section, select the Main Branch
  - Once the Main Branch has been selected the page will being deployment.

The live site can be found at: <https://nivdek.github.io/RPS/index.html>

## Credits

- Favicon was made with [Favicon.io](https://favicon.io/)
- Fonts came from [Google Fonts](https://fonts.google.com/)
-  [This Youtube Tutorial](https://www.youtube.com/watch?v=n1_vHArDBRA&ab_channel=BroCode) was a big help in creating the function for determining winner