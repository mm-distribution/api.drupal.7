# SearchConfigSettingsForm::getInfo()

- **Type:** Method
- **File:** [`modules/search/search.test`](../_file.md), lines 1448–1454 · [local source](../../../../../source/modules/search/search.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/search.test#L1448-L1454)
- **Class:** [SearchConfigSettingsForm](../SearchConfigSettingsForm.md)
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
      'name' => 'Config settings form',
      'description' => 'Verify the search config settings form.',
      'group' => 'Search',
    );
  }
```

---
_Drupal 7.103 · [modules/search/search.test](https://github.com/drupal/drupal/blob/7.103/modules/search/search.test) · Licensed GPL-2.0-or-later (see LICENSE)._
