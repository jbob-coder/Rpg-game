/**
 * Standalone text RPG domain spike v0.1. No UI, map, external dependencies or
 * engine assumptions. Every name, balance number and location is illustrative,
 * NOT approved canon or a promised final character progression system.
 */
export const GAME_VERSION = 1;

const CLASSES = Object.freeze({
  guardian: {label: 'Guardia', stats: {strength: 6, endurance: 6, perception: 4, empathy: 3}},
  scribe: {label: 'Escribiente', stats: {strength: 3, endurance: 4, perception: 6, empathy: 6}}
});
const BACKGROUNDS = Object.freeze({
  artisan: {label: 'Familia artesana', rarity: 'Common', bonuses: {endurance: 1}, coins: 5,
    opening: 'El taller despierta con el golpe regular de un martillo. Fuera, los carros avanzan lentamente hacia el mercado.'},
  noble_heir: {label: 'Heredero noble', rarity: 'Epic', bonuses: {empathy: 1}, coins: 9,
    opening: 'En la casa de huéspedes, una criada deja el desayuno junto a la ventana. En la calle, los comerciantes discuten los retrasos de los carros.'}
});

function assert(condition, message) { if (!condition) throw new Error(message); }
function clone(value) { return JSON.parse(JSON.stringify(value)); }
function uniquePush(array, value) { if (!array.includes(value)) array.push(value); }
function eventId(id) { return `world.${id}`; }

export function createGame({name, classId, backgroundId, seed = 1} = {}) {
  assert(typeof name === 'string' && name.trim().length >= 1 && name.trim().length <= 40, 'Nombre inválido (1–40 caracteres)');
  assert(Object.hasOwn(CLASSES, classId), 'Clase inicial desconocida');
  assert(Object.hasOwn(BACKGROUNDS, backgroundId), 'Background desconocido');
  assert(Number.isSafeInteger(seed) && seed >= 0, 'Semilla inválida');
  const cls = CLASSES[classId], bg = BACKGROUNDS[backgroundId];
  const stats = { ...cls.stats };
  for (const [stat, bonus] of Object.entries(bg.bonuses)) stats[stat] += bonus;
  return {
    version: GAME_VERSION,
    day: 1,
    seed, // Reserved for future content selection; not used as randomness in v0.1.
    character: {
      name: name.trim(), classId, backgroundId, backgroundRarity: bg.rarity,
      originFacts: [`Origen elegido: ${bg.label}`, `Clase inicial: ${cls.label}`],
      stats,
      skills: {negotiation: 1, labor: 1}, // Illustrative proficiency, not class abilities.
      hp: {current: 20, max: 20}, stamina: {current: 10, max: 10},
      coins: bg.coins, locationId: 'lodging',
      history: [{id: 'origin', day: 1, text: `Comienzas con el trasfondo ${bg.label} y la clase ${cls.label}.`}]
    },
    world: {marketStatus: 'normal', marketOutcome: null, priceIndex: 100, merchantTrust: 0,
      intervention: null, mediationAttempted: false, supplyAttempted: false},
    scheduled: [
      {id: 'dispute-start', day: 2, priority: 0},
      {id: 'dispute-outcome', day: 4, priority: 0},
      {id: 'market-prices', day: 6, priority: 0}
    ],
    processed: [],
    worldLedger: [], // World truth, never handed to UI directly.
    knowledge: [] // Player-visible discoveries only.
  };
}

