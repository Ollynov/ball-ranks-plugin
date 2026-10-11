// Node 20+. Discovery is free; --data consumes up to five product requests.
const endpoint = 'https://ballranks.com/api/mcp';
const headers = { 'Content-Type': 'application/json', Accept: 'application/json, text/event-stream' };
if (process.env.BALL_RANKS_API_KEY) headers.Authorization = `Bearer ${process.env.BALL_RANKS_API_KEY}`;
const cases = [
  ['get_season_rankings', { sport: 'football', scoring_format: 'ppr', limit: 10 }],
  ['get_week_rankings', { sport: 'football', week: 4, position: 'WR', scoring_format: 'half_ppr', limit: 10 }],
  ['get_season_rankings', { sport: 'basketball', limit: 5 }],
  ['get_player_rankings', { sport: 'basketball', player: 'victor-wembanyama' }],
  ['get_player_projections', { sport: 'football', player: 'lamar-jackson', scope: 'weekly', week: 4, scoring_format: 'ppr' }],
];
let id = 0;
async function call(method, params) {
  const response = await fetch(endpoint, {
    method: 'POST', headers, signal: AbortSignal.timeout(30000),
    body: JSON.stringify({ jsonrpc: '2.0', id: ++id, method, params }),
  });
  const body = await response.text();
  const payloads = response.headers.get('content-type')?.includes('text/event-stream')
    ? body.split(/\r?\n/).filter(line => line.startsWith('data: ')).map(line => JSON.parse(line.slice(6)))
    : [JSON.parse(body)];
  const payload = payloads.find(value => value.id === id) ?? payloads.find(value => value.error);
  if (!payload) throw new Error(`No JSON-RPC response for ${method}`);
  return { status: response.status, payload };
}
const initialized = await call('initialize', {
  protocolVersion: '2025-06-18', capabilities: {}, clientInfo: { name: 'ball-ranks-review-check', version: '1.0.0' },
});
if (initialized.payload.error) throw new Error(initialized.payload.error.message);
console.log(JSON.stringify({ method: 'initialize', status: initialized.status, result: initialized.payload.result }));
const discovered = await call('tools/list', {});
const tools = discovered.payload.result?.tools;
if (!tools || tools.length !== 4 || new Set(tools.map(tool => tool.name)).size !== 4) throw new Error('Expected four distinct tools');
for (const [name] of cases) {
  const tool = tools.find(value => value.name === name);
  if (!tool?.title || !tool.outputSchema || tool.annotations?.readOnlyHint !== true ||
      tool.annotations?.destructiveHint !== false || tool.annotations?.openWorldHint !== true) {
    throw new Error(`Missing review metadata: ${name}`);
  }
}
console.log(JSON.stringify({ method: 'tools/list', status: discovered.status, tools: tools.map(({ name, title, annotations }) => ({ name, title, annotations })) }));
if (process.argv.includes('--data')) {
  for (const [name, args] of cases) {
    const { status, payload } = await call('tools/call', { name, arguments: args });
    const result = payload.result;
    const content = result?.structuredContent;
    console.log(JSON.stringify({ name, arguments: args, status, error: payload.error,
      isError: result?.isError, content: content ?? result?.content }));
    if (payload.error || result?.isError || !content?.sourceUrl || !content?.meta ||
        !(content.rankings?.length || content.ranking || content.projection)) {
      process.exitCode = 1;
    }
    // A blocked credential/quota applies to the remaining cases; do not retry it.
    if ([401, 403, 429].includes(status)) break;
  }
}
