# SearchMatchTestCase

- **Type:** Class
- **File:** [`modules/search/search.test`](_file.md), lines 17–244 · [local source](../../../../source/modules/search/search.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/search.test#L17-L244)
- **Module/theme:** search

## Signature

```php
class SearchMatchTestCase extends DrupalWebTestCase
```

## Documentation

```text
Indexes content and queries it.
```

## Methods (derived index)

- [getInfo()](SearchMatchTestCase/getInfo.md)
- [setUp()](SearchMatchTestCase/setUp.md) — Implementation setUp().
- [testMatching()](SearchMatchTestCase/testMatching.md) — Test search indexing.
- [_setup()](SearchMatchTestCase/_setup.md) — Set up a small index of items to test against.
- [getText()](SearchMatchTestCase/getText.md) — _test_: Helper method for generating snippets of content.
- [getText2()](SearchMatchTestCase/getText2.md) — _test2_: Helper method for generating snippets of content.
- [_testQueries()](SearchMatchTestCase/_testQueries.md) — Run predefine queries looking for indexed terms.
- [_testQueryMatching()](SearchMatchTestCase/_testQueryMatching.md) — Test the matching abilities of the engine.
- [_testQueryScores()](SearchMatchTestCase/_testQueryScores.md) — Test the scoring abilities of the engine.

---
_Drupal 7.103 · [modules/search/search.test](https://github.com/drupal/drupal/blob/7.103/modules/search/search.test) · Licensed GPL-2.0-or-later (see LICENSE)._