function recordWorld(game, id, text) {
  assert(!game.processed.includes(id), `Evento duplicado: ${id}`);
  game.processed.push(id);
  game.worldLedger.push({id: eventId(id), day: game.day, text});
}
function resolveEvent(game, event) {
  const w = game.world;
  if (game.processed.includes(event.id)) return;
  switch (event.id) {
    case 'dispute-start':
      w.marketStatus = 'disputed';
      recordWorld(game, event.id, 'Un retraso en el suministro provoca un conflicto entre comerciantes y cargadores.');
      return;
    case 'dispute-outcome': {
      assert(w.marketStatus === 'disputed', 'La disputa no está activa');
      const outcome = w.intervention === 'mediation' ? 'agreement'
        : w.intervention === 'supplies' ? 'resupplied' : 'merchant_lockout';
      w.marketOutcome = outcome;
      w.marketStatus = outcome === 'merchant_lockout' ? 'restricted' : 'settled';
      recordWorld(game, event.id, ({agreement:'Las partes llegan a un acuerdo con mediación.',
        resupplied:'Los nuevos suministros permiten que continúe el trabajo.',
        merchant_lockout:'Sin acuerdo, los comerciantes restringen la descarga y continúan las disputas.'})[outcome]);
      return;
    }
    case 'market-prices':
      assert(w.marketOutcome !== null, 'Falta el resultado del conflicto');
      w.priceIndex = w.marketOutcome === 'merchant_lockout' ? 125 : 100;
      recordWorld(game, event.id, w.priceIndex > 100
        ? 'La escasez eleva los precios del mercado.' : 'Los precios se mantienen sin una subida extraordinaria.');
      return;
    default: throw new Error(`Evento no reconocido: ${event.id}`);
  }
}
function advanceDays(game, count) {
  assert(Number.isSafeInteger(count) && count >= 1 && count <= 30, 'Tiempo inválido');
  for (let i = 0; i < count; i++) {
    game.day++;
    const ready = game.scheduled.filter(e => e.day <= game.day && !game.processed.includes(e.id))
      .sort((a,b) => a.day - b.day || a.priority - b.priority || a.id.localeCompare(b.id));
    for (const event of ready) resolveEvent(game, event);
  }
}
function discover(game, id, description) {
  if (game.knowledge.includes(id)) return;
  game.knowledge.push(id);
  game.character.history.push({id:`known.${id}`, day:game.day, text:description});
}
function inspectMarket(game) {
  game.character.locationId = 'market';
  if (game.world.marketOutcome) {
    const messages = {
      agreement:'Los puestos siguen abiertos. Dos delegados anuncian que los cargadores y comerciantes alcanzaron un acuerdo.',
      resupplied:'Llegan carros cargados. Un comerciante reconoce que las entregas evitaron el cierre de los puestos.',
      merchant_lockout:'Varios puestos están cerrados. Una vendedora explica que los comerciantes restringieron las descargas al fracasar las conversaciones.'
    };
    discover(game, 'market_outcome', messages[game.world.marketOutcome]);
  } else if (game.world.marketStatus === 'disputed') {
    discover(game, 'market_dispute', 'En el mercado, los cargadores se niegan a descargar hasta que se resuelvan las tarifas. Los comerciantes discuten junto a los carros detenidos.');
  } else {
    discover(game, 'market_normal', 'Los comerciantes preparan sus mesas. Los carros tardan, pero los puestos permanecen abiertos.');
  }
  if (game.day >= 6) {
    discover(game, 'market_prices', game.world.priceIndex > 100
      ? 'Los precios subieron desde tu última visita; un tendero culpa a la falta de suministros.'
      : 'Los precios se mantienen cercanos a los que recuerdas.');
  }
}
function eligible(game, type) {
  const c = game.character, w = game.world;
  const knowsDispute = game.knowledge.includes('market_dispute');
  if (type === 'mediate') return knowsDispute && w.marketStatus === 'disputed' &&
    !w.intervention && !w.mediationAttempted && c.stamina.current >= 3;
  if (type === 'carry_supplies') return knowsDispute && w.marketStatus === 'disputed' &&
    !w.intervention && !w.supplyAttempted && c.stamina.current >= 4;
  return false;
}

/** Applies a command to a cloned, serializable state. No change on failed commands. */
export function dispatch(state, command) {
  const game = validateState(clone(state));
  assert(command && typeof command.type === 'string', 'Acción inválida');
  const c = game.character, w = game.world;
  switch (command.type) {
    case 'wait': advanceDays(game, 1); break;
    case 'rest':
      advanceDays(game, 1);
      c.stamina.current = Math.min(c.stamina.max, c.stamina.current + 5);
      break;
    case 'visit_market': inspectMarket(game); break;
    case 'mediate': {
      assert(eligible(game, 'mediate'), 'La mediación no está disponible');
      c.stamina.current -= 3;
      w.mediationAttempted = true;
      const score = c.stats.empathy + c.skills.negotiation;
      if (score >= 7) {
        w.intervention = 'mediation';
        w.merchantTrust += 2;
        c.history.push({id:'intervention.mediation',day:game.day,text:'Presentaste una propuesta que ambas partes aceptaron considerar.'});
      } else {
        w.merchantTrust -= 1;
        c.history.push({id:'intervention.mediation_failed',day:game.day,text:'Intentaste mediar, pero ninguna parte cedió.'});
      }
      break;
    }
    case 'carry_supplies': {
      assert(eligible(game, 'carry_supplies'), 'No puedes participar en el reparto ahora');
      c.stamina.current -= 4;
      w.supplyAttempted = true;
      const score = c.stats.strength + c.stats.endurance + c.skills.labor;
      if (score >= 12) {
        w.intervention = 'supplies';
        w.merchantTrust += 1;
        c.history.push({id:'intervention.supplies',day:game.day,text:'Ayudaste a descargar los carros sin que se perdieran más suministros.'});
      } else {
        c.history.push({id:'intervention.supplies_failed',day:game.day,text:'El esfuerzo te superó; los carros siguen esperando.'});
      }
      break;
    }
    default: throw new Error(`Acción desconocida: ${command.type}`);
  }
  return game;
}
function openingFor(game) { return BACKGROUNDS[game.character.backgroundId].opening; }

