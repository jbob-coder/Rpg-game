/** Simple terminal demonstrator. No dependencies, no persistence/Android UI. */
import {createInterface} from 'node:readline/promises';
import {stdin,stdout} from 'node:process';
import {createGame,dispatch,getViewModel,DEMO_CATALOG} from '../src/game.mjs';

const rl=createInterface({input:stdin,output:stdout});
let game=createGame({name:'Viajero',classId:'guardian',backgroundId:'artisan'});
console.log('RPG de texto — demostración de lógica (nombres y números no canon)');
console.log('Clases de ejemplo:',DEMO_CATALOG.classes);
console.log('Trasfondos de ejemplo:',DEMO_CATALOG.backgrounds);
try {
  for (;;) {
    const view=getViewModel(game);
    console.log(`\nDÍA ${view.day} · ${view.character.name} · ${view.character.classLabel}`);
    console.log(`FUE ${view.character.stats.strength} · EMP ${view.character.stats.empathy} · STA ${view.character.stamina.current}/${view.character.stamina.max}`);
    console.log('\n'+view.narrative.join('\n\n'));
    const options=view.choices.filter(c=>c.enabled);
    options.forEach((choice,index)=>console.log(`${index+1}. ${choice.label}`));
    console.log('0. Salir');
    const input=await rl.question('Acción: ');
    if(input.trim()==='0')break;
    const choice=options[Number(input)-1];
    if(!choice){console.log('Selección inválida.');continue;}
    try {game=dispatch(game,{type:choice.id});}
    catch(error){console.log('Acción rechazada:',error.message);}
  }
} finally {rl.close();}
