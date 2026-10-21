# SearchEmbedForm::getInfo()

- **Type:** Method
- **File:** [`modules/search/search.test`](../_file.md), lines 1882–1888 · [local source](../../../../../source/modules/search/search.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/search.test#L1882-L1888)
- **Class:** [SearchEmbedForm](../SearchEmbedForm.md)
- **Module/theme:** search

## Signature

```php
public static function getInfo()
```

## Documentation

_No docblock in source._

## Code

```php
  public static function getInfo() {
    return array(
      'name' => 'Embedded forms',
      'description' => 'Verifies that a form embedded in search results works',
      'group' => 'Search',
    );
  }
```

---
_Drupal 7.103 · [modules/search/search.test](https://github.com/drupal/drupal/blob/7.103/modules/search/search.test) · Licensed GPL-2.0-or-later (see LICENSE)._
