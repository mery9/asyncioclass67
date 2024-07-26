import aiofiles
import asyncio
import json
from pathlib import Path

pokemonapi_directory = './assignment07/pokemon/pokemonapi'
pokemonmove_directory = './assignment07/pokemon/pokemonmove'

async def pokemon_file(file_path):
    # Read the contents of the json file.
    async with aiofiles.open(file_path, mode='r') as f:
        contents = await f.read()
    
    # Load it into a dictionary and create a list of moves.
    pokemon = json.loads(contents)
    name = pokemon['name']
    moves = [move['move']['name'] for move in pokemon['moves']]
    
    async with aiofiles.open(f'{pokemonmove_directory}/{name}_moves.txt', mode='w') as f:
        await f.write('\n'.join(moves))

async def main():
    tasks = []
    pathlist = Path(pokemonapi_directory).glob('*.json')
    
    for path in pathlist:
        task = asyncio.create_task(pokemon_file(path))
        tasks.append(task)
    
    await asyncio.gather(*tasks)

asyncio.run(main())