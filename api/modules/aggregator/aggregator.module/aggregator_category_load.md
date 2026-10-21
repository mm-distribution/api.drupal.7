# aggregator_category_load()

- **Type:** Function
- **File:** [`modules/aggregator/aggregator.module`](_file.md), lines 709–716 · [local source](../../../../source/modules/aggregator/aggregator.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.module#L709-L716)
- **Module/theme:** aggregator

## Signature

```php
function aggregator_category_load($cid)
```

## Documentation

```text
Loads an aggregator category.

@param $cid
  The category id.

@return
  An associative array describing the category.
```

## Code

```php
function aggregator_category_load($cid) {
  $categories = &drupal_static(__FUNCTION__);
  if (!isset($categories[$cid])) {
    $categories[$cid] = db_query('SELECT * FROM {aggregator_category} WHERE cid = :cid', array(':cid' => $cid))->fetchAssoc();
  }

  return $categories[$cid];
}
```

---
_Drupal 7.103 · [modules/aggregator/aggregator.module](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.module) · Licensed GPL-2.0-or-later (see LICENSE)._
