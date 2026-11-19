import { describe, expect, it } from 'vitest'
import { AiError, parseAiResponse, sanitizeQuestion, validateQuestion } from '../services/aiClient'

describe('aiClient validation', () => {
  it('sanitizes control characters', () => expect(sanitizeQuestion('a\u0000b\n\n c')).toBe('ab c'))
  it('rejects too short and too long input', () => {
    expect(() => validateQuestion('hi')).toThrow(AiError)
    expect(() => validateQuestion('x'.repeat(1001))).toThrow(AiError)
  })
  it('accepts a normal question', () => expect(validateQuestion('  What is bail?  ')).toBe('What is bail?'))
})

describe('parseAiResponse', () => {
  it('parses a complete answer and drops bad citations', () => {
    const a = parseAiResponse({
      shortAnswer: 'Short',
      nextSteps: ['one', 2, ''],
      citations: [
        { title: 'Ok', url: 'https://example.gov.pk/a' },
        { title: 'Bad', url: 'javascript:alert(1)' },
        { title: 'NoUrl' },
      ],
    })
    expect(a.shortAnswer).toBe('Short')
    expect(a.nextSteps).toEqual(['one'])
    expect(a.citations).toHaveLength(1)
  })
  it('accepts wrapped {answer:{}} shape', () => expect(parseAiResponse({ answer: { shortAnswer: 'x' } }).shortAnswer).toBe('x'))
  it('rejects malformed payloads', () => {
    expect(() => parseAiResponse(null)).toThrow(AiError)
    expect(() => parseAiResponse({ foo: 1 })).toThrow(AiError)
  })
  it('allows insufficient-evidence answers', () => expect(parseAiResponse({ insufficientEvidence: true }).insufficientEvidence).toBe(true))
})
