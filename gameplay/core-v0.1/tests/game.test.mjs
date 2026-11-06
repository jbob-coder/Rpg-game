import test from 'node:test';
import assert from 'node:assert/strict';
import {createGame,dispatch,getViewModel,saveGame,loadGame} from '../src/game.mjs';

const artisan=()=>createGame({name:'A',classId:'guardian',backgroundId:'artisan',seed:17});
const highborn=()=>createGame({name:'B',classId:'scribe',backgroundId:'noble_heir',seed:17});
const next=(g,type)=>dispatch(g,{type});
const days=(g,count)=>{for(let i=0;i<count;i++)g=next(g,'wait');return g;};

test('creación: clase/background son requeridos y modifican stats, rareza y comienzo',()=>{
  assert.throws(()=>createGame({name:'x',classId:'unknown',backgroundId:'artisan'}),/Clase/);
  assert.throws(()=>createGame({name:'x',classId:'guardian',backgroundId:'unknown'}),/Background/);
  const a=artisan(), b=highborn();
  assert.equal(a.character.stats.endurance,7);
  assert.equal(b.character.stats.empathy,7);
  assert.equal(b.character.backgroundRarity,'Epic');
  assert.match(getViewModel(a).narrative[0],/taller/);
  assert.match(getViewModel(b).narrative[0],/huéspedes/);
});

test('mundo autónomo: la disputa y los precios cambian sin intervención ni abrir Story',()=>{
  const g=days(artisan(),5);
  assert.equal(g.day,6);
  assert.equal(g.world.marketOutcome,'merchant_lockout');
  assert.equal(g.world.priceIndex,125);
  assert.equal(g.worldLedger.length,3);
  assert.deepEqual(g.processed,['dispute-start','dispute-outcome','market-prices']);
  assert.equal(g.character.history.length,1);
  const view=getViewModel(g);
  assert.equal(view.journal.length,1);
  assert.equal(JSON.stringify(view).includes('merchant_lockout'),false);
  assert.equal(JSON.stringify(view).includes('disputa'),false);
});

test('conocimiento: visita revela consecuencias sin reescribir evento ni historia previa',()=>{
  const before=days(artisan(),5);
  const snapshot=JSON.stringify(before.worldLedger);
  const after=next(before,'visit_market');
  assert.equal(after.knowledge.includes('market_outcome'),true);
  assert.equal(after.knowledge.includes('market_prices'),true);
  assert.equal(after.character.history.length,3);
  assert.equal(JSON.stringify(after.worldLedger),snapshot);
  const twice=next(after,'visit_market');
  assert.equal(twice.character.history.length,3);
  assert.equal(after.character.originFacts[0],'Origen elegido: Familia artesana');
});

test('consecuencias: empatía/negociación permite mediar; fuerza/aguante permite suministrar',()=>{
  let mediator=next(highborn(),'wait');
  mediator=next(mediator,'visit_market');
  assert.equal(getViewModel(mediator).choices.find(c=>c.id==='mediate').enabled,true);
  mediator=next(mediator,'mediate');
  assert.equal(mediator.character.stamina.current,7);
  mediator=days(mediator,4);
  assert.equal(mediator.world.marketOutcome,'agreement');
  assert.equal(mediator.world.priceIndex,100);

  let worker=next(artisan(),'wait');
  worker=next(worker,'visit_market');
  worker=next(worker,'carry_supplies');
  worker=days(worker,4);
  assert.equal(worker.world.marketOutcome,'resupplied');
  assert.equal(worker.character.stamina.current,6);

  let fail=next(artisan(),'wait');
  fail=next(fail,'visit_market');
  fail=next(fail,'mediate');
  assert.equal(fail.world.intervention,null);
  assert.equal(fail.world.merchantTrust,-1);
  assert.throws(()=>next(fail,'mediate'),/no está disponible/);
});

test('bloqueos se validan en dominio, sin mutar estado ante comandos rechazados',()=>{
  const base=artisan(), copy=saveGame(base);
  assert.throws(()=>next(base,'mediate'),/no está disponible/);
  assert.throws(()=>next(base,'unknown'),/desconocida/);
  assert.equal(saveGame(base),copy);
  let g=next(base,'wait');
  g=next(g,'visit_market');
  g=days(g,2);
  assert.throws(()=>next(g,'carry_supplies'),/no puedes/i);
});

test('guardado/carga, idempotencia, determinismo y protección contra versión incompatible',()=>{
  let g=days(artisan(),2);
  const restored=loadGame(saveGame(g));
  assert.deepEqual(restored,g);
  const a=days(g,3),b=days(restored,3);
  assert.deepEqual(a,b);
  assert.equal(a.worldLedger.length,3);
  assert.equal(new Set(a.processed).size,3);
  const bad={...a,version:999};
  assert.throws(()=>loadGame(JSON.stringify(bad)),/incompatible/);
});

test('narración no tiene conocimiento omnisciente; visitar cambia lo que sabe, no lo ocurrido',()=>{
  const hidden=next(artisan(),'wait');
  const hiddenView=getViewModel(hidden);
  assert.equal(JSON.stringify(hiddenView).includes('cargadores'),false);
  const observed=next(hidden,'visit_market');
  assert.match(getViewModel(observed).narrative.join(' '),/cargadores/);
  assert.equal(hidden.world.marketStatus,observed.world.marketStatus);
});
