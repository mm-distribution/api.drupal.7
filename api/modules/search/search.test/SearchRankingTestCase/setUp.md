# SearchRankingTestCase::setUp()

- **Type:** Method
- **File:** [`modules/search/search.test`](../_file.md), lines 394–396 · [local source](../../../../../source/modules/search/search.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/search.test#L394-L396)
- **Class:** [SearchRankingTestCase](../SearchRankingTestCase.md)
- **Module/theme:** search

## Signature

```php
function setUp()
```

## Documentation

```text
Implementation setUp().
```

## Code

```php
  function setUp() {
    parent::setUp('search', 'statistics', 'comment');
  }
```

---
_Drupal 7.103 · [modules/search/search.test](https://github.com/drupal/drupal/blob/7.103/modules/search/search.test) · Licensed GPL-2.0-or-later (see LICENSE)._
