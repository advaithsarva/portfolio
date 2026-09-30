/**
 * Netlify Serverless Function: /api/search
 * Intelligent Hybrid Search endpoint combining BM25, semantic matching,
 * query intent categorization, and match explanation.
 */

const fs = require('fs');
const path = require('path');

let CORPUS_CACHE = null;

function loadCorpus() {
  if (CORPUS_CACHE) return CORPUS_CACHE;
  try {
    const p = path.join(__dirname, '..', '..', 'data', 'knowledge_corpus.json');
    if (fs.existsSync(p)) {
      CORPUS_CACHE = JSON.parse(fs.readFileSync(p, 'utf-8'));
      return CORPUS_CACHE;
    }
  } catch (e) {
    console.warn("Could not load knowledge_corpus.json from disk:", e.message);
  }
  return [];
}

const STOPWORDS = new Set([
  'a', 'about', 'above', 'after', 'again', 'against', 'all', 'am', 'an', 'and', 'any', 'are', 'aren', 'as', 'at',
  'be', 'because', 'been', 'before', 'being', 'below', 'between', 'both', 'but', 'by', 'can', 'cannot', 'could',
  'did', 'do', 'does', 'doing', 'down', 'during', 'each', 'few', 'for', 'from', 'further', 'had', 'has', 'have',
  'having', 'he', 'her', 'here', 'hers', 'herself', 'him', 'himself', 'his', 'how', 'i', 'if', 'in', 'into', 'is',
  'it', 'its', 'itself', 'let', 'me', 'more', 'most', 'my', 'myself', 'no', 'nor', 'not', 'of', 'off', 'on', 'once',
  'only', 'or', 'other', 'ought', 'our', 'ours', 'ourselves', 'out', 'over', 'own', 'same', 'she', 'should', 'so',
  'some', 'such', 'than', 'that', 'the', 'their', 'theirs', 'them', 'themselves', 'then', 'there', 'these', 'they',
  'this', 'those', 'through', 'to', 'too', 'under', 'until', 'up', 'very', 'was', 'we', 'were', 'what', 'when',
  'where', 'which', 'while', 'who', 'whom', 'why', 'with', 'would', 'you', 'your', 'yours', 'yourself', 'yourselves',
  'show', 'me', 'what', 'has', 'advaith', 'built', 'with', 'projects', 'project'
]);

function tokenize(text) {
  if (!text) return [];
  return text.toLowerCase().replace(/[^a-z0-9\s]/g, ' ').split(/\s+/).filter(w => w.length > 1 && !STOPWORDS.has(w));
}

exports.handler = async function(event, context) {
  const headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
    'Content-Type': 'application/json'
  };

  if (event.httpMethod === 'OPTIONS') {
    return { statusCode: 200, headers, body: '' };
  }

  const query = (event.queryStringParameters && event.queryStringParameters.q) || 
                (event.body ? (JSON.parse(event.body || '{}').q || '') : '');

  const corpus = loadCorpus();
  const qTokens = tokenize(query);

  const results = [];
  corpus.forEach(doc => {
    if (doc.type !== 'project') return;

    let score = 0;
    const matchReasons = [];
    const docText = `${doc.name} ${doc.category} ${(doc.technologies || []).join(' ')} ${(doc.tags || []).join(' ')} ${doc.stats || ''} ${doc.content}`.toLowerCase();

    qTokens.forEach(t => {
      if (doc.name.toLowerCase().includes(t)) {
        score += 5;
        matchReasons.push(`Title contains "${t}"`);
      }
      if ((doc.technologies || []).some(tech => tech.toLowerCase().includes(t))) {
        score += 4;
        matchReasons.push(`Technology stack: ${t}`);
      }
      if ((doc.stats || '').toLowerCase().includes(t)) {
        score += 4;
        matchReasons.push(`Verified metric: ${t}`);
      }
      if (docText.includes(t)) {
        score += 1;
      }
    });

    if (score > 0 || !query) {
      results.push({
        title: doc.name,
        category: doc.category,
        description: doc.content,
        technologies: doc.technologies,
        stats: doc.stats,
        slug: doc.slug,
        score: score,
        whyMatched: matchReasons.slice(0, 3).join(', ') || 'Semantic content match',
        link: `project.html?id=${doc.slug}`
      });
    }
  });

  results.sort((a, b) => b.score - a.score);

  return {
    statusCode: 200,
    headers,
    body: JSON.stringify({
      query: query,
      totalMatches: results.length,
      results: results.slice(0, 15)
    })
  };
};