/** The frontend gets only what the protagonist knows, never the worldLedger. */
export function getViewModel(state) {
  const game = validateState(state), c = game.character;
  const knowing = new Set(game.knowledge);
  const scene = [
    game.day === 1 ? openingFor(game) : `Día ${game.day}. La ciudad conserva su ritmo, aunque no conozcas todas las decisiones tomadas fuera de tu vista.`,
    c.locationId === 'lodging'
      ? 'El sonido de las ruedas llega desde la calle. Hay asuntos que siguen su curso mientras decides qué hacer.'
      : 'Entre las mesas y los carros, la gente habla en voz baja y observa quién escucha.',
  ];
  const journal = c.history.map(e => ({...e}));
  const knownLatest = [...journal].reverse().find(e => e.id.startsWith('known.') || e.id.startsWith('intervention.'));
  if (knownLatest) scene.push(knownLatest.text);
  const choices = [
    {id:'visit_market', label:'Acercarte al mercado',enabled:true},
    {id:'wait', label:'Dejar pasar un día',enabled:true},
    {id:'rest', label:'Descansar un día',enabled:true}
  ];
  if (knowing.has('market_dispute') && game.day < 4) {
    choices.push({id:'mediate',label:'Proponer una mediación',enabled:eligible(game,'mediate'),
      requirements:'Disputa activa; 3 de resistencia. Empatía y negociación influyen en el resultado.'});
    choices.push({id:'carry_supplies',label:'Ayudar a transportar suministros',enabled:eligible(game,'carry_supplies'),
      requirements:'Disputa activa; 4 de resistencia. Fuerza, aguante y trabajo influyen en el resultado.'});
  }
  return {
    day: game.day,
    character: {name:c.name,classId:c.classId, classLabel:CLASSES[c.classId].label,
      backgroundId:c.backgroundId,backgroundLabel:BACKGROUNDS[c.backgroundId].label,
      backgroundRarity:c.backgroundRarity, stats:{...c.stats},skills:{...c.skills},
      hp:{...c.hp},stamina:{...c.stamina},coins:c.coins},
    narrative: scene,
    choices,
    journal,
    // Do not expose market outcome, hidden events, raw world or secret flags here.
  };
}
export function validateState(state) {
  assert(state && typeof state === 'object' && state.version === GAME_VERSION, 'Versión de partida incompatible');
  assert(Number.isSafeInteger(state.day) && state.day >= 1, 'Reloj de juego inválido');
  assert(state.character && Object.hasOwn(CLASSES,state.character.classId), 'Clase corrupta');
  assert(Object.hasOwn(BACKGROUNDS,state.character.backgroundId), 'Origen corrupto');
  for (const key of ['scheduled','processed','worldLedger','knowledge']) assert(Array.isArray(state[key]), `Falta ${key}`);
  assert(state.world && typeof state.world.marketStatus === 'string', 'Mundo inválido');
  assert(state.character.history && Array.isArray(state.character.history), 'Historial inválido');
  assert(new Set(state.processed).size === state.processed.length, 'Eventos procesados duplicados');
  return state;
}
export function saveGame(state) { return JSON.stringify(validateState(state)); }
export function loadGame(json) {
  assert(typeof json === 'string' && json.length < 1_000_000, 'Tamaño de partida inválido');
  return validateState(JSON.parse(json));
}
export const DEMO_CATALOG = Object.freeze({
  classes: Object.fromEntries(Object.entries(CLASSES).map(([id,c])=>[id,c.label])),
  backgrounds: Object.fromEntries(Object.entries(BACKGROUNDS).map(([id,b])=>[id,{label:b.label,rarity:b.rarity}]))
});
