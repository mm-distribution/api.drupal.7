# SearchSetLocaleTest::testSearchWithNumericLocale()

- **Type:** Method
- **File:** [`modules/search/search.test`](../_file.md), lines 2168–2178 · [local source](../../../../../source/modules/search/search.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/search.test#L2168-L2178)
- **Class:** [SearchSetLocaleTest](../SearchSetLocaleTest.md)
- **Module/theme:** search

## Signature

```php
public function testSearchWithNumericLocale()
```

## Documentation

```text
Verify that search works with a numeric locale set.
```

## Code

```php
  public function testSearchWithNumericLocale() {
    // French decimal point is comma.
    setlocale(LC_NUMERIC, 'fr_FR');

    // An exception will be thrown if a float in the wrong format occurs in the
    // query to the database, so an assertion is not necessary here.
    db_select('search_index', 'i')
      ->extend('searchquery')
      ->searchexpression('tapir', 'node')
      ->execute();
  }
```

---
_Drupal 7.103 · [modules/search/search.test](https://github.com/drupal/drupal/blob/7.103/modules/search/search.test) · Licensed GPL-2.0-or-later (see LICENSE)._
