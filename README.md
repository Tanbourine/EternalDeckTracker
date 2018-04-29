# EternalDeckTracker
Tracks what cards you have left


## Card.py
This will take the csv data that is imported from the game and correlate it to
the json database to obtain the card's metadata. It will then create a card
object with the data.

## Deck.py
This will take the card object and sort it in various ways


## TODO
- [x] probability colors
- [x] custom display column displaying the cost or influence
- [x] make probability a label instead of button
- [ ] file menu to change sort method
- [x] reset button
- [ ] change font size


#### Main GUI Layout

```
|----------------------------|
|                            |
|                            |
|           units            |
|                            |
|                            |
|----------------------------|
|                            |
|                            |
|           spells           |
|                            |
|                            |
|----------------------------|
|                            |
|                            |
|           power            |
|                            |
|                            |
|----------------------------|

```
