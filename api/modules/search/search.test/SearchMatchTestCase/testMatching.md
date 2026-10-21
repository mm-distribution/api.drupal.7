# SearchMatchTestCase::testMatching()

- **Type:** Method
- **File:** [`modules/search/search.test`](../_file.md), lines 36–39 · [local source](../../../../../source/modules/search/search.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/search.test#L36-L39)
- **Class:** [SearchMatchTestCase](../SearchMatchTestCase.md)
- **Module/theme:** search

## Signature

```php
function testMatching()
```

## Documentation

```text
Test search indexing.
```

## Code

```php
  function testMatching() {
    $this->_setup();
    $this->_testQueries();
  }
```

---
_Drupal 7.103 · [modules/search/search.test](https://github.com/drupal/drupal/blob/7.103/modules/search/search.test) · Licensed GPL-2.0-or-later (see LICENSE)._
