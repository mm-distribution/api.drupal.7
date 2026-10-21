# SearchPageOverride::testSearchPageHook()

- **Type:** Method
- **File:** [`modules/search/search.test`](../_file.md), lines 1970–1975 · [local source](../../../../../source/modules/search/search.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/search.test#L1970-L1975)
- **Class:** [SearchPageOverride](../SearchPageOverride.md)
- **Module/theme:** search

## Signature

```php
function testSearchPageHook()
```

## Documentation

_No docblock in source._

## Code

```php
  function testSearchPageHook() {
    $keys = 'bike shed ' . $this->randomName();
    $this->drupalGet("search/dummy_path/{$keys}");
    $this->assertText('Dummy search snippet', 'Dummy search snippet is shown');
    $this->assertText('Test page text is here', 'Page override is working');
  }
```

---
_Drupal 7.103 · [modules/search/search.test](https://github.com/drupal/drupal/blob/7.103/modules/search/search.test) · Licensed GPL-2.0-or-later (see LICENSE)._
