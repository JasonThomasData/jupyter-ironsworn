This is a journal system that will track state for Ironsworn. This allows you to update the character, journey, enemies, bonds, and vows in the flow of the journal. I did this because I often got confused about whether I had updated my health, supply, momentum and spirit after a move. With this event-driven method, you can run your journal's steps again to update the game state.

I enjoy using printed assets, dice, rulebook etc, so this journal doesn't do those things. It's just a way to update the game state with events.

### Installation

This project uses a Jupyter Notebook, which is modified to appear as an Ironsworn journal.

To run these steps, I install a virtualenv. I run a Debian machine but I suppose it should work wherever you can use Bash.

	virtualenv venv
	source venv/bin/activate
	pip install -r requirements.txt
	
### Usage

	jupyter notebook

To write text, create a new cell and use the markdown editing option.

To run the steps to update the game, choose a code cell.

Each function updates the game state and then prints the state for the player to see

There are these functions defined for player's use:

- health(update)
	update player health with update value, positive or negative
- supply
	update player supply with update value, positive or negative
- spirit
	update player spirit with update value, positive or negative
- momentum
	update player momentum with update value, positive or negative
- printStatus
	display the player status
- newEnemy(name, rank)
	creates a new enemy, of chosen rank
- newJourney(name, rank)
	creates a new journey, of chosen rank
- newBond()
	creates a new bond. This just adds a tick to your bond track 
- newVow(name, rank)
	creates a new journey, of chosen rank
- progressEnemy(name)
	adds one progress, ticks according to the enemy rank
- progressJourney(name)
	adds one progress, ticks according to the journey rank
- progressVow(name)
	adds one progress, ticks according to the vow rank
- enemyInflictsHarm(name)
	does player damage, according to the enemy rank	

### LICENCE

The standard MIT licence applies.

