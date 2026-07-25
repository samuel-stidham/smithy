---
name: evaluate
description: Evaluate a library, tool, or approach against stated criteria, with cited research and an optional spike. Ends in one recommendation.
argument-hint: "[library, tool, or approach, plus the decision criteria]"
disable-model-invocation: true
---

# /forge:evaluate

Answer one engineering decision with evidence and end with one
recommendation. Never a survey of options with the choice left to
the reader.

The question is: $ARGUMENTS

If `$ARGUMENTS` is empty, ask what decision needs making.

## Workflow

1. **Pin the decision.** The question, the candidates, and the
   criteria. Take criteria from the owner when given. Otherwise
   propose them, state them, and proceed.
2. **Weigh the repo.** The existing stack, read from its manifests,
   is a criterion by default. The winner on paper can lose to the
   option the codebase already speaks.
3. **Research.** Docs, changelogs, maintenance signals, license,
   and security history, through the `web-browsing` skill. Claims
   follow the `citations` skill. Nothing gets recommended on model
   memory alone.
4. **Spike when paper is not enough.** Throwaway code in a scratch
   directory answers what reading cannot: real API feel, real
   performance, real integration friction. Spike code never lands
   in the repo.
5. **Recommend.** One recommendation, the reasoning, and each
   runner-up with the reason it lost. State what evidence would
   change the answer. Do not soften the recommendation to be
   agreeable.

## Boundaries

Read-mostly. The spike stays in scratch space. Adopting the
recommendation is `/forge:do-work`.
