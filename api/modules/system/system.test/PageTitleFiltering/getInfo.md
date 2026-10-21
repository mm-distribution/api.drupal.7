# PageTitleFiltering::getInfo()

- **Type:** Method
- **File:** [`modules/system/system.test`](../_file.md), lines 1591–1597 · [local source](../../../../../source/modules/system/system.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test#L1591-L1597)
- **Class:** [PageTitleFiltering](../PageTitleFiltering.md)
- **Module/theme:** system

## Signature

```php
public static function getInfo()
```

## Documentation

```text
Implement getInfo().
```

## Code

```php
  public static function getInfo() {
    return array(
      'name' => 'HTML in page titles',
      'description' => 'Tests correct handling or conversion by drupal_set_title() and drupal_get_title() and checks the correct escaping of site name and slogan.',
      'group' => 'System'
    );
  }
```

---
_Drupal 7.103 · [modules/system/system.test](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test) · Licensed GPL-2.0-or-later (see LICENSE)._
