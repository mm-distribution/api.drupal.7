# SearchSetLocaleTest::setUp()

- **Type:** Method
- **File:** [`modules/search/search.test`](../_file.md), lines 2152–2163 · [local source](../../../../../source/modules/search/search.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/search.test#L2152-L2163)
- **Class:** [SearchSetLocaleTest](../SearchSetLocaleTest.md)
- **Module/theme:** search

## Signature

```php
function setUp()
```

## Documentation

_No docblock in source._

## Code

```php
  function setUp() {
    parent::setUp('search');

    // Create a simple node so something will be put in the index.
    $info = array(
      'body' => array(LANGUAGE_NONE => array(array('value' => 'Tapir'))),
    );
    $this->drupalCreateNode($info);

    // Run cron to index.
    $this->cronRun();
  }
```

---
_Drupal 7.103 · [modules/search/search.test](https://github.com/drupal/drupal/blob/7.103/modules/search/search.test) · Licensed GPL-2.0-or-later (see LICENSE)._
